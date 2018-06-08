def distance(p1, p2):
    ''' Euclidean distance between `p1` and `p2` '''
    return ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)**0.5


def closest_pair(points):
    '''
    Find the closest pair of points, where each `point` in the list of points
    `points` is a tuple containing an x coordinate and y coordinate, and the
    distance is the usual euclidean distance
    
    >>> closest_pair([(0, 0), (2, 0), (1, 1), (1, 3)])
    (0, 0), (1, 1)

    '''
    if len(points) <= 1:
        raise ValueError("More than 1 point should be provided")

    # sort the points by x value for use later on
    sorted_points = sorted(points)

    # get the order of the y values as well
    sorted_y_idxs = sorted(range(len(points)),
                           key=lambda i: sorted_points[i][1])

    def _closest_pair(i, j):
        '''
        Find the closest pair of points in `sorted_points` from index `i` to
        index `j`
        The closest pair of points can be obtained by finding:
          (1) the closest pair of points in the left half of the sorted list
          (2) the closest pair of points in the right half of the sorted list
          (3) the closest pair of points between the two points found in (1)
              and the two points found in (2) (need to do this in O(n) time)
        '''
        if j == i + 1:
            return i, j, distance(sorted_points[i], sorted_points[j])

        # middle x value of the points
        m = (sorted_points[i][0] + sorted_points[j][0])/2.
        # get the closest points and their distance to the left of x=m,
        # and the closest point and their distance to the right of x=m
        li, lj, dl = _closest_pair(i, (i+j)/2)
        ri, rj, dr = _closest_pair((i+j)/2 + 1, j)

        # the smaller of the two distances
        delta = min(dl, dr)

        # Need to check if there exists a point on the left hand side and a
        # point on the right hand side that are less than `delta` apart
        # To do this, we need only compare 




    return _closest_pair(0, len(sorted_points)-1)
