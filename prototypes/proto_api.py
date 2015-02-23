#!/usr/bin/env python
from pychrosome import api

# We are going to study the genome of the Mycobacterium Tuberculosis
koch = genome("Mycobacterium Tuberculosis", 10)

koch.add_chromosome(chromosome(1, 2023))
koch.add_chromosome(chromosome(2, 442))
koch.add_chromosome(chromosome(3, 23))

koch.access(1).add_gene("CUTE")
koch.access(1).add_gene("ugly")

koch.access(2).add_gene("TOXIC")
koch.access(2).add_gene("TOXIC")

koch.access(3).add_gene("NO_NUCLEUM")
koch.access(3).add_gene("70S RIBOSOMES")

koch.list_chromosomes()
koch.list_all_genes()