from setuptools import setup

setup(
    name="GoogleStorage",
    version="1.0",
    author="Sachin Edward",
    author_email="edward9494@gmail.com",
    description="Google Cloud storage Wrapper",
    url="https://github.com/sachinedward/GoogleStorageWrapper",
    packages=['GoogleStorage'],
    include_package_data=True,
    install_requires=['google-cloud', 'google-api-python-client', 'oauth2client']
)
