from pydantic import BaseModel
import datetime

get_configuration = "get_configuration"
get_captures_list = "get_captures_list"
get_captures = "get_captures"
get_logs_list = "get_logs_list"
get_logs = "get_logs"
capture_traffic = "capture_traffic"
execute_command = "execute_command"
default_filter = "tcp"
default_time = 30
default_names = "" # Can be multiple TODO
default_command = ""

class Command(BaseModel):
    
        action: str   #get-configuration etc
        bpf_filter: str
        time: int
        names: str  #Can be multiple TODO
        command: str #what to do when execute-command action is used