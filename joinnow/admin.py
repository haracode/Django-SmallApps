from django.contrib import admin

# Register your models here.
from .models import SignUp # dot = relative import

class JoinNowAdmin(admin.ModelAdmin):
    class Meta:
        model = JoinNow
        
admin.site.register(JoinNow, JoinNowAdmin)