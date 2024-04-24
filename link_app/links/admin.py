from datetime import timezone, timedelta

from django.contrib import admin

from users.models import Users
from .models import Links

admin.site.register(Users)


class LinkAdmin(admin.ModelAdmin):
    def delete_unused_links(self, request, queryset):
        # Определение критериев неиспользуемой ссылки, например, не использовалась в течение последних 30 дней
        seven_days_ago = timezone.now() - timedelta(days=7)
        unused_links = queryset.filter(last_accessed=seven_days_ago)

        # Удаление неиспользуемых ссылок
        unused_links.delete()


admin.site.register(Links, LinkAdmin)
