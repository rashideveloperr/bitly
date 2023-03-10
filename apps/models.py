from django.contrib.auth.models import User
from django.db.models import Model, URLField, ForeignKey, CASCADE, DateTimeField


# Create your models here.
class Link(Model):
    long = URLField('Long Link')
    short = URLField('Short Link')
    user = ForeignKey(User, CASCADE)
    created_at = DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at', )