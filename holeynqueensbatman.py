
class Board:
  EMPTY = 1
  HOLE = 0
  QUEEN = 2

  def __init__(self, n, holes):
    self.n = n
    self.board = [None] * n
    for i in range(n):
      self.board[i] = [Board.EMPTY] * n
    
    for hole in holes:
      self.board[hole[0]][hole[1]] = Board.HOLE
      

  def print_board(self):
    print('-' * len(self.board[0] * 2))
    for row in self.board:
      print(*row)
    print('-' * len(self.board[0] * 2))

  def available(self, r, c):
    return (self.available_row(r) and self.available_col(c) and self.available_diag(r, c))
  
  def available_row(self, target_r):
    row = self.board[target_r]
    for c in row:
      if c != Board.EMPTY:
        return False
    return True
  
  def available_col(self, target_c):
    for r in range(n):
      for c in range(n):
        if c == target_c and self.board[r][c] != Board.EMPTY:
          return False
    return True
  
  def in_bounds(self, r, c):
    return  0 <= r < n and 0 <= c < n

  def available_diag(self, target_r, target_c):

    r = target_r
    c = target_c
    # top left
    while self.in_bounds(r, c):
      if self.board[r][c] != Board.EMPTY:
        return False
      r -= 1
      c -= 1

    r = target_r
    c = target_c
    # top right
    while self.in_bounds(r, c):
      if self.board[r][c] != Board.EMPTY:
        return False
      r -= 1
      c += 1
    
    r = target_r
    c = target_c
    # bottom left
    while self.in_bounds(r, c):
      if self.board[r][c] != Board.EMPTY:
        return False
      r += 1
      c -= 1
    
    r = target_r
    c = target_c
    # bottom right
    while self.in_bounds(r, c):
      if self.board[r][c] != Board.EMPTY:
        return False
      r += 1
      c += 1
    
    return True
        






while True:
  n, num_holes = map(int, input().split()) 

  if n == 0 and num_holes == 0:
    break

  holes = []
  for _ in range(num_holes):
    r, c = map(int, input().split())
    holes.append((r, c))


  num_queens = 0
  x = 0
  while num_queens <= n:
    num_queens = 0
    board = Board(n, holes)
    for r in range(x, n):
      if num_queens == n:
        break
      for c in range(n):
        if board.available(r, c):
          board.board[r][c] = Board.QUEEN
          num_queens += 1
    x += 1
  
  
  board.print_board()
          

      
