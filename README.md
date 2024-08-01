to use website run the following:

python manage.py makemigrations

python manage.py migrate

python manage.py runserver


then, on a seperate terminal, run 

wayback --record

This will begin a local webserver. However, none of the website is accessible without an account. to create one, use the following:

python manage.py createsuperuser

once the user is created, use the credential to login in to the website at 127.0.0.1:8000. by default, the super user does not have permission to modify collections. to do so, go to manage users, select detail on your superuser, select edit profile, and check off the collection manager box.
