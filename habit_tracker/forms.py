from django import forms
from .models import WorkOut
from ckeditor.widgets import CKEditorWidget


class WorkOutForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter title of todays your work out',
                                                          'class':'form-control'
                                                          }))
    content = forms.CharField(widget=CKEditorWidget(attrs={'placeholder': 'Enter your work out here...'}))
    
    class Meta:
        model = WorkOut
        fields = ("title", "category", "content")
        exclude = ["created_ad", "updated_at"]
    
    # def __init__(self,*args, **kwargs):
    #     super(WorkOutForm, self).__init__(*args, **kwargs)
    #     self.fields['title'].widget_attrs['placeholder'] = "Enter your today's workout Title"

    #     for field in self.fields:
    #         self.fields[field].widget.attrs['class'] = 'form-control'