from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    STATUS_CHOICES = (
        (1, ("CEO")),
        (2, ("Dev Manager")),
        (3, ("Testing Manager")),
        (4, ("Developer")),
        (5, ("Tester"))
    )
    email = forms.EmailField(required=True,
                         label='Email',
                         error_messages={'exists': 'Oops'})
    # status = forms.ChoiceField(choices = STATUS_CHOICES, label="Designation", initial='Developer', widget=forms.Select(), required=True)
    first_name = forms.CharField(max_length=30, required=True, label="Designation", help_text="<ul><li>CEO</li> <li>Dev Manager</li> <li>Testing Manager</li> <li>Developer</li> <li>Tester</li></ul>")

    class Meta:
        model = User
        fields = ("username", "email", "first_name", "password1", "password2")

        def save(self, commit=True):
            user = super(SignUpForm, self).save(commit=False)
            user.email = self.cleaned_data["email"]
            user.first_name = self.cleaned_data["first_name"]
            # user.status = self.cleaned_data["status"]
            if commit:
                user.save()
            return user
