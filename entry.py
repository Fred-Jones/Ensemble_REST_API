# Should make base class from which all modules inherit

#
# ###GENOME HELPER TEST
# from GenomeHelper import GenomeHelper
# # print GenomeHelper.readGenomeFromFasta('./TestData/testSeqs.fasta')
# seq, q = GenomeHelper.readGenomeFromFastq('./TestData/testSeq.fastq')
# print seq, q
#
#
# ##GET ARCHIVE TEST
from Archive import Archive
# from ComparativeGenomics import GetGentree
result = Archive.GetArchive().getArchiveById(id='ENSG00000157764')
print result.json()

rs = Archive.GetArchive().getArchiveById('ENSG00000157764', type='xml')

print rs.text

##POST ARCHIVE TEST
# result = Archive.GetArchive().postArchiveById(type='json', data = ["ENSG00000157764", "ENSG00000248378"])
# result2 = Archive.GetArchive().postArchiveById(type='xml', data = ["ENSG00000157764", "ENSG00000248378"])
# print result.json()
# print result2.text
#
# ###GET GENTREE TEST
# from ComparativeGenomics import GetGeneTree
# tstId = 'ENSGT00390000003602'
# r = GetGeneTree.GetGenTree().getGeneTreeById(tstId, type='json')
# rz = GetGeneTree.GetGeneTree().getGeneTreeById(tstId, type='xml')
# print r.json(), rz.text
# r3 = GetGeneTree.GetGenteTee().getGeneTreeById(tstId, type='nh')
# print r3.text
# r4 = GetGeneTree.GetGeneTree().getGeneTreeById(tstId, type='phyloxml', aligned=False, sequence='cdna')
# print r4.text
#
# GETCROSSREFERENCE TEST
# from CrossReference import GetCrossReference
# tstSpec = 'homo_sapiens'
# tstSymb = 'BRCA2'
# result = GetCrossReference.GetCrossRef().getCrossRefBySymbol('homo_sapiens', 'BRCA2')
# # resultXml = GetCrossReference.GetCrossRef().getCrossRefBySymbol('homo_sapiens', 'BRCA2', type='xml')
# # resultExtDb = GetCrossReference.GetCrossRef().getCrossRefBySymbol('homo_sapiens', 'BRCA2', extdb='HGNC')
# print result.json()
# #

# POSTLOOKUP TEST
# Lookup multiple ids supplied as a python list of strings
# from Lookup import PostLookup
# idArray = ["ENSG00000157764", "ENSG00000248378" ]
# result = PostLookup.PostLookup().postLookupById(ids = idArray)
# resDict = result.json()
#
# for id in idArray:
#     print resDict[id]['assembly_name']

############## from Lookup import GetLookup
############## print GetLookup.server
############## server = 'serverzzz'
############## print GetLookup.server

# from Information import GetInfo
# print GetInfo.GetInfo().printServer()

# from ComparativeGenomics import Archive
