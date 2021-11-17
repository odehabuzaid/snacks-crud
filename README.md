# Django CRUD
[Live Version ](https://django-snacks-crud.herokuapp.com/admin/)
- username : admin
- passowrd : admin@123

> Django CRUD Heroku Deployement

## Structure

<img src='https://i.ibb.co/b3xztMv/structure.jpg'>

## Deployment

1. add  [gunicorn](https://pypi.org/project/gunicorn/) [django-heroku](https://pypi.org/project/django-heroku/) to your project.

```bash
$poetry add gunicorn django-heroku
```

in case of troubles adding gunicorn , use :
```bash
$pip install gunicorn

# must be added to current virtual envirounment 
$poetry add gunicorn
```

2. open __project/settings.py__ 

```py
import django_heroku
.
.
.
# Activate Django-Heroku.
django_heroku.settings(locals())
```


3. Create `requirement.txt` file manualy in the root of reposotory directory .
```bash
$touch requirements.txt
# add the following to the file:
Django
django_heroku
gunicorn
# additional packages if exist
```
4. Create `Procfile` (Case-sensitive) file in the root of reposotory directory .
```bash
$touch Procfile
# add the following line
web: python manage.py runserver 0.0.0.0:$PORT

```
5. after pushing changes to github
6. log in to `heroku`
7. from the dashboard -> `new` select `Create new app`
8. enter application name -> click `create app`
9. from `Deployment method` section -> connect to github -> `search` your repository -> click `connect`
10. from deploy section (manual / auto) Choose a branch to deploy.
11. click `Deploy Branch`.

<img src='https://i.ibb.co/HrmhdhV/deployed.jpg' >

12. in the up-right corner of current page -> `more` -> `run console`  
do migrate & create a super user
    ```bash
    python manage.py migrate
    # OK
    python manage.py createsuperuser
    # follow createsuperuser prompt

    ```
1. open your app .

### _Note_ : your secret key is exposed in this case , if you would like to create a new secret key do the following :


```bash
$(venv) echo "SECRET_KEY=$(openssl rand -base64 32)" > .env

$(venv) python manage.py shell

>>> from django.core.management.utils import get_random_secret_key
>>> print(get_random_secret_key())
# secret key will appear here 
$5osg_xk6i)-r123rg83i9y7s9@bh&&vg@9u&@h7w&z25+7s$k
# remove the SECRET_KEY from settings.py
# in heroku -> Settings -> Reveal Config Vars -> add :
key : SECRET_KEY
value : # the above randomly generated secret key 
$5osg_xk6i)-r123rg83i9y7s9@bh&&vg@9u&@h7w&z25+7s$k

```

