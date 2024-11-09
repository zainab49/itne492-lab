def tower_of_hanoi(n, source, auxiliary, target):
    if n == 1:
        print(f"Move ring 1 from {source} to {target}")
        return
    tower_of_hanoi(n - 1, source, target, auxiliary)
    print(f"Move ring {n} from {source} to {target}")
    tower_of_hanoi(n - 1, auxiliary, source, target)

# Execute the Tower of Hanoi with 4 rings
tower_of_hanoi(4, 'A', 'B', 'C')
