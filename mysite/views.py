from django.shortcuts import redirect, render
from django.http import Http404
from datetime import datetime

from mysite.models import Post, Product


# =========================================
# 新聞直播頻道
# =========================================

TV_LIST = [
    {
        'name': '中天',
        'tvcode': '5xPxrn9kdME',
        'official_url': 'https://www.ctitv.com.tw/'
    },
    {
        'name': '華視',
        'tvcode': 'SS917AxC04c',
        'official_url': 'https://news.cts.com.tw/live'
    },
    {
        'name': '民視',
        'tvcode': 'yguQ1SzPM5U',
        'official_url': 'https://www.ftvnews.com.tw/'
    },
    {
        'name': '中視',
        'tvcode': '_HBqlHJJiOw',
        'official_url': 'https://www.ctv.com.tw/'
    },
]


# =========================================
# 首頁
# =========================================

def homepage(request):
    posts = Post.objects.all()
    now = datetime.now()

    return render(
        request,
        'index.html',
        {
            'posts': posts,
            'now': now,
        }
    )


# =========================================
# 單篇文章
# =========================================

def showpost(request, slug):

    try:
        post = Post.objects.get(slug=slug)

        return render(
            request,
            'post.html',
            {
                'post': post,
            }
        )

    except Post.DoesNotExist:
        return redirect('/')


# =========================================
# 關於我
# =========================================

def about(request):

    return render(
        request,
        'about.html'
    )


# =========================================
# 二手手機列表
# =========================================

def listing(request):

    products = Product.objects.all()

    return render(
        request,
        'list.html',
        {
            'products': products,
        }
    )


# =========================================
# 二手手機詳細資料
# =========================================

def disp_detail(request, sku):

    try:

        p = Product.objects.get(
            sku=sku
        )

    except Product.DoesNotExist:

        raise Http404(
            '找不到指定的品項編號'
        )

    return render(
        request,
        'disp.html',
        {
            'p': p,
        }
    )


# =========================================
# 新聞直播
# =========================================

def news_live(request, tvno=0):

    if not 0 <= tvno < len(TV_LIST):

        return redirect(
            'news-live-home'
        )

    tv_list = TV_LIST
    tv = tv_list[tvno]

    posts = Post.objects.all()

    now = datetime.now()

    return render(
        request,
        'index.html',
        {
            'tv': tv,
            'tvno': tvno,
            'tv_list': tv_list,
            'posts': posts,
            'now': now,
        }
    )


# =========================================
# 二手車庫存
# P51～P55
# =========================================

def carlist(request, maker=0):

    car_maker = [
        'SAAB',
        'Ford',
        'Honda',
        'Mazda',
        'Nissan',
        'Toyota',
    ]

    car_list = [

        [],

        [
            'Fiesta',
            'Focus',
            'Modeo',
            'EcoSport',
            'Kuga',
            'Mustang',
        ],

        [
            'Fit',
            'Odyssey',
            'CR-V',
            'City',
            'NSX',
        ],

        [
            'Mazda3',
            'Mazda5',
            'Mazda6',
            'CX-3',
            'CX-5',
            'MX-5',
        ],

        [
            'Tida',
            'March',
            'Livina',
            'Sentra',
            'Teana',
            'X-Trail',
            'Juke',
            'Murano',
        ],

        [
            'Camry',
            'Altis',
            'Yaris',
            '86',
            'Prius',
            'Vios',
            'RAV4',
            'Wish',
        ],
    ]

    if not 0 <= maker < len(car_maker):

        maker = 0

    maker_name = car_maker[maker]

    cars = car_list[maker]

    return render(
        request,
        'carlist.html',
        {
            'car_maker': car_maker,
            'maker': maker,
            'maker_name': maker_name,
            'cars': cars,
        }
    )


# =========================================
# 二手車價格
# P62～P65
# =========================================

def carprice(request, maker=0):

    car_maker = [
        'Ford',
        'Honda',
        'Mazda',
    ]

    car_list = [

        [
            {
                'model': 'Fiesta',
                'price': 203500
            },
            {
                'model': 'Focus',
                'price': 605000
            },
            {
                'model': 'Mustang',
                'price': 900000
            },
        ],

        [
            {
                'model': 'Fit',
                'price': 450000
            },
            {
                'model': 'City',
                'price': 150000
            },
            {
                'model': 'NSX',
                'price': 1200000
            },
        ],

        [
            {
                'model': 'Mazda3',
                'price': 329999
            },
            {
                'model': 'Mazda5',
                'price': 603000
            },
            {
                'model': 'Mazda6',
                'price': 850000
            },
        ],
    ]

    if not 0 <= maker < len(car_maker):

        maker = 0

    maker_name = car_maker[maker]

    cars = car_list[maker]

    return render(
        request,
        'carprice.html',
        {
            'car_maker': car_maker,
            'maker': maker,
            'maker_name': maker_name,
            'cars': cars,
        }
    )