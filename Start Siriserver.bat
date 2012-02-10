@echo off                                       
echo                              000000
echo                           00        00
echo                           00        00
echo                           00        00
echo                           00        00
echo                           00        00
echo                           00        00
echo                           00--------00
echo                         1 00        00 1
echo                         1 00        00 1
echo                         1 00        00 1
echo                         1 00        00 1
echo                         1 00        00 1
echo                         1 00        00 1
echo                           1 00    00 1
echo                              111111
echo                                11
echo                                11
echo                            ____11____
echo.                    
start python dns.py
start python siriserver.py
cd plugins
serverstatus.bat
