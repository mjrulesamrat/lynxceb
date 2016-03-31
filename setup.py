from setuptools import setup
from setuptools.command.install_lib import install_lib as _install_lib
from distutils.command.build import build as _build
from distutils.cmd import Command


class compile_translations(Command):
    description = 'compile message catalogs to MO files via django compilemessages'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        import os
        from django.core.management import execute_from_command_line, CommandError

        curdir = os.getcwd()
        ceb_dir = os.path.realpath('lynxceb')
        os.chdir(ceb_dir)
        try:
            execute_from_command_line(['django-admin', 'compilemessages'])
        except CommandError:
            pass
        finally:
            os.chdir(curdir)


class build(_build):
    sub_commands = [('compile_translations', None)] + _build.sub_commands


class install_lib(_install_lib):
    def run(self):
        self.run_command('compile_translations')
        _install_lib.run(self)

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
      cmdclass={'build': build, 'install_lib': install_lib,
        'compile_translations': compile_translations},
      zip_safe=False)