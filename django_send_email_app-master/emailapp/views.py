from django.shortcuts import render
from django.http import JsonResponse
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.conf import settings

# Create your views here.
def send_email_api(request):
    send_email_from_app()
    data = {
        'success': True,
        'message': 'api to send an email'
    }
    return JsonResponse(data)

def send_email_from_app():
    html_tpl_path = 'email_templates/welcome.html'
    name= 'Ranjit Shinde'
    # html_tpl_path = f'<html><body><h1 style:"color:red">hello {name}</h1></body></html>'
    context_data={'name':name}
    email_html_template = get_template(html_tpl_path).render(context_data)
    # email_html_template = html_tpl_path
    # receiver_email = 'rohit.jadhav@weagile.net'
    receiver_email = 'ranjitshinde9404@gmail.com'
    email_msg = EmailMessage('Welcome to Ranjit Pvt Ltd',
                                email_html_template,
                                settings.APPLICATION_EMAIL,
                                [receiver_email],
                                reply_to=[settings.APPLICATION_EMAIL]
                                )
    # this is the crucial part that sends email as html content but not as a plain text
    email_msg.content_subtype = 'html'
    email_msg.send(fail_silently=False)









