import os, csv
from error import Error
from error import InvalidFileInputParameterException, UnSupportedFileException, InvalidMatrixInputException, GenericErrorException
from typing import List

# Folder for uploaded files
UPLOAD_FOLDER = 'uploaded\\files'
SUPPORTED_EXTENSIONS = ['csv']


class Util(object):
	
	def is_file_allowed(filename: str) -> bool:
		if '.' in filename:
			return filename.rsplit('.',1)[1].lower() in SUPPORTED_EXTENSIONS
		return False

	@staticmethod
	def upload_file(uploaded_file) -> str:
		# get the uploaded file   
		if not uploaded_file.filename:
			print("Error:: Invalid input file parameter")
			raise InvalidFileInputParameterException	

		if not Util.is_file_allowed(uploaded_file.filename):
			print("Error:: Unsupported extension")
			raise UnSupportedFileException
		
		# set the file path  
		file_path = os.path.join(UPLOAD_FOLDER, uploaded_file.filename)
		          
		print("Info:: Saving file to path: ", file_path)
		uploaded_file.save(file_path)	

		if not os.path.isfile(file_path):
			print("Error:: Error in saving file locally on server")
			raise GenericErrorException

		return file_path		

	@staticmethod
	def parse_csv(filePath) -> List[List[int]]:
		matrix = []
		columns = 0
		with open(filePath) as csv_file:
		    csv_reader = csv.reader(csv_file, delimiter=',')
		    line_count = 0
		    for row in csv_reader:
		    	print(row)
		    	matrix_row = []
		    	for numStr in row:
		    		num = numStr.strip()
		    		if not num.isdigit():
		    			print("Error:: Expecting integer matrix values but found: ", num)
		    			raise InvalidMatrixInputException
		    		matrix_row.append(int(num))		    	
		    	if matrix and len(matrix[-1]) != len(matrix_row):
		    		print("Error:: Matrix is not square and has rows of variable length.")
		    		raise InvalidMatrixInputException
		    	matrix.append(matrix_row)
		if len(matrix) == 0:
			print("Error:: Matrix is empty")
			raise InvalidMatrixInputException
		return matrix
