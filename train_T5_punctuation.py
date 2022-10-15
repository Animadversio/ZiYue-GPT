"""
A simple experimental model to test Seq2Seq on adding punctuation to ancient Chinese text.
Using the curated ctex dataset.
"""
# https://stackoverflow.com/questions/71948525/huggingface-t5-base-with-seq2seqtrainer-runtimeerror-expected-all-tensors-to-be
from transformers import T5Tokenizer, T5ForConditionalGeneration

tokenizer = T5Tokenizer.from_pretrained("Langboat/mengzi-t5-base")
# model = T5ForConditionalGeneration.from_pretrained("Langboat/mengzi-t5-base")

#%%
from pathlib import Path
from datasets import Dataset, DatasetDict, load_dataset
from transformers import AutoTokenizer, T5Tokenizer, Seq2SeqTrainer

max_input_length = 64
max_target_length = 64
def preprocess_function(examples):
    text = examples["text"]
    text_nopunct = text.replace("。", "").replace("？", "").replace("！", "").replace("，", "")\
        .replace("：", "").replace("“", "").replace("”", "")

    # No breaking space text as the input
    model_inputs = tokenizer(text_nopunct, max_length=max_input_length, padding=True, truncation=True)
    # Setup the tokenizer for targets
    with tokenizer.as_target_tokenizer():
        labels = tokenizer(examples["text"], max_length=max_target_length, padding=True, truncation=True)

    model_inputs["text_no_punct"] = text_nopunct
    model_inputs["labels"] = labels["input_ids"]
    return model_inputs


paths = [str(x) for x in Path("./Datasets/ctext_sentence/").glob("**/*.txt")]
dataset = load_dataset("text", data_files=
              {"train": paths, })

tokenized_datasets = dataset.map(preprocess_function, batched=False)
# short_dataset = dataset.filter(lambda example, idx: len(example["text"]) <= 50, with_indices=True)

print(tokenized_datasets['train'][10]["text_no_punct"], "\t", tokenized_datasets['train'][10]["text"])
print(tokenized_datasets['train'][100]["text_no_punct"], "\t", tokenized_datasets['train'][100]["text"])
print(tokenized_datasets['train'][1000]["text_no_punct"], "\t", tokenized_datasets['train'][1000]["text"])

tokenized_datasets = tokenized_datasets.remove_columns(["text_no_punct", "text"])

train_test = tokenized_datasets["train"].train_test_split(test_size=0.2)
tokenized_datasets_split = DatasetDict({
    'train': train_test['train'],
    'test': train_test['test']})

train_dataset = tokenized_datasets_split["train"].shuffle(seed=42)
test_dataset = tokenized_datasets_split["test"].shuffle(seed=42)

#%%
from transformers import AutoModelForSeq2SeqLM, DataCollatorForSeq2Seq, \
    Seq2SeqTrainingArguments, Seq2SeqTrainer

model = AutoModelForSeq2SeqLM.from_pretrained("Langboat/mengzi-t5-base")
# model = AutoModelForSeq2SeqLM.from_pretrained(model_checkpoint)
batch_size = 64
model_name = "mengzi-t5-base"
args = Seq2SeqTrainingArguments(
    output_dir=f"{model_name}-finetuned-punctuation",
    evaluation_strategy="epoch",
    learning_rate=2e-5,
    per_device_train_batch_size=batch_size,
    per_device_eval_batch_size=batch_size,
    save_steps=1000,
    save_total_limit=10,
    weight_decay=0.01,
    num_train_epochs=1,
    predict_with_generate=True,
    fp16=True,
    # push_to_hub=True,
)
data_collator = DataCollatorForSeq2Seq(tokenizer, model=model)
trainer = Seq2SeqTrainer(
    model=model,
    args=args,
    train_dataset=train_dataset,
    eval_dataset=test_dataset,
    data_collator=data_collator,
    tokenizer=tokenizer,
    # compute_metrics=compute_metrics,
)

trainer.train()