from setuptools import find_packages, setup

setup(
    name='serializer',
    packages=find_packages(),
    version='0.1.0',
    description='My json, toml, yaml serializer/parser library',
    author='daftcod',
    author_email='MsterHeisenberg@mail.com',
    setup_requires=['pytest-runner', 'pyyaml'],
    url='https://github.com/DaftCod/ISP-2022-053504/',
    license='MIT',
)
