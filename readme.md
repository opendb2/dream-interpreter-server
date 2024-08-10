### Start in Ec2 server
```
cd /home/dream-interpreter-server
sudo nohup python3.9 main.py > my_script.log &
```
### check port
``
sudo netstat -tuln | grep 7000
``
