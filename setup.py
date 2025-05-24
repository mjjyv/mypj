from setuptools import setup, find_packages

setup(
    name="my_project",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "flask",
        "flask-admin",
        "flask-sqlalchemy",
    ],
    author="mjjyv",
    author_email="minhvueye363@gmail.com",
    description="A Flask project with admin interface",
)
