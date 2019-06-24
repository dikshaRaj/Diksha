from django import forms
from home.models import Book,Author,Genre


class BookForms(forms.Form):
    class Meta:
        book=Book
        fields=('name','genre','purchase_date','author')
        
    title=forms.ModelChoiceField(
        queryset=Book.objects.all(),
        empty_label='Title',widget=forms.Select(attrs={'name':'book','id':'book',
        'class':'custom-select'})
    )

    author=forms.ModelChoiceField(
        queryset=Author.objects.all(),
        empty_label='Author',widget=forms.Select(attrs={'name':'author','id':'author',
        'class':'custom-select'})
    )
    purchase_date = forms.DateField(label='',widget=forms.DateInput(
            attrs={'placeholder':'Purchase_Date','name':'date','id':'date','class':'form-control'}))
    

    genre=forms.ModelMultipleChoiceField(queryset=Genre.objects.all(), widget=forms.CheckboxSelectMultiple)

class SearchForm(forms.Form):
    q=forms.CharField(label='',
        widget=forms.TextInput(attrs={'placeholder':'search','maxlength':'30',
        'class':'form-control'}))
