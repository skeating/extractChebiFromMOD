__author__ = 'Sarah'

import sys

def get_ref(line):
    vars = line.split(' ')
    for var in vars:
        if var.startswith('Reactome:'):
            parts = var.split(':')
            if len(parts) > 1 and parts[1].startswith('R-'):
                return parts[1]
    return ''


def get_id(line):
    vars = line.split(' ')
    for var in vars:
        if var.startswith('PR'):
            return var
    return ''

def get_reactome_ref(termlines):
    id = ''
    ref = ''
    for line in termlines:
        if line.startswith('id'):
            id = get_id(line)
        elif line.startswith('xref'):
            ref = get_ref(line)
    if ref != '' and id != '':
        term = dict({'id': id, 'reactome': ref})
        return term
    else:
        return None


def get_term(lines, i):
    termlines = []
    j = i + 1
    nextline = lines[j]
    while nextline != '' and nextline != '\n':
        termlines.append(nextline)
        j += 1
        nextline = lines[j]
    return [termlines, j]


def get_terms(lines):
    terms = []
    for i in range(0, len(lines)):
        if not lines[i].startswith('[Term]'):
            continue
        else:
            if not lines[i+1].startswith('id: PR:'):
                continue
            else:
                [termlines, i] = get_term(lines, i)
                term = get_reactome_ref(termlines)
                if term:
                    terms.append(term)
    return terms

def main(args):
    # pro file
    filename = './data/pro_reasoned.obo'
    f = open(filename, 'r')
    lines = f.readlines()
    f.close()
    terms = get_terms(lines)
    filename = './data/pro_ref.csv'
    f = open(filename, 'w')
    for term in terms:
        f.write('{0},{1}'.format(term['reactome'], term['id']))
    f.close()



if __name__ == '__main__':
    main(sys.argv)
