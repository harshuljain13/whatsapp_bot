from setuptools import setup

setup(
    name='whatsappbot',
    version='0.0.1.0',
    description='whatsapp bot for advertising',
    author='Harshul Jain',
    license='MIT',
    packages=['bot'],
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stablegit
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
    author_email='harshulrobo@gmail.com',
    url='https://github.com/harshul1610/whatsapp_bot',
    install_requires=[
        "selenium==2.48.0",
        "wheel==0.24.0",
        "xlrd==0.9.4"
    ],
    entry_points={
        'console_scripts': [
            'bot = bot.main:main'
        ]
    }
)
