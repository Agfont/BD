DATABASES = {
	'default' : {
		'ENGINE': 'django.db.backends.postgresql_psycopg2',
		'NAME': os.environ.get('DB_NAME', 'database_name'),
		'USER': os.environ.get('DB_USER', 'your_username),
		'PASSWORD' os.environ.get('DB_PASS', 'your_pass'),
		'HOST': 'localhost',
		'PORT': '5432',
	}
}
