from django.conf.urls import url

from .views import product_list_view, ProductDetailSlugView

urlpatterns = [
    url(r'^$', product_list_view, name='list'),
    url(r'^(?P<slug>[\w-]+)/$', ProductDetailSlugView.as_view(), name='detail'),
]
