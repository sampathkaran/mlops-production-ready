# ref - https://github.com/aymanejaz/End-To-End-Data-Science-Project

# Excpetion syntax

# class MyCustomError(Exception):
#     """Optional: Docstring explaining the exception"""
#     def __init__(self, message):
#         super().__init__(message)  # Call the base class constructor


import sys

def get_error_message(error):
    # here _ denotes not considering
    # tb store the value of traceback
    _,_,tb= sys.exc_info()
    # get the file name
    filename = tb.tb_frame.f_code.co_filename
    # format it to print the filename, line number, error etc
    error_message = "The error occurred on the file {} line number {} and error is {}".format(filename, tb.tb_lineno,str(error))
    return error_message


class UsVisaException(Exception):
    """Optional: Docstring explaining the exception"""
    def __init__(self, error_message):
        super().__init__(error_message)
        self.error_message = get_error_message(error_message)
    def __str__(self):
        return self.error_message