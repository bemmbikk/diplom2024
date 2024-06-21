from django.urls import path, re_path
from . import views
app_name = 'profi_main'
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('', views.index, name='index'), 
    path('about/', views.about, name='about'),
    path('products/', views.product_list, name='product_list'),
    path('contacts/', views.contacts, name='contacts'),
    re_path(r'^(?P<category_slug>[-\w]+)/$', views.product_list, name='product_list_by_category'),
    re_path(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail, name='product_detail'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)