#!/usr/bin/env python

"""
This file is part of the Pychrosome project, ran by TwentyPeople International.
Note: For cross-platform reasons, Pychrosome uses Python 2.7.6. Python 2.x is generally
pre-installed in most Linux distros and Mac OS X.
It probably could be ran by Python 3.x if needed (we try to make it as compatible as possible) but
beware it is NOT supported nor guaranteed to work.

Filename: chromosome.py
Class name: chromosome
Constructor arguments: number, length
Description: Creates a new chromosome that can hold <length> genes, identified by <number>.
"""

from gene import gene

class chromosome:
  def __init__(self, n, l):
    self.number = n  # Chromosome nr...
    self.length = l  # How many genes in the chromosome?
    self.locus = []  # Every locus has a gene, there are self.length locus
    # A chromosome has many genes
    self.genes = []
  
  # Add a gene to the chromosome
  def add_gene(self, g):
    if not isinstance(g, gene):
      # Generate a gene instance
      g = gene(g)

    if len(self.locus) >= self.length:
      print("Error: All the locus of the chromosome %d are full!" % self.number)
    else:
      self.genes.append(g)
      lpos = len(self.locus)
      self.locus.append(self.genes[len(self.genes) - 1])
      print("Gene  " + g.name + " correctly added to the locus " + str(lpos + 1) + " of the chromosome " + str(self.number) + ".")

  # Try to find a gene in this chromosome
  def find_gene(self, gname):
    k = 0
    found = False
    while (k < len(self.locus)):
      if self.locus[k].name == gname:
        print("Found gene " + gname + " in locus number " + str(k + 1) + " of the chromosome " + str(self.number) + ".")
        found = True
      k = k + 1
    if not found:
      print("Couldn't find gene " + gname + " in chromosome " + str(self.number) + ".")

  # List all the genes in this chromosome
  def list_genes(self):
    k = 1  # Counter
    for loci in self.locus:
      print("Gene " + loci.name + " is hosted in locus " + str(k) + " of the chromosome " + str(self.number) + ".")
      k = k + 1


