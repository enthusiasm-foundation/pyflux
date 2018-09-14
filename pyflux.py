import requests
import json
import csv

class Result(object):
    def __init__(self, headers, lines):
        self.headers=headers
        self.lines=lines
#end

class Specification(object):
    def __init__(self, arg):
        self.arg = arg

    def json(self):
        return json.dumps(self.arg);

class AST(object):
    def __init__(self, arg):
        self.arg = arg


def _results(text_results):
    res = []
    for tresult in text_results.split("\n\r\n"):
        reader = csv.reader(tresult.split('\n'), delimiter=',')
        headers = next(reader)
        lines = []
        for row in reader:
            lines.append(row)

        res.append(Result(headers, lines))

    return res
#end

class Flux(object):
    """a client for Flux"""
    def __init__(self, server, port=8093, version='v2'):
        self.server = server
        self.port = port
        self.version = version

    def _encode(self, query):
        return '{"query": '+json.dumps(query)+'}'

    #Convert a query-string from fluxlang syntax to AST
    def convert_to_ast(self, query):
        return requests.post('http://'+self.server+'/'+self.version+'/flux/ast', data = self._encode(query)).text
    #end

    def conver_to_spec(self, query):
        return requests.post('http://'+self.server+'/'+self.version+'/flux/spec', data = self._encode(query)).text
    #end

    #Executes a query
    def eval_query(self, query):
        r = requests.post('http://'+self.server+'/query', data = self._encode(query))
        return _results(r.text) # end

    #Executes a query
    def eval_spec(self, spec):
        r = requests.post('http://'+self.server+'/query', spec)
        return _results(r.text)
    #end


