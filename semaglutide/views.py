from django.shortcuts import render
from mail.models import Injection_Booking
from django.template.loader import render_to_string
from django.conf import settings
from django.core.mail import send_mail



def home(request):
    if request.method == "POST":
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        message = request.POST['message']
        
        Injection_Booking.objects.create(
            name = name,
            phone = phone,
            email = email,
            message = message

        )
        html = render_to_string('book.html', {
                'name': name,
                'phone': phone,
                'email': email,
                'message': message
        })
        from_email = settings.EMAIL_HOST_USER
        send_mail("New Injection Booking Query Generated",html,from_email,[from_email],html_message=html)  

        # Send confirmation email to the customer
        customer_html = render_to_string('customer_email.html', {
            'name': name,
            'phone': phone,
            'email': email,
            'message': message
        })
        send_mail("Thank you for your Injection Booking", customer_html, from_email, [email], html_message=customer_html)
    
        return render(request, 'thanks.html', {'name': name})
        
    return render(request, 'index.html')

def howtotake(request):
    return render(request, 'how-to-take.html')  
         
def faq(request):
    if request.method == "POST":
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        message = request.POST['message']
        
        Injection_Booking.objects.create(
            name = name,
            phone = phone,
            email = email,
            message = message

        )
        html = render_to_string('book.html', {
                'name': name,
                'phone': phone,
                'email': email,
                'message': message
        })
        from_email = settings.EMAIL_HOST_USER
        send_mail("New Injection Booking Query Generated",html,from_email,[from_email],html_message=html)  

        # Send confirmation email to the customer
        customer_html = render_to_string('customer_email.html', {
            'name': name,
            'phone': phone,
            'email': email,
            'message': message
        })
        send_mail("Thank you for your Injection Booking", customer_html, from_email, [email], html_message=customer_html)
    
        return render(request, 'thanks.html', {'name': name})
    return render(request, 'faq.html')            







    
        
    


         


