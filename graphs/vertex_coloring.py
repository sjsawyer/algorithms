def vertex_coloring(graph, m):
    '''
    Try to color the vertices of the graph `graph` using `m` colors so that no
    two adjacent vertices are of the same color. If possible, returns a
    coloring for the vertices. If not possible, returns None.

    Note: `graph` is in adjacency list format, where the keys of `graph` are
    the nodes in the graph, and the values are sets containing the adjacent
    nodes in the graph.

    '''
    # available colors
    colors = set(range(1, m+1))
    # Store the colors of each vertex
    # 0 will indicate no color, and 1, 2, ..., m will represent the colors
    color_dict = {}
    for node in graph:
        color_dict[node] = 0

    # attempt to color the vertices in an arbitrary order
    vertices = graph.keys()

    def _color_vertex(graph, color_dict, vertices, idx):
        '''
        Check if there is a way to color the `graph` using vertices that have
        already been successfully colored in `color_dict`, considering the
        vertex at `vertices[idx]`
        '''
        if idx == len(vertices):
            # We have colored all vertices
            return color_dict
        # current vertex
        vertex = vertices[idx]
        # We try to color the next vertex
        used_colors = set(color_dict[neighbour] for neighbour in graph[vertex]
                          if color_dict[neighbour])
        available_colors = colors.difference(used_colors)
        for color in available_colors:
            color_dict[vertex] = color
            coloring = _color_vertex(graph, color_dict, vertices, idx+1)
            if coloring is not None:
                return coloring
            # a coloring was not possible with this choice, try next color
            continue
        # we were not able to color the vertex, backtrack
        color_dict[vertex] = 0
        return None

    # Start the coloring from `vertices[0]`
    return _color_vertex(graph, color_dict, vertices, 0)


def main():
    from sample_graphs import g1
    print vertex_coloring(g1, 3)


if __name__ == '__main__':
    main()
