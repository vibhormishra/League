import unittest
from matrix_operations import MatrixOperations

class TestMatrixOperations(unittest.TestCase):
	
	def test_echo(self):
		matrix = [[1,2,3],[4,5,6],[7,8,9]]
		matrixOperations = MatrixOperations(matrix)
		self.assertEqual(matrixOperations.echo(), '1,2,3\n4,5,6\n7,8,9', 'Incorrect matrix output format')

	def test_echo_single_element(self):
		matrix = [[1]]
		matrixOperations = MatrixOperations(matrix)
		self.assertEqual(matrixOperations.echo(), '1', 'Incorrect matrix output format')

	def test_invert(self):
		matrix = [[1,2,3],[4,5,6],[7,8,9]]
		matrixOperations = MatrixOperations(matrix)
		self.assertEqual(matrixOperations.invert(), '1,4,7\n2,5,8\n3,6,9', 'Incorrect result from invert method')

	def test_flatten(self):
		matrix = [[1,2,3],[4,5,6],[7,8,9]]
		matrixOperations = MatrixOperations(matrix)
		self.assertEqual(matrixOperations.flatten(), '1,2,3,4,5,6,7,8,9', 'Incorrect result from flatten method')

	def test_sum(self):
		matrix = [[1,2,3],[4,5,6],[7,8,9]]
		matrixOperations = MatrixOperations(matrix)
		self.assertEqual(matrixOperations.sum(), 45, 'Incorrect sum of matrix elements')

	def test_sum_negative_elements(self):
		matrix = [[1,-20],[4,5]]
		matrixOperations = MatrixOperations(matrix)
		self.assertEqual(matrixOperations.sum(), -10, 'Incorrect sum of matrix elements')

	def test_multiply(self):
		matrix = [[1,2,3],[4,5,6],[7,8,9]]
		matrixOperations = MatrixOperations(matrix)
		self.assertEqual(matrixOperations.multiply(), 362880, 'Incorrect matrix elements product')

	def test_multiply_zero_result(self):
		matrix = [[1,0,3],[4,5,6],[7,8,9]]
		matrixOperations = MatrixOperations(matrix)
		self.assertEqual(matrixOperations.multiply(), 0, 'Incorrect matrix elements product')

	def test_multiply_negative_result(self):
		matrix = [[-1,-2],[-4,5]]
		matrixOperations = MatrixOperations(matrix)
		self.assertEqual(matrixOperations.multiply(), -40, 'Incorrect matrix elements product')


matrix_operations_suite = unittest.TestLoader().loadTestsFromTestCase(TestMatrixOperations)
runner = unittest.TextTestRunner()
runner.run(matrix_operations_suite)                      
