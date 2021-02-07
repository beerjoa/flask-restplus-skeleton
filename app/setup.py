from setuptools import setup, find_packages

setup(
    name='sample.flask-restplus-skeleton',
    version='1.0.0',
    description='A skeleton which can serve as a base for Flask-restplus app',
    url='https://github.com/beerjoa/flask-restplus-skeleton',
    license='Apache',
    author='beerjoa',
    author_email='beerjoa@kakao.com',
    keywords='sample flask flask-restplus setuptools',
    packages=find_packages(),
    python_requires='>=3',
    include_package_data=True,
    install_requires=[
        'Flask==1.1.1',
        'flask_restplus==0.13.0',
        'Flask_Cors==3.0.8',
        'Flask_JWT_Extended==3.24.1',
        'Flask-Migrate==2.6.0',
        'PyJWT==1.6.4',
        'Werkzeug==0.16.1',
        'pytest==6.2.2',
        'python-dotenv==0.15.0'
    ],
    setup_requires=['pytest-runner'],
    tests_require=['pytest']
)
