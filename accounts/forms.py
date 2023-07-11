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

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
             raise forms.ValidationError(
                    "비밀 번호 확인이 다릅니다. 다시 입력해 주세요.")


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