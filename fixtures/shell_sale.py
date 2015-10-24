import random
from core.models import Ordered, Sale
from fixtures.gen_random_values import *

ordered_len = Ordered.objects.all().count()
j = 0

for i in range(1, ordered_len + 1):
    ordered = Ordered.objects.get(pk=i)
    paid = random.choice([1, 0])
    if paid == 1:
        date_paid = gen_timestamp(2014, 2015) + '+00'
    else:
        date_paid = None
    if ordered.status == 'co':
        Sale.objects.create(
            ordered=ordered,
            paid=paid,
            date_paid=date_paid,
            method='débito',
            deadline='30 dias'
        )
        j += 1

print('%d Sales salvo com sucesso.' % j)
