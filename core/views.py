from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.conf import settings
from django.db.models import Q
from django.views.generic import TemplateView, ListView, DetailView
from .models import Customer, Book, Store


def home(request):
    return render(request, 'index.html')


def customer_list(request):
    customers_all = Customer.objects.all()
    ''' filtra os clientes '''
    q = request.GET.get('search_box')
    if q:
        customers_all = customers_all.filter(
            Q(first_name__icontains=q) |
            Q(last_name__icontains=q)
        )
    ''' conta os clientes '''
    count = customers_all.count()

    paginator = Paginator(customers_all, 8)  # mostra 8 itens por pagina
    page = request.GET.get('page')
    try:
        customers = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        customers = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        customers = paginator.page(paginator.num_pages)
    ctx = {'customers': customers, 'count': count, 'name_plural': 'clientes'}
    return render(request, 'core/customer_list.html', ctx)


class CounterMixin(object):

    def get_context_data(self, **kwargs):
        ''' counter registers '''
        context = super(CounterMixin, self).get_context_data(**kwargs)
        context['count'] = self.get_queryset().count()
        return context


class NameSearchMixin(object):

    def get_queryset(self):
        queryset = super(NameSearchMixin, self).get_queryset()
        q = self.request.GET.get('search_box')
        if q:
            return queryset.filter(name__icontains=q)
        return queryset


class BookList(CounterMixin, NameSearchMixin, ListView):
    template_name = 'core/book_list.html'
    model = Book
    context_object_name = 'books'
    paginate_by = 7

    def get_context_data(self, **kwargs):
        context = super(BookList, self).get_context_data(**kwargs)
        context['name_plural'] = 'livros'
        return context

    # def get_queryset(self):
    #     ''' use prefetch_related for m2m performance '''
    #     b = Book.objects.prefetch_related('authors').all()
    #     return b


class BookDetail(DetailView):
    template_name = 'core/book_detail.html'
    model = Book


class StoreList(CounterMixin, NameSearchMixin, ListView):
    template_name = 'core/store_list.html'
    model = Store
    context_object_name = 'stores'

    def get_context_data(self, **kwargs):
        context = super(StoreList, self).get_context_data(**kwargs)
        context['name_plural'] = 'lojas'
        return context

    # def get_queryset(self):
    #     ''' use prefetch_related for m2m performance '''
    #     s = Store.objects.prefetch_related('books').all()
    #     return s


class StoreDetail(DetailView):
    template_name = 'core/store_detail.html'
    model = Store
