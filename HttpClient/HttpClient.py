import requests
import Model.Command as Command
import json
import os
import Model.Name as name_model

protocol_prefix = "http://"
get_file_suffix = "/file"

def send_command(URL, command : Command):

    data = json.dumps(command.__dict__)
    status_code = None
    try:
        response = requests.post(url=URL, data=data)
        status_code = response.status_code
    except Exception as ex:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        print(message)
    return status_code



def get_filenames(URL):
    status_code = None
    try:
        response = requests.get(url=URL)
        status_code = response.status_code
        result = response.json()
    except Exception as ex:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        print(message)
    # extracting data in json format

    return result



#Agent will send proper file(name) to FileApi endpoint
def get_file(host_address,name):
    status_code = None
    name_obj = name_model.Name(name = name)
    data = json.dumps(name_obj.__dict__)
    url = protocol_prefix + host_address + get_file_suffix
    try:
        response = requests.post(url=url, data=data)
        if name.endswith(".pcapng"):
            path = os.path.join("Captures", name)
        elif name.endswith(".evtx"):
            path = os.path.join("Logs", name)
        file_to_save = open(path, "wb")
        file_to_save.write(response.content)
        file_to_save.close()
        print(path)
        print(response.status_code)
    except Exception as ex:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        print(message)

