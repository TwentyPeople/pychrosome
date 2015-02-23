#!/usr/bin/env python

"""
This file is part of the Pychrosome project, ran by TwentyPeople International.
Note: For cross-platform reasons, Pychrosome uses Python 2.7.6. Python 2.x is generally
pre-installed in most Linux distros and Mac OS X.
It probably could be ran by Python 3.x if needed (we try to make it as compatible as possible) but
beware it is NOT supported nor guaranteed to work.

Filename: pychrosome.py
Class name: none
Constructor arguments: none
Description: Testing sandbox for pychrosome.
"""

from chromosome import Chromosome
from gene import Gene
from genome import Genome


# Create a few genes (primitive, no AA sequences yet)
h = Gene("HTT")
h2 = Gene("HPP")
h3 = Gene("EHE")
h4 = Gene("PIP")
h5 = Gene("A4F")
h6 = Gene("BFB")

# Create a chromosome
c = Chromosome(1, 5)

# Add a few genes to c
c.add_gene("hi")  # Shows error! Not a gene.
c.add_gene(h)
c.add_gene(h2)
c.add_gene(h3)
c.add_gene(h4)
c.add_gene(h5)
c.add_gene(h6)

# List all genes in chromosome 1
c.list_genes()

# Find some genes in c
c.find_gene("HEH")
c.find_gene("HPP")
c.find_gene("AHA")
c.find_gene("HTT")
c.find_gene("BFB")

# Create a genome for the specie Bitch
gnm = Genome("Bitch", 2)

# Add the earlier created chromosome c (full already)
gnm.add_chromosome(c)
gnm.list_chromosomes()

# Add a new anonymous chromosome
gnm.add_chromosome(Chromosome(2, 3))
gnm.list_chromosomes()

# Try and add another anonymous chromosome
gnm.add_chromosome(Chromosome(3, 666))  # Throws error -> not any more space available
gnm.list_chromosomes()

# Hard-coded way to add a gene to the anonymous chromosome
gnm.chromosomes[1].add_gene(Gene("PXP"))

# Syntactic sugar for the above
gnm.access(2).add_gene(Gene("PTP"))

# Try and find it hard-codedly
gnm.chromosomes[1].find_gene("PXP")

# Sugarish alternative
gnm.access(2).find_gene("PTP")
gnm.list_chromosomes()

# Syntactic sugar for the above (search globally in the whole genome)
gnm.search("PXP")

# List all genes in the Bitch genome
gnm.list_all_genes()

print("----------------------CHANGE----------------------")
# We are going to study the genome of the Mycobacterium Tuberculosis
koch = Genome("Mycobacterium Tuberculosis", 10)

koch.add_chromosome(Chromosome(1, 2023))
koch.add_chromosome(Chromosome(2, 442))
koch.add_chromosome(Chromosome(3, 23))

koch.access(1).add_gene("CUTE")
koch.access(1).add_gene("ugly")

koch.access(2).add_gene("TOXIC")
koch.access(2).add_gene("TOXIC")

koch.access(3).add_gene("NO_NUCLEUM")
koch.access(3).add_gene("70S RIBOSOMES")

koch.list_chromosomes()
koch.list_all_genes()

koch.search("TOXIC")