
import os

BASE_DIR = os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))

SECRET_KEY = 'gig3521ck+d*wuz-l@5^nvv2_1cqtfzjfhnp$qhz9x1-cctn$4'


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'social.apps.django_app.default',
    'django_registration',
    'social_django',

    'cursos',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'myweb.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social.apps.django_app.context_processors.backends',
                'social.apps.django_app.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'myweb.wsgi.application'

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

LANGUAGE_CODE = 'es-PE'

TIME_ZONE = 'America/Lima'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = os.path.join(BASE_DIR, 'static'),

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'  # servicio de correo smtp
EMAIL_PORT = 25
EMAIL_HOST_USER = 'jmexebio27@gmail.com'  # id de correo electrónico
EMAIL_HOST_PASSWORD = 'jesus2711'  # password
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
SERVER_EMAIL = EMAIL_HOST_USER
ACCOUNT_ACTIVATION_DAYS = 7

AUTHENTICATION_BACKENDS = (
    'social.backends.facebook.FacebookAppOAuth2',
    'social.backends.facebook.FacebookOAuth2',
    'social.backends.twitter.TwitterOAuth',
    'social.backends.google.GoogleOpenId',
    'social.backends.google.GoogleOAuth2',
    'social.backends.google.GoogleOAuth',
    'django.contrib.auth.backends.ModelBackend'
)
SOCIA_AUTH_LOGIN_REDIRECT_URL = '/'
LOGIN_REDIRECT_URL = '/'
SOCIAL_AUTH_TWITTER_KEY = 'vPR7TESmRImP7ktjNP3o6z6i6'
SOCIAL_AUTH_TWITTER_SECRET = 'GpKa6YIXdJDxgVv8xW7B2qIyej16tj1XUPheylEHXgfdSoBWaQ'

SOCIAL_AUTH_FACEBOOK_KEY = '494411674440568'
SOCIAL_AUTH_FACEBOOK_SECRET = 'cdfbb10628adf313138325026e7c628f'

SOCIAL_AUTH_GOOGLE_KEY = os.environ.get("GOOGLE_KEY")
SOCIAL_AUTH_GOOGLE_SECRET = os.environ.get("GOOGLE_SECRET")
