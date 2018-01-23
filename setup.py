from setuptools import setup

setup(
    name='mercedes-api',
    version='0.0.2',
    description='Retrieve info from mercedes api.',
    url='https://github.com/RiRomain/python-mercedes-api/',
    license='MIT',
    author='RiTomain',
    author_email='romain.rinie@googlemail.com',
    packages=['mercedesapi'],
    install_requires=['requests'],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers'
    ]
)
