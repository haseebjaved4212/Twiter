from django.contrib import admin
# pyrefly: ignore [missing-import]
from .models import Tweet


# Register your models here.

admin.site.register(Tweet)
