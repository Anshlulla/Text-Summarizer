from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, Trainer, TrainingArguments, DataCollatorForSeq2Seq 
import torch
import os
from datasets import load_from_disk
from srcc.textSummarizer.entity import ModelTrainerConfig

class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config
    
    def train(self):
        device = "cuda" if torch.cuda.is_available() else "cpu"
        tokenizer = AutoTokenizer.from_pretrained(self.config.model)
        model = AutoModelForSeq2SeqLM.from_pretrained(self.config.model).to(device)
        data_collator = DataCollatorForSeq2Seq(tokenizer=tokenizer, model=model)

        dataset = load_from_disk(self.config.data_path)

        training_args = TrainingArguments(
            output_dir=self.config.root_dir,               # where to save model/checkpoints
            num_train_epochs=1,                            # total training epochs
            warmup_steps=500,                              # number of warmup steps for learning rate scheduler
            per_device_train_batch_size=1,                 # batch size per GPU/TPU core/CPU
            weight_decay=0.01,                             # strength of weight decay
            logging_steps=10,                              # log every 10 steps
            evaluation_strategy="steps",                   # evaluation strategy
            eval_steps=500,                                # evaluate every 500 steps
            save_steps=int(1e6),                           # save checkpoint every 1M steps
            gradient_accumulation_steps=16,                # accumulate gradients to simulate larger batch
        )

        trainer = Trainer(model=model, 
                          args=training_args,
                          tokenizer=tokenizer,
                          data_collator=data_collator,
                          train_dataset=dataset["test"],
                          eval_dataset=dataset["validation"])
        
        trainer.train()

        model.save_pretrained(os.path.join(self.config.root_dir, "pegasus-fine-tuned"))
        tokenizer.save_pretrained(os.path.join(self.config.root_dir, "tokenizer"))