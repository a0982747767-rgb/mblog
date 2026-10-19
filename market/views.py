from django.shortcuts import render

from market import models


def index(request):
    products = models.Product.objects.all()

    return render(
        request,
        'market_index.html',
        {
            'products': products,
        }
    )


def detail(request, id):
    try:
        product = models.Product.objects.get(id=id)

        images = models.PPhoto.objects.filter(
            product=product
        )

    except models.Product.DoesNotExist:
        product = None
        images = []

    return render(
        request,
        'detail.html',
        {
            'product': product,
            'images': images,
        }
    )