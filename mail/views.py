from django.shortcuts import render,redirect
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from . models import Contact
from django.contrib import messages



def contact(request):
    if request.method == "POST":

        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        
        Contact.objects.create(
            name = name,
            email = email,
            message = message
        )
        html = render_to_string('contactquery.html', {
                'name': name,
                'email': email,
                'message': message
        })
        from_email = settings.EMAIL_HOST_USER
        send_mail("New Contact Query Generated",html,from_email,[from_email],html_message=html)
        messages.success(request,"Message Sent Successfully")
        return redirect('contact')


    return render(request,'contact.html')


       
