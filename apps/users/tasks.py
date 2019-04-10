from django.template import loader
from django.core.mail.message import EmailMessage
from django.conf import settings
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from apps.users.models import User
from celery import shared_task


@shared_task
def recovery_password_mail(email, request):
    to_email = email
    print("holaaaaaaaaaaa")
    user = User.objects.filter(email=email).first()
    id = user.pk
    token = default_token_generator.make_token(user)
    domain = get_current_site(request).domain
    protocol = 'https' if request.is_secure() else 'http'
    user = User.objects.get(pk=id)
    context = {
        'id': id,
        'token': token,
        'domain': domain,
        'protocol': protocol,
        'user': user
    }
    print(user)
    html_user = loader.get_template("accounts/mail/password_reset.html")
    user_context_html = html_user.render(context)
    subject_user, from_email = 'Cambiar Contraseña', 'DAN MUSIC <email>'

    send_message_async.delay(subject_user, user_context_html, from_email, to_email)


@shared_task
def send_invitation_mail(email, request):
    protocol = 'https' if request.is_secure() else 'http'
    data = {'user': request.user, 'domain': get_current_site(request), 'protocol': protocol}
    template = loader.get_template('accounts/users/invitation_register.html')
    html = template.render(dict(data))
    subject_user, from_email = 'Únete a Dan Music', 'Dan Music <email>'
    send_message_async.delay(subject_user, html, from_email, email)


def send_message(subject_user, user_context_html, from_email, to_email):
    message_user = EmailMessage(subject_user, user_context_html, from_email, [to_email])
    message_user.content_subtype = "html"
    message_user.send(fail_silently=True)


send_message_async = shared_task(send_message)
