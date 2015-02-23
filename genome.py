#!/usr/bin/env python

"""
This file is part of the Pychrosome project, ran by TwentyPeople International.
Note: For cross-platform reasons, Pychrosome uses Python 2.7.6. Python 2.x is generally
pre-installed in most Linux distros and Mac OS X.
It probably could be ran by Python 3.x if needed (we try to make it as compatible as possible) but
beware it is NOT supported nor guaranteed to work.

Filename: genome.py
Class name: genome
Constructor arguments: specie, chromosomes_number
Description: Holds the genome of a <specie>, with <chromosomes_number> chromosomes. This is used for the
             `genotype` class to provide an individual's genotype.
"""

from chromosome import chromosome
from gene import gene


class genome:
  def __init__(self, specie, cr_n):
    self.specie = specie   # Specie's name (homo sapiens?) for reference only.
    self.cr_n = cr_n       # How many chromosomes does this genome hold? NOTE: do NOT count duplicates (e.g. 23 for humans)
    self.chromosomes = []  # No chromosomes yet.

  # Add a chromosome to this genome.
  def add_chromosome(self, chrom):
    # Check if there's still space available
    if len(self.chromosomes) >= self.cr_n:
      print("Error: There are already " + str(self.cr_n) + " chromosomes in the genome for " + self.specie + ".")
      return 0

    # Check if it is a chromosome
    if not isinstance(chrom, chromosome):
      print("Error: Expected a chromosome object! (self.add_chromosome(chromosome))")
      return 0

    # Add it
    self.chromosomes.append(chrom)
    print("Added a chromosome to the genome!")

  # List chromosomes in the genome
  def list_chromosomes(self):
    if not self.chromosomes:
      print("There are no chromosomes added to this genome yet.")
    else:
      for chroma in self.chromosomes:
        print("Chromosome number " + str(chroma.number) + " holds " + str(len(chroma.genes)) + "/" + str(chroma.length) + " genes.")


  #----------SYNTACTIC SUGAR BELOW---------#

  # Access a chromosome by it's natural index
  def access(self, idx):
    if not len(self.chromosomes) >= idx:
      print("Error: Can't access chromosome " + str(idx) + ": not found.")
      return 0
    else:
      return self.chromosomes[idx - 1]

  # Find a gene in all the chromosomes available in this genome
  def search(self, gname):
    for chroma in self.chromosomes:
      chroma.find_gene(gname)

  # List all genes in all chromosomes
  def list_all_genes(self):
    for chroma in self.chromosomes:
      chroma.list_genes()