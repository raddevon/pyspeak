from distutils.core import setup


setup(name='PySpeak',
      version='0.1.1',
      py_modules=['pyspeak'],
      url='https://github.com/raddevon/pyspeak',
      license='MIT',
      author='Devon Campbell',
      author_email='devon@raddevon.com',
      description='A ThingSpeak API wrapper for Python',
      include_package_data=True,
      platforms='any',
      install_requires=[
          'distribute==0.6.27',
          'py==1.4.13',
          'pytest==2.3.4',
          'simplejson==3.1.3',
          'requests==2.20.0'
      ],
      classifiers=[
          'Natural Language :: English',
          'Environment :: Web Environment',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
          'Topic :: Software Development :: Libraries :: Python Modules'
      ]
      )
