class GetArchive:
    req = __import__('requests')
    json = __import__('json')

    def __init__(self):
        self.server = 'http://rest.ensembl.org'
        self.ext = '/archive/id/'

        self.headerJson = {'Content-Type' : 'application/json'}
        self.headerXml = {'Content-Type': 'application/xml'}

        self.postHeaderJson = {'Content-Type': 'application/json', 'Accept': 'aaplication/json'}
        self.postHeaderXml = {'Content-Type': 'application/xml', 'Accept': 'application/xml'}

    def getArchiveById(self, id, type='json'):
        typeOpts = {
            'xml': self.headerXml,
            'json': self.headerJson
        }
        header = typeOpts[type]
        content = self.server + self.ext + id + '?'
        result = self.req.get(content, headers = header)

        if not result.ok:
            return result.raise_for_status()
        return result

    def postArchiveById(self, type='json', data=[]):
        typeOpts = {
            'json': self.postHeaderJson,
            'xml': self.postHeaderXml
        }
        header = typeOpts[type]
        input = self.json.dumps({'id': data})
        content = self.server + self.ext
        result = self.req.post(content, headers = header, data = input)

        if not result.ok:
            return result.raise_for_status()

        return result
