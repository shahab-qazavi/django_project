from django import forms
from fold_menu.models import Document
from django.contrib.auth.models import User
from jalali_date.fields import JalaliDateField, SplitJalaliDateTimeField
from jalali_date.widgets import AdminJalaliDateWidget, AdminSplitJalaliDateTime
# from persiandate.widgets import PersianDateInput
from .models import BarTime ,Bar

class UploadFileForm(forms.Form):
    file = forms.FileField()


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('description', 'image', )


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', "username",)


# class MyForm(forms.Form):
#     my_date = forms.DateField(widget=PersianDateInput)


# class TestForm(forms.ModelForm):
#     class Meta:
#         model = Bar()
#         fields = ('name', 'date', 'date_time')
#
#     def __init__(self, *args, **kwargs):
#         super(TestForm, self).__init__(*args, **kwargs)
#         self.fields['date'] = JalaliDateField(label=_('date'), # date format is  "yyyy-mm-dd"
#             widget=AdminJalaliDateWidget # optional, to use default datepicker
#         )
#
#         # you can added a "class" to this field for use your datepicker!
#         # self.fields['date'].widget.attrs.update({'class': 'jalali_date-date'})
#
#         self.fields['date_time'] = SplitJalaliDateTimeField(label=_('date time'),
#             widget=AdminSplitJalaliDateTime # required, for decompress DatetimeField to JalaliDateField and JalaliTimeField
#         )

