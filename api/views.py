from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import HttpResponse,JsonResponse
from .models import BigramLanguageModel,MultiHeadAttention,Head,device,stoi,decode
# Create your views here.
import os
import joblib,torch
pathToModel=os.path.join(os.getcwd(),'api','gpt1model','GPT5000.pb')
# m=joblib.load(os.path.join(os.getcwd(),'api','gpt1model','GPT5000.joblib'))

m = torch.load(pathToModel,map_location=torch.device('cpu'))
m.eval()
print(pathToModel)
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

