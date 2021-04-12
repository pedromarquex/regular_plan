run:
	python manage.py runserver
migrate:
	python manage.py makemigrations
	python manage.py migrate
test:
	python manage.py test
seed:
	python manage.py loaddata user.json
	python manage.py loaddata plan.json
celery:
	celery -A regular_plan worker -l info
