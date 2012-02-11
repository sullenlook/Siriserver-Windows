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
cd scripts             
start python dns.py
cd plugins
start serverstatus.bat
cd ..
:start
python siriserver.py
goto start
