from setuptools import setup

setup(
    author='Quinlan Pfiffer',
    author_email='qpfiffer@gmail.com',
    url='https://code.kyoto.io/qpfiffer/olegdb-python',
    name='olegdb-python',
    description='Python wrappers for generic OlegDB methods.',
    version='0.1',
    license='BSD',
    keywords='OlegDB',
    packages=['olegdb-python'],
    zip_safe=False,
    install_requires = [
        "requests"
    ]
)
