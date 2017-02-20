from setuptools import setup

setup(
    author='Quinlan Pfiffer',
    author_email='qpfiffer@gmail.com',
    url='https://github.com/infoforcefeed/olegdb-python',
    name='olegdb-python',
    description='Python wrappers for generic OlegDB methods.',
    version='0.1.5',
    license='BSD',
    keywords='OlegDB',
    packages=['olegdb'],
    zip_safe=False,
    install_requires = [
        "requests",
        "msgpack-python>=0.4.1"
    ]
)
