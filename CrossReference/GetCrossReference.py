class GetCrossRef:
    req = __import__('requests')

    def __init__(self):
        self.server = 'http://rest.ensembl.org'
        self.ext = '/xrefs/symbol'

        self.headerJson = {'Content-Type' : 'application/json'}
        self.headerXml = {'Content-Type': 'application/xml'}

    def getCrossRefBySymbol(self, species='', symbol='', extdb='', type='json'):
        typeOpts = {
            'json': self.headerJson,
            'xml': self.headerXml
        }

        base = self.server + self.ext + '/'
        res = self.req.get(base + species + '/' + symbol + '?' + 'external_db=' + extdb, headers=typeOpts[type])
        if not res.ok:
            return res.raise_for_status()
        return res
