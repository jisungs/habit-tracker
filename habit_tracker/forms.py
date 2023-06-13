from django import forms
from .models import WorkOut


class WorkOutForm(forms.ModelForm):

    class Meta:
        model = WorkOut
        fields = ("title", "content", "category")
        exclude = ["created_ad", "updated_at"]