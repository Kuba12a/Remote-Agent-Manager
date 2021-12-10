import Model.Command as command_model
import HttpClient.HttpClient as http_client
from pprint import pprint



def get_configuration(host_address):
    print("siema1")
    command = command_model.Command
    print("siema2222222")
    command.set_action(command_model.get_configuration)
    url = host_address + "/command"
    result = http_client.send_command(url,command)
    pprint(result)
    



def capture_traffic(host_address, bpf_filter, time):
    command = command_model.Command()
    command.set_action(command_model.capture_traffic)
    command.set_parameters(bpf_filter)
    command.set_time(time)
    url = host_address + "/command"
    http_client.send_command(url,command)


def get_captures_list(host_address):
    url = host_address + "/filenames/pcapng" 
    result = http_client.get_filenames(url)
    pprint(result)

    


def get_captures(host_address,names):
    url = host_address + "/file"
    for n in names:
        http_client.get_file(url,n)


