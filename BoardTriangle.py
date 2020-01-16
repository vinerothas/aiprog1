from Peg import Peg


class BoardTriangle:
    def __init__(self, depth):
        self.depth = depth
        self.board = []
        if depth < 4:
            raise Exception('Depth {} too small'.format(depth))
        for i in range(1, depth + 1):
            self.board.insert(i-1,[])
            for j in range(1, i + 1):
                self.board[i-1].insert(j-1, Peg(i-1,j-1))

        self.board[2][1].hasPeg = False
