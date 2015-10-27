class BaseE:
    req = __import__('requests')
    json = __import__('json')
    def __init__(self):
        self.server = 'http://rest.ensembl.org'

        self.headerJson = {'Content-Type' : 'application/json'}
        self.headerXml = {'Content-Type': 'application/xml'}

        self.postHeaderJson = {'Content-Type': 'application/json', 'Accept': 'aaplication/json'}
        self.postHeaderXml = {'Content-Type': 'application/xml', 'Accept': 'application/xml'}
