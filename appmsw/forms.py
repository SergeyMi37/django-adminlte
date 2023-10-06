from django.forms import ModelForm, Textarea, TextInput, Select
from appmsw.models import Param, Comment
from django.contrib.auth.models import User
from django.forms import CharField, PasswordInput
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class ParamForm(ModelForm):
    class Meta:
        model = Param
        # Описываем поля, которые будем заполнять в форме
        fields = ['name', 'desc','category', 'paropt', 'enabled', 'public','code']
        widgets = {
            'name': TextInput(attrs={"placeholder": _('name-param'), "class": "blue"}),
            'code': Textarea(attrs={"placeholder": _('code-param'),'rows':13, 'cols':80}),
        }
        labels = {
            'name': '',
            'paropt': 'type',
            'code': 'json'
        }


class UserRegistrationForm(ModelForm):
    class Meta:
        model = User
        fields = ["username", "email"]

    password1 = CharField(label="password", widget=PasswordInput) #***
    password2 = CharField(label="password confirm", widget=PasswordInput)

    # clean_имяПоля - проверка
    def clean_password2(self):  # кастомный валидатор
        pass1 = self.cleaned_data.get("password1")
        pass2 = self.cleaned_data.get("password2")
        if pass1 and pass2 and pass1 == pass2:
            return pass2 #возвращаем это же поле
        raise ValidationError(_('Passwords do not match or are empty'))

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class CommentForm(ModelForm):
   class Meta:
       model = Comment
       fields = ['text']