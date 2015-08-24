# class GetLookup:
#     req = __import__('requests')
#
#     def __init__(self):
#         self.server = 'http://rest.ensembl.org/'
#         self.ext = 'lookup/id/'
#         self.typeOpts = {
#             'json': {'Content-Type' : 'application/json'},
#             'xml': {'Content-Type': 'application/xml'},
#             'nh': {'Content-Type': 'text/x-nh'},
#             'phyloxml': {'Content-Type': 'text/x-phyloxml+xml'}
#         }
#
#     def getLookupById(self, id, species='', db='core', expand=False, format=[], callback=''):
#         extension = self.ext + id
#         payload = {
#             'species': species,
#             'db_type': db,
#             'expand': expand,
#             'format': format,
#             'callback': callback
#         }
#
#         r.get(self.server + extension, headers=header, params=payload)
#         if not r.ok:
#             r.raise_for_status()
#             sys.exit()
#
#         return r


# ext = 'lookup/id/'
# typeOpts = {
#     'json': {'Content-Type' : 'application/json'},
#     'xml': {'Content-Type': 'application/xml'},
#     'nh': {'Content-Type': 'text/x-nh'},
#     'phyloxml': {'Content-Type': 'text/x-phyloxml+xml'}
# }
#
#
# def getLookupById(self, id, species='', db='core', expand=False, format=[], callback=''):
#     extension = self.ext + id
#     payload = {
#         'species': species,
#         'db_type': db,
#         'expand': expand,
#         'format': format,
#         'callback': callback
#     }
#
#     r.get(server + extension, headers=header, params=payload)
#     if not r.ok:
#     r.raise_for_status()
#     sys.exit()
#
#     return r
