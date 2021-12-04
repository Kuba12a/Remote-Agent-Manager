import Model.Command as command_model
import HttpClient.HttpClient as http_client


def execute_command(host_address,execution_command):
    command = command_model.Command(action=command_model.execute_command,
                                    parameters= execution_command )
    http_client.send_command(host_address,command)

def get_configuration(host_address):
    command = command_model.Command(action=command_model.get_configuration)
    http_client.send_command(host_address,command)
    #TODO rezultat powinno wyświetlić
