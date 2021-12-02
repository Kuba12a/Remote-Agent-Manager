import Model.Command as command_model
import HttpClient.HttpClient as http_client





def execute_command(host_address,execution_command):

    command = command_model.Command(action=command_model.get_logs, bpf_filter = command_model.default_filter,
                                    time = command_model.default_time, names = command_model.default_names,
                                     command = execution_command  )
    http_client.send_command(host_address,command)
    