##Switched up implementation
##Find the species and database for a single identifier
# import os


class PostLookup():
    req = __import__('requests')
    json = __import__('json')

    def __init__(self):
        self.server = 'http://rest.ensembl.org/'
        self.ext = 'lookup/id/'
        self.typeOpts = {
            'json': {'Content-Type' : 'application/json'},
            'xml': {'Content-Type': 'application/xml'},
            'nh': {'Content-Type': 'text/x-nh'},
            'phyloxml': {'Content-Type': 'text/x-phyloxml+xml'}
        }

    def postLookupById(self, ids, type = 'json', species='', db='core', expand=False, form=[], callback=''):
        extension = self.ext
        typeOpts = self.typeOpts
        if not ids:
            print "Must include argument ids=<Python list of Ensemble Ids>"
        print ids
        payload = {
        "ids": ids,
            'species': species,
            'db_type': db,
            'expand': expand,
            'format': form,
            'callback': callback
        }

        result = self.req.post(self.server + self.ext, headers = typeOpts[type], data = self.json.dumps(payload))
        if not result.ok:
            result.raise_for_status()
            sys.exit()

        return result
