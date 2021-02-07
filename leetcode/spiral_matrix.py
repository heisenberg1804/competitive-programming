class Solution(object):
    def spiralOrder(self, matrix):
        x = []
        k=0
        l=0
        m, n = len(matrix), len(matrix[0])
        while (k<m and l<n):
            for i in list(range(l, n)):
                x.append(matrix[k][i])
            k += 1

            for i in list(range(k,m)):
                x.append(matrix[i][n-1])

            n -= 1

            if (k<m): #is this condition necessary???
                for i in list(range(n-1, l-1, -1)): # why l-1 ???
                    x.append(matrix[m-1][i])
            m -=1

            if (l<n):  #is this condition necessary???
                for i in list(range(m-1,k-1, -1)):
                    x.append(matrix[i][l])
            l += 1 
        return x

        
