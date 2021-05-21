# pypit

simple python SSH tarpit
```
usage: pypit [-h] [-p 22] [-t 5] [-l]

simple SSH tarpit

optional arguments:
  -h, --help        show this help message and exit
  -p 22, --port 22  port to listen on (default 22)
  -t 5, --time 5    seconds to wait between connection checks (default 5)
  -l, --logging     if you want logging enabled (/var/log/pypit.log)
```

# installation

just download the .py and .service files using wget and make it executable with chmod +x
```
wget https://raw.githubusercontent.com/Fingo2409/pypit/master/pypit.py
wget https://raw.githubusercontent.com/Fingo2409/pypit/master/pypit.service
chmod +x pypit.py
```

move the pypit.service file to /etc/systemd/system and create a symlink of pypit.py to /usr/local/bin

```
sudo ln -s /path/to/pypit.py /usr/local/bin/pypit
sudo mv pypit.service /etc/systemd/system
```

pypit is using port 22 (ssh) to listen for connections. if you want another port change the "ExecStart" line in pypit.service

```
ExecStart=/usr/local/bin/pypit -l -p <port>
```

if everything is done you can start the service and enable it for automatic start

```
sudo systemctl start pypit.service
sudo systemctl enable pypit.service
```

that's all. now have a look at the log.

```
tail -f /var/log/pypit.log

[*] Listening as :::22
12:57:54 [+] 45.141.xx.xx is connected.
12:57:58 [+] 186.3.xxx.xxx is connected.
12:57:58 [+] 58.186.xx.xxx is connected.
12:57:59 [+] 79.98.xxx.x is connected.
13:01:34 [+] 61.177.xxx.xx is connected.
13:01:54 [-] 61.177.xxx.xx connection closed after 20 seconds.
13:03:18 [-] 186.3.xxx.xxx connection closed after 320 seconds.
13:03:18 [-] 58.186.xx.xxx connection closed after 320 seconds.
13:03:19 [-] 79.98.xxx.x connection closed after 320 seconds.
13:03:20 [+] 186.3.xxx.xxx is connected.
13:03:20 [+] 58.186.xx.xxx is connected.
13:03:21 [+] 79.98.xxx.xx is connected.
```
