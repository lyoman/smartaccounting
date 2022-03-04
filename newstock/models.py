from django.utils import timezone
from django.contrib.auth.models import Permission
from django.db import models
from django.conf import settings


NAME_CHOICES = (
    ("SHE", "SHE"),
    ("HR", "HR"),
    ("Finance", "Finance"),
    ("Technical Services", "Technical Services"),
    ("Reduction", "Reduction"),
    ("Engineering", "Engineering"),
    ("Security", "Security"),
)


def user_directory_path(instance, filename):
  
    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)

class NewStock(models.Model):
    user           = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete = models.CASCADE)
    # name           = models.CharField(max_length=250, choices=NAME_CHOICES)
    name           = models.CharField(max_length=250, null=False, blank=False)
    invoice        = models.ImageField(upload_to = user_directory_path)

    description    = models.TextField(blank = True)
    quantity       = models.CharField(max_length=250, null=False, blank=False)
    # price          = models.CharField(max_length=250, null=False, blank=False)
    amount         = models.DecimalField(max_digits=6, decimal_places=2)
    active         = models.BooleanField(default=True)
    updated        = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp      = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-timestamp", "-updated"]


class SoldStock(models.Model):
    user           = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete = models.CASCADE)
    # name           = models.CharField(max_length=250, choices=NAME_CHOICES)
    stockname      = models.ForeignKey(NewStock, default=1, on_delete = models.CASCADE)
    description    = models.TextField(blank = True)
    quantity       = models.CharField(max_length=250, null=False, blank=False)
    quantity_left  = models.CharField(max_length=250, null=False, blank=False)
    # price          = models.CharField(max_length=250, null=False, blank=False)
    amount         = models.DecimalField(max_digits=6, decimal_places=2)
    total_amount   = models.DecimalField(max_digits=6, decimal_places=2)
    # active         = models.BooleanField(default=True)
    updated        = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp      = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.description

    class Meta:
        ordering = ["-timestamp", "-updated"]
