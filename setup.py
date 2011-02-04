#!/usr/bin/env python

from setuptools import setup
import memcache

setup(name="python-memcached",
      version=memcache.__version__,
      description="Pure python memcached client",
      long_description=open("README").read(),
      author="Evan Martin",
      author_email="martine@danga.com",
      maintainer="Jessica Stanton",
      maintainer_email="jess.m.stanton@gmail.com",
      url="http://github.com/jess-is-coding/python-memcached",
      py_modules=["memcache"],
      zip_safe=False,
      package_data = {
          '': ['*.py'],
      },
      classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Python Software Foundation License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ])

