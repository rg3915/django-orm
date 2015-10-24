from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse_lazy
from .lists import gender_list, treatment_list, status_list


class TimeStampedModel(models.Model):
    created = models.DateTimeField(
        _('criado em'), auto_now_add=True, auto_now=False)
    modified = models.DateTimeField(
        _('modificado em'), auto_now_add=False, auto_now=True)

    class Meta:
        abstract = True


class Person(models.Model):
    gender = models.CharField(_(u'gênero'), max_length=1, choices=gender_list)
    treatment = models.CharField(
        _('tratamento'), max_length=4, choices=treatment_list, blank=True)
    first_name = models.CharField(_('nome'), max_length=30)
    last_name = models.CharField(_('sobrenome'), max_length=30)
    birthday = models.DateTimeField(_('nascimento'), null=True, blank=True)
    email = models.EmailField(_('e-mail'), blank=True)
    active = models.BooleanField(_('ativo'), default=True)
    blocked = models.BooleanField(_('bloqueado'), default=False)

    class Meta:
        abstract = True

    def __str__(self):
        return self.first_name + " " + self.last_name

    full_name = property(__str__)


class Customer(Person):
    pass

    class Meta:
        ordering = ['first_name']
        verbose_name = 'cliente'
        verbose_name_plural = 'clientes'


class Seller(Person):
    internal = models.BooleanField(_('interno'), default=True)
    commissioned = models.BooleanField(_('comissionado'), default=True)
    commission = models.DecimalField(
        _(u'comissão'), max_digits=6, decimal_places=2, default=0.01, blank=True)

    class Meta:
        ordering = ['first_name']
        verbose_name = u'vendedor'
        verbose_name_plural = u'vendedores'


# Multi-Table Inheritance
class PF(Customer):
    cpf = models.CharField(_('CPF'), max_length=11)
    rg = models.CharField(_('RG'), max_length=10)

    class Meta:
        verbose_name = u'pessoa física'
        verbose_name_plural = u'pessoas físicas'


class PJ(Customer):
    cnpj = models.CharField(_('CNPJ'), max_length=14)
    ie = models.CharField(_('IE'), max_length=10)

    class Meta:
        verbose_name = u'pessoa jurídica'
        verbose_name_plural = u'pessoas jurídicas'


class Ordered(TimeStampedModel):
    customer = models.ForeignKey(
        'Customer', verbose_name=_('cliente'), related_name='cliente_pedido')
    status = models.CharField(
        _('status'), max_length=2, choices=status_list, default='pe')

    class Meta:
        ordering = ['-id']
        verbose_name = 'pedido'
        verbose_name_plural = 'pedidos'

    def __str__(self):
        return str(self.customer)


class Sale(models.Model):
    ordered = models.OneToOneField('Ordered', verbose_name=_('pedido'))
    paid = models.BooleanField(_('pago'), default=False)
    date_paid = models.DateTimeField(_('pago em'), null=True, blank=True)
    method = models.CharField(_('forma de pagto'), max_length=20, blank=True)
    deadline = models.CharField(
        _('prazo de entrega'), max_length=50, blank=True)

    class Meta:
        ordering = ['-id']
        verbose_name = 'venda'
        verbose_name_plural = 'vendas'

    def __str__(self):
        return str(self.ordered)


class Author(models.Model):
    name = models.CharField(_('nome'), max_length=50, unique=True)
    age = models.PositiveIntegerField(_('idade'))

    class Meta:
        ordering = ['name']
        verbose_name = 'autor'
        verbose_name_plural = 'autores'

    def __str__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField(_('nome'), max_length=50, unique=True)
    num_awards = models.PositiveIntegerField(_(u'prêmios'))

    class Meta:
        ordering = ['name']
        verbose_name = 'editora'
        verbose_name_plural = 'editoras'

    def __str__(self):
        return self.name


class Book(TimeStampedModel):
    isbn = models.IntegerField(null=True, blank=True)
    name = models.CharField(_('nome'), max_length=50)
    rating = models.FloatField(_(u'classificação'), default=1)
    authors = models.ManyToManyField('Author', verbose_name='autores')
    publisher = models.ForeignKey('Publisher', verbose_name='editora')
    price = models.DecimalField(_(u'preço'), max_digits=5, decimal_places=2)
    stock_min = models.PositiveIntegerField(_(u'Estoque mínimo'), default=0)
    stock = models.IntegerField(_('Estoque atual'), null=True, blank=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'livro'
        verbose_name_plural = 'livros'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('book_detail', kwargs={'pk': self.pk})


class Store(models.Model):
    name = models.CharField(_('nome'), max_length=50)
    books = models.ManyToManyField('Book', verbose_name='livros')

    class Meta:
        ordering = ['name']
        verbose_name = 'loja'
        verbose_name_plural = 'lojas'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('store_detail', kwargs={'pk': self.pk})
