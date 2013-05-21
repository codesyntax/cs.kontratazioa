# -*- coding: utf-8 -*-
"""
This module contains the tool of cs.kontratazioa
"""
import os
from setuptools import setup, find_packages

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

version = '2.1'

long_description = (
    read('README.txt')
    + '\n' +
    read('CHANGES.txt')
    )

setup(name='cs.kontratazioa',
      version=version,
      description="A product to publish public contract information in Spanish Public Administration's websites",
      long_description=long_description,
      classifiers=[
        'Framework :: Plone',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        ],
      keywords='',
      author='Lur Ibargutxi',
      author_email='libargutxi@codesyntax.com',
      url='http://github.com/codesyntax/cs.kontratazioa',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['cs', ],
      include_package_data=True,
      zip_safe=False,
      install_requires=['setuptools',
                        # -*- Extra requirements: -*-
                        'Plone'
                        ],
      entry_points="""
      # -*- entry_points -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
