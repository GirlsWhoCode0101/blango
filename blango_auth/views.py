from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
# from blango_auth.forms import PasswordResetForm


@login_required
def profile(request):
    return render(request, "blango_auth/profile.html")

#  overwrite auth_view and change this in url.py
#def password_reset_view(request):
#    password_reset = PasswordResetForm()
#    return render(request, "registration/password_reset.html")
