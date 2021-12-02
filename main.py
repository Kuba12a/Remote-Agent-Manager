import click
import os
import ActionManagers.ExecuteCommandManager as execute_command_manager
import ActionManagers.PcapManager as pcap_manager
import ActionManagers.LogManager as log_manager

#main groupf to serve multiple commands 
@click.group()
def main():
    pass


#command section
@main.command()
@click.option('--host', default=[], help='Enter host address', required=True)
def get_configuration(host):
    """ Get web configuration from remote agent """
    try:
        print("Wysylam zapytanie do agenta o pobranie jego konfiguracji sieciowej ")
        pcap_manager.get_configuration(host)
    except Exception as ex:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        print(message)
    print("Zakonczono")



@main.command()
@click.option('--host', help='Enter host address', required=True)
@click.option('--filter', default='tcp', help='Enter BPF filter for host to capture')
@click.option('--time', default='300', help='Enter capture time')
def capture_traffic(host, filter, time):
    """ Manage capturing traffic on host """
    try:
        print("Zarządzam packet capture na zdalnym agencie")
        pcap_manager.capture_traffic(host,filter, time)
    except Exception as ex:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        print(message)
    print("Zakonczono")
    



@main.command()
@click.option('--host', help='Enter host address', required=True)
def get_captures_list(host):
    """ Get PCAP list from agent """
    try:
        print("Pobieram list pcapow od agenta")
        pcap_manager.get_captures_list(host)
    except Exception as ex:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        print(message)
    print("Zakonczono")



@main.command()
@click.option('--host', help='Enter host address', required=True)
@click.option('--names', default=[], prompt="Enter file name >", help='Enter pcaps files names', multiple=True)
def get_captures(host, names):
    """ Get PCAPs from agent """
    try:
        print("Pobieram pcapy od agenta")
        pcap_manager.get_captures(host,names)
    except Exception as ex:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        print(message)
    print("Zakonczono")




@main.command()
@click.option('--host', help='Enter host address', required=True)
def get_logs_list(host):
    """ Get Logs list from agent """
    try:
        print("Pobieram liste logów od agenta")
        log_manager.get_logs_list(host)
    except Exception as ex:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        print(message)
    print("Zakonczono")



@main.command()
@click.option('--host', help='Enter host address', required=True)
@click.option('--names', default=[], prompt="Enter file name >", help='Enter pcaps files names', multiple=True)
def get_logs(host, names):
    """ Get Logs from agent """
    try:
        print("Pobieram logi od agenta")
        log_manager.get_logs(host,names)
    except Exception as ex:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        print(message)
    print("Zakonczono")



@main.command()
@click.option('--host', help='Enter host address', required=True)
@click.option('--command', help='Enter execution command', required=True)
def execute_command(host, command):
    """ Execute command on remote agent """
    try:
        print("Wykonuje komende na agencie")
        execute_command_manager.execute_command(host,command)
    except Exception as ex:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        print(message)
    print("Zakonczono")





#start of the programm
if __name__ == '__main__':
    main()