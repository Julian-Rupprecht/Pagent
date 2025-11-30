from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'index.html')

def chat(request): 
    if request.method == 'POST': 
        prompt = request.POST.get('prompt')
        model = request.POST.get('model')

        print(f"Received prompt: {prompt} with model: {model}")

        return HttpResponse("Prompt received", status=200)