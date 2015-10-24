import random
from core.models import Customer, Ordered

REPEAT = 50
customer_len = Customer.objects.all().count()

for i in range(REPEAT):
    c = random.randint(1, customer_len)
    customer = Customer.objects.get(pk=c)
    status = random.choice(['ca', 'pe', 'co'])
    Ordered.objects.create(
        customer=customer,
        status=status
    )

print('%d Ordereds salvo com sucesso.' % REPEAT)
