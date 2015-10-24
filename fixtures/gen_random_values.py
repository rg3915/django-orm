# -*- coding: utf-8 -*-
import random
import rstr
import datetime
from decimal import Decimal


def gen_age(min_age=15, max_age=99):
    # gera numeros inteiros entre 15 e 99
    return random.randint(min_age, max_age)


def gen_doc(doc='cpf'):
    if doc == 'cpf':
        return rstr.rstr('1234567890', 11)
    elif doc == 'cnpj':
        return rstr.rstr('1234567890', 14)
    elif doc == 'rg':
        return rstr.rstr('1234567890', 10)


def gen_ncm():
    return rstr.rstr('123456789', 8)


def gen_phone():
    # gera um telefone no formato (xx) xxxx-xxxx
    return '({0}) {1}-{2}'.format(
        rstr.rstr('1234567890', 2),
        rstr.rstr('1234567890', 4),
        rstr.rstr('1234567890', 4))


def gen_timestamp(min_year=1915, max_year=1996):
    # gera um datetime no formato yyyy-mm-dd hh:mm:ss.000000
    year = random.randint(min_year, max_year)
    month = random.randint(11, 12)
    day = random.randint(1, 28)
    hour = random.randint(1, 23)
    minute = random.randint(1, 59)
    second = random.randint(1, 59)
    microsecond = random.randint(1, 999999)
    date = datetime.datetime(
        year, month, day, hour, minute, second, microsecond).isoformat(" ")
    return date


def gen_decimal(max_digits, decimal_places):
    num_as_str = lambda x: ''.join(
        [str(random.randint(0, 9)) for i in range(x)])
    return Decimal("%s.%s" % (num_as_str(max_digits - decimal_places),
                              num_as_str(decimal_places)))
gen_decimal.required = ['max_digits', 'decimal_places']


def gen_ipi():
    num_as_str = lambda x: ''.join(
        [str(random.randint(0, 9)) for i in range(x)])
    return Decimal("0.%s" % (num_as_str(2)))


def gen_city():
    list_city = [
        [u'Belo Horizonte', 'MG'],
        [u'Belém', 'PA'],
        [u'Brasília', 'DF'],
        [u'Campinas', 'SP'],
        [u'Campo Grande', 'MS'],
        [u'Curitiba', 'PR'],
        [u'Duque de Caxias', 'RJ'],
        [u'Fortaleza', 'CE'],
        [u'Goiânia', 'GO'],
        [u'Guarulhos', 'SP'],
        [u'Maceió', 'AL'],
        [u'Manaus', 'AM'],
        [u'Natal', 'RN'],
        [u'Porto Alegre', 'RS'],
        [u'Recife', 'PE'],
        [u'Rio de Janeiro', 'RJ'],
        [u'Salvador', 'BA'],
        [u'São Gonçalo', 'RJ'],
        [u'São Luís', 'MA'],
        [u'São Paulo', 'SP'],
    ]
    return random.choice(list_city)


def gen_city_online():
    # https://raw.githubusercontent.com/felipefdl/cidades-estados-brasil-json/master/Cidades.json
    # fazer leitura de json, importar os dados e randomizar numa lista
    pass
