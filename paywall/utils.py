from django.core.mail import send_mail


def send_welcome_email(to_email, from_email="from@example.com", subject="Welcome to paywall",
                       message="Here is the message.", fail_silently=False):
    """Tiny wrapper for built-in send_email"""

    send_mail(subject, message, from_email, [to_email], fail_silently=fail_silently)
