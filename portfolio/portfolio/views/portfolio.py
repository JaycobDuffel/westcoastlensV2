from django.shortcuts import render

from ..models.Image import Image


def portfolio_page(request):
    background = Image.objects.filter(location="BG").first()
    portrait_image = Image.objects.filter(location="POR").order_by('order').first()
    couples_image = Image.objects.filter(location="CO").order_by('order').first()
    wedding_image = Image.objects.filter(location="WE").order_by('order').first()
    boudoir_image = Image.objects.filter(location="BO").order_by('order').first()

    context = {
        "categories": [
            {
                "name": 'Portraits',
                "image": portrait_image,
                "url": 'portraits',
            },
            {
                "name": 'Couples and Engagement',
                "image": couples_image,
                "url": 'couplesandengagement',
            },
            {
                "name": 'Wedding and Elopement',
                "image": wedding_image,
                "url": 'weddingandelopement',
            },
            {
                "name": 'Boudoir',
                "image": boudoir_image,
                "url": 'boudoir',
            }
        ],
        "background": background
    }
    return render(request, "portfolio.html", context)


def portrait_page(request):
    images = Image.objects.filter(location="POR").order_by("order").exclude(order = -1)
    background = Image.objects.filter(location="BG").first()

    context = {
        "images": images,
        "background": background
    }
    return render(request, "portfolio_page.html", context)

def boudoir_page(request):
    images = Image.objects.filter(location="BO").order_by("order").exclude(order = -1)
    background = Image.objects.filter(location="BG").first()

    context = {
        "images": images,
        "background": background
    }
    return render(request, "portfolio_page.html", context)

def couples_page(request):
    images = Image.objects.filter(location="CO").order_by("order").exclude(order = -1)
    background = Image.objects.filter(location="BG").first()

    context = {
        "images": images,
        "background": background
    }
    return render(request, "portfolio_page.html", context)

def wedding_page(request):
    images = Image.objects.filter(location="WE").order_by("order").exclude(order = -1)
    background = Image.objects.filter(location="BG").first()

    context = {
        "images": images,
        "background": background
    }
    return render(request, "portfolio_page.html", context)
