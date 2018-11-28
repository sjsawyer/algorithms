"""
roomba.py

This module provides a roomba class, which will enter into a room and clean it.
The algorithm is simply DFS on a grid, however with the added restriction that
we can only travel vertically and horizontally one square at any given time.
That is, when a new cell on the grid is popped off the stack, we cannot simply
jump to it, as we are a vacuum that cannot break the space-time continuum. We
must travel one cell at a time on our grid to reach it.

"""


class Roomba:
    """A roomba vacuum to clean a room.

    Given a room

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
        assert self._valid_tile(self.current), \
            "Roomba placed on an invalid tile at {}".format(self.current)

    def _valid_tile(self, coord):
        ''' Check if we can move to the tile at `coord` '''
        y, x = coord
        return ((0 <= x < len(self.room[0])) and
                (0 <= y < len(self.room)) and
                self.room[y][x] != '#')

    def _move_forward(self):
        ''' Move the roomba one square forward

        Returns:
            bool: True if roomba has moved, False if it was impossible for
            roomba to move forward

        Effects:
            Mutates self.current

        '''

        dy, dx = 0, 0
        if self.heading == self.Heading.NORTH or \
           self.heading == self.Heading.SOUTH:
            # We're moving vertically
            if self.heading == self.Heading.NORTH:
                dy -= 1
            else:
                dy += 1
        else:
            # We're moving horizontally
            if self.heading == self.Heading.EAST:
                dx += 1
            else:
                dx -= 1
        new_coordinate = (self.current[0] + dy, self.current[1] + dx)
        if self._valid_tile(new_coordinate):
            self.current = new_coordinate
            return True
        else:
            return False

    def _rotate(self, target_heading):
        ''' Rotate the roomba to be facing `target_heading`
        '''
        difference = target_heading - self.heading
        if abs(difference) == 3:
            # simpler to reverse the direction of rotation
            if difference == -3:
                difference = 1
            else:
                difference = -1
        if difference > 0:
            self._rotate_cw(difference)
        else:
            self._rotate_ccw(-1*difference)

    def _rotate_cw(self, n):
        ''' Perform `n` 90 degree rotations clockwise '''
        self.heading = (self.heading + n) % 4

    def _rotate_ccw(self, n):
        ''' Perform `n` 90 degree rotations clockwise '''
        self.heading = (self.heading - n) % 4

    def clean(self):
        ''' Clean the current spot in the room '''
        self.room[self.current[0]][self.current[1]] = 'c'

    def _move(self, target_tile):
        ''' Move from the current tile to `target_tile`

        NOTE: Assumes `self.current` and `target_tile` are adjacent
        '''
        # Make sure we need to move
        if target_tile == self.current:
            return False
        # First adjust the heading
        if self.current[0] != target_tile[0]:
            # move vertically
            if self.current[0] > target_tile[0]:
                # move up
                self._rotate(self.Heading.NORTH)
            else:
                # move down
                self._rotate(self.Heading.SOUTH)
        else:
            # move horizontally
            if self.current[1] > target_tile[1]:
                # move left
                self._rotate(self.Heading.WEST)
            else:
                # move right
                self._rotate(self.Heading.EAST)
        # move forward
        return self._move_forward()

    def _set_parent(self, parent, child):
        ''' Set the `parent` tile of `child` tile in self._parent_array
        '''
        self._parent_array[child[0]][child[1]] = parent

    def _get_parent(self):
        ''' Get parent of the current tile
        '''
        return self._parent_array[self.current[0]][self.current[1]]

    def _get_neighbours(self):
        ''' Return the valid neighbours of the current state
        '''
        current_y, current_x = self.current
        # Get all possible neighbouring tiles (possibly invalid)
        neighbours = ((current_y-1, current_x),
                      (current_y+1, current_x),
                      (current_y, current_x-1),
                      (current_y, current_x+1))
        # Filter for only the valid tiles we have not cleaned yet
        neighbours = set((neighbour for neighbour in neighbours
                          if self._valid_tile(neighbour)))
        return neighbours

    def clean_room(self):
        ''' Clean the entire room

        Moves the roomba around the room in a DFS manner, cleaning dirty
        tiles as we come to them. Returns the roomba to its starting
        coordinate when it is finished.

        '''
        # Every time we go to a new tile, we will clean it and add it's valid
        # neighbours onto a stack to be visited.
        seen, to_clean = set(), []
        # Initialize `to_clean` with the current tile
        # (this tile has no parent, which we can use as a terminating condition)
        to_clean.append(self.current)
        seen.add(self.current)
        # start cleaning
        while to_clean:
            dirty_tile = to_clean.pop()
            # move to the tile, if we can
            old_current = self.current
            if self._move(dirty_tile):
                assert self.current == dirty_tile
                # keep track of where we've come from
                self._set_parent(old_current, self.current)
            # clean the tile
            self.clean()
            # add our neighbours to be cleaned
            neighbours_to_clean = \
                filter(lambda neighbour: neighbour not in seen,
                       self._get_neighbours())
            if neighbours_to_clean:
                for neighbour in neighbours_to_clean:
                    to_clean.append(neighbour)
                    seen.add(neighbour)
            else:
                # Nothing to do from here, backtrack
                # Put below logic in a function?
                parent = self._get_parent()
                while parent:
                    self._move(parent)
                    if to_clean and to_clean[-1] in self._get_neighbours():
                        # We have backtracked far enough
                        break
                    parent = self._get_parent()

def main():
    room = [[' ', ' ', ' ', '#'],
            [' ', '#', '#', ' '],
            [' ', ' ', '#', ' '],
            [' ', ' ', ' ', ' '], ]
    roomba = Roomba(room, (0, 0))
    roomba.clean_room()


if __name__ == '__main__':
    main()
