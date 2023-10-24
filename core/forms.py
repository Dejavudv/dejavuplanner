
from stripe import Review
from django import forms
from core.models import *


class ProductReviewForm(forms.ModelForm):
    review = forms.CharField(widget=forms.Textarea(attrs={'placeholder': "write review"}))


    class Meta:
        model = ProductReview
        fields = ['review', 'rating']







