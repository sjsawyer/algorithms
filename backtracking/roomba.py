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

    def _valid_tile(self, coord):
        ''' Check if we can move to the tile at `coord` '''
        try:
            return self.room[coord[0]][coord[1]] != '#'
        except IndexError:
            return False

    def _move(self):
        ''' Move the roomba one square forward

        Returns:
            bool: True if roomba has moved, False if it was impossible for
            roomba to move forward

        Effects:
            Mutates self.current

        '''

        dx, dy = 0, 0
        if self.heading == Heading.NORTH or Heading.SOUTH:
            # We're moving vertically
            if self.heading == Heading.NORTH:
                dy += 1
            else:
                dy -= 1
        else:
            # We're moving horizontally
            if self.heading == Heading.EAST:
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

    @staticmethod
    def _get_moves(src_tile, target_tile):
        ''' Get the moves necessary to go from `src_tile` to `target_tile`

        NOTE: Assumes `src_tile` and `target_tile` are adjacent
        '''
        pass

    def _get_unvisited_neighbours(self, cleaned):
        ''' Return the neighbours of the current state that we have not yet seen
        '''
        pass

    def _undo_action(self, move_to_undo):
        ''' Reverse the action taken in `move_to_undo` '''
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
        # Store the actions we have taken
        actions = []
        # Initialize `to_clean` with the current tile
        to_clean.append(self.current)
        # start cleaning
        while to_clean:
            dirty_tile = to_clean.pop()
            # move to the tile
            moves = self._get_moves(self.current, dirty_tile)
            for move in moves:
                move()
            # Store these moves for future use
            actions.append(moves)
            # clean the tile
            self.clean()
            # add our neighbours to be cleaned
            dirty_neighbours = self._get_unvisited_neighbours(cleaned)
            if not dirty_neighbours:
                # no where to go from here, undo the last move
                moves_to_undo = actions.pop()
                self._undo_action(moves_to_undo)
            for adjacent_tile in self._get_unvisited_neighbours(cleaned):
                to_clean.append(adjacent_tile)
        # in case we have cleaned all tiles and are not at the starting point
        for action in actions:
            self._undo_action(action)















