from django.shortcuts import render
from django.core.mail import EmailMessage

from ..models.Image import Image

def home_page(request):

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        email_message = EmailMessage(
            subject=name + " : " + subject,
            body=message,
            to=["your gmail"],
            headers={"Reply-To": email},
        )
        email_message.send()

    return render(request, "index.html")
