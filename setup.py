from setuptools import setup, find_packages

setup(
    name='py3-sdb',
    version='1.0.7',
    packages=find_packages(),

    author='DDavid701',
    author_email='ddavid701@gmail.com',
    description='SDB is a simple database for beginners.',
    url='https://github.com/DDavid701/sdb',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    long_description=open('sdb/readme.md').read(),
    long_description_content_type='text/markdown',
    python_requires='>=3.10',
)