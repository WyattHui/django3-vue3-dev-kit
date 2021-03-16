from setuptools import find_packages, setup

setup(
    name='django3-vue3-dev-kit',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'django~=3.1',
        'django-cors-headers~=3.7',
        'djangorestframework~=3.12'
    ]
)
