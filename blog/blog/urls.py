from django.contrib import admin
from django.urls import path, include
from .views import hello_word

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello_word),
    path('blog/', include('website.urls')),
    ]
