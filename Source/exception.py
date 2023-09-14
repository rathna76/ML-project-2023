import sys

def error_messege_detail(error, error_detail:sys):
    _,_exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    erro_mesege="Error occured in python script name [{{0}] line number [{1}] error message[{2}]".format(
    file_name, exc_tb.tb_lineno,str(error))

    return error_messege

    

class CustomException(Exception):
    def__init_(self,error_messege,error_detail:sys):
        super().__init__(error_messege)
        self.error_messege=error_messege_detail(error_messege,error_detail=error_detail)
    
    def_str_(self):
        return self.error_messege





       

