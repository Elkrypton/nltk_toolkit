from django.shortcuts import render
from tools.stemmer import PorterStemming, LancasterStemming, SnowballStemming
from forms import Stemmer
# Create your views here.


def process_text(request):
    if request.method == 'POST':
        form = Stemmer(request.POST)
        if form.is_valid():
            content = form.cleaned_data['content']
            stemming_type = form.cleaned_data['stemming_type']
            if stemming_type == 'porter':
                stemmed_content = PorterStemming(content)
            elif stemming_type == 'lancaster':
                stemmed_content = LancasterStemming(content)
            
            elif stemming_type == "snowball":
                stemmed_content = SnowballStemming(content)
            
            else:
                stemmed_content = content 
    else:
        form = Stemmer()
    
    return render(request, 'stemmer.html', {'form':form})