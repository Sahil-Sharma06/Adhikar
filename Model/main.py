from fastapi import FastAPI
from transformers import T5Tokenizer, T5ForConditionalGeneration, AdamW
import torch
model_save_path = "model"
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# Inference Function
def generate_answer(question, model, tokenizer, device, max_length=128):
    model.eval()
    with torch.no_grad():
        input_text = f"question: {question} </s>"
        input_ids = tokenizer.encode(input_text, return_tensors="pt").to(device)
        attention_mask = torch.ones_like(input_ids).to(device)  # Since we use padding='max_length' during training

        generated_ids = model.generate(
            input_ids=input_ids,
            attention_mask=attention_mask,
            max_length=max_length,
            num_beams=4,
            early_stopping=True
        )

        answer = tokenizer.decode(generated_ids[0], skip_special_tokens=True)
    return answer

#  Load the Fine-Tuned Model for Inference
fine_tuned_model = T5ForConditionalGeneration.from_pretrained(model_save_path).to(device)
fine_tuned_tokenizer = T5Tokenizer.from_pretrained(model_save_path)

example_question = "Dominos failed to fulfill its obligations under a joint venture agreement."
generated_answer = generate_answer(example_question, fine_tuned_model, fine_tuned_tokenizer, device)  
print(f"Question: {example_question}\nAnswer: {generated_answer}")



# Initialize the FastAPI app
app = FastAPI()

# Define a basic GET route
@app.get("/")
async def root(): 
    return {"message": "Hello! world"}

# Define another route that takes a path parameter
@app.get("/question/{question}")
async def get_ans(question: str):
    generated_answer = generate_answer(question, fine_tuned_model, fine_tuned_tokenizer, device) 
    return {"message": f"{generated_answer}"}
