import os
from decouple import Csv, config

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', cast=bool, default=False)

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ecovias'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'watcher.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'watcher.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Recife'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

BASE_URL = 'https://api.ecorodovias.com.br/anonymous/ecorodovias-portal/ecovias/playful-map'
BING_KEY = config('BING_KEY')

IMAGES = [
    {
        'description': 'Mapa do Transito',
        'url': 'https://dev.virtualearth.net/REST/V1/Imagery/Map/Road/-23.890673%2C-46.485485/12?mapSize=600,600&format=png&mapLayer=TrafficFlow&key=' + BING_KEY
    },
    {
        'description': 'Planalto Imigrantes Km.20',
        'url': 'http://api.ecorodovias.com.br/anonymous/ecorodovias-portal/ecovias/boletim/camera/5'
    },
    {
        'description': 'Pedágio Imigrantes Km.32',
        'url': 'http://api.ecorodovias.com.br/anonymous/ecorodovias-portal/ecovias/boletim/camera/4'
    },
    {
        'description': 'Interligação Planalto Km.40',
        'url': 'http://api.ecorodovias.com.br/anonymous/ecorodovias-portal/ecovias/boletim/camera/15'
    },
    {
        'description': 'Serra Imigrantes Km.48',
        'url': 'http://api.ecorodovias.com.br/anonymous/ecorodovias-portal/ecovias/boletim/camera/6'
    },
    {
        'description': 'Anchieta (Ribeirão Couros) Km. 13',
        'url': 'http://api.ecorodovias.com.br/anonymous/ecorodovias-portal/ecovias/boletim/camera/11'
    },
    {
        'description': 'Pedágio Anchieta Km.31',
        'url': 'http://api.ecorodovias.com.br/anonymous/ecorodovias-portal/ecovias/boletim/camera/14'
    },
]

EMAIL_HOST = config('EMAIL_HOST')
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
EMAIL_PORT = config('EMAIL_PORT')
EMAIL_FROM = config('EMAIL_FROM')

