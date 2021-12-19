import Model.Command as command_model
import HttpClient.HttpClient as http_client
import pprint



def get_logs_list(host_address):

    #command = command_model.Command(action=command_model.get_logs_list)
    url = host_address
    result = http_client.get_logs(url)
    pprint.pprint(result)



def get_logs(host_address,names):
    url = host_address
    for n in names:
        http_client.get_file(url,n)
