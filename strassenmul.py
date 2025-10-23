def gumarum(X,Y):
  n = len(X)
  Z = []
  for i in range(n):
    Z.append([])
    for j in range(n):
      Z[i].append(X[i][j]+Y[i][j])
  return Z
def hanum(X,Y):
  n = len(X)
  Z = []
  for i in range(n):
    Z.append([])
    for j in range(n):
      Z[i].append(X[i][j]-Y[i][j])
  return Z
def strassenmul(X,Y):
  n = len(X)
  if n == 2:
    a,b,c,d = X[0][0],X[0][1],X[1][0],X[1][1]
    e,f,g,h = Y[0][0],Y[0][1],Y[1][0],Y[1][1]
    P1 = a*(f-h)
    P2 = (a+b)*h
    P3 = (c+d)*e
    P4 = d*(g-e)
    P5 = (a+d) * (e+h)
    P6 = (b-d) * (g+h)
    P7 = (a-c) * (e+f)
    return [[P5+P4-P2+P6,P1+P2],[P3+P4,P1+P5-P3-P7]]
  A = [row[:n//2] for row in X[:n//2]]
  B = [row[n//2:] for row in X[:n//2]]
  C = [row[:n//2] for row in X[n//2:]]
  D = [row[n//2:] for row in X[n//2:]]
  E = [row[:n//2] for row in Y[:n//2]]
  F = [row[n//2:] for row in Y[:n//2]]
  G = [row[:n//2] for row in Y[n//2:]]
  H = [row[n//2:] for row in Y[n//2:]]
  p1 = strassenmul(A,hanum(F,H))
  p2 = strassenmul(gumarum(A,B),H)
  p3 = strassenmul(gumarum(C,D),E)
  p4 = strassenmul(D,hanum(G,E))
  p5 = strassenmul(gumarum(A,D),gumarum(E,H))
  p6 = strassenmul(hanum(B,D),gumarum(G,H))
  p7 = strassenmul(hanum(A,C),gumarum(E,F))
  A0 = gumarum(gumarum(p5,p6),hanum(p4,p2))
  B0 = gumarum(p1,p2)
  C0 = gumarum(p3,p4)
  D0 = gumarum(hanum(p1,p7),hanum(p5,p3))
  Z = []
  for i in range(n//2):
    Z.append(A0[i] + B0[i])
  for i in range(n//2):
    Z.append(C0[i] + D0[i])
  return Z

x = [[2, 0, 1, 3],[1, 2, 0, 4],[3, 1, 2, 1],[0, 1, 3, 2]]
y = [[1, 2, 1, 0],[0, 1, 2, 1],[3, 0, 1, 2],[2, 1, 0, 1]]
result = strassenmul(x, y)
for row in result:
    print(row)
