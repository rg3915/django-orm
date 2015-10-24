from django.contrib import admin
from .models import Customer, Seller, Ordered, Sale, Author, Publisher, Book, Store, PF, PJ
# from .models import Person, Product


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('gender', 'treatment', '__str__',
                    'birthday', 'email', 'active', 'blocked')


class SellerAdmin(admin.ModelAdmin):
    list_display = ('gender', 'treatment', '__str__',
                    'birthday', 'email', 'active', 'blocked', 'internal', 'commissioned', 'commission')


class OrderedAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'status', 'created')
    list_filter = ('status',)


class SaleAdmin(admin.ModelAdmin):
    list_display = ('id', 'ordered', 'date_paid', 'method', 'deadline', 'paid')


class PFAdmin(admin.ModelAdmin):
    list_display = ('gender', 'treatment', '__str__',
                    'birthday', 'email', 'cpf', 'rg', 'active', 'blocked')


class PJAdmin(admin.ModelAdmin):
    list_display = ('gender', 'treatment', '__str__',
                    'birthday', 'email', 'cnpj', 'ie', 'active', 'blocked')

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Seller, SellerAdmin)
admin.site.register(Ordered, OrderedAdmin)
admin.site.register(Sale, SaleAdmin)
admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(Book)
admin.site.register(Store)
admin.site.register(PF, PFAdmin)
admin.site.register(PJ, PJAdmin)

'''
admin.site.register(Person)
admin.site.register(Product)
'''
