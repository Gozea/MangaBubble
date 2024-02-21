import configparser

import torch
import accelerate
import transformers
from transformers import AutoModelForSeq2SeqLM, DataCollatorForSeq2Seq, Seq2SeqTrainingArguments, Seq2SeqTrainer, AutoTokenizer
from datasets import load_dataset, load_metric

# configuration
config = configparser.ConfigParser()
config.read("config.ini")

# device
device = "cuda" if torch.cuda.is_available() else "cpu"

# download dataset and checkpoint
data = config["dataset"]["dataset"].split("/")
load_data = load_dataset(data[0], data[1])
data_split = load_data["train"].train_test_split(test_size=config["dataset"]["test_size"])
model_checkpoint = config["model"]["model_checkpoint"]


# load model, tokenizer and data collator
model = AutoModelForSeq2SeqLM.from_pretrained(model_checkpoint)
tokenizer = AutoTokenizer.from_pretrained(model_checkpoint, src_lang=config["dataset"]["input_code"], tgt_lang=config["dataset"]["target_code"])
data_collator = DataCollatorForSeq2Seq(tokenizer, model=model)


# tokenize dataset
def preprocess(dataset, tokenizer, src_lang, tgt_lang):
    input = [src for src in dataset[src_lang]]
    target = [tgt for tgt in dataset[tgt_lang]]
    tokenized_input = tokenizer(input, text_target=target, padding=True, truncation=True, return_tensors='pt')
    return tokenized_input

tokenized_data = data_split.map(lambda x: preprocess(x, tokenizer, config["dataset"]["input"],config["dataset"]["target"]), batched=True)


# metric
metric = load_metric(config["metric"]["metric"])

def compute_metrics(eval_preds):
    preds, labels = eval_preds
    # decode tokens
    decoded_preds = tokenizer.batch_decode(preds, skip_special_tokens=True)
    # Replace -100 in the labels as we can't decode them.
    labels = np.where(labels != -100, labels, tokenizer.pad_token_id)
    decoded_labels = tokenizer.batch_decode(labels, skip_special_tokens=True)
    # Some simple post-processing
    # strip extra spaces
    decoded_preds = [pred.strip() for pred in decoded_preds]
    decoded_labels = [label.strip() for label in decoded_labels]
    # glue words into one string
    decoded_preds = [" ".join(decoded_preds)]
    decoded_labels = [[" ".join(decoded_labels)]]
    result = metric.compute(predictions=decoded_preds, references=decoded_labels)
    result = {config["metric"]["metric"]: result["score"]}
    prediction_lens = [np.count_nonzero(pred != tokenizer.pad_token_id) for pred in preds]
    result["gen_len"] = np.mean(prediction_lens)
    result = {k: round(v, 4) for k, v in result.items()}
    return result


# training parameters
batch_size = config["args"]["batch_size"]
args = Seq2SeqTrainingArguments(
    config["args"]["model_dir"]
    learning_rate=config["args"]["learning_rate"],
    per_device_train_batch_size=batch_size,
    per_device_eval_batch_size=batch_size,
    weight_decay=config["args"]["weight_decay"],
    num_train_epochs=config["args"]["num_train_epochs"],
    predict_with_generate=config["args"]["predict_with_generate"],
    fp16=config["args"]["fp16"],
    evaluation_strategy=config["args"]["evaluation_strategy"],
    eval_steps=config["args"]["eval_steps"],
    eval_accumulation_steps=config["args"]["eval_accumulation_steps"]
)

# Seq2SeqTrainer
trainer = Seq2SeqTrainer(
    model,
    args,
    train_dataset=tokenized_data["train"],
    eval_dataset=tokenized_data["test"],
    data_collator=data_collator,
    tokenizer=tokenizer,
    compute_metrics=compute_metrics,
)

# training
trainer.train()
