class Solution:
    def setZeroes(self, matrix):
        colsList = []
        for row in matrix:
            if row.count(0) > 0:
                for j in range(len(row)):
                    if row[j] == 0:
                        colsList.append(j)
                    row[j] = 0
        for row in matrix:
            for j in colsList:
                row[j] = 0