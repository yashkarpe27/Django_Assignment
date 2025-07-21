# myproject/settings.py
INSTALLED_APPS = [
    'myapp.apps.MyappConfig',
]

# myapp/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db import transaction

@receiver(post_save, sender=User)
def signal_receiver(sender, instance, **kwargs):
    in_atomic = transaction.get_connection().in_atomic_block
    print("Is signal in transaction?", in_atomic)

# myapp/apps.py
from django.apps import AppConfig

class MyappConfig(AppConfig):
    name = 'myapp'

    def ready(self):
        import myapp.signals

# python manage.py shell
from django.db import transaction
from django.contrib.auth.models import User
import time

with transaction.atomic():
    username = f"signal_test_{int(time.time())}"  # ensures uniqueness
    user = User.objects.create(username=username)
