import os
from pathlib import Path
from django.contrib.messages import constants as messages
import django_heroku


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-o(3y^em*!y70@r2cm(ae6ga5blg9wfc$qur5mo(ms^no^5)2e4'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'whitenoise.runserver_nostatic',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blogapp',
    'tinymce',
    'django_filters',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'blog.urls'

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

WSGI_APPLICATION = 'blog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/


STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

WHITENOISE_USE_FINDERS = True

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')


STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


TINYMCE_DEFAULT_CONFIG = {
    'selector': 'textarea',
    'theme': 'modern',
    'block_formats': 'Paragraph=p; Heading 1=h1; Heading 2=h2; Heading 3=h3; Heading 4=h4; Heading 5=h5; Heading '
                     '6=h6; Preformatted=pre',
    'plugins': 'media link image preview codesample contextmenu table code textcolor lists',
    'extended_valid_elements': "iframe[src|frameborder|style|scrolling|class|width|height|name|align]",
    'menubar': False,
    'toolbar': 'undo redo | bold italic underline fontselect fontsizeselect | alignleft aligncenter alignright '
               ' blockquote alignjustify backcolor forecolor '
                ' bullist numlist lineheight | outdent indent | table | link media image | codesample | preview code',
    'toolbar_persist': True,
    'toolbar_sticky': True,
    'contextmenu': 'formats blocks | link image media',
    'inline': False,
    'statusbar': True,
    'height': 420,
    'branding': False,
    'toolbar_mode ': 'sliding',
    'font_formats': 'Andale Mono=andale mono,times; Arial=arial,helvetica,sans-serif; Arial Black=arial black,'
                    'avant garde; Balsamiq Sans=balsamiq sans; Book Antiqua=book antiqua,palatino; Calibri=calibri; '
                    'Caveat=caveat; Caveat Brush=caveat brush; Comic Sans MS=comic sans ms,sans-serif; Courier '
                    'New=courier new,courier; Georgia=georgia,palatino; Helvetica=helvetica; Merriweather '
                    'Sans=merriweather sans Impact=impact, '
                    'chicago; Oswald=oswald; Open Sans=open sans; Open Sans Condensed=open sans condensed; '
                    'Roboto=roboto; Roboto Condensed=roboto condensed; Roboto Slab=roboto slab; Source Sans '
                    'Pro=source sans pro; Symbol=symbol; Tahoma=tahoma,arial,helvetica,sans-serif; Terminal=terminal, '
                    'monaco; Times New Roman=times new roman,times; Trebuchet MS=trebuchet ms,'
                    'geneva; Verdana=verdana,geneva; Webdings=webdings; Wingdings=wingdings,zapf dingbats;',
    'fontsize_formats': '8pt 10pt 12pt 14pt 16pt 18pt 24pt 36pt 48pt',
    'lineheight_formats': '1 1.1 1.2 1.3 1.4 1.5 2',
    'max_width': 1300,
    'resize': True,
    'style_formats': [
        {'title': 'Bold text', 'inline': 'b'},
        {'title': 'Red background', 'inline': 'span', 'styles': {'background-color': '#ff0000'}},
        {'title': 'Block', 'block': 'div', 'styles': {'background-color': '#FFFAF0'}},
    ], }

TINYMCE_COMPRESSOR = True


LOGIN_REDIRECT_URL = 'index'
LOGOUT_REDIRECT_URL = 'login'

MESSAGE_TAGS = {
    messages.DEBUG: 'alert-info',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}

django_heroku.settings(locals())
