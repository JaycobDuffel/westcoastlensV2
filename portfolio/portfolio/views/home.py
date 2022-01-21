from django.shortcuts import render
from django.core.mail import EmailMessage

from ..models.Images import Images

def home_page(request):
    images = Images.objects.filter(location="HO").order_by("order")
    print(len(images))

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

    context = {
      "images": images,
      }
    return render(request, "index.html", context)
