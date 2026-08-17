from datasets import load_dataset

datasets = load_dataset("stanfordnlp/imdb")
print(datasets)
print(datasets["train"][1])
