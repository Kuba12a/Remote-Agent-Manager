import Model.Command as command_model
import HttpClient.HttpClient as http_client


def execute_command(host_address,execution_command):
    command = command_model.Command(parameters = execution_command, action = command_model.execute_command)

    url = host_address
    http_client.send_command(url, command)
