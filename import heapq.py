import heapq

class PuzzleState:
    def __init__(self, board, zero_pos, g=0, parent=None):
        self.board = board
        self.zero_pos = zero_pos 
        self.g = g 
        self.h = self.misplaced_tiles()  
        self.f = self.g + self.h  
        self.parent = parent  

    def misplaced_tiles(self):
        goal = [0,1, 2, 3, 4, 5, 6, 7, 8]
        return sum(1 for i in range(9) if self.board[i] != goal[i])

    def get_neighbors(self):
        neighbors = []
        row, col = self.zero_pos
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  

        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < 3 and 0 <= new_col < 3:
                new_board = self.board[:]
                new_board[row * 3 + col], new_board[new_row * 3 + new_col] = new_board[new_row * 3 + new_col], new_board[row * 3 + col]
                neighbors.append(PuzzleState(new_board, (new_row, new_col), self.g + 1, self))

        return neighbors

    def __lt__(self, other):
        return self.f < other.f

    def print_path(self):
        if self.parent is not None:
            self.parent.print_path()
        print(self.board_to_string())
        print("\n")

    def board_to_string(self):
        return "\n".join(
            " ".join(str(self.board[i * 3 + j]) for j in range(3)) for i in range(3)
        )

def a_star(initial_board):
    zero_pos = initial_board.index(0)
    initial_state = PuzzleState(initial_board, (zero_pos // 3, zero_pos % 3))

    open_set = []
    heapq.heappush(open_set, initial_state)
    closed_set = set()

    while open_set:
        current_state = heapq.heappop(open_set)

        if current_state.h == 0:  
            print("Solution found:")
            current_state.print_path()
            return current_state.g

        closed_set.add(tuple(current_state.board))

        for neighbor in current_state.get_neighbors():
            if tuple(neighbor.board) in closed_set:
                continue

            if not any(neighbor.board == state.board for state in open_set):
                heapq.heappush(open_set, neighbor)

    return None  

initial_board = [5,4,0,6,1,8,7,3,2]
steps = a_star(initial_board)
print(f'Solution found in {steps} moves' if steps is not None else 'No solution found.')
