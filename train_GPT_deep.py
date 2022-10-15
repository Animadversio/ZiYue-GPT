"""Code for training GPT2 on the ctext dataset"""
from pathlib import Path
from datasets import load_dataset
from transformers import GPT2Tokenizer, BertTokenizerFast

tokenizer_bert = BertTokenizerFast.from_pretrained('bert-base-chinese',
    additional_special_tokens=["<s>","<pad>","</s>","<unk>","<mask>"],
    pad_token='<pad>' ,max_len=512)

print("token num", len(tokenizer_bert.get_vocab()))
#%%
paths = [str(x) for x in Path("./ctext_sentence/").glob("**/*.txt")]
dataset = load_dataset("text", data_files=
              {"train": paths, })
dataset = dataset.map(lambda examples:
        tokenizer_bert(examples["text"]),
        batched=True)
short_dataset = dataset.filter(lambda example, idx: len(example["text"]) <= 50, with_indices=True)

print(short_dataset['train'][10])
#%%
from transformers import DataCollatorForLanguageModeling
from transformers import GPT2Model, GPT2Config, GPT2LMHeadModel
from transformers import Trainer, TrainingArguments

# Initializing a GPT2 configuration
configuration = GPT2Config(vocab_size=25000, n_layer=12)
model = GPT2LMHeadModel(config=configuration)

data_collator = DataCollatorForLanguageModeling(
    tokenizer=tokenizer_bert, mlm=False,
)

training_args = TrainingArguments(
    output_dir="./AncChn_L12_output",
    overwrite_output_dir=True,
    num_train_epochs=100,
    per_gpu_train_batch_size=64,
    save_steps=10_000,
    save_total_limit=10,
)

trainer = Trainer(
    model=model,
    args=training_args,
    data_collator=data_collator,
    train_dataset=short_dataset['train'],
    # prediction_loss_only=True,
)

trainer.train(resume_from_checkpoint="/home/binxuwang/Datasets/AncChn_L12_output/checkpoint-60000")
model.save_pretrained("/home/binxuwang/Ziyue-GPT2-deep")
tokenizer_bert.save_pretrained("/home/binxuwang/Ziyue-GPT2-deep")

