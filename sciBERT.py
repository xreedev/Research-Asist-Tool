from transformers import AutoTokenizer, AutoModel
import data
# Load SciBERT tokenizer
tokenizer = AutoTokenizer.from_pretrained("allenai/scibert_scivocab_uncased")

# Load SciBERT model
model = AutoModel.from_pretrained("allenai/scibert_scivocab_uncased")

inputs = tokenizer(data.ieee_paper_data, return_tensors="pt")
outputs = model(**inputs)
print(outputs)
