from datasets import load_dataset

dataset = load_dataset("stanfordnlp/imdb", split="train")

dataset.to_parquet("imbd_train.parquet")
