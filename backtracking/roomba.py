"""
This module provides a roomba class, which will enter into a room and clean it.
An example is provided in the main function.

"""


class Roomba:
    """A roomba vacuum to clean a room.

    <more thorough decription of the class>

    Attributes:
        room (list of list of characters): room to be cleaned
        starting_coordinate (2-tuple of ints): coordinate in the room
            `room` at which to begin and end cleaning.

    """
    class Heading:
        ''' Enumeration for the orientation of the Rooma '''
        NORTH = 0
        EAST  = 1
        SOUTH = 2
        WEST  = 3

    def __init__(self, room, starting_coordinate, heading=Heading.NORTH):
        ''' Place the roomba in the room so we can start cleaning.

        Args:
            room (list of list of characters): room to be cleaned
            starting_coordinate (2-tuple of ints): coordinate in the room
                `room` at which to begin and end cleaning.
            heading (Heading): orientation of the roomba

        Returns:
            None

        '''
        self.room = room
        self.current = starting_coordinate
        self.heading = heading
        self._parent_array = [[None for _ in self.room[0]]
                              for _ in self.room]

    def _valid_tile(self, coord):
        ''' Check if we can move to the tile at `coord` '''
        try:
            return self.room[coord[0]][coord[1]] != '#'
        except IndexError:
            return False

    def _move_forward(self):
        ''' Move the roomba one square forward

        Returns:
            bool: True if roomba has moved, False if it was impossible for
            roomba to move forward

        Effects:
            Mutates self.current

        '''

        dx, dy = 0, 0
        if self.heading == self.Heading.NORTH or self.Heading.SOUTH:
            # We're moving vertically
            if self.heading == self.Heading.NORTH:
                dy += 1
            else:
                dy -= 1
        else:
            # We're moving horizontally
            if self.heading == self.Heading.EAST:
                dx += 1
            else:
                dx -= 1
        new_coordinate = (self.current[0] + dx, self.current[1] + dy)
        if self.valid_tile(new_coordinate):
            self.current = new_coordinate
            return True
        else:
            return False

    def _rotate_cw(self, n):
        ''' Perform `n` 90 degree rotations clockwise '''
        self.heading = (self.heading + n) % 4

    def _rotate_ccw(self, n):
        ''' Perform `n` 90 degree rotations clockwise '''
        self.heading = (self.heading - n) % 4

    def clean(self):
        ''' Clean the current spot in the room '''
        self.room[self.current[0]][self.current[1]] = 'c'

    def _move(target_tile):
        ''' Move from the current tile to `target_tile`

        NOTE: Assumes `self.current` and `target_tile` are adjacent
        '''
        moves = []
        # First adjust the heading
        if self.current[0] == target_tile[0]:
            # move vertically
            if self.current[0] > target_tile[0]:
                # move up



        else:
            # move_horizontally


        # obtain moves (list of _move_forward, _rotate_ccw, _rotate_cw)
        # ... <add that logic here> ...
        for move in moves:
            move()

    def _set_parent(self, parent, child):
        ''' Set the `parent` tile of `child` tile in self._parent_array
        '''
        self._parent_array[child[0]][child[1]] = parent

    def _get_parent(self):
        ''' Get parent of the current tile
        '''
        return self._parent_array[self.current[0]][self.current[1]]

    def _get_unvisited_neighbours(self, cleaned):
        ''' Return the neighbours of the current state that we have not yet seen
        '''
        pass

    def clean_room(self):
        ''' Clean the entire room

        Moves the roomba around the room in a DFS manner, cleaning dirty
        tiles as we come to them. Returns the roomba to its starting
        coordinate when it is finished.

        '''
        # Every time we go to a new tile, we will clean it and add it's valid
        # neighbours onto a stack to be visited.
        cleaned, to_clean = set(), []
        # Initialize `to_clean` with the current tile
        # (this tile has no parent, which we can use as a terminating condition)
        to_clean.append(self.current)
        # start cleaning
        while to_clean:
            dirty_tile = to_clean.pop()
            # move to the tile
            self._move(dirty_tile)
            # keep track of where we've come from
            self._set_parent(self.current, dirty_tile)
            # clean the tile
            self.clean()
            # add our neighbours to be cleaned
            dirty_neighbours = self._get_unvisited_neighbours(cleaned)
            if dirty_neighbours:
                # Add these onto the stack
                for neighbour in dirty_neighbours:
                    to_clean.append(neighbour)
            else:
                # Nothing to do from here, backtrack
                # Put below logic in a function?
                parent = self._get_parent()
                while parent:
                    self._move(parent)
                    if self._get_unvisited_neighbours(cleaned):
                        # We have backtracked far enough
                        # This should always be true
                        assert to_clean[-1] in self._get_unvisited_neighbours
                        break
                    parent = self._get_parent()
