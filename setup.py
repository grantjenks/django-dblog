import pathlib
import re

from setuptools import setup
from setuptools.command.test import test as TestCommand


class Tox(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import tox

        errno = tox.cmdline(self.test_args)
        exit(errno)


with open('README.rst') as reader:
    readme = reader.read()

dblog_init_path = pathlib.Path(__file__).parent / 'dblog' / '__init__.py'
dblog_init = dblog_init_path.read_text()
match = re.search(r"^__version__ = '(.+)'$", dblog_init, re.MULTILINE)
version = match.group(1)

setup(
    name='django-dblog',
    version=version,
    description='Django Database Logs',
    long_description=readme,
    author='Grant Jenks',
    author_email='contact@grantjenks.com',
    url='https://grantjenks.com/docs/django-dblog/',
    project_urls={
        'Documentation': 'https://grantjenks.com/docs/django-dblog/',
        'Funding': 'https://gum.co/django-dblog',
        'Source': 'https://github.com/grantjenks/django-dblog',
        'Tracker': 'https://github.com/grantjenks/django-dblog/issues',
    },
    license='Apache 2.0',
    packages=['dblog'],
    tests_require=['tox'],
    cmdclass={'test': Tox},
    python_requires='>=3',
    install_requires=['Django'],
    classifiers=(
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ),
)
