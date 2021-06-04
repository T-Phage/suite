from django import forms
from .models import *

class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    GEN_CHOICES = [('select', ''),
                   ('male', 'Male'),
                   ('female', 'Female'),
                   ('other', 'Other')]
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                                    'placeholder': 'enter password'}))
    password2 = forms.CharField(label='Password confirmation',
                                widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                  'placeholder': 're-enter password'}))
    department = forms.ModelChoiceField(queryset=Department.objects.all(),
                                        widget=forms.Select(attrs={'class': 'form-control'}))
    # faculty = forms.ModelChoiceField(queryset=Faculty.objects.all(),
    #                                  widget=forms.Select(attrs={'class': 'form-control'}))
    gender = forms.ChoiceField(choices=GEN_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'email'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'username'}))
    othername = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                              'placeholder': 'othernames'}))
    surname = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter your surname'}))
    firstname = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter firstname'}))

    # faculty = forms.SelectMultiple(attrs={'required': "required"})

    class Meta:
        model = MyUser
        fields = ('firstname', 'email', 'username', 'department', 'password1',
                  'password2', 'gender', 'surname', 'othername')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return

ROLECHOICES = [('private', 'Private'),
           ('medium', 'Medium'),
           ('public', 'Public')]
class SiteForm(forms.ModelForm):
    site_visibilty = forms.CharField(label='Visibility', widget=forms.RadioSelect(choices=ROLECHOICES, attrs={'class': 'form-ckeck'}))
    site_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Enter the name of the site...', 'class': 'form-control'}))
    site_url = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control hidden'}))

    site_id = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'site id...', 'class': 'form-control', 
                                                            'aria-disabled':'true'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control', 'rows':'10', 'cols':'40',
                                                    'style':'margin-top: 0px; margin-bottom: 3px; height: 167px;'}))
    created_by = forms.ModelChoiceField(label='',queryset=MyUser.objects.all(),
                                        widget=forms.Select(attrs={'class': 'form-control hidden'}))
    
    class Meta:
        model = Site
        fields = ["site_name", "site_id", "site_url", "description", 'site_visibilty', 'created_by',]

class FolderForm(forms.ModelForm):
    folder_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter the folder name...', 'class': 'form-control'}))

    class Meta:
        model = Folder
        fields = ['folder_name', 'folder_url', 'is_rep', 'faculty', 'department', 'created_by', 'main_folder', 'site',]

class FileForm(forms.ModelForm):
    # filepath = forms.FileField(required=False)
    class Meta:
        model = File
        fields = ["filepath", "file_url", "uploaded_by", 'department', 'faculty', 'is_rep', 'folder', 'site',]
