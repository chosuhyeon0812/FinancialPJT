"""
Django settings for back project.

Generated by 'django-admin startproject' using Django 4.2.4.
s
For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-z102w&z6e^si#4%n*x5#(nma18yc)$$e=dw)b*74ojzp88&vy%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    # 설치한 앱
    'accounts',
    'articles',
    'deposits',

    # DRF
    'rest_framework',
    'rest_framework.authtoken',

    # API 문서화
    'drf_spectacular',

    # auth 권한 설정
    'django.contrib.sites',
    'dj_rest_auth',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'dj_rest_auth.registration',

    # url 권한 설정
    'corsheaders',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

SITE_ID = 1

# DRF auth settings
# Token 인증을 기본으로 사용하도록 설정
# 11.16 23:05 경범 수정 : REST_FRAMEWORK 코드 주석 해제
REST_FRAMEWORK = {
    # DRF를 위한 OPEN API 문서화
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
        
    # Authentication
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
    # permission
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
}

# 11.17 10:14 경범 수정 코드 추가
# 미들웨어 건 들 지 말 것.

MIDDLEWARE = [
    "allauth.account.middleware.AccountMiddleware",
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]



CORS_ALLOWED_ORIGINS = [
    'http://127.0.0.1:5173',
    'http://localhost:5173',
]

ROOT_URLCONF = 'back.urls'

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

WSGI_APPLICATION = 'back.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# 사용자 수정
AUTH_USER_MODEL = 'accounts.User'

# ALL AUTH 수정
# dj-rest-auth 는 email 을 필수적으로 사용하도록 구현되어 있으므로, 해당 사항을 수정
# 11.16 23:05 경범 수정 : 171,172 코드 주석 해제
ACCOUNT_EMAIL_REQUIRED = False
ACCOUNT_EMAIL_VERIFICATION = None
# # django 인증 시스템에서 사용할 백엔드 클래스 지정
# # 기본 인증 백엔드와 allauth 패키지에서 제공하는 인증 백엔드를 모두 사용하겠다는 설정.
# 11.16 23:05 경범 수정 : 176-186 코드 주석 해제
AUTHENTICATION_BACKENDS = (
    # django 기본 인증 백엔드
    "django.contrib.auth.backends.ModelBackend",
    # django-allauth 패키지에서 제공하는 인증 백엔드 클래스.
    "allauth.account.auth_backends.AuthenticationBackend",
)


REST_AUTH = {
'REGISTER_SERIALIZER': 'accounts.serializers.CustomRegisterSerializer',
}

ACCOUNT_ADAPTER = 'accounts.models.CustomAccountAdapter'

