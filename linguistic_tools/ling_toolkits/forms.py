from django import forms

stemming_choices = (
    ('porter', 'Porter Stemmer'),
    ('lancaster', 'Lancaster Stemmer'),
    ('snowball', 'SnowballStemmer')
)

class Stemmer(forms.Form):
    content = forms.CharField(widget=forms.Textarea)
    stemming_type = forms.CharField(choices=stemming_choices,widget=forms.RadioSelect)
