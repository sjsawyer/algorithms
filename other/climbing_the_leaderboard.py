'''
Alice is playing an arcade game and wants to climb to the top of the
leaderboard. Can you help her track her ranking as she plays? The game uses
Dense Ranking, so its leaderboard works like this:

    The player with the highest score is ranked number 1 on the leaderboard.
    Players who have equal scores receive the same ranking number, and the next
    player(s) receive the immediately following ranking number.

We want to determine Alice's rank as she progresses up the leaderboard. For
example, the four players on the leaderboard have high scores of 100, 90, 90,
and 80. Those players will have ranks 1, 2, 2, and 3, respectively. If Alice's
scores are 70, 80 and 105, her rankings after each game are 4, 3 and 1.

You are given an array, scores, of monotonically decreasing leaderboard scores,
and another array, alice, of Alice's scores for the game. You must return a list
of integers that should indicate the current rank of alice after her game.

[https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem]

'''


def climbingLeaderboard(scores, alice):
    '''
    Solves the problem in linear time using a two pointer method by first
    calculating the maximum possible rank and iterating once through the
    list of scores and through alice's scores.

    Note: Scores in descending order, alice in ascending order

    '''
    n_scores = len(scores)
    # Get the current last place ranking
    ranking = 1
    for i in range(n_scores-1):
        if scores[i+1] != scores[i]:
            ranking += 1
    # keep track of the leaderboard
    lb = []
    # pointer to end of scores and beginning of alice
    s = n_scores-1
    a = 0
    while a < len(alice) and s > -1:
        # always move the score pointer to the first unique score
        while s > 0 and scores[s] == scores[s-1]:
            s -= 1
        # if alices score is less than the next score, her ranking is one
        # "below" the next ranking
        if alice[a] < scores[s]:
            lb.append(ranking+1)
            a += 1
        # if alices score is equal to the next score, her ranking is the same
        elif alice[a] == scores[s]:
            lb.append(ranking)
            a += 1
        # alice's score is greater than the next score
        else:
            # edge case for when alice is in first
            if s == 0:
                while a < len(alice):
                    lb.append(ranking)
                    a += 1
            # her ranking goes up
            ranking -= 1
            s -= 1
    return lb
    

def main():
    scores = [100, 100, 100, 40, 40, 20, 20]
    alice = [5, 5, 40, 40, 60, 120]
    expected_out = [4, 4, 2, 2, 2, 1]
    actual_out = climbingLeaderboard(scores, alice)
    print "Expected: {}".format(expected_out)
    print "Actual:   {}".format(actual_out)

    scores2 = [295, 294, 291, 287, 287, 285, 285, 284, 283, 279, 277, 274, 274, 271, 270, 268, 268, 268, 264, 260, 259, 258, 257, 255, 252, 250, 244, 241, 240, 237, 236, 236, 231, 227, 227, 227, 226, 225, 224, 223, 216, 212, 200, 197, 196, 194, 193, 189, 188, 187, 183, 182, 178, 177, 173, 171, 169, 165, 143, 140, 137, 135, 133, 130, 130, 130, 128, 127, 122, 120, 116, 114, 113, 109, 106, 103, 99, 92, 85, 81, 69, 68, 63, 63, 63, 61, 57, 51, 47, 46, 38, 30, 28, 25, 22, 15, 14, 12, 6, 4]

    alice2 = [5, 5, 6, 14, 19, 20, 23, 25, 29, 29, 30, 30, 32, 37, 38, 38, 38, 41, 41, 44, 45, 45, 47, 59, 59, 62, 63, 65, 67, 69, 70, 72, 72, 76, 79, 82, 83, 90, 91, 92, 93, 98, 98, 100, 100, 102, 103, 105, 106, 107, 109, 112, 115, 118, 118, 121, 122, 122, 123, 125, 125, 125, 127, 128, 131, 131, 133, 134, 139, 140, 141, 143, 144, 144, 144, 144, 147, 150, 152, 155, 156, 160, 164, 164, 165, 165, 166, 168, 169, 170, 171, 172, 173, 174, 174, 180, 184, 187, 187, 188, 194, 197, 197, 197, 198, 201, 202, 202, 207, 208, 211, 212, 212, 214, 217, 219, 219, 220, 220, 223, 225, 227, 228, 229, 229, 233, 235, 235, 236, 242, 242, 245, 246, 252, 253, 253, 257, 257, 260, 261, 266, 266, 268, 269, 271, 271, 275, 276, 281, 282, 283, 284, 285, 287, 289, 289, 295, 296, 298, 300, 300, 301, 304, 306, 308, 309, 310, 316, 318, 318, 324, 326, 329, 329, 329, 330, 330, 332, 337, 337, 341, 341, 349, 351, 351, 354, 356, 357, 366, 369, 377, 379, 380, 382, 391, 391, 394, 396, 396, 400]

    expected_out2 = [88, 88, 87, 85, 84, 84, 83, 82, 81, 81, 80, 80, 80, 80, 79, 79, 79, 79, 79, 79, 79, 79, 77, 75, 75, 74, 73, 73, 73, 71, 71, 71, 71, 71, 71, 70, 70, 69, 69, 68, 68, 68, 68, 67, 67, 67, 66, 66, 65, 65, 64, 64, 62, 61, 61, 60, 59, 59, 59, 59, 59, 59, 58, 57, 56, 56, 55, 55, 53, 52, 52, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 50, 50, 50, 50, 49, 49, 48, 48, 47, 47, 47, 45, 43, 42, 42, 41, 38, 36, 36, 36, 36, 35, 35, 35, 35, 35, 35, 34, 34, 34, 33, 33, 33, 33, 33, 32, 30, 28, 28, 28, 28, 27, 27, 27, 26, 23, 23, 22, 22, 20, 20, 20, 18, 18, 15, 15, 14, 14, 13, 13, 11, 11, 10, 10, 8, 8, 7, 6, 5, 4, 4, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    actual_out2 = climbingLeaderboard(scores2, alice2)
    assert expected_out2 == actual_out2


if __name__ == '__main__':
    main()
