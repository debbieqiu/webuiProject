from setuptools import setup, find_packages

setup(
    name='webuiapi',
    version='1.0.0',
    packages=find_packages(),
    url='https://github.com/webuiProject',
    license='',
    author='debbieqiu',
    author_email='debbieqiu@outlook.com',
    description='webuiapi',
    install_requires=[
        'Flask',
        'numpy',
        'pandas',
        # add other dependencies here
    ]
)
