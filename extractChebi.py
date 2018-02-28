__author__ = 'Sarah'

import sys

def get_term(lines, i):
    nextline = lines[i+1]
    length = len(nextline)
    id = nextline[4:length-1]

    nextline = lines[i+2]
    length = len(nextline)
    name = nextline[6:length-1]

    nextline = lines[i+3]
    start = nextline.find('ChEBI:')
    chebi = ''
    if start != -1:
        comma = nextline.find(',', start)
        chebi = nextline[start+6: comma]

    if chebi != '':
        term = dict({'id': id, 'name': name, 'chebi': chebi})
        return term
    else:
        return None


def get_terms(lines):
    terms = []
    for i in range(0, len(lines)):
        if not lines[i].startswith('[Term]'):
            continue
        else:
            term = get_term(lines, i)
            if term:
                terms.append(term)
            i += 3
    return terms

def main(args):
    # psimod file
    filename = './data/psimod_obo.txt'
    f = open(filename, 'r')
    lines = f.readlines()
    f.close()
    terms = get_terms(lines)


if __name__ == '__main__':
    main(sys.argv)
