from typing import List

class MatrixOperations:

		def __init__(self, matrix:List[List['int']]):			
			self.matrix = matrix
			self.r, self.c = len(self.matrix), len(self.matrix[0])


		def echo(self) -> str:
			output = ''
			for i,row in enumerate(self.matrix):
				output += ','.join([str(num) for num in row])
				if i < self.r-1:
					output += '\n'
			return output


		def invert(self) -> str:			
			for i in range(self.r):
				for j in range(i+1, self.c):
					self.matrix[i][j], self.matrix[j][i] = self.matrix[j][i], self.matrix[i][j]

			return self.echo()

		def flatten(self) -> str:
			flattenStr = ''
			for i in range(self.r):
				for j in range(self.c):
					flattenStr += (',' if flattenStr else '') + str(self.matrix[i][j])

			return flattenStr

		def sum(self) -> int:
			matrixSum = 0
			for i in range(self.r):
				for j in range(self.c):
					matrixSum += self.matrix[i][j]

			return matrixSum

		def multiply(self) -> int:
			product = 1
			for i in range(self.r):
				for j in range(self.c):
					product *= self.matrix[i][j]
			return product




