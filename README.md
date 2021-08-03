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

move the pypit.service file to /etc/systemd/system and pypit.py to /usr/local/bin

```
sudo mv pypit.py /usr/local/bin
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
2021-08-03_12:25:29 [+] 77.132.xx.xx is connected.
2021-08-03_12:31:20 [-] 77.132.xx.xx connection closed after 350 seconds.
2021-08-03_12:31:22 [+] 77.132.xx.xx is connected.
2021-08-03_12:32:23 [+] 218.92.x.xxx is connected.
2021-08-03_12:32:38 [-] 218.92.x.xxx connection closed after 15 seconds.
2021-08-03_12:36:42 [-] 77.132.xx.xx connection closed after 320 seconds.
2021-08-03_12:36:43 [+] 77.132.xx.xx is connected.
2021-08-03_12:42:03 [-] 77.132.xx.xx connection closed after 320 seconds.
2021-08-03_12:42:04 [+] 77.132.xx.xx is connected.
2021-08-03_12:44:15 [+] 205.185.xxx.xxx is connected.
2021-08-03_12:44:25 [-] 205.185.xxx.xxx connection closed after 10 seconds.
```
