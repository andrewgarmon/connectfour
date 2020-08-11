class Board:
    def __init__(self, size):
        self.size = size
        self.initialize_board()

    def initialize_board(self):
        self.tiles = [['-' for i in range(self.size)] for j in range(self.size)]
        self.heights = [0] * self.size

    def print_board(self):
        for row in self.tiles:
            for tile in row:
                print(tile, end = "  ")
            print('')
        for i in range(1,self.size+1):
            if (i < 10):
                print(str(i), end="  ")
            else:
                print(str(i), end=" ")
        print('')

    def place_tile(self, column, piece):
        if self.heights[column] == self.size:
            return False
        else:
            self.heights[column] += 1
            self.tiles[self.size - self.heights[column]][column] = piece
            return True

    def check_win(self, piece):
        # Check for row win
        for row in self.tiles:
            count = 0
            for tile in row:
                if tile == piece:
                    count += 1
                    if count >= 4:
                        return True
                else:
                    count = 0

        #Check for column win
        for i in range (0, self.size):
            if self.heights[i] > 3:
                count = 0
                for j in range(0,self.size):
                    if self.tiles[j][i] == piece:
                        count += 1
                        if count >= 4:
                            return True
                    else:
                        count = 0
        #Check for diagonal win
        # L to R, Bottom to Top
        for i in range(3, self.size):
            count = 0
            for j in range(0, i+1):
                if self.tiles[i-j][j] == piece:
                    count += 1
                else:
                    count = 0
                if count == 4:
                    return True
        #R to L, Bottom to Top
        for i in range(3, self.size):
            count = 0
            for j in range(0, i+1):
                if self.tiles[i-j][self.size - j - 1] == piece:
                    count += 1
                else:
                    count = 0
                if count == 4:
                    return True
        
        #L to R, Top to Bottom
        for i in range(0, self.size - 3):
            count = 0
            for j in range(0, self.size - i):
                if self.tiles[i+j][j] == piece:
                    count += 1
                else:
                    count = 0
                if count == 4:
                    return True

        # R to L, Top to Bottom
        for i in range(0, self.size - 3):
            count = 0
            for j in range (0, self.size - i):
                if self.tiles[i+j][self.size - j - 1] == piece:
                    count += 1
                else:
                    count = 0
                if count == 4:
                    return True
        return False
            
    def check_full(self):
        for row in self.tiles:
            for tile in row:
                if tile == '-':
                    return False
        return True