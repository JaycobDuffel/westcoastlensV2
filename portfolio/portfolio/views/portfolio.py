from django.shortcuts import render

from ..models.Image import Image

def portfolio_page(request):
    images = Image.objects.filter(location="PO").order_by("order")



    context = {
      "categories": [
          {
              "name": 'Portraits',
              "image": images[0],
              "url": 'portraits',
          },
          {
              "name": 'Couples and Engagement',
              "image": images[1],
              "url": 'couplesandengagement',
          },
          {
              "name": 'Wedding and Elopement',
              "image": images[2],
              "url": 'weddingandelopement',
          },
          {
              "name": 'Boudoir',
              "image": images[3],
              "url": 'boudoir',
          }
      ]
      }
    return render(request, "portfolio.html", context)
