from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django_registration.forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm
from blango_auth.models import User
from django.forms.widgets import PasswordInput, TextInput

class BlangoRegistrationForm(RegistrationForm):
    class Meta(RegistrationForm.Meta):
        model = User

    def __init__(self, *args, **kwargs):
        super(BlangoRegistrationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit("submit", "Register"))


class CustomAuthForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput(attrs={'class': 'validate', 'value': 'DemoUser'}))
    password = forms.CharField(widget=PasswordInput(attrs={'value': 'impassword'}))

# overwrite auth_view and use crispy form
"""
class ResetPasswordForm(PasswordResetForm):
  class Meta(PasswordResetForm.Meta):
    model = User

  def __init__(self, *args, **kwargs):
    super(PasswordResetForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit("submit", "Reset Password"))
"""