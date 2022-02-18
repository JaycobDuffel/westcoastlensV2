from django.shortcuts import render
from django.core.mail import EmailMessage
from django.core import serializers

from ..models.Images import Images

def packages_page(request):
    images = Images.objects.filter(location="HO").order_by("order")

    print(len(images))

    context = {
      "images": images,
      "packages": [
          {
              "name": 'Bronze',
              "price": 150,
              "delivery_method": 'Online Gallery',
              "num_of_images": 15,
              "duration": '25 minutes',
              "contact_for_details": False
          },
          {
                "name": 'Silver',
                "price": 200,
                "delivery_method": 'Online Gallery',
                "num_of_images": 25,
                "duration": '45 minutes',
                "contact_for_details": False
          },
          {
                "name": 'Gold',
                "price": 300,
                "delivery_method": 'Online Gallery',
                "num_of_images": 40,
                "duration": '90 minutes',
                "contact_for_details": False
          },
          {
              "name": 'Wedding/Elopement',
              "price": 750,
              "contact_for_details": True,
          }
      ]
      }
    return render(request, "packages.html", context)
