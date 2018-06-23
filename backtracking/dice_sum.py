def dice_sum(n, s):
    '''
    Return all possible combinations of `n` dice that add up to the sum `s`
    '''
    # Store all of the possible combinations
    all_combinations = []
    def _dice_sum(rolled_so_far, n_remaining, s_remaining):
        '''
        Generate all possible combinations of `n` dice that add up to the sum
        `s` that begin with `rolled_so_far`, where the number of nice we have
        left to roll is `n_remaining` and the sum we have left to make with
        those dice is `s_remaining`

        '''
        if s_remaining == 0 and n_remaining == 0:
            # append a copy of rolled_so_far to avoid all_combinations
            # containing references to the same list
            all_combinations.append(list(rolled_so_far))
        elif s_remaining < 0 or n_remaining < 0:
            pass
        elif 6*n_remaining < s_remaining:
            # Early stopping condition, no solutions from here
            pass
        else:
            # Try all possible combinations
            for i in range(1, 6+1):
                rolled_so_far.append(i)
                _dice_sum(rolled_so_far, n_remaining-1, s_remaining-i)
                rolled_so_far.pop()
    # populate all_combinations
    _dice_sum([], n, s)
    return all_combinations


def main():
    num_dice = 3
    desired_sum = 6
    possible_rolls = dice_sum(num_dice, desired_sum)
    print possible_rolls


if __name__ == '__main__':
    main()
