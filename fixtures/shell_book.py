import random
import csv
from core.models import Book, Author, Publisher
from django.core.exceptions import ObjectDoesNotExist
from fixtures.gen_random_values import *

book_list = []

''' Lendo os dados de clientes_.csv '''
with open('fixtures/csv/books_.csv', 'r') as f:
    r = csv.DictReader(f)
    for dct in r:
        book_list.append(dct)
    f.close()

REPEAT = len(book_list)

for i in range(REPEAT):
    name_author = book_list[i]['authors']
    age = gen_age()
    ''' Para não criar atores duplicados ... '''
    try:
        ''' Com get pega o nome do ator. '''
        author = Author.objects.get(name=name_author)
    except ObjectDoesNotExist:
        ''' Se não existir, então cria o ator. '''
        Author.objects.create(
            name=name_author,
            age=age,
        )
    name_publisher = book_list[i]['publisher']
    num_awards = gen_age(1, 1000)
    ''' Para não criar editoras duplicadas ... '''
    try:
        ''' Com get pega o nome da editora. '''
        publisher = Publisher.objects.get(name=name_publisher)
    except ObjectDoesNotExist:
        ''' Se não existir, então cria a editora. '''
        Publisher.objects.create(
            name=name_publisher,
            num_awards=num_awards,
        )
    ''' Cadastra os livros '''
    publisher = Publisher.objects.get(name=name_publisher)
    name_book = book_list[i]['name']
    try:
        ''' Com get pega o nome do livro. '''
        book = Book.objects.get(name=name_book)
        ''' Inserindo os autores nos livros '''
        author = Author.objects.get(name=name_author)
        book.authors.add(author)
    except ObjectDoesNotExist:
        ''' Se não existir, então cria o livro. '''
        book_obj = Book(
            isbn=random.randint(1, 9999999999),
            name=name_book,
            rating=gen_decimal(3, 2),
            # author=author,
            publisher=publisher,
            price=gen_decimal(3, 2),
            stock_min=random.randint(1, 100),
            stock=random.randint(1, 1000),
        )
        book_obj.save()
        ''' Inserindo os autores nos livros '''
        book = Book.objects.get(pk=book_obj.id)
        author = Author.objects.get(name=name_author)
        book.authors.add(author)

print('%d Books salvo com sucesso.' % REPEAT)
