# myproject/settings.py
INSTALLED_APPS = [
    'myapp.apps.MyappConfig.',
]

# myapp/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
import threading

@receiver(post_save, sender=User)
def my_receiver(sender, instance, **kwargs):
    print("Signal received")
    print("Signal thread:", threading.current_thread().ident)

# myapp/apps.py
from django.apps import AppConfig

class MyappConfig(AppConfig):
    name = 'myapp'

    def ready(self):
        import myapp.signals

# python manage.py shell
import threading
from django.contrib.auth.models import User

print("Caller thread:", threading.current_thread().ident)
user = User.objects.create(username="test_user")
