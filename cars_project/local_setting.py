# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-=-om6^&c^=r^&thr=%bux3apgw8=5^cq6=#eby07@qr7a0qc94'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cars_database',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'password'
    }
}