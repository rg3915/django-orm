install:
	pip install -r requirements.txt

migrate:
	./manage.py makemigrations
	./manage.py migrate

createuser:
	./manage.py createsuperuser --username='admin' --email=''

backup:
	./manage.py dumpdata core --format=json --indent=2 > fixtures.json

load:
	./manage.py loaddata fixtures.json

run:
	./manage.py runserver

shell_customer:
	./manage.py shell < fixtures/shell_customer.py

shell_seller:
	./manage.py shell < fixtures/shell_seller.py

shell_pf:
	./manage.py shell < fixtures/shell_pf.py

shell_pj:
	./manage.py shell < fixtures/shell_pj.py

shell_ordered:
	./manage.py shell < fixtures/shell_ordered.py

shell_sale:
	./manage.py shell < fixtures/shell_sale.py

shell_book:
	./manage.py shell < fixtures/shell_book.py

shell_store:
	./manage.py shell < fixtures/shell_store.py

pdf:
	latexmk -pdf -shell-escape django_orm.tex

pvc:
	latexmk -pdf -shell-escape -pvc django_orm.tex

pdf43:
	latexmk -pdf -shell-escape django_orm43.tex

pvc43:
	latexmk -pdf -shell-escape -pvc django_orm43.tex

clear:
	latexmk -c
	rm *.nav *.snm *.vrb

initial: install migrate createuser load

fixtures: shell_customer shell_seller shell_pf shell_pj shell_ordered shell_sale shell_book shell_store
