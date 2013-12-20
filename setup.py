# coding:utf-8

from setuptools import setup, find_packages


setup(name='flanker-address',
      version='0.4.4',
      description='Mailgun Parsing Tools',
      long_description=open('README.rst').read(),
      classifiers=[],
      keywords='',
      author='Mailgun Inc.',
      author_email='admin@mailgunhq.com',
      url='http://mailgun.net',
      license='Apache 2',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=True,
      install_requires=[
          'chardet>=1.0.1',
          'dnsq>=1.0',
          'expiringdict>=1.0',
      ],
      )
