#!/usr/bin/env python

# This is Python 2!

class chromosome:
  def __init__(self, n, l):
    self.number = n  # Chromosome nr...
    self.length = l  # How many genes in the chromosome?
    self.locus = []  # Every locus has a gene, there are self.length locus
    # A chromosome has many genes
    self.genes = []
  
  def add_gene(self, g):
    if len(self.locus) >= self.length:
      print("Error: All the locus of the chromosome %d are full!" % self.number)
    else:
      self.genes.append(g)  # Add the gene to the 
      lpos = len(self.locus)
      self.locus.append(self.genes[len(self.genes) - 1])
      print("Gene  " + g.name + " correctly added to the locus " + str(lpos + 1) + " of the chromosome " + str(self.number) + ".")

  def find_gene(self, gname):
    k = 0
    while (k < len(self.locus)):
      if self.locus[k].name == gname:
        print("Found gene " + gname + " in locus number " + str(k + 1) + " of the chromosome " + str(self.number) + ".")
        return True
      else:
        k = k + 1
    print("Couldn't find gene " + gname + " in chromosome " + str(self.number) + ".")
