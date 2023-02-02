# League

## How to run this locally

*Note: Recommended Python3.6 or higher. And the following steps were performed and tested on Windowns OS*

1) The code is using Flask library in Python to host a server locally with the endpoints. The flask can be installed using this command: ```pip install flask```
2) Now to start up the server, run this command: ```python <local_path_to_this_file>\flask_app.py```
3) These APIs were tested using CURL in CMD and can be accessed using following urls locally. Each of the following are POST requests that require matrix.csv file present in current directory from where the request is being hit in CMD/terminal
   - curl -F file=@matrix.csv http://127.0.0.1:5000/echo  
   - curl -F file=@matrix.csv http://127.0.0.1:5000/invert 
   - curl -F file=@matrix.csv http://127.0.0.1:5000/flatten 
   - curl -F file=@matrix.csv http://127.0.0.1:5000/sum 
   - curl -F file=@matrix.csv http://127.0.0.1:5000/multiply 

## Code Structure
- The file that has the ```main``` function is ```flask_app.py```. This file defines all five endpoints: ```echo```, ```invert```, ```flatten```, ```sum``` and ```multiply```.
- The ```matrix_operations.py``` file has ```MatrixOperations``` class that defines methods for matrix operations.
- The ```matrix_operations_test.py``` file has ```TestMatrixOperations``` class that defines all test methods with different cases for testing all matrix operations.
- The ```error.py``` file has ```Error``` class and other custom exception classes for error handling.
- The ```util.py``` file has ```Util``` class that defines basic util functions like uploading, saving file and parsing the CSV file.
- The ```util_test.py``` file has ```TestUtil``` class that defines all test cases for testing csv file upload, save and parse.

## Running unit tests

- To run the unit test files, use the following commands. Unit tests use ```unittest``` library that usually come along with all Python3.8 or above installations. Each unit test file has cases to check for different kind of inputs and also checks for right exception being thrown in case of unexpected or invalid input.
  - ```python <local_path_to_this_file>\util_test.py```
  - ```python <local_path_to_this_file>\matrix_operations_test.py```

![Unit test example execution](https://user-images.githubusercontent.com/24560549/216331179-155b909e-0dc7-41aa-87c3-ee64163962af.JPG)
![API requests example](https://user-images.githubusercontent.com/24560549/216331186-7f492f12-4074-43f4-bcb2-2b5f7f693ac7.JPG)

