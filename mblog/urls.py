from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

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

from market import views as market_views


urlpatterns = [

    # Django Admin
    path(
        'admin/',
        admin.site.urls
    ),

    # 原本首頁
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

    # 原本二手商品
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

    # Unit 6 中古手機賣場
    path(
        'market/',
        market_views.index,
        name='market-home'
    ),

    # Unit 6 商品詳細頁
    path(
        'detail/<int:id>',
        market_views.detail,
        name='detail-url'
    ),

] + static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)