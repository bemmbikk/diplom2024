from profi_main.views import index,contact
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from authorization.views import register
from cart.views import my_courses

urlpatterns = [
    path('', register, name='register'),
    path("admin/", admin.site.urls),
    path('my_courses/', my_courses, name='my_courses'),
    path('cart/', include('cart.urls', namespace='cart')),
    path('contact/', contact, name='contact'),  
    path('authorization/', include('authorization.urls', namespace='authorization')),
    path('', include('profi_main.urls', namespace='profi_main')),
]
