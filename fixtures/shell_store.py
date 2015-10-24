import random
import csv
from core.models import Book, Store
from fixtures.gen_random_values import *

store_list = []

''' Lendo os dados de stores_.csv '''
with open('fixtures/csv/stores_.csv', 'r') as f:
    r = csv.DictReader(f)
    for dct in r:
        store_list.append(dct)
    f.close()

REPEAT = len(store_list)
BOOK_COUNT = Book.objects.all().count()

for i in range(REPEAT):
    ''' pegando o nome da loja no dicionário '''
    name_store = store_list[i]['store']
    ''' criando uma instância do objeto Store '''
    store_obj = Store(name=name_store)
    ''' salvando o objeto '''
    store_obj.save()
    ''' Inserindo os livros nas lojas '''
    n = random.randint(1, BOOK_COUNT)
    for j in range(n):
        ''' usando get para pegar o id da loja '''
        store = Store.objects.get(pk=store_obj.id)
        ''' retornando todos os livros '''
        book_obj = Book.objects.all()
        ''' list compreension '''
        l = [i.id for i in book_obj]
        ''' escolhendo um dos ids randomicamente '''
        v = random.randint(l[0], l[len(l) - 1])
        book = book_obj.get(pk=v)
        ''' inserindo o livro na loja '''
        store.books.add(book)

print('%d Books salvo com sucesso.' % REPEAT)
