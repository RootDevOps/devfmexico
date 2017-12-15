from django import forms
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
    )

User = get_user_model()

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget = forms.PasswordInput)
    
    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        
        if username and password:
            user = authenticate(username = username, password = password)
        if not user:
            raise forms.ValidationError("This user dont exist")
        if not user.check_password(password):
            raise forms.ValidationError("This pass dont exist")
        if not user.is_active:
            raise forms.ValidationError("This user is not longer active")
        return super(UserLoginForm, self).clean(*args, **kwargs)
    
class UserRegisterForm(forms.ModelForm):
    email = forms.CharField(label = 'Email')
    email_verify = forms.EmailField(label = 'Confirm Email')
    password = forms.CharField(widget = forms.PasswordInput)
    class Meta:
        model = User
        fields = [
                'email',
                'email_verify',
                'password',
                'username',
            ]
    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        email_verify = self.cleaned_data.get('email_verify')
        if email != email_verify:
            raise forms.ValidationError("Emails dont match")
        email_exist = User.objects.filter(email = email)
        if email_exist.exists():
            raise forms.ValidationError("This email has been register with other user")
        return super(UserRegisterForm, self).clean(*args, **kwargs)
    
