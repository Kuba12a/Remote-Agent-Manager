import Model.Command as command_model
import HttpClient.HttpClient as http_client
from pprint import pprint



def get_configuration(host_address):
    command = command_model.Command(action = command_model.get_configuration)

    url = host_address
    result = http_client.send_command(url,command)
    pprint(result)
    



def capture_traffic(host_address, bpf_filter, time):
    command = command_model.Command(action = command_model.capture_traffic, parameters = bpf_filter, time = time)
    url = host_address
    http_client.send_command(url,command)


def get_captures_list(host_address):
    url = host_address
    result = http_client.get_filenames(url)
    pprint(result)

    


def get_captures(host_address,names):
    for n in names:
        http_client.get_file(host_address,n)


