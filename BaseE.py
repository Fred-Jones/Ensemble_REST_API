class BaseE:
    req = __import__('requests')
    json = __import__('json')
    def __init__(self):
        self.server = 'http://rest.ensembl.org'
