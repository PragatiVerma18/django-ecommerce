from django.db.models import Q
from django.shortcuts import render
from products.models import Product

def search_product_view(request):
    print(request.GET)
    query = request.GET.get('q')
    print(query)
    if query is not None:
        lookup = Q(title__icontains=query) | Q(description__icontains=query)
        queryset = Product.objects.filter(lookup).distinct()
    else:
        queryset = Product.objects.featured()
    context = {
        'object_list': queryset
    }
    return render(request, "search/view.html", context)
