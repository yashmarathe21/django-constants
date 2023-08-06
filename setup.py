from setuptools import setup  # type: ignore

with open("README.md") as f:
    long_description = f.read()


setup(
    name="django_constants",
    version="1.0.0",
    description=(
        "This is a Django app designed to store global constants with different data types. It provides a central location to manage and access configuration values that can be easily reused throughout your Django project."
    ),
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Framework :: Django",
        "Framework :: Django :: 3.2",
    ],
    url="https://github.com/yashmarathe21/django-constants",
    author="Yash Marathe",
    author_email="yashmarathe21@gmail.com",
    keywords="django python constants",
    license="MIT",
    python_requires=">=3.6",
    packages=["django_constants", "django_constants/migrations/"],
    install_requires=["Django>=3.2"],
)
