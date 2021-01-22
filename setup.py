from setuptools import setup, find_packages

setup(name='gym_reversi',
      version='1.0',
      packages=[package for package in find_packages()
                if package.startswith('reversi')],
      install_requires=[]
      )