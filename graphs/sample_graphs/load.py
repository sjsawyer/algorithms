def _parse_adjacency_list(edge_lst):
    '''
    `edge_lst` is a list of strings, where each string begins with a node
    '<node>: ', and is followed by a comma separated list of the nodes
    it is adjacent to in the graph.
    '''
    graph = {}
    for edges in edge_lst:
        node, neighbours = edges.split(": ")
        neighbours = neighbours.split(",")
        graph[node] = set(neighbours)
    return graph


def from_txt(filepath):
    '''
    Read a graph from a text file of a suitable format and return it in the
    specified format.
    '''
    format = None
    graph = None

    with open(filepath, 'rb') as f:
        line = f.readline()
        while "FORMAT" not in line:
            line = f.readline()
        # line is now the FORMAT specification line
        format = line.split("FORMAT: ")[1].strip()
        while "GRAPH" not in line:
            line = f.readline()
        # next line starts the graph declaration
        graph = map(lambda l: l.strip(), f.readlines())

    # remove any trailing empty lines
    while not graph[-1]:
        del(graph[-1])

    if format == "ADJACENCY_LIST":
        graph = _parse_adjacency_list(graph)

    else:
        return ValueError("Unrecognized format")

    return graph

