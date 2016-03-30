from setuptools import setup

def readme():
	with open('README.rst') as f:
		return f.read()

setup(name='lynxceb',
      version='0.1',
      description='Lynx Custom Email Backend for Django powered applications',
      long_description=readme(),
      url='http://github.com/mjrulesamrat/lynxceb',
      author='Jay Modi',
      author_email='mjrulesamrat@gmail.com',
      license='MIT',
      packages=['lynxceb'],
      install_requires=[
          'Django',
      ],
      include_package_data=True,
      zip_safe=False)