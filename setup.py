from setuptools import find_packages, setup

setup(
    name='py-mapper',
    packaves=find_packages(include=['pymapper']),
    version='0.0.1',
    description='Python mapper library',
    author='Felipe Endlich',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner'],
    test_require=['pytest'],
    test_suite='tests'
)
