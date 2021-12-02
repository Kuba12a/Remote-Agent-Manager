import Model.Command as command_model
import HttpClient.HttpClient as http_client



def get_logs_list(host_address):

    command = command_model.Command(action=command_model.get_logs_list,bpf_filter = command_model.default_filter,
                                    time = command_model.default_time, names = command_model.default_names,
                                     command = command_model.default_command  )
    http_client.send_command(host_address,command)
    #TODO rezultat powinno wyświetlić



def get_logs(host_address,names):

    command = command_model.Command(action=command_model.get_logs, bpf_filter = command_model.default_filter,
                                    time = command_model.default_time, names = names,
                                     command = command_model.default_command  )
    http_client.send_command(host_address,command)
    #TODO powinno pobrać pliki do jakiegoś folderu lokalnego np Logs