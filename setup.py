import os
import shutil

from setuptools import setup, find_packages, Command

import ocspbuilder


class CleanCommand(Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        folder = os.path.dirname(os.path.abspath(__file__))
        for sub_folder in ['build', 'dist', 'ocspbuilder.egg-info']:
            full_path = os.path.join(folder, sub_folder)
            if os.path.exists(full_path):
                shutil.rmtree(full_path)


setup(
    name='ocspbuilder',
    version=ocspbuilder.__version__,

    description=(
        'Creates and signs online certificate status protocol (OCSP) '
        'requests and responses for X.509 certificates'
    ),
    long_description='Docs for this project are maintained at https://github.com/wbond/ocspbuilder#readme.',

    url='https://github.com/wbond/ocspbuilder',

    author='wbond',
    author_email='will@wbond.net',

    license='MIT',

    classifiers=[
        'Development Status :: 4 - Beta',

        'Intended Audience :: Developers',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: PyPy',

        'Topic :: Security :: Cryptography',
    ],

    keywords='crypto pki x509 certificate ocsp',

    install_requires=[
        'asn1crypto>=0.13',
        'oscrypto>=0.12'
    ],
    packages=find_packages(exclude=['tests*', 'dev*']),

    test_suite='dev.tests.make_suite',

    cmdclass={
        'clean': CleanCommand,
    }
)
