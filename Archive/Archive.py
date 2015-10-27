from BaseE import BaseE as BE
class GetArchive(BE):

    ext = '/archive/id/'

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
