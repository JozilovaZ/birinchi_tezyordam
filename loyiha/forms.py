from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm

User = get_user_model()


class RoyxatdanOtishForm(forms.ModelForm):
    parol = forms.CharField(
        label="Parol",
        widget=forms.PasswordInput(attrs={'class': 'form-input', 'placeholder': 'Parol'}),
        min_length=6,
    )
    parol2 = forms.CharField(
        label="Parolni tasdiqlang",
        widget=forms.PasswordInput(attrs={'class': 'form-input', 'placeholder': 'Parolni tasdiqlang'}),
        min_length=6,
    )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Foydalanuvchi nomi'}),
            'first_name': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Ismingiz'}),
            'email': forms.EmailInput(attrs={'class': 'form-input', 'placeholder': 'Email (ixtiyoriy)'}),
        }
        labels = {
            'username': 'Foydalanuvchi nomi',
            'first_name': 'Ism',
            'email': 'Email',
        }

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Bu foydalanuvchi nomi band.")
        return username

    def clean(self):
        cleaned = super().clean()
        p1 = cleaned.get('parol')
        p2 = cleaned.get('parol2')
        if p1 and p2 and p1 != p2:
            self.add_error('parol2', "Parollar mos kelmadi.")
        return cleaned

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['parol'])
        if commit:
            user.save()
        return user


class KirishForm(AuthenticationForm):
    username = forms.CharField(
        label="Foydalanuvchi nomi",
        widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Foydalanuvchi nomi', 'autofocus': True}),
    )
    password = forms.CharField(
        label="Parol",
        widget=forms.PasswordInput(attrs={'class': 'form-input', 'placeholder': 'Parol'}),
    )
    error_messages = {
        'invalid_login': "Foydalanuvchi nomi yoki parol xato.",
        'inactive': "Akkount faol emas.",
    }
