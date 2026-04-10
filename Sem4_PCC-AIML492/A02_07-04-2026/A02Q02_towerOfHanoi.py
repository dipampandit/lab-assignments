# Implement Tower of Hanoi and count total moves.

def tower_of_hanoi(disc, source, aux, to, moves=0):
    if disc == 1:
        print(f"Move disk 1 from {source} to {to}")
        return moves + 1

    moves = tower_of_hanoi(disc - 1, source, to, aux, moves)

    print(f"Move disk {disc} from {source} to {to}")
    moves += 1

    moves = tower_of_hanoi(disc - 1, aux, source, to, moves)

    return moves

disc = int(input("Enter number of disks: "))
total_moves = tower_of_hanoi(disc, 'A', 'B', 'C')
print("Total moves:", total_moves)