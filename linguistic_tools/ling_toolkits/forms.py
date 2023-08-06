from django import forms

stemming_choices = (
    ('porter', 'PorterStemmer'),
    ('lancaster', 'LancasterStemmer'),
    ('snowball', 'SnowballStemmer')
)

class Stemmer(forms.Form):
    word = forms.CharField(max_length=100)
    stemmer_choice = forms.CharField(label="Choose your Stemmer Option:", widget=forms.RadioSelect(choices=stemming_choices))
    