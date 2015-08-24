##
#Parse out genome from FASTA file
##
##
#WILL CONCATENATE multiple sequences from a file
#into one genome string
##

def readGenomeFromFasta(filename):
    genome = ''
    with open(filename, 'r') as f:
        for line in f:
            if not line[0] == '>':
                genome += line.rstrip()
    return genome

##
#Returns a tuple of (<sequence>, <quality>)
##
def readGenomeFromFastq(filename):
    genome = ''
    q = ''
    if not filename.endswith(('.fastq', '.FASTQ', '.fq')):
        print "It appears %s is not a FASTQ file"%filename

    with open(filename, 'r') as file:
        for line in file:
            if line[0] == '@':
                ##ADD NEXT LINE TO GENOME
                genome = file.next()
            elif line[0] == '+':
                ##ADD NEXT LINE TO Q
                q = file.next()
    return genome, q
