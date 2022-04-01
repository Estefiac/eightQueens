from random import randrange

board = []
population = []
uniquePop = []

class EightQueen:

   def __init__(self):
      self.generations = 0
      self.position = 0
      self.newP = 0
      self.collision = -1
      for i in range(8): # Se crea la matriz sin reinas
         board.append([0] * 8)
      self.createBoard()
      while self.collision != 0:
         self.createGeneration()

   def createBoard(self):
      print("\nInitial Board of 8x8:\n")
      for row in board:
         print(row)

   def createGeneration(self):
      if self.generations == 0:
         for i in range(8):
            col = randrange(8)
            board[i][col] = 1
            population.append(col)
         self.generations += 1
         print("\nInitial Population:\n")
         print('\n{} Generation!\n'.format(self.generations))
         for row in board:
            print(row)
      else:
         self.crossOver()
         self.generations += 1
         print('\n{} Generation!\n'.format(self.generations))
         for row in board:
            print(row)
         self.displayData()

   def displayData(self):
      print("\nGenotipos: {}".format(population))
      self.suma = 0
      self.suma = self.checkCollision()
      self.collision = self.suma
      self.fitness = (-((28.0 - self.collision) / 28.0) + 1) * 10 
      print("\nCollisions: {}".format(self.collision))
      print("\nFitness: {0:.2f}%".format(self.fitness))

   def crossOver(self):
      for i in range(1,3): # Cambiar 1 reinas
         self.newP = 0
         self.newP = self.checkPosition()
         if self.newP != -1:
            self.position = randrange(8) #Selecciona posicion aleatoria
            board[self.position][population[self.position]] = 0 # Elimina reina anterior board[1][pob[1]] = 0
            population[self.position] = self.newP # añade nueva reina a la poblacion
            board[self.position][population[self.position]] = 1 # añade reina al tablero
         else:
            self.moveQueens()

   def checkPosition(self):
      uniquePop = list(set(population))
      if uniquePop != [0, 1, 2, 3, 4, 5, 6, 7]:
         val = randrange(8)
         if val in uniquePop and val != population[self.position]:
            return self.checkPosition()
         else:
            return val
      else:
         return -1

   def moveQueens(self):
      self.current = randrange(8)
      self.previous = randrange(8)
      if self.current != self.previous:
         board[self.current][population[self.current]] = 0
         board[self.previous][population[self.previous]] = 0
         population[self.current], population[self.previous] = population[self.previous], population[self.current]
         board[self.current][population[self.current]] = 1
         board[self.previous][population[self.previous]] = 1

   def checkCollision(self):
   	  #Checar diagonal derecha 
      self.counter = 0
      self.row = 0
      for col in population:
         i = self.row + 1
         j = col + 1
         while(j != 8 and i != 8):
            if board[i][j] == board[self.row][col]:
               self.counter += 1
            i += 1
            j += 1
         self.row += 1
      #Checar diagonal derecha 
      self.popInv = []
      self.matrizInv = []
      for a in range(8):
         self.element = 7 - population[a]
         self.popInv.append(self.element)

      for i in range(8):
         self.matrizInv.append([0] * 8)

      for newE in range(8):
         self.matrizInv[newE][self.popInv[newE]] = 1

      self.row = 0
      for col in self.popInv:
         i = self.row + 1
         j = col + 1
         while(j != 8 and i != 8):
            if self.matrizInv[i][j] == self.matrizInv[self.row][col]:
               self.counter += 1
            i += 1
            j += 1
         self.row += 1

      return self.counter 

def main():
   EightQueen()

if __name__ == "__main__":
   main()
