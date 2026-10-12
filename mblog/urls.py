from django.contrib import admin
from django.urls import path

from mysite.views import (
    homepage,
    showpost,
    about,
    listing,
    disp_detail,
    news_live,
    carlist,
    carprice,
)


urlpatterns = [

    # Django Admin
    path(
        'admin/',
        admin.site.urls
    ),


    # 首頁
    path(
        '',
        homepage,
        name='home'
    ),


    # 部落格文章
    path(
        'post/<slug:slug>/',
        showpost,
        name='show-post'
    ),


    # 關於我
    path(
        'about/',
        about,
        name='about'
    ),


    # 二手手機
    path(
        'list/',
        listing,
        name='product-list'
    ),

    path(
        'list/<str:sku>/',
        disp_detail,
        name='product-detail'
    ),


    # 新聞直播
    path(
        'news/',
        news_live,
        name='news-live-home'
    ),

    path(
        'news/<int:tvno>/',
        news_live,
        name='news-live'
    ),


    # 二手車庫存
    path(
        'carlist/',
        carlist,
        name='carlist-home'
    ),

    path(
        'carlist/<int:maker>/',
        carlist,
        name='carlist-url'
    ),


    # 二手車價格
    path(
        'carprice/',
        carprice,
        name='carprice-home'
    ),

    path(
        'carprice/<int:maker>/',
        carprice,
        name='carprice-url'
    ),
]