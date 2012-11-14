from setuptools import setup, find_packages
import os

PACKAGE = 'trac_pytest'
version = '0.1'
long_description = open("README").read()
classifiers = [
"Programming Language :: Python",
  ("Topic :: Software Development :: "
  "Libraries :: Python Modules")]

setup(name=PACKAGE,
  version=version,
  description='py.test fixture for trac',
  long_description=long_description,
  classifiers=classifiers,
  keywords='trac, py.test, fixture',
  author='Rainer Hihn',
  author_email='rainer.hihn@inquant.de',
  url='http://www.inquant.de',
  license='GPLv3',
  packages=find_packages(exclude=['ez_setup']),
  include_package_data=True,
  install_requires=[],
  # test_suite= nose.collector ,
  # test_requires=[ Nose ],
  #entry_points=
  # -*- Entry points: -*-
  )
