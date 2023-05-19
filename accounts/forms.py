from django import forms 
from .models import Account

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'비밀번호를 입력하세요.'
    }))

    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'입력한 비밀번호를 확인해 주세요.'
    }))

    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'password', 'address', 'detail_address']

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] = '성을 입력해 주세요.'
        self.fields['last_name'].widget.attrs['placeholder'] = '이름을 입력해주세요.'
        self.fields['phone_number'].widget.attrs['placeholder'] = '핸드폰번호를 입력해주세요.'
        self.fields['email'].widget.attrs['placeholder'] = '이메일을 입력해 주세요.'
        self.fields['address'].widget.attrs['placeholder'] = '주소를 입력해 주세요.'
        self.fields['detail_address'].widget.attrs['placeholder'] = '상세 주소를 입력해 주세요.'

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'