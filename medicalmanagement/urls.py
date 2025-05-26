from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView, LoginView
from customer import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home.as_view(), name='home'),
    path('customer/', include('customer.urls')),
    path('logout', LogoutView.as_view(template_name='insurance/logout.html'), name='logout'),
    #path('aboutus/', views.aboutus_view),
    path('afterlogin', views.afterlogin_view, name='afterlogin'),
    path('adminlogin', LoginView.as_view(template_name='insurance/adminlogin.html'), name='adminlogin'),
]
