# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-#(#zs989sho)+u7_kpur4%54keum#kv@q&9!^-rf81sx@z9#me'

DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'music_library_database',
        'USER': 'root',
        'PASSWORD': 'password',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'autocommit':True
        }
    }
}