## manylinks

Personal project to store multiple social media links.
### A Simple project Manylink app built with Django and templates styled with Bootstrap framework.

Running the Project Locally
### First, clone the repository to your local machine :
git clone https://github.com/Mahinwal/manylinks.git

### Create a virtual environment :
```$ python -m virtualenv venv```

### Activate the virtual environment on Linux :
```$ source venv/bin/activate```

### Install the requirements :
```$ pip install -r requirements.txt```

### Run collect static :
```$ python manage.py collectstatic```

#### To create an superuser account, use this command :
```$ python manage.py createsuperuser```
### Apply the migrations :
```$ python manage.py migrate```
### Finally, run the development server :
```$ python manage.py runserver```

### The project will be available at : http://localhost:8000
