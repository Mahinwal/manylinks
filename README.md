## manylinks
### A Simple project Manylink app built with Django and templates styled with Bootstrap framework.
# Personal project to store multiple social media links.

### Login 
![login-screen](https://github.com/Mahinwal/manylinks/assets/26764519/173a9a90-473b-41b9-bddb-c3f6c808648c)
### Signup
![signup-screen](https://github.com/Mahinwal/manylinks/assets/26764519/032f5410-f6e4-46a3-9e8a-2970168f9394)

### My many link profile view
![profile-screen](https://github.com/Mahinwal/manylinks/assets/26764519/dea878c7-2019-4e73-bd32-ee3ab0bee472)


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
