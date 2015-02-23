from unittest import TestCase
from genome import Genome
from chromosome import Chromosome

__author__ = 'tomeu'


class TestGenome(TestCase):
    def test_add_chromosome(self):
        gnm = Genome("Test", 2)
        # Testing the constructor here
        self.assertEquals([], gnm.chromosomes)
        gnm.add_chromosome(Chromosome(1, 3))
        self.assertEquals(1, gnm.chromosomes[0].number)
        self.assertEquals(1, len(gnm.chromosomes))
        # Test exceptions
        self.assertRaises(TypeError, lambda: gnm.add_chromosome("hey"))
        gnm.cr_n = 1
        self.assertRaises(IndexError, lambda: gnm.add_chromosome(Chromosome(1, 1)))

    def test_access(self):
        gnm = Genome("Test", 1)
        gnm.add_chromosome(Chromosome(1, 1))
        self.assertEquals([], gnm.access(1).genes)
        gnm.access(1).add_gene("HTT")
        self.assertEquals("HTT", gnm.access(1).genes[0].name)