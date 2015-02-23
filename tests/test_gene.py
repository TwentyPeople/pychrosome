from unittest import TestCase
from gene import Gene

__author__ = 'tomeu'


class TestGene(TestCase):
    def test___init__(self):
        gn = Gene("HTT")
        self.assertEqual("HTT", gn.name)