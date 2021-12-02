# Remote-Agent-Manager

### Usage

### 1. Get web configuration from remote agent
```
python main.py get-configuration 
--host [remote agent address] *required
```

### 2. Manage traffice capture on remote agent
```
python main.py capture-traffic 
--host [remote agent address] *required
--filter [BPF filter for host to capture] *default=tcp
--time [Capture time in seconds] *default=30s
```

### 3. Get PCAPs list from remote agent
```
python main.py get-captures-list 
--host [remote agent address] *required
```

### 4. Get PCAPs from remote agent
```
python main.py get-captures
--host [remote agent address] *required
--names *prompt pops up, enter files names >
```

### 5. Get Logs list from remote agent
```
python main.py get-logs-list 
--host [remote agent address] *required
```

### 6. Get Logs from remote agent
```
python main.py get-logs
--host [remote agent address] *required
--names *prompt pops up, enter files names >
```

### 7. Execute command on remote agent
```
python main.py execute-command
--host [remote agent address] *required
--command [command to execute] *required
```


