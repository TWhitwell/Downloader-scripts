import signal
import time
import psutil
import os
import subprocess
import checkprocess
from networkinterfacechecker import available_networks, vpn

# Check if any bittorent process was running or not.
# If so do nothing
exec(open("networkinterfacechecker.py").read())
if checkprocess.checkIfProcessRunning('qbittorrent') and vpn != False:
    pass
# If not - kill and start nordvpn
else:
    # kill qbittorrent just in case
    PROCNAME = "BitTorrent.exe"
    for proc in psutil.process_iter():
        # check whether the process name matches
        if proc.name() == PROCNAME:
            proc.kill()
    # kill NordVPN
    PROCNAME = "NordVPN.exe"
    for proc in psutil.process_iter():
        # check whether the process name matches
        if proc.name() == PROCNAME:
            proc.kill()
    os.startfile(r"C:\Program Files\NordVPN\NordVPN.exe")
    # wait 30 seconds
    time.sleep(30)
    # ensure VPN is connected
    exec(open("networkinterfacechecker.py").read())
    if 'NordLynx' not in available_networks:
        vpn = False
        if checkprocess.checkIfProcessRunning('NordVPN'):
            subject = 'NordVPN failed'
            plain = 'NordVPN is not connecting to a server'
            html = '<b> NordVPN is not connecting to a server </b>'
            exec(open("emailer.py").read())
    else:
        # start bittorent
        os.startfile(r"C:\Users\Tom\AppData\Roaming\BitTorrent\BitTorrent.exe")
        # checks that bittorent started
        if checkprocess.checkIfProcessRunning('bittorrent'):
            # email me
            subject = 'VPN Connected + qbit restarted'
            plain = 'NordVPN lost connection. Restarted NordVPN + qbittorent '
            html = '<b>NordVPN lost connection. Restarted NordVPN + qbittorent </b>'
            exec(open("emailer.py").read())

        else:
            # failed - will try again email
            subject = 'qbittorrent not started'
            plain = 'NordVPN lost connection. Restarted NordVPN + but qbittorrent wont start will be trying again '
            html = '<b> NordVPN lost connection. Restarted NordVPN + but qbittorrent wont start will be trying again </b>'
            exec(open("emailer.py").read())
