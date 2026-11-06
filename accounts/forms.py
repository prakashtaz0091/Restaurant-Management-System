from django import forms
from django.contrib.auth.password_validation import validate_password


from django import forms
from django.contrib.auth.password_validation import validate_password


class SignupForm(forms.Form):

    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'id': 'email',
            'placeholder': 'Enter your email',
            'autocomplete': 'email',
            'class': (
                'w-full px-4 py-3 border border-gray-300 rounded-lg '
                'text-sm text-gray-800 placeholder-gray-400 '
                'focus:outline-none focus:ring-2 focus:ring-blue-500 '
                'focus:border-blue-500 transition'
            ),
        }),
        error_messages={
            'required': 'Email is required.',
            'invalid': 'Enter a valid email address.',
        }
    )

    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'id': 'password',
            'placeholder': 'Create a password',
            'autocomplete': 'new-password',
            'minlength': '8',
            'class': (
                'w-full px-4 py-3 pr-12 border border-gray-300 rounded-lg '
                'text-sm text-gray-800 placeholder-gray-400 '
                'focus:outline-none focus:ring-2 focus:ring-blue-500 '
                'focus:border-blue-500 transition'
            ),
        }),
        validators=[validate_password],
        error_messages={
            'required': 'Password is required.',
        }
    )

    confirm_password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'id': 'confirm_password',
            'placeholder': 'Confirm your password',
            'autocomplete': 'new-password',
            'class': (
                'w-full px-4 py-3 pr-12 border border-gray-300 rounded-lg '
                'text-sm text-gray-800 placeholder-gray-400 '
                'focus:outline-none focus:ring-2 focus:ring-blue-500 '
                'focus:border-blue-500 transition'
            ),
        }),
        error_messages={
            'required': 'Please confirm your password.',
        }
    )

    def clean(self):
        cleaned_data = super().clean()

        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password:
            if password != confirm_password:
                self.add_error(
                    'confirm_password',
                    'Passwords do not match.'
                )

        return cleaned_data