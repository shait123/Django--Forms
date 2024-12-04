from django import forms
from .models import Review
from django.forms import ModelForm


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = "__all__"
        labels = {
            'first_name':"YOUR FIRST NAME",
            'last_name' :"Last Name",
            'stars':"Rating"
        }
        error_message = {
            'stars':{
                'min_value':"YO! Min value is 1",
                'max_value':"YO! max value of 5"
            }
        }

#class ReviewForm(forms.Form):
    #first_name = forms.CharField(label='First Name', max_length=100)
  #   review = forms.CharField(label='please write your review here',
        #                    widget=forms.Textarea(attrs={'class':'myform',
         #                   'rows':'2','cols':'2'}))