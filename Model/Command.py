from pydantic import BaseModel
from typing import Optional
import datetime

# actions
get_configuration = "get_configuration"
# get_captures_list = "get_captures_list"
# get_captures = "get_captures"
# get_logs_list = "get_logs_list"
# get_logs = "get_logs"
capture_traffic = "capture_traffic"
execute_command = "execute_command"

'''
action: how data passed to Agent should be interpreted - type of command
names: names of files to be downloaed from agent - default: ""
time: time for pcap generation - default: 30
parameter: parameters for commands - default: ""
        get_configuration: which configuration
        execute_command: command to be executed
        get_captures: BPF filter
        .
        .
        .
'''


class Command(BaseModel):
    action: str
    time: Optional[int] = None
    parameters: Optional[str] = None


