# python_snake

## snake_1.py

Simple snake game with Python.

## snake_2.py

- Add "check" for collision with the snake's body if the user presses the opposite direction of the snake's current direction.
- Add go through the wall feature.
- Fix bug: when a snake hits the wall, the snake was adding a new segment to the body.

## snake_3.py

- Add lives functionality.
- Restructure the code.

## snake_4.py
- Add blessed

## snake_5.py
- Restructure the code based on https://replit.com/talk/share/imagehttpsstoragegoogleapiscom/125833/576335
- fix terminal
- add fruits random-appearance

## snake_6.py
- Code taken from https://replit.com/talk/share/snake-game-but-youre-the-food/126048
- add fruits random-appearance







## Set up for the Django project:

1. User stories on GitHub;
2. Project Board on GitHub connecting to User stories;
3. Basic wireframe, commit to Github;
4. Build your ERD (Entity Relationship Diagram) of your models;
5. Initialize your Django project: 

`django-admin startproject library`

6. Create your app:

`python3 manage.py startapp sales`

7. Start your server:

`python3 manage.py runserver`

8. Create your models;

9. Pack up your model changes into a migration file:

`python3 manage.py makemigrations`

10. Migrate - apply the migration to the database:

`python3 manage.py migrate`

11. Create your superuser:

`python3 manage.py createsuperuser`

12. Register your models in admin.py;

13. Add your allauth setup

14. Deploy to Heroku/Render