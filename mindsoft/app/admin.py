from django.contrib import admin

# Register your models here.
from app.models import dept_model,auth_model
admin.site.register(dept_model)
admin.site.register(auth_model)
