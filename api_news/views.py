from django.shortcuts import render
import requests
# Your API key is: cd43a137c659423f961a90a3e8ead57f
# Create your views here.
#API_KEY='cd43a137c659423f961a90a3e8ead57f'
def home(request):
    country= request.GET.get('country')
    category= request.GET.get('category')
    language= request.GET.get('language')
    if category:
        url = f'https://newsapi.org/v2/top-headlines?category={category}&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
    elif country:
        url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
    elif language:
        url = f'https://newsapi.org/v2/top-headlines?language={language}&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
    context = {
        'articles': articles
    }
    return render(request,'index.html',context)