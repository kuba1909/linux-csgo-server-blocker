COLOR_GREEN = '\033[92m'
COLOR_RED = '\033[91m'
COLOR_YELLOW = '\033[93m'
END_COLOR = '\033[0m'


class ServerInfo:
    def __init__(self, desc, ping):
        self.desc = desc
        self.ping = ping

    def print(self, i):
        print('(' + COLOR_GREEN + str(i) + END_COLOR + ')', end='')
        if i < 10:
            print('\t', end='')
        print('\t-\t', end='')
        if self.ping <= 32:
            print(COLOR_GREEN, end='')
        elif self.ping < 100:
            print(COLOR_YELLOW, end='')
        else:
            print(COLOR_RED, end='')
        print(str(self.ping) + 'ms' + END_COLOR, end='')
        if self.ping < 10:
            print('\t', end='')
        print('\t-\t' + self.desc)
