from distutils.core import setup, find_packages


setup(name='PySpeak',
      version='0.1',
      py_modules=find_packages(),
      install_requires=[
          'distribute==0.6.27',
          'py==1.4.13',
          'pytest==2.3.4',
          'simplejson==3.1.3'
      ]
      )
