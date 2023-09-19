from django.core.mail import send_mail
from django.utils import timezone
from datetime import timedelta
from .models import Task, Notification


def send_task_notification(task, content):
    user = task.user

    notification = Notification(user=user, task=task, content=content)
    notification.save()

    subject = "Уведомление о задаче"
    message = content
    from_email = "abdykadyrovsyimyk0708@gmail.com"
    recipient_list = [user.email]

    send_mail(subject, message, from_email, recipient_list, fail_silently=False)


def schedule_task_notifications():
    tomorrow = timezone.now() + timedelta(days=1)
    tasks_due_tomorrow = Task.objects.filter(deadline=tomorrow)

    for task in tasks_due_tomorrow:
        content = f"Срок выполнения задачи '{task.title}' истекает завтра."
        send_task_notification(task, content)
