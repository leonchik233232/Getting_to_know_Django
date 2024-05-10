    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django_dump_load_utf8',
    'catalog',
]


LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'UTC'



DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Фидбек от пользователя тут
FEEDBACK_FILE_PATH = BASE_DIR.joinpath('feedback.txt')