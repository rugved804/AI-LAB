
def print_board(state):
    n = len(state)
    board = [["."] * n for _ in range(n)]
    for col, row in enumerate(state):
        board[row][col] = "Q"
    for row in board:
        print(" ".join(row))
    print()

def attacking_pairs(state):
    attacks = 0
    n = len(state)
    for i in range(n):
        for j in range(i + 1, n):
            if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
                attacks += 1
    return attacks

def generate_neighbors(state):
    neighbors = []
    n = len(state)
    for i in range(n):
        for j in range(i + 1, n):
            neighbor = state[:]
            neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
            neighbors.append(neighbor)
    return neighbors

def hill_climbing(initial_state):
    current_state = initial_state
    current_cost = attacking_pairs(current_state)
    step = 0
    
    while True:
        print(f"Step {step}: Current state (Cost = {current_cost})")
        print_board(current_state)
        step += 1
        
        neighbors = generate_neighbors(current_state)
        
        print(f"Generated {len(neighbors)} neighbors:")
        for idx, neighbor in enumerate(neighbors):
            print(f"  Neighbor {idx+1}: (Cost = {attacking_pairs(neighbor)})")
            print_board(neighbor)
        
        next_state = None
        next_cost = float('inf')
        
        for neighbor in neighbors:
            cost = attacking_pairs(neighbor)
            if cost < next_cost:
                next_state = neighbor
                next_cost = cost
        
        if next_cost >= current_cost:
            print("No better neighbors found, terminating.\n")
            break
        
        print(f"Moving to better state: (Cost = {next_cost})")
        print_board(next_state)
        current_state = next_state
        current_cost = next_cost
    
    return current_state, current_cost

initial_state = [3, 1, 2, 0]

goal_state, goal_cost = hill_climbing(initial_state)

if goal_cost == 0:
    print("Goal state reached!")
    print_board(goal_state)
else:
    print(f"Local minimum reached with cost {goal_cost}.")
    print_board(goal_state)
