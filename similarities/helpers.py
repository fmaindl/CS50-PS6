from enum import Enum


class Operation(Enum):
    """Operations"""

    DELETED = 1
    INSERTED = 2
    SUBSTITUTED = 3

    def __str__(self):
        return str(self.name.lower())


def distances(a, b):
    """Calculate edit distance from a to b"""
    height = len(a)
    width = len(b)


    matrix=[[(0, None) for i in range(width+1)] for j in range(height+1)]

    for i in range(1, (height + 1)):
        matrix[i][0] = (i, Operation.DELETED)

    for j in range(1, (width + 1)):
        matrix[0][j] = (j, Operation.INSERTED)

    for i in range(1, (height + 1)):
        for j in range(1, (width + 1)):
            del_cost, _ = matrix[i-1][j]
            ins_cost, _ = matrix[i][j-1]
            sub_cost, _ = matrix[i-1][j-1]


            del_cost += 1
            ins_cost += 1

            if a[i-1] != b[j-1]:
                sub_cost += 1


            if min(del_cost, ins_cost, sub_cost) == del_cost:
                matrix[i][j] = (del_cost, Operation.DELETED)

            elif min(del_cost, ins_cost, sub_cost) == ins_cost:
                matrix[i][j] = (ins_cost, Operation.INSERTED)

            elif min(del_cost, ins_cost, sub_cost) == sub_cost:
                matrix[i][j] = (ins_cost, Operation.SUBSTITUTED)


    return matrix

