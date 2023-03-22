from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import HttpResponse
from .models import BigramLanguageModel,MultiHeadAttention,Head,device,stoi,decode
# Create your views here.
import os
import joblib,torch
pathToModel=os.path.join(os.getcwd(),'api','gpt1model','GPT5000.pb')
# m=joblib.load(os.path.join(os.getcwd(),'api','gpt1model','GPT5000.joblib'))

m = torch.load(pathToModel,map_location=torch.device('cpu'))
m.eval()
print(pathToModel)
def modelTest(request):
    # model = BigramLanguageModel()
    # print(os.getcwd())
    print(device)
    context = torch.zeros((1, 1), dtype=torch.long, device=device)
    output=decode(m.generate(context, max_new_tokens=2000)[0].tolist())
    print(output)
    return HttpResponse(output)
@api_view(['POST'])
def getData(request):
    output={'outputString':'huihuihui'}
    return Response(output)
