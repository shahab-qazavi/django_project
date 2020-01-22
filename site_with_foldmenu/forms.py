from django import forms
from fold_menu.models import Document , EditModel
from django.contrib.auth.models import User

class UploadFileForm(forms.Form):
    file = forms.FileField()


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('description', 'image', )

#
# class UserForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ('first_name', 'last_name', 'email', 'phone')

    # def __init__(self, *args, **kwargs):
    #     current_user = kwargs.pop('current_user')
    #     super(EditForm, self).__init__(*args, **kwargs)
    #     self.fields['employer'] = current_user

