from flask import Flask, url_for, request, url_for
import json, os, csv
from error import Error
import traceback
from util import Util, UPLOAD_FOLDER
from error import GenericErrorException
from matrix_operations import MatrixOperations


api = Flask(__name__)
api.config["DEBUG"] = True

@api.route("/echo", methods=['POST'])
def matrix_echo():          
      try: 
        file_path = Util.upload_file(request.files['file'])
        data = Util.parse_csv(file_path)
        matrixOps = MatrixOperations(data)
        return  matrixOps.echo()     
      except Exception as e:
        return Error(e).get_json() 

@api.route("/invert", methods=['POST'])
def matrix_invert():          
      try: 
        file_path = Util.upload_file(request.files['file'])
        data = Util.parse_csv(file_path)
        matrixOps = MatrixOperations(data)
        return  matrixOps.invert()     
      except Exception as e:
        return Error(e).get_json() 

@api.route("/flatten", methods=['POST'])
def matrix_flatten():          
      try: 
        file_path = Util.upload_file(request.files['file'])
        data = Util.parse_csv(file_path)
        matrixOps = MatrixOperations(data)
        return  matrixOps.flatten()     
      except Exception as e:
        return Error(e).get_json() 

@api.route("/sum", methods=['POST'])
def matrix_sum():          
      try: 
        file_path = Util.upload_file(request.files['file'])
        data = Util.parse_csv(file_path)
        matrixOps = MatrixOperations(data)
        return  str(matrixOps.sum())
      except Exception as e:
        return Error(e).get_json() 

@api.route("/multiply", methods=['POST'])
def matirx_multiply():          
      try: 
        file_path = Util.upload_file(request.files['file'])
        data = Util.parse_csv(file_path)
        matrixOps = MatrixOperations(data)
        return  str(matrixOps.multiply())
      except Exception as e:
        return Error(e).get_json()                               

if __name__ == '__main__':    
  if not os.path.exists(UPLOAD_FOLDER):
    print("Info:: Upload folder path doesn't exists. Creating folders... [",UPLOAD_FOLDER,"]") 
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
  api.run()