INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'book_store.appsBookStoreConfig',
]

DATABASES = {
    'default': {
        'ENGINE' : 'django.db.backends.mysql',
        'NAME' : 'mydatabase',
        'USER' : 'mydatabaseuser',
        'PASSWORD' : 'mypassword',
        'HOST' : 'localhost',
        'PORT' : '3306',
}
}
 