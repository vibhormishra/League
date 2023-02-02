import json 

ERROR_INVALID_FILE_INPUT = "Invalid file input"
ERROR_UNSUPPORTED_FILE = 'Unsupported file. Only supported format is [.csv]'
ERROR_INVALID_MATRIX_INPUT = 'Input Matrix is not supported. Require non-empty square matrix with only integer values'
GENERIC_ERROR = "Something went wrong"

class InvalidFileInputParameterException(Exception):
	def __init__(self, message=ERROR_INVALID_FILE_INPUT):
		self.message = message
		super().__init__(message)

class UnSupportedFileException(Exception):
	def __init__(self, message=ERROR_UNSUPPORTED_FILE):
		self.message = message
		super().__init__(message)	

class InvalidMatrixInputException(Exception):
	def __init__(self, message=ERROR_INVALID_MATRIX_INPUT):
		self.message = message
		super().__init__(message)	

class GenericErrorException(Exception):
	def __init__(self, message=GENERIC_ERROR):
		self.message = message
		super().__init__(message)						

class Error:
	def __init__(self, e: Exception):
		if isinstance(e, InvalidFileInputParameterException):
			self.error_str = ERROR_INVALID_FILE_INPUT
		elif isinstance(e, UnSupportedFileException):
			self.error_str = ERROR_UNSUPPORTED_FILE
		elif isinstance(e, InvalidMatrixInputException):
			self.error_str = ERROR_INVALID_MATRIX_INPUT				
		else:
			self.error_str = GENERIC_ERROR

	def get_json(self) -> dict:
		return json.dumps({'error':self.error_str})