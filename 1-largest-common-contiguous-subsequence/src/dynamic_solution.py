"""An algorithm for getting the largest common contiguous subsequence"""

from typing import List, Tuple, Sequence


def lccs(sequence_a: Sequence, sequence_b: Sequence) -> Tuple[int, int, List[int]]:
    """Get all lccs (largest common contiguous subsequence) between 2 sequences"""

    # Sort the strings according to size
    if len(sequence_a) <= len(sequence_b):
        min_sequence, max_sequence = sequence_a, sequence_b
        min_i = 0
    else:
        min_sequence, max_sequence = sequence_b, sequence_a
        min_i = 1

    # Lengths of the strings
    m, n = len(min_sequence), len(max_sequence)

    # The return values
    size = 0  # Size of the lccs
    starts = []  # The starting index of all contiguous subsequences with length of lccs

    # The size of the current contiguous subsequence
    cur_size = None

    # Which side of the perimeter comparison space we currently are in
    state = None  # None -> middle, True -> Right, False -> Left

    # Identifier of middle and perimeter diagonals in the comparison space
    p = 0  # Middle
    q = m - 1  # Perimeter -> The identifier of the perimeter diagonal is its length

    # Index at the string
    x, y = 0, 0  # x -> max_string, y -> min_string

    while True:

        # Stop searching if size of current found lccs is larger than remaining diagonals' length
        if state is not None:
            if size > q:
                return min_i, size, starts

        # Obtain x or y depending on the state
        if state is None:
            x = y + p
        elif state:
            x = (n - 1) - ((q - 1) - y)
        else:
            y = (m - 1) - ((q - 1) - x)

        # Determine whether a common contiguous subsequence is still running
        if max_sequence[x] == min_sequence[y]:
            if cur_size is None:
                cur_size = 0
            cur_size += 1
        else:
            cur_size = None

        # Determine the size of the lccs and if other contiguous subsequences share this length and are therefore to be included
        if cur_size is not None:
            if cur_size >= size:
                if cur_size > size:
                    starts = []
                    size = cur_size
                starts.append(y - size + 1)

        # Stop if at completion of the last diagonal
        if x == 0 and y == (m - 1):
            return min_i, size, starts

        # GO TO THE NEXT X OR Y, P OR Q
        diag_break_cond = ((2 * size) > q) and (cur_size is None)
        if state is None:
            if y == (m - 1):
                if p == (n - m) or ((2 * size) > m):
                    state = True
                    x, y = 0, 0
                    cur_size = None
                    continue
                cur_size = None
                p += 1
            y = (y + 1) % m

        elif state:
            if y == (q - 1) or diag_break_cond:
                state = False
                x = 0
                cur_size = None
            y = (y + 1) % q

        else:
            if x == (q - 1) or diag_break_cond:
                state = True
                y = 0
                cur_size = None
                q -= 1
            x = (x + 1) % q
