"""Still needs some work to properly include the test_site and sqlite db"""

from setuptools import setup

setup(
    name="django-monthfield",
    version="1.1.0",
    author="Matthys Kroon",
    author_email="matthysk@clearspark.co.za",
    packages=["month"],
    install_requires=["django>3"],
    include_package_data=True,
    url="https://github.com/clearspark/django-monthfield",
    license="BSD licence, see LICENCE",
    description="Provides a field for storing months (YYYY-MM) on django models.",
    long_description=open("README.rst").read(),
    zip_safe=False,
)
