from django.conf.urls import include, url
from django.contrib import admin
from core import views as v

urlpatterns = [
    url(r'^$', v.home, name='home'),
    url(r'^customers/$', v.customer_list, name='customer_list'),

    url(r'^books/$', v.BookList.as_view(), name='book_list'),
    url(r'^books/(?P<pk>\d+)/$', v.BookDetail.as_view(), name='book_detail'),

    url(r'^stores/$', v.StoreList.as_view(), name='store_list'),
    url(r'^stores/(?P<pk>\d+)/$', v.StoreDetail.as_view(), name='store_detail'),

    url(r'^admin/', include(admin.site.urls)),
]
