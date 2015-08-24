import sys

from Bio import Phylo
from ComparativeGenomics import GetGeneTree

tstId = 'ENSGT00390000003602'
print 'Loading from Ensemble...'
r4 = GetGeneTree.GetGeneTree().getGenetreeById(tstId, type='phyloxml', aligned=False, sequence='cdna')

# print 'Loaded phyloxml from Ensemble', type(r4.text)

print sys.argv
print 'Tyring conversion to ASCII...'
testphyloXML = open('./TestData/tstphylo.xml', 'r')
# testphyloXML.write(r4.text)

trees = Phylo.parse('./TestData/tstphylo.xml', 'phyloxml').next()
Phylo.draw_ascii(trees)
