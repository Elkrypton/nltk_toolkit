from django.shortcuts import render, HttpResponseRedirect, reverse, HttpResponse
from tools.stemmer import PorterStemming, LancasterStemming, SnowballStemming
from tools.frequency_dist import FrequencyDistribution
from .forms import Stemmer, FrequencyForm
# Create your views here.


def process_text(request):
    if request.method == 'POST':
        form = Stemmer(request.POST)
        if form.is_valid():
            content = form.cleaned_data['content']
            stemming_type = form.cleaned_data['stemming_type']
            if stemming_type == 'porter':
                stemmed_content = PorterStemming(content)
                print(stemmed_content)
            elif stemming_type == 'lancaster':
                stemmed_content = LancasterStemming(content)
                print(stemmed_content)
            
            elif stemming_type == "snowball":
                stemmed_content = SnowballStemming(content)
                print(stemmed_content)
            
            else:
                stemmed_content = content 
    else:
        form = Stemmer()
    
    return render(request, 'stemmer.html', {'form':form})

def FrequencyDist(request):
    if request.method == 'POST':
        form = FrequencyForm(request.POST)
        if form.is_valid():
            words  = form.cleaned_data['words']
            freq = FrequencyDistribution(words)
    else:
        form = FrequencyForm()
    
    return render(request, 'frequency_dist.html', {'form':form})