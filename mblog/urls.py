from django.urls import path
from django.contrib import admin
from mysite.views import homepage, showpost, about, listing, disp_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage),
    path('post/<slug:slug>/', showpost),
    path('about/', about),
    path('list/', listing),
    path('list/<str:sku>/', disp_detail),
]