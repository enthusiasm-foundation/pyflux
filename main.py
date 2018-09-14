from sys import argv
from pyflux import Flux

if __name__== "__main__":

    host = 'hackmilan.a.influxcloud.net'
    version = 'v2'

    f = Flux(host, 8080, version)

    results = f.eval_query(argv[1])
    print(results[0].lines[0])

    ast = f.convert_to_ast(argv[1])
    print(ast)

    spec = f.conver_to_spec(argv[1])
    print(spec)
