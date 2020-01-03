from setuptools import setup, find_packages


setup(
    name='celery_zabbix',
    version='1.2.0.dev0',
    author='Zeit Online, linuxtechie',
    author_email='zon-backend@zeit.de, myself@linuxtechie.com',
    url='https://github.com/linuxtechie/celery_zabbix',
    description="Sends task execution metrics to Zabbix",
    long_description='\n\n'.join(
        open(x).read() for x in ['README.rst', 'CHANGES.txt']),
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    license='BSD',
    install_requires=[
        'celery',
        'scales',
        'setuptools',
        'protobix',
    ],
    extras_require={'test': [
        'mock',
        'pytest',
    ]},
    entry_points={
        'celery.commands': [
            'zabbix = celery_zabbix.receiver:Command',
        ]
    }
)
