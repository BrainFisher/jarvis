import mimetypes
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from notes.models import Note
from task_manager.models import Task

class CustomUser(AbstractUser):
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    avatar_choice = models.CharField(max_length=255, blank=True, null=True)
    storage_limit = models.BigIntegerField(default=50 * 1024 * 1024)  # Ліміт за замовчуванням 50 МБ

    def get_used_storage(self):
        used_storage = sum(file.file.size for file in self.file_set.all())
        return used_storage

    def __str__(self):
        return self.username


def user_directory_path(instance, filename):
    return f'user_{instance.user.id}/{filename}'


class File(models.Model):
    CATEGORY_CHOICES = [
        ('image', 'Image'),
        ('document', 'Document'),
        ('video', 'Video'),
        ('other', 'Other'),
    ]

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    file = models.FileField(upload_to=user_directory_path)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, blank=True)
    name = models.CharField(max_length=255, default="Untitled")
    uploaded_at = models.DateTimeField(auto_now_add=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, null=True, blank=True, related_name='files')
    note = models.ForeignKey(Note, on_delete=models.CASCADE, null=True, blank=True, related_name='files')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.category:
            mime_type, _ = mimetypes.guess_type(self.file.name)
            if mime_type:
                if mime_type.startswith('image'):
                    self.category = 'image'
                elif mime_type.startswith('video'):
                    self.category = 'video'
                elif mime_type in ['application/pdf', 'application/msword',
                                   'application/vnd.openxmlformats-officedocument.wordprocessingml.document']:
                    self.category = 'document'
                else:
                    self.category = 'other'
            else:
                self.category = 'other'
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.file.delete(save=False)
        super().delete(*args, **kwargs)


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    avatar_choice = models.CharField(max_length=255, blank=True, choices=[
        ('avatar (1).jpg', 'Avatar 1'),
        ('avatar (2).jpg', 'Avatar 2'),
        ('avatar (3).jpg', 'Avatar 3'),
        ('avatar (4).jpg', 'Avatar 4'),
        ('avatar (5).jpg', 'Avatar 5'),
        ('avatar (6).jpg', 'Avatar 6'),
        ('avatar (7).jpg', 'Avatar 7'),
        ('avatar (8).jpg', 'Avatar 8'),
        ('avatar (9).jpg', 'Avatar 9'),
        ('avatar (10).jpg', 'Avatar 10'),
        ('avatar (11).jpg', 'Avatar 11'),
        ('avatar (12).jpg', 'Avatar 12'),
        ('avatar (13).jpg', 'Avatar 13'),
        ('avatar (14).jpg', 'Avatar 14'),
        ('avatar (15).jpg', 'Avatar 15'),
        ('avatar (16).jpg', 'Avatar 16'),
        ('avatar (17).jpg', 'Avatar 17'),
        ('avatar (18).jpg', 'Avatar 18'),
        ('avatar (19).jpg', 'Avatar 19'),
        ('avatar (20).jpg', 'Avatar 20'),
        ('avatar (21).jpg', 'Avatar 21'),
        ('avatar (22).jpg', 'Avatar 22'),
        ('avatar (23).jpg', 'Avatar 23'),
        ('avatar (24).jpg', 'Avatar 24'),
        ('avatar (25).jpg', 'Avatar 25'),
        ('avatar (26).jpg', 'Avatar 26'),
        ('avatar (27).jpg', 'Avatar 27'),
        ('avatar (28).jpg', 'Avatar 28'),
        ('avatar (29).jpg', 'Avatar 29'),
        ('avatar (30).jpg', 'Avatar 30'),
        ('avatar (31).jpg', 'Avatar 31'),
        ('avatar (32).jpg', 'Avatar 32'),
        ('avatar (33).jpg', 'Avatar 33'),
        ('avatar (34).jpg', 'Avatar 34'),
        ('avatar (35).jpg', 'Avatar 35'),
        ('avatar (36).jpg', 'Avatar 36'),
        ('avatar (37).jpg', 'Avatar 37'),
        ('avatar (38).jpg', 'Avatar 38'),
        ('avatar (39).jpg', 'Avatar 39'),
        ('avatar (40).jpg', 'Avatar 40'),
        ('avatar (41).jpg', 'Avatar 41'),
        ('avatar (42).jpg', 'Avatar 42'),
        ('avatar (43).jpg', 'Avatar 43'),
        ('avatar (44).jpg', 'Avatar 44'),
        ('avatar (45).jpg', 'Avatar 45'),
        ('avatar (46).jpg', 'Avatar 46'),
        ('avatar (47).jpg', 'Avatar 47'),
        ('avatar (48).jpg', 'Avatar 48'),
        ('avatar (49).jpg', 'Avatar 49'),
        ('avatar (50).jpg', 'Avatar 50'),
        ('avatar (51).jpg', 'Avatar 51'),
        ('avatar (52).jpg', 'Avatar 52'),
        ('avatar (53).jpg', 'Avatar 53'),
        ('avatar (54).jpg', 'Avatar 54'),
        ('avatar (55).jpg', 'Avatar 55'),
        ('avatar (56).jpg', 'Avatar 56'),
        ('avatar (57).jpg', 'Avatar 57'),
        ('avatar (58).jpg', 'Avatar 58'),
        ('avatar (59).jpg', 'Avatar 59'),
        ('avatar (60).jpg', 'Avatar 60'),
        ('avatar (61).jpg', 'Avatar 61'),
        ('avatar (62).jpg', 'Avatar 62'),
        ('avatar (63).jpg', 'Avatar 63'),
        ('avatar (64).jpg', 'Avatar 64'),
        ('avatar (65).jpg', 'Avatar 65'),
        ('avatar (66).jpg', 'Avatar 66'),
        ('avatar (67).jpg', 'Avatar 67'),
        ('avatar (68).jpg', 'Avatar 68'),
        ('avatar (69).jpg', 'Avatar 69'),
        ('avatar (70).jpg', 'Avatar 70'),
        ('avatar (71).jpg', 'Avatar 71'),
        ('avatar (72).jpg', 'Avatar 72'),
        ('avatar (73).jpg', 'Avatar 73'),
        ('avatar (74).jpg', 'Avatar 74'),
        ('avatar (75).jpg', 'Avatar 75'),
        ('avatar (76).jpg', 'Avatar 76'),
        ('avatar (77).jpg', 'Avatar 77'),
        ('avatar (78).jpg', 'Avatar 78'),
        ('avatar (79).jpg', 'Avatar 79'),
        ('avatar (80).jpg', 'Avatar 80'),
        ('avatar (81).jpg', 'Avatar 81'),
        ('avatar (82).jpg', 'Avatar 82'),
        ('avatar (83).jpg', 'Avatar 83'),
        ('avatar (84).jpg', 'Avatar 84'),
        ('avatar (85).jpg', 'Avatar 85'),
        ('avatar (86).jpg', 'Avatar 86'),
        ('avatar (87).jpg', 'Avatar 87'),
        ('avatar (88).jpg', 'Avatar 88'),
        ('avatar (89).jpg', 'Avatar 89'),
        ('avatar (90).jpg', 'Avatar 90'),
        ('avatar (91).jpg', 'Avatar 91'),
        ('avatar (92).jpg', 'Avatar 92'),
        ('avatar (93).jpg', 'Avatar 93'),
        ('avatar (94).jpg', 'Avatar 94'),
        ('avatar (95).jpg', 'Avatar 95'),
        ('avatar (96).jpg', 'Avatar 96'),
        ('avatar (97).jpg', 'Avatar 97'),
        ('avatar (98).jpg', 'Avatar 98'),
        ('avatar (99).jpg', 'Avatar 99'),
        ('avatar (100).jpg', 'Avatar 100'),
        ('avatar (101).jpg', 'Avatar 101'),
        ('avatar (102).jpg', 'Avatar 102'),
        ('avatar (103).jpg', 'Avatar 103'),
        ('avatar (104).jpg', 'Avatar 104'),
        ('avatar (105).jpg', 'Avatar 105'),
        ('avatar (106).jpg', 'Avatar 106'),
        ('avatar (107).jpg', 'Avatar 107'),
        ('avatar (108).jpg', 'Avatar 108'),
        ('avatar (109).jpg', 'Avatar 109'),
        ('avatar (110).jpg', 'Avatar 110'),
        ('avatar (111).jpg', 'Avatar 111'),
        ('avatar (112).jpg', 'Avatar 112'),
        ('avatar (113).jpg', 'Avatar 113'),
        ('avatar (114).jpg', 'Avatar 114'),
        ('avatar (115).jpg', 'Avatar 115'),
        ('avatar (116).jpg', 'Avatar 116'),
        ('avatar (117).jpg', 'Avatar 117'),
        ('avatar (118).jpg', 'Avatar 118'),
        ('avatar (119).jpg', 'Avatar 119'),
        ('avatar (120).jpg', 'Avatar 120'),
        ('avatar (121).jpg', 'Avatar 121'),
        ('avatar (122).jpg', 'Avatar 122'),
        ('avatar (123).jpg', 'Avatar 123'),
        ('avatar (124).jpg', 'Avatar 124'),
        ('avatar (125).jpg', 'Avatar 125'),
        ('avatar (126).jpg', 'Avatar 126'),
        ('avatar (127).jpg', 'Avatar 127'),
        ('avatar (128).jpg', 'Avatar 128'),
        ('avatar (129).jpg', 'Avatar 129'),
        ('avatar (130).jpg', 'Avatar 130'),
        ('avatar (131).jpg', 'Avatar 131'),
        ('avatar (132).jpg', 'Avatar 132'),
        ('avatar (133).jpg', 'Avatar 133'),
        ('avatar (134).jpg', 'Avatar 134'),
        ('avatar (135).jpg', 'Avatar 135'),
        ('avatar (136).jpg', 'Avatar 136'),
        ('avatar (137).jpg', 'Avatar 137'),
        ('avatar (138).jpg', 'Avatar 138'),
        ('avatar (139).jpg', 'Avatar 139'),
        ('avatar (140).jpg', 'Avatar 140'),
        ('avatar (141).jpg', 'Avatar 141'),

    ])

    def __str__(self):
        return f"{self.user.username}'s profile"


class Contact(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    birthday = models.DateField()

    def __str__(self):
        return self.name


class News(models.Model):
    source = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return self.title
