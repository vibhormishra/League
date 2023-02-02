import unittest, io, os
from util import Util, UPLOAD_FOLDER
from werkzeug.datastructures import FileStorage
from error import InvalidFileInputParameterException, UnSupportedFileException, InvalidMatrixInputException, GenericErrorException

class UploadedFile:
	def __init__(self, filename, iostream):
		self.filename = filename
		self.iostream

class TestUtil(unittest.TestCase):

	def test_upload_file_valid_name(self):		
		file_name = 'test_matrix.csv'
		file_storage = FileStorage(io.BytesIO(b"abcdef"), file_name)
		file_path = os.path.join(UPLOAD_FOLDER, file_name)
		self.assertEqual(Util.upload_file(file_storage), file_path, "Failed to process file: test_matrix.csv")

	def test_upload_file_invalid_file_name(self):
		file_name = ''
		file_storage = FileStorage(io.BytesIO(b"abcdef"), file_name)
		file_path = os.path.join(UPLOAD_FOLDER, file_name)
		self.assertRaises(InvalidFileInputParameterException, Util.upload_file, file_storage)

	def test_upload_file_unsupported_file(self):
		file_name = 'test_matrix.jpg'
		file_storage = FileStorage(io.BytesIO(b""), file_name)
		file_path = os.path.join(UPLOAD_FOLDER, file_name)
		self.assertRaises(UnSupportedFileException, Util.upload_file, file_storage)


	def test_parse_csv(self):
		file_name = 'test_matrix.csv'
		file_storage = FileStorage(io.BytesIO(b"1,2,3\n4,5,6\n7,8,9"), file_name)		
		file_path = os.path.join(UPLOAD_FOLDER, file_name)
		file_storage.save(file_path)
		self.assertEqual(Util.parse_csv(file_path), [[1,2,3],[4,5,6],[7,8,9]], "Matrix parsed from csv is not correct")

	def test_parse_csv_uneven_rows(self):
		file_name = 'test_matrix.csv'
		file_storage = FileStorage(io.BytesIO(b"1,2,3\n4,5,6,10\n7,8,9"), file_name)		
		file_path = os.path.join(UPLOAD_FOLDER, file_name)
		file_storage.save(file_path)
		self.assertRaises(InvalidMatrixInputException, Util.parse_csv, file_path)		

	def test_parse_csv_non_int_values(self):
		file_name = 'test_matrix.csv'
		file_storage = FileStorage(io.BytesIO(b"1.0,2,3.8\n4,5,6\n7,8,9"), file_name)		
		file_path = os.path.join(UPLOAD_FOLDER, file_name)
		file_storage.save(file_path)
		self.assertRaises(InvalidMatrixInputException, Util.parse_csv, file_path)

utils_suite = unittest.TestLoader().loadTestsFromTestCase(TestUtil)
runner = unittest.TextTestRunner()
runner.run(utils_suite) 		
