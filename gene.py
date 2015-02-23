#!/usr/bin/env python

"""
This file is part of the Pychrosome project, ran by TwentyPeople International.
Note: For cross-platform reasons, Pychrosome uses Python 2.7.6. Python 2.x is generally
pre-installed in most Linux distros and Mac OS X.
It probably could be ran by Python 3.x if needed (we try to make it as compatible as possible) but
beware it is NOT supported nor guaranteed to work.

Filename: gene.py
Class name: gene
Constructor arguments: name, {future: seq}
Description: Very simple model for a gene -- to be expanded. Holds a gene coded <name>.
             {future: Also holds the AA sequence of this gene.}
""" 
class gene:
  def __init__(self, name):
    self.name = name