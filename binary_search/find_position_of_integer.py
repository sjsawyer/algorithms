'''
Q: Given a list of sorted integers, find the position of an integer in the
   list, and return None if it does not exist.

A: Perform binary search on the list.
   First check the middle element of the list.
   If it is less than the integer we are looking for, recurse on the
   right half of the list.
   Else if it is greater than the integer we are looking for, recurse on the
   left half of the list.
   Otherwise the middle element is the integer we are looking for.
'''

def get_position(arr, x):
    '''
    Returns the position of the integer `x` in the sorted list of integers
    `arr`, and None if `x` is not in `arr`.
    '''
    def _get_position(sidx, eidx):
        '''
        Helper function that returns the position of `x` in `arr`, using
        the knowledge that if `x` exists in `arr`, it is contained within
        `arr[sidx:eidx+1]`
        '''
        if sidx > eidx:
            return None
        midx = (sidx + eidx)/2
        if arr[midx] > x:
            return _get_position(sidx, midx-1)
        elif arr[midx] < x:
            return _get_position(midx+1, eidx)
        else:
            return midx
    # Start the search on the entire list
    return _get_position(0, len(arr)-1)
        
