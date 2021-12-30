def pr():
  for x in board:
    for y in x:
      print(y,end="|")
    print()

def win(p):
  for x in board:
    if x.count(p)==3:
      return True
  for x in range(3):
    k=0
    for y in range(3):
      if board[y][x]==p:
        k+=1
    if k==3:
      return True
  k,j=0,0
  for x in range(3):
    if board[x][x]==p:
      k+=1
    if board[x][2-x]==p:
      j+=1
  if k==3 or j==3:
    return True
  return False

def draw():
  for x in board:
    for y in x:
      if y=='-':
        return False
  return True

def computer():
  for i in range(3):
    for j in range(3):
      if board[i][j]=='-':
        board[i][j]='O'
        if win('O'):
          return
        board[i][j]='-'
  for i in range(3):
    for j in range(3):
      if board[i][j]=='-':
        board[i][j]='X'
        if win('X'):
          board[i][j]='O'
          return
        board[i][j]='-'
  for i in range(3):
    for j in range(3):
      if board[i][j]=='-':
        board[i][j]='O'
        return



board=[['-','-','-'],
       ['-','-','-'],
       ['-','-','-']]

while True:
  if draw():
    print("Match drawn")
    break
  if not win('X') and not win('O'):
    print("Player X turn")
    x,y=map(int,input().split())
    board[x-1][y-1]='X'
    pr()
  else:
    break
  if not win('X') and not win('O'):
    print("Computer turn")
    computer()
    pr()
  else:
    break
  
if win('X'):
  print("Player X won")
elif win('O'):
  print("Computer won")
