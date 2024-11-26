from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    status = models.BooleanField(default=False)  # False - не выполнено, True - выполнено
    deadline = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title


from django.db.models.signals import post_save
from django.dispatch import receiver
from .telegram_bot import send_telegram_message

@receiver(post_save, sender=Task)
def notify_telegram(sender, instance, created, **kwargs):
    if created:
        message = f'Создана новая задача: {instance.title}'
    else:
        message = f'Задача обновлена: {instance.title}, статус: {"Выполнено" if instance.status else "Не выполнено"}'
    send_telegram_message(message)

