@echo off
echo Just up>serveruptime.txt
PING -n 3600 127.0.0.1>nul
echo 1h>serveruptime.txt
PING -n 3600 127.0.0.1>nul
echo 2h>serveruptime.txt
PING -n 3600 127.0.0.1>nul
echo 3h>serveruptime.txt
PING -n 3600 127.0.0.1>nul
echo 4h>serveruptime.txt
PING -n 3600 127.0.0.1>nul
echo 5h>serveruptime.txt
echo please reboot server and this script!!!
PING -n 3600 127.0.0.1>nul
echo please reboot server and this script!!!
echo ERRPR>serveruptime.txt