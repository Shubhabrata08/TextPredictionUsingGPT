from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import HttpResponse,JsonResponse
from .models import BigramLanguageModel,MultiHeadAttention,Head,device,stoi,decode
# Create your views here.
import torch
import torch.nn.functional as F
from transformers import GPT2Tokenizer, GPT2LMHeadModel
import os
import joblib,torch
pathToModel=os.path.join(os.getcwd(),'api','gpt1model','GPT5000.pb')
pathToGPT2Model=os.path.join(os.getcwd(),'api','gpt2model','pytorch_model.bin')
pathToGPT2Tokenizer=os.path.join(os.getcwd(),'api','gpt2model')

# m=joblib.load(os.path.join(os.getcwd(),'api','gpt1model','GPT5000.joblib'))

m = torch.load(pathToModel,map_location=torch.device('cpu'))
m.eval()
# print(pathToModel)
@api_view(['POST'])
def modelTest(request):
    # model = BigramLanguageModel()
    # print(os.getcwd())
    # print(device)
    num_char=int(request.POST['num_char'])
    context = torch.zeros((1, 1), dtype=torch.long, device=device)
    # context[0]
    outputString=decode(m.generate(context, max_new_tokens=num_char)[0].tolist())
    # outputString=outputString.replace("\n",'<br />')
    print(outputString[:1])
    while(outputString[:1]=="\n"):
        outputString=outputString[1:]
    output={'outputString':outputString}
    print(output)
    return JsonResponse(output)

# ----------------GPT-2----------------------

# Load pre-trained GPT-2 model and tokenizer
tokenizer = GPT2Tokenizer.from_pretrained(pathToGPT2Tokenizer,local_files_only=True)
gpt2model = GPT2LMHeadModel.from_pretrained(pathToGPT2Tokenizer,local_files_only=True)

# Set model to evaluation mode
gpt2model.eval()

# Define function to predict next word given input sequence
def predict_next_word(text, num_words=1, temperature=1.0):
    # Tokenize input sequence and convert to tensor
    input_ids = torch.tensor(tokenizer.encode(text)).unsqueeze(0)
    print(input_ids)
    # Generate num_words next words
    for i in range(num_words):
        # Generate hidden representations of input sequence
        with torch.no_grad():
            outputs = gpt2model(input_ids)
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

@api_view(['POST'])
def gpt2Test(request):
    inputString=(request.POST['inpString'])
    print(type(inputString))
    # outputString="HUI"
    outputString=predict_next_word(inputString,num_words=20)
    output={'outputString':outputString}
    print(output)
    return JsonResponse(output)



