
# Vision Studios

## Requirements
- asgiref==3.4.1
- dj-database-url==0.5.0
- Django==3.2.7
- django-crispy-forms==1.13.0
- gunicorn==20.1.0
- psycopg2-binary==2.9.1
- pytz==2021.3
- sqlparse==0.4.2
- typing-extensions==3.10.0.2

<br />

## How to use the code

**Step #1** -  Clone the sources

```bash
$ git clone https://github.com/sdet-ro/blidarVision.git
$ cd blidarVision
```

**Step #2** - Create a virtual environment

```bash
$ # Virtualenv modules installation (Unix based systems)
$ virtualenv env
$ source env/bin/activate
$
$ # Virtualenv modules installation (Windows based systems)
$ # virtualenv env
$ # .\env\Scripts\activate
```

**Step #3** - Install dependencies using PIP

```bash
$ pip install -r requirements.txt
```

**Step #4** - Start the API server

```bash
$ python manage.py migrate
$ python manage.py runserver
```

The API server will start using the default port `8000`.

<br />

## Deploying to DigitalOcean
<br />

**Configuring app**
```bash
- Click the Edit link next to the `Run commands`
  # gunicorn --worker-tmp-dir /dev/shm isionStudios.wsgi
- Click the Edit link next to the `Environment Variables`
  # DJANGO_ALLOWED_HOSTS -> ${APP_DOMAIN}
  # DATABASE_URL -> ${mydb.DATABASE_URL}
  # DEBUG -> True
  # DJANGO_SECRET_KEY -> 5.?('D<dZ,$)Jc_
        Don’t forget to click the Encrypt check box 
- To set up your database, click the Add a Database button.
```

**Finalize and Launch**

     Select "Professional App" and then click "Launch App" at the bottom. Your app will build and deploy:

**Finalize and Launch**

 Go to "Console tab" and perform the Django first launch tasks by running the following commands:
 ```bash
    python manage.py migrate

    python manage.py createsuperuser
```
Type admin name, email, password

## Reference this url for more detail.

   https://www.digitalocean.com/community/tutorials/how-to-deploy-django-to-app-platform

## Manage Domain

   https://docs.digitalocean.com/products/app-platform/how-to/manage-domains/


