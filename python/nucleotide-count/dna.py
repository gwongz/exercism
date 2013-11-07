import re

class DNA(object):
	def __init__(self, strand):
		self.strand = strand
		self.nucleotides = "ACGT"
		self.counts = {}
		for nucleotide in self.nucleotides:
			self.counts[nucleotide] = 0

	def nucleotide_counts(self):
		for nucleotide in self.strand:	
			self.counts[nucleotide] += 1
		return self.counts 
	
	def count(self, nucleotide):	
		valid = re.compile('^[ACTGU][ACTGU]*$')
		result = re.match(valid, nucleotide)
		if not result:
			raise ValueError, ("%s is not a nucleotide." % nucleotide)

		else:
			strand = list(self.strand)
			return strand.count(nucleotide) if nucleotide != 'U' else 0