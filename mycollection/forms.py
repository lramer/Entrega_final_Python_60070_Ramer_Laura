from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import  UserChangeForm

class UserEditForm(UserChangeForm):
    password = forms.CharField(
        help_text='',
        widget= forms.HiddenInput(),required=False
    )
    password1 = forms.CharField(label='Contraseña',widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir Contraseña',widget=forms.PasswordInput)

    class Meta:
        model= User
        fields=('first_name','last_name','email')
    
    def clean_password2(self) -> str:
        
        password1= self.cleaned_data['password1']
        password2= self.cleaned_data['password2']

        if password2 != password1:
            raise forms.ValidationError('Las contraseñas son diferentes, intenta de nuevo...')
        return password2
        
         
class createavatarform(forms.ModelForm):

    class Meta:
        model= User_avatar
        fields= ('imagen',)      



class ColeccionForm(forms.ModelForm):
    class Meta:
        model = Coleccion
        fields = ('__all__')  # Solo campos que deseas editar directamente


class AgregarComicForm(forms.ModelForm):
    comics = forms.ModelMultipleChoiceField(queryset=Comic.objects.all(), widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Coleccion
        fields = ['comics']


class ContactForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    email = forms.EmailField()
    mensaje = forms.CharField(widget=forms.Textarea)       