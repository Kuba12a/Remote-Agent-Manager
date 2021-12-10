import Model.Command as command_model
import HttpClient.HttpClient as http_client


def execute_command(host_address,execution_command):
    command = command_model.Command()
    command.set_action(command_model.execute_command)
    command.set_parameters(execution_command)
    url = host_address + "/command"
    http_client.send_command(url,command)
