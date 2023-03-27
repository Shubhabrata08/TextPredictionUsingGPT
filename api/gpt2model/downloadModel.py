import torch
import torch.nn.functional as F
from transformers import GPT2Tokenizer, GPT2LMHeadModel

# Load pre-trained GPT-2 model and tokenizer
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = GPT2LMHeadModel.from_pretrained('gpt2')

# Set model to evaluation mode
model.eval()

# Define function to predict next word given input sequence
def predict_next_word(text, num_words=1, temperature=1.0):
    # Tokenize input sequence and convert to tensor
    input_ids = torch.tensor(tokenizer.encode(text)).unsqueeze(0)
    print(input_ids)
    # Generate num_words next words
    for i in range(num_words):
        # Generate hidden representations of input sequence
        with torch.no_grad():
            outputs = model(input_ids)
            logits = outputs[0][:, -1, :] / temperature
            softmax_logits = F.softmax(logits, dim=-1)
            next_word_id = torch.multinomial(softmax_logits, num_samples=1)

        # Add next word to input sequence
        # print(next_word_id.unsqueeze(0))
        input_ids = torch.cat([input_ids, next_word_id], dim=-1)
        # print(input_ids)

    # Decode output sequence and return predicted text
    output_text = tokenizer.decode(input_ids.squeeze(), skip_special_tokens=True)
    return output_text