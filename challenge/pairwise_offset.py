def pairwise_offset(sequence, fillvalue='*', offset=0):
    tuples = []
    for index in range (0, len(sequence) + offset):
        if index < len(sequence) and index - offset >= 0:
            tuples.append((sequence[index], sequence[index - offset]))
        elif index < len(sequence):
            tuples.append((sequence[index], fillvalue))
        elif index - offset < 0:
            tuples.append((fillvalue, fillvalue))
        else:
            tuples.append((fillvalue, sequence[index - offset]))
    return tuples
