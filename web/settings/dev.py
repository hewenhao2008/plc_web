# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'plc_web',
        'USER': 'root',
        'PASSWORD': 'touhou',
        'HOST': '127.0.0.1',
        'PORT': 3306
    }
}
