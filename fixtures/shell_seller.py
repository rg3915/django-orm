import random
from core.models import Seller
from fixtures.gen_random_values import *
from fixtures.gen_names import *

REPEAT = 20

for i in range(REPEAT):
    g = random.choice(['M', 'F'])
    if g == 'M':
        treatment = gen_male_first_name()['treatment']
        first_name = gen_male_first_name()['first_name']
    else:
        treatment = gen_female_first_name()['treatment']
        first_name = gen_female_first_name()['first_name']
    last_name = names.get_last_name()
    birthday = gen_timestamp() + '+00'
    email = first_name[0].lower() + '.' + last_name.lower() + '@example.com'
    active = random.choice([1, 0])
    blocked = random.choice([1, 0])
    internal = random.choice([1, 0])
    commissioned = random.choice([1, 0])
    commission = random.choice([0.01, 0.02, 0.03, 0.04, 0.05])
    Seller.objects.create(
        gender=g,
        treatment=treatment,
        first_name=first_name,
        last_name=last_name,
        birthday=birthday,
        email=email,
        active=active,
        blocked=blocked,
        internal=internal,
        commissioned=commissioned,
        commission=commission
    )

print('%d Sellers salvo com sucesso.' % REPEAT)
