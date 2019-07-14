from django.conf.urls import url

from .views import search_product_view
app_name = 'search'
urlpatterns = [
    url(r'^$', search_product_view, name='query'),
]
