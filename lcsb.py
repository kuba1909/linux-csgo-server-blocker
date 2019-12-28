import json
import os
import re
import threading
import urllib.request
from typing import List

from serverinfo import ServerInfo

URL = 'https://raw.githubusercontent.com/SteamDatabase/SteamTracking/master/Random/NetworkDatagramConfig.json'


class PingThread(threading.Thread):
    def __init__(self, desc: str, relays):
        threading.Thread.__init__(self)
        self.desc = desc
        self.relays = relays

    def run(self):
        ping_server(self.desc, self.relays)


print('Fetching SteamDatabase servers list from GitHub...')
urlopen = urllib.request.urlopen(URL)
servers = json.load(urlopen)['pops']
serverinfos: List[ServerInfo] = []
threads: List[PingThread] = []

COLOR_YELLOW = '\033[93m'
END_COLOR = '\033[0m'


def ping_server(desc, relays) -> None:
    ping = -1
    for relay in relays:
        if ping != -1:
            break
        pingline = os.popen('ping -c 1 -W 1 ' + relay['ipv4'] + ' | grep time=').read()
        match = re.search('^.+time[=](\\d*)[.].+ms$', pingline)
        if match is not None:
            ping = int(match[1])
        else:
            match = re.search('^.+time[=](\\d*)[\t ]+ms$', pingline)
            if match is not None:
                ping = int(match[1])
    if ping != -1:
        serverinfos.append(ServerInfo(desc, ping))


def is_number(s: str) -> bool:
    try:
        float(s)
        return True
    except ValueError:
        return False


def get_user_input() -> None:
    print('\nPlease choose the first index to be blocked in the firewall')
    print(COLOR_YELLOW + 'Warning!' + END_COLOR + ' All the servers below your choice will be blocked as well')
    user_input: str = input('lcsb (0-' + str((len(serverinfos) - 1)) + ')#')
    while is_number(user_input) is not True or int(user_input) < 0 or int(user_input) >= len(serverinfos):
        print('\nPlease choose the first index to be blocked in the firewall')
        user_input: str = input('lcsb (0-' + str(len(serverinfos) - 1) + ')#')
    print(
        '\nBlocking all servers in the range from ' + serverinfos[int(user_input)].desc + ' to ' + serverinfos[-1].desc)


server_count: int = 0
for server in servers.items():
    try:
        if server[1]['geo'] and server[1]['desc'] and server[1]['relays']:
            server_count += 1
            thread: PingThread = PingThread(server[1]['desc'], server[1]['relays'])
            thread.start()
            threads.append(thread)
    except KeyError:
        pass

print('Fetched list. Pinging ' + str(server_count) + ' servers...')

for thread in threads:
    thread.join()

serverinfos.sort(key=lambda x: x.ping, reverse=False)

for index, item in enumerate(serverinfos):
    item.print(index)

get_user_input()
