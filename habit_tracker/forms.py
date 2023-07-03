from django import forms
from .models import WorkOut
from ckeditor.widgets import CKEditorWidget


class WorkOutForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter title of todays your work out',
                                                          'class':'form-control'
                                                          }))
    content = forms.CharField(widget=CKEditorWidget())

    def __init__(self, *args, **kwargs):
        initial_category = 'English'  # Replace with your desired default category name
        super().__init__(*args, **kwargs)
        self.fields['category'].initial = initial_category
    
    class Meta:
        model = WorkOut
        fields = ("title", "category", "content")
        exclude = ["created_at", "updated_at"]
    
    # def __init__(self,*args, **kwargs):
    #     super(WorkOutForm, self).__init__(*args, **kwargs)
    #     self.fields['title'].widget_attrs['placeholder'] = "Enter your today's workout Title"

    #     for field in self.fields:
    #         self.fields[field].widget.attrs['class'] = 'form-control'