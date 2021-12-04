import Model.Command as command_model
import HttpClient.HttpClient as http_client


def capture_traffic(host_address, bpf_filter, time):
    command = command_model.Command(action=command_model.capture_traffic,
                                    parameters = bpf_filter,
                                    time = time)
    http_client.send_command(host_address,command)


def get_captures_list(host_address):

    command = command_model.Command(action=command_model.get_captures_list)
    http_client.send_command(host_address,command)
    #TODO rezultat powinno wyświetlić


def get_captures(host_address,names):

    command = command_model.Command(action=command_model.get_captures, 
                                    names = names)
    http_client.send_command(host_address,command)
    #TODO powinno pobrać pliki do jakiegoś folderu lokalnego np Captures



