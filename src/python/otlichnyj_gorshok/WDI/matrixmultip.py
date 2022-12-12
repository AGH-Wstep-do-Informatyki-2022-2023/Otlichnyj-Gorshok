
def multip(X,Y):
    result = Y
    for i in range(len(Y[0])):
        for j in range(len(y)):
            result[i][j] = 0;
    for i in range(len(X)):
       for j in range(len(Y[0])):
           for k in range(len(Y)):
               result[i][j] += X[i][k] * Y[k][j]
