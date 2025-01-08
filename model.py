from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# Load model and tokenizer
model_name = "YOUR_MODEL_NAME"
tokenizer = AutoTokenizer.from_pretrained(model_name, token="your hugging-space token")
model = AutoModelForCausalLM.from_pretrained(model_name, token="your hugging-space token")

# Create input text
input_text = "Who are you?"

# Tokenize input
inputs = tokenizer(input_text, return_tensors="pt")

# Generate response
outputs = model.generate(
    inputs["input_ids"],
    max_length=100,
    num_return_sequences=1,
    temperature=0.7,
    pad_token_id=tokenizer.eos_token_id
)

# Decode and print response
response = tokenizer.decode(outputs[0], skip_special_tokens=True)
print(response)