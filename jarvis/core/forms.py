from django import forms
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth.models import User

from .models import CustomUser, File, Profile


class ProfileForm(forms.ModelForm):
    AVATAR_CHOICES = [
        ('cs-love-avatar-6.jpg', 'Avatar 1'),
        ('cs-love-avatar-57.jpg', 'Avatar 2'),
        ('cs-love-avatar-58.jpg', 'Avatar 3'),
        ('cs-love-avatar-59.jpg', 'Avatar 4'),
        ('cs-love-avatar-550.jpg', 'Avatar 5'),
        ('cs-love-avatar-551.jpg', 'Avatar 6'),
        ('cs-love-avatar-552.jpg', 'Avatar 7'),
        ('cs-love-avatar-553.jpg', 'Avatar 8'),
        ('cs-love-avatar-555.jpg', 'Avatar 9'),
        ('cs-love-avatar-556.jpg', 'Avatar 10'),
        ('cs-love-avatar-557.jpg', 'Avatar 11'),
        ('cs-love-avatar-558.jpg', 'Avatar 12'),
        ('cs-love-avatar-559.jpg', 'Avatar 13'),
        ('cs-love-avatar-561.jpg', 'Avatar 14'),
        ('cs-love-avatar-562.jpg', 'Avatar 15'),
        ('cs-love-avatar-563.jpg', 'Avatar 16'),
        ('cs-love-avatar-564.jpg', 'Avatar 17'),
        ('cs-love-avatar-566.jpg', 'Avatar 18'),
        ('cs-love-avatar-567.jpg', 'Avatar 19'),
        ('cs-love-avatar-568.jpg', 'Avatar 20'),
        ('cs-love-avatar-569.jpg', 'Avatar 21'),
        ('cs-love-avatar-570.jpg', 'Avatar 22'),
        ('cs-love-avatar-571.jpg', 'Avatar 23'),
        ('cs-love-avatar-572.jpg', 'Avatar 24'),
        ('cs-love-avatar-573.jpg', 'Avatar 25'),
        ('cs-love-avatar-574.jpg', 'Avatar 26'),
        ('cs-love-avatar-576.jpg', 'Avatar 27'),
        ('cs-love-avatar-577.jpg', 'Avatar 28'),
        ('cs-love-avatar-578.jpg', 'Avatar 29'),
        ('cs-love-avatar-579.jpg', 'Avatar 30'),
        ('cs-love-avatar-582.jpg', 'Avatar 31'),
        ('cs-love-avatar-583.jpg', 'Avatar 32'),
        ('cs-love-avatar-584.jpg', 'Avatar 33'),
        ('cs-love-avatar-585.jpg', 'Avatar 34'),
        ('cs-love-avatar-586.jpg', 'Avatar 35'),
        ('cs-love-avatar-589.jpg', 'Avatar 36'),
        ('cs-love-avatar-593.jpg', 'Avatar 37'),
        ('cs-love-avatar-595.jpg', 'Avatar 38'),
        ('cs-love-avatar-598.jpg', 'Avatar 39'),
        ('cs-love-avatar-599.jpg', 'Avatar 40'),
        ('cs-love-avatar-600.jpg', 'Avatar 41'),
        ('cs-love-avatar-601.jpg', 'Avatar 42'),
        ('cs-love-avatar-602.jpg', 'Avatar 43'),
        ('cs-love-avatar-603.jpg', 'Avatar 44'),
        ('cs-love-avatar-604.jpg', 'Avatar 45'),
        ('cs-love-avatar-605.jpg', 'Avatar 46'),
        ('cs-love-avatar-607.jpg', 'Avatar 47'),
        ('cs-love-avatar-608.jpg', 'Avatar 48'),
        ('cs-love-avatar-616 (1).jpg', 'Avatar 49'),
        ('cs-love-avatar-616.jpg', 'Avatar 50'),
        ('cs-love-avatar-617.jpg', 'Avatar 51'),
        ('cs-love-avatar-618.jpg', 'Avatar 52'),
        ('cs-love-avatar-619.jpg', 'Avatar 53'),
        ('cs-love-avatar-622.jpg', 'Avatar 54'),
        ('cs-love-avatar-643.jpg', 'Avatar 55'),
        ('cs-love-avatar-647.jpg', 'Avatar 56'),
        ('cs-love-avatar-648.jpg', 'Avatar 57'),
        ('cs-love-avatar-650.jpg', 'Avatar 58'),
        ('cs-love-avatar-651.jpg', 'Avatar 59'),
        ('cs-love-avatar-653.jpg', 'Avatar 60'),
        ('cs-love-avatar-654.jpg', 'Avatar 61'),
        ('cs-love-avatar-667.jpg', 'Avatar 62'),
        ('cs-love-avatar-670.jpg', 'Avatar 63'),
        ('cs-love-avatar-678.jpg', 'Avatar 64'),
        ('cs-love-avatar-693.jpg', 'Avatar 65'),
        ('cs-love-avatar-703.jpg', 'Avatar 66'),
        ('cs-love-avatar-704.jpg', 'Avatar 67'),
        ('cs-love-avatar-708.jpg', 'Avatar 68'),
        ('cs-love-avatar-6000.jpg', 'Avatar 69'),
        ('cs-love-avatar-6001.jpg', 'Avatar 70'),
        ('cs-love-avatar-6002.jpg', 'Avatar 71'),
        ('cs-love-avatar-6003.jpg', 'Avatar 72'),
        ('cs-love-avatar-6005.jpg', 'Avatar 73'),
        ('cs-love-avatar-6006.jpg', 'Avatar 74'),
        ('cs-love-avatar-6007.jpg', 'Avatar 75'),
        ('cs-love-avatar-6008.jpg', 'Avatar 76'),
        ('cs-love-avatar-6009.jpg', 'Avatar 77'),
        ('cs-love-avatar-6010.jpg', 'Avatar 78'),
        ('cs-love-avatar-6011.jpg', 'Avatar 79'),
        ('cs-love-avatar-6012.jpg', 'Avatar 80'),
        ('cs-love-avatar-6013.jpg', 'Avatar 81'),
        ('cs-love-avatar-6014.jpg', 'Avatar 82'),
        ('cs-love-avatar-6015.jpg', 'Avatar 83'),
        ('cs-love-avatar-6016.jpg', 'Avatar 84'),
        ('cs-love-avatar-6017.jpg', 'Avatar 85'),
        ('cs-love-avatar-6018.jpg', 'Avatar 86'),
        ('cs-love-avatar-6019.jpg', 'Avatar 87'),
        ('cs-love-avatar-6021.jpg', 'Avatar 88'),
        ('cs-love-avatar-6022.jpg', 'Avatar 89'),
        ('cs-love-avatar-6023.jpg', 'Avatar 90'),
        ('cs-love-avatar-6024.jpg', 'Avatar 91'),
        ('cs-love-avatar-6025.jpg', 'Avatar 92'),
        ('cs-love-avatar-6026.jpg', 'Avatar 93'),
        ('cs-love-avatar-6027.jpg', 'Avatar 94'),
        ('cs-love-avatar-6028.jpg', 'Avatar 95'),
        ('cs-love-avatar-6029.jpg', 'Avatar 96'),
        ('cs-love-avatar-6030.jpg', 'Avatar 97'),
        ('cs-love-avatar-6031.jpg', 'Avatar 98'),
        ('cs-love-avatar-6032.jpg', 'Avatar 99'),
        ('cs-love-avatar-6033.jpg', 'Avatar 100'),
        ('cs-love-avatar-6034.jpg', 'Avatar 101'),
        ('cs-love-avatar-6035.jpg', 'Avatar 102'),
        ('cs-love-avatar-6036.jpg', 'Avatar 103'),
        ('cs-love-avatar-6037.jpg', 'Avatar 104'),
        ('cs-love-avatar-6038.jpg', 'Avatar 105'),
        ('cs-love-avatar-6039.jpg', 'Avatar 106'),
        ('cs-love-avatar-6040.jpg', 'Avatar 107'),
        ('cs-love-avatar-6041.jpg', 'Avatar 108'),
        ('cs-love-avatar-6042.jpg', 'Avatar 109'),
        ('cs-love-avatar-6043.jpg', 'Avatar 110'),
        ('cs-love-avatar-6047.jpg', 'Avatar 111'),
        ('cs-love-avatar-6048.jpg', 'Avatar 112'),
        ('cs-love-avatar-6049.jpg', 'Avatar 113'),
        ('cs-love-avatar-6051.jpg', 'Avatar 114'),
        ('cs-love-avatar-6052.jpg', 'Avatar 115'),
        ('cs-love-avatar-6053.jpg', 'Avatar 116'),
        ('cs-love-avatar-6055.jpg', 'Avatar 117'),
        ('cs-love-avatar-6056.jpg', 'Avatar 118'),
        ('cs-love-avatar-6057.jpg', 'Avatar 119'),
        ('cs-love-avatar-6062.jpg', 'Avatar 120'),
        ('cs-love-avatar-6063.jpg', 'Avatar 121'),
        ('cs-love-avatar-6064.jpg', 'Avatar 122'),
        ('cs-love-avatar-6065.jpg', 'Avatar 123'),
        ('cs-love-avatar-6066.jpg', 'Avatar 124'),
        ('cs-love-avatar-6067.jpg', 'Avatar 125'),
        ('cs-love-avatar-6068.jpg', 'Avatar 126'),
        ('cs-love-avatar-6069.jpg', 'Avatar 127'),
        ('cs-love-avatar-6070.jpg', 'Avatar 128'),
        ('cs-love-avatar-6072.jpg', 'Avatar 129'),
        ('cs-love-avatar-6073.jpg', 'Avatar 130'),
        ('cs-love-avatar-6075.jpg', 'Avatar 131'),
        ('cs-love-avatar-6076.jpg', 'Avatar 132'),
        ('cs-love-avatar-6077.jpg', 'Avatar 133'),
        ('cs-love-avatar-6078.jpg', 'Avatar 134'),
        ('cs-love-avatar-6079.jpg', 'Avatar 135'),
        ('cs-love-avatar-6080.jpg', 'Avatar 136'),
        ('cs-love-avatar-6085.jpg', 'Avatar 137'),
        ('cs-love-avatar-6101.jpg', 'Avatar 138'),
        ('cs-love-avatar-6109.jpg', 'Avatar 139'),
        ('cs-love-avatar-6111.jpg', 'Avatar 140'),
        ('cs-love-avatar-6112.jpg', 'Avatar 141'),
    ]

    avatar_choice = forms.ChoiceField(choices=AVATAR_CHOICES, required=False)

    class Meta:
        model = Profile
        fields = ['avatar_choice']


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        max_length=100, required=True, widget=forms.TextInput())
    email = forms.CharField(
        max_length=100, required=True, widget=forms.TextInput())
    password1 = forms.CharField(
        max_length=50, required=True, widget=forms.PasswordInput())
    password2 = forms.CharField(
        max_length=50, required=True, widget=forms.PasswordInput())

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']


class FileUploadForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.file:
            self.fields['name'].initial = self.instance.file.name

    class Meta:
        model = File
        fields = ['file', 'category', 'name', 'task', 'note']
        widgets = {
            'category': forms.Select(choices=File.CATEGORY_CHOICES),
            'name': forms.TextInput(attrs={'readonly': 'readonly'}),
        }

    def clean_file(self):
        file = self.cleaned_data.get('file')
        user = self.instance.user

        if file.size > settings.MAX_FILE_SIZE:
            raise forms.ValidationError(
                f'File size must be under {settings.MAX_FILE_SIZE / (1024 * 1024)} MB. Current file size is {file.size / (1024 * 1024)} MB.')

        if user.get_used_storage() + file.size > user.storage_limit:
            raise forms.ValidationError(
                'You have exceeded your storage limit.')

        return file


class CustomPasswordChangeForm(PasswordChangeForm):
    class Meta:
        model = CustomUser
        fields = ['old_password', 'new_password1', 'new_password2']
