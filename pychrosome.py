#!/usr/bin/env python
from chromosome import chromosome
from gene import gene

# Simple IO and functionality tests

h = gene("HTT")
h2 = gene("HPP")
h3 = gene("EHE")
h4 = gene("PIP")
h5 = gene("A4F")
h6 = gene("BFB")

c = chromosome(1, 5)
c.add_gene(h)
c.add_gene(h2)
c.add_gene(h3)
c.add_gene(h4)
c.add_gene(h5)
c.add_gene(h6)
c.locus
c.genes

c.find_gene("HEH")
c.find_gene("HPP")
c.find_gene("AHA")
c.find_gene("HTT")
c.find_gene("BFB")