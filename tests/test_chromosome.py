from unittest import TestCase
from chromosome import Chromosome
from gene import Gene

__author__ = 'tomeu'


class TestChromosome(TestCase):
    # Test the constructor

    def test___init__(self):
        perc = Chromosome(1, 5)
        self.assertEquals(1, perc.number)
        self.assertEquals(5, perc.length)
        self.assertEquals([], perc.genes)
        self.assertEquals([], perc.locus)

    # Test the addition of a gene
    def test_add_gene(self):
        self.assertEquals(True, Chromosome(1, 1).add_gene("HTT"))
        self.assertEquals(True, Chromosome(1, 1).add_gene(Gene("HTT")))
        # Add a gene to the persistent chromosome
        perc = Chromosome(1, 1)
        perc.add_gene("HTT")
        self.assertEquals(1, len(perc.genes))
        self.assertEquals("HTT", perc.genes[0].name)
        self.assertEquals(1, len(perc.locus))
        self.assertEquals("HTT", perc.locus[0].name)

        # Exceptions

        self.assertRaises(IndexError, lambda: perc.add_gene("RSX"))

    # Test finding a gene
    def test_find_gene(self):
        perc = Chromosome(1, 2)
        perc.add_gene("HTT")
        perc.add_gene("MIT")
        self.assertEquals(True, perc.find_gene("HTT"))
        self.assertEquals(True, perc.find_gene("MIT"))
        self.assertEquals(False, perc.find_gene("HEH"))