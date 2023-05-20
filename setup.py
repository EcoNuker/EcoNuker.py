from setuptools import setup, find_packages

setup(
    name='econuker',
    version='1.0.2',
    author='YumYummity',
    author_email='034nop@gmail.com',
    description='API wrapper for https://api.econuker.xyz',
    long_description='A Python library for interacting with EcoNuker\'s API.',
    url='https://github.com/EcoNuker/EcoNuker-API-Python/',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Internet :: WWW/HTTP',
    ],
    python_requires='>=3.9',
    install_requires=[
        'requests',
        'aiohttp'
    ],
)
