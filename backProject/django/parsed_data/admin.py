from django.contrib import admin

# Register your models here.
from parsed_data.models import schoolData
from parsed_data.models import blogData
from parsed_data.models import newsData

admin.site.register(schoolData)
admin.site.register(blogData)
admin.site.register(newsData)