'''
You are playing a Flip Game with your friend.

You are given a string currentState that contains only '+' and '-'. You and your friend take turns to flip two consecutive "++" into "--". The game ends when a person can no longer make a move, and therefore the other person will be the winner.

Return all possible states of the string currentState after one valid move. You may return the answer in any order. If there is no valid move, return an empty list [].



Example 1:

Input: currentState = "++++"
Output: ["--++","+--+","++--"]
Example 2:

Input: currentState = "+"
Output: []


Constraints:

1 <= currentState.length <= 500
currentState[i] is either '+' or '-'.

'''

class Solution:
    def generatePossibleNextMoves(self, currentState: str) -> List[str]:
        next_possible_states = []
        for index in range(len(currentState) - 1):
            if currentState[index] == '+' and currentState[index + 1] == '+':
                next_state = currentState[:index] + "--" + currentState[index + 2:]
                next_possible_states.append(next_state)

        return next_possible_states

