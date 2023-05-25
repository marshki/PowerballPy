from setuptools import setup

setup(
        name='powerballpy',
        version='0.1.2',
        author='M. Krinitz',
        author_email='<marshall [at] morethantomorrow [dot] org>',
        description='Pseudo-random number generator for Powerball lottery in Python 3.',
        url='https://github.com/marshki/PowerballPy',
        packages='powerballpy',
        install_requires=[
            'prettytable',
        ],
        classifiers=[

            'Development Status :: 5 - Production/Stable',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3.8',
            'Programming Language :: Python :: 3.9',
        ],
)
