to use website run the following:
python manage.py migrate
python manage.py runserver

This will begin a local webserver. However, none of the website is accessible without an account. to create one, use the following:

python manage.py createsuperuser

once the user is created, use the credential to login in to the website. by default, the super user does not have permission to modify collections. to do so, go to manage users, select detail on your superuser, select edit profile, and check off the collection manager box.
