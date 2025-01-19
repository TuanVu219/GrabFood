from pathlib import Path
from dotenv import load_dotenv
import os
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

SECRET_KEY = os.environ.get("SECRET_KEY")
DEBUG = int(os.environ.get("DEBUG", default=0))
ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS").split(" ")

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions', #Great packaged to access abstract models
    'django_filters', #Used with DRF
    'rest_framework', #DRF package
    'GrabFood', # New app
    'rest_framework.authtoken'
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

ROOT_URLCONF = 'PBL5.urls'

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

WSGI_APPLICATION = 'PBL5.wsgi.application'

ROOT_URLCONF = 'PBL5.urls'

AUTH_USER_MODEL = 'GrabFood.User'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


REST_FRAMEWORK = {
    # Loại bỏ JSON:API exception handler và thay bằng mặc định của DRF
    'EXCEPTION_HANDLER': 'rest_framework_json_api.exceptions.exception_handler',
    # Sử dụng JSONParser của DRF thay vì JSON:API
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',  # Phân tích yêu cầu JSON thuần túy
    ),

    # Sử dụng token authentication của DRF
   'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],

    # Sử dụng JSONRenderer của DRF để trả về JSON thuần túy
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',  # Trả về dữ liệu dưới dạng JSON
        'rest_framework.renderers.BrowsableAPIRenderer',  # Cho phép duyệt API qua trình duyệt
    ),

    # Metadata mặc định của DRF
    'DEFAULT_METADATA_CLASS': 'rest_framework.metadata.SimpleMetadata',

    # Các filter backend mặc định của DRF
    'DEFAULT_FILTER_BACKENDS': (
        'rest_framework.filters.OrderingFilter',
        'rest_framework.filters.SearchFilter',
        'django_filters.rest_framework.DjangoFilterBackend',  # Dùng filter backend của Django Filters
    ),

    # Param tìm kiếm mặc định
    'SEARCH_PARAM': 'search',

    # Cấu hình cho các lớp renderer trong môi trường test
    'TEST_REQUEST_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',  # Sử dụng JSONRenderer cho môi trường test
    ),
    'TEST_REQUEST_DEFAULT_FORMAT': 'json',  # Định dạng mặc định là JSON
}

