from django.core.management.base import BaseCommand
import time
from datetime import datetime, timedelta
from links.models import Links  # Импортируйте модель вашей таблицы из базы данных


class Command(BaseCommand):
    help = 'Проверяет базу данных на наличие определенных данных'

    def handle(self, *args, **kwargs):
        while True:
            time_now = datetime.now()
            new_date = time_now - timedelta(days=7) #через 7 дней неактивности удаляем ссылку

            if Links.objects.filter(last_accessed=new_date).exists():
                Links.objects.filter(last_accessed=new_date).delete()

            # Пауза между проверками (например, каждые 10 секунд)
            time.sleep(36000)