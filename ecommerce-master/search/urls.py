from django.conf.urls import url

from .views import search_product_view

urlpatterns = [
    url(r'^$', search_product_view, name='query'),
]
