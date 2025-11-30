n = int(input())

left_intervals = [0] * n
right_intervals = [0] * n

for i in range(n):
    left_intervals[i], right_intervals[i] = map(int, input().split())

# Calculate total perimeter assuming no shared walls
total_boundaries = sum((right_intervals[i] - left_intervals[i]) * 4 for i in range(n))


def side_by_side_walls(start, end):
    """Return a list of cell positions in a row interval."""
    return [start + i for i in range(end - start)]


def find_shared_walls(left, right):
    """Calculate the total number of shared walls horizontally and vertically."""
    horizontal_shared = sum(max(0, right[i] - left[i] - 1) for i in range(n))

    vertical_cells = [side_by_side_walls(left[i], right[i]) for i in range(n)]

    vertical_shared = sum(
        len(set(vertical_cells[i]) & set(vertical_cells[i + 1])) for i in range(n - 1)
    )

    return horizontal_shared + vertical_shared


# Adjust total perimeter by subtracting shared walls (each shared wall reduces 2 units)
print(total_boundaries - find_shared_walls(left_intervals, right_intervals) * 2)
