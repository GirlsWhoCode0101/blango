from django import forms
from blog.models import Comment
from crispy_forms.layout import Submit
from crispy_forms.helper import FormHelper


class CommentForm(forms.ModelForm):
  # helper class to not have redundant fields
  # which would be in the model and the form
  class Meta:
    model = Comment
    fields = ["content"]  # here we can use all 
    # available fields from the model

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)  # inherits constuctor in correct order
    self.helper = FormHelper()  # helps to customize our form
    self.helper.add_input(Submit('submit', 'Submit'))
