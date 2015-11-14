from setuptools import setup, find_packages

from pip.req import parse_requirements

install_requires = [str(line.req) for line in parse_requirements(filename='requirements.txt', session=False)]


setup(
    name='project-app',
    version='1.0.0',
    author='',
    author_email='',
    url='https://github.com/stealthbv/project',
    package_dir={'': 'src'},
    packages=find_packages('src'),
    install_requires=install_requires,
    zip_safe=False,
    include_package_data=True,
)
