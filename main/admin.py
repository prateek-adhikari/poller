from django.contrib import admin
from main.models import Question,Choice,Answer
# Register your models here.
admin.site.register([
    Question,
    Choice,
    Answer,
])