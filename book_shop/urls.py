"""book_shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from book_shop import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('checkout/', views.checkout, name="checkout"),
    path('account/', views.account, name="account"),
    path('login/', views.login, name="login"),
    path('contact/', views.contact, name="contact"),
    path('book/', views.book, name="book"),
    path('feature/', views.feature, name="feature"),
    path('about/', views.about, name="about"),
    path('book_offer/', views.book_offer, name="book_offer"),
    path('sales_off/', views.sales_off, name="sales_off"),
    path('book/<int:book_id>', views.bookDetails)
    
  
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)