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


def _parse_adjacency_matrix(edge_lst):
    '''
    `edge_lst` is a list of strings, where each string begins with a node
    '<node>: ', and is followed by a comma separated list of weights for the
    edge connecting it to every other node in the graph. A weight of 0 means
    there is no connection between two nodes.
    '''
    graph = [[None for _ in edge_lst] for _ in edge_lst]
    labels = [None for _ in edge_lst]
    for i in xrange(len(edge_lst)):
        node, weights = edge_lst[i].split(": ")
        weights = weights.split(",")
        for j in xrange(len(weights)):
            graph[i][j] = int(weights[j])
        labels[i] = node
    return graph, labels

def _parse_adjacency_matrix_with_heuristic(edge_lst):
    split_idx = edge_lst.index("EUCLIDEAN_COORDS:")
    edge_lst, heuristic = edge_lst[:split_idx-1], edge_lst[split_idx+1:]
    graph, labels = _parse_adjacency_matrix(edge_lst)
    coords = [map(float, s.split(': ')[-1].split(',')) for s in heuristic]
    return graph, labels, coords


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
        data = _parse_adjacency_list(graph)
    elif format == "ADJACENCY_MATRIX":
        data = _parse_adjacency_matrix(graph)
    elif format == "ADJACENCY_MATRIX_WITH_HEURISTIC":
        data = _parse_adjacency_matrix_with_heuristic(graph)
    else:
        return ValueError("Unrecognized format")

    return data

