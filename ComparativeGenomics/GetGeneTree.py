class GetGeneTree:
    req = __import__('requests')

    def __init__(self):
        self.server = 'http://rest.ensembl.org'
        self.ext = '/genetree/id/'

        self.headerJson = {'Content-Type' : 'application/json'}
        self.headerXml = {'Content-Type': 'application/xml'}
        self.headerNh = {'Content-Type': 'text/x-nh'}
        self.headerXphyloXml = {'Content-Type': 'text/x-phyloxml+xml'}

    def getGenetreeById(self, id, type='', query='', sequence='', aligned=False):
        if aligned:
            aligned = 1
        else :
            aligned = 0
        typeOpts = {
            'json': self.headerJson,
            'xml': self.headerXml,
            'nh': self.headerNh,
            'phyloxml': self.headerXphyloXml
        }
        header = typeOpts[type]
        content = self.server + self.ext + id + '?' + str(aligned) + sequence
        result = self.req.get(content, headers = header)

        if not result.ok:
            return result.raise_for_status()

        return result
    
