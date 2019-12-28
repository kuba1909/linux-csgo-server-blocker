# linux-csgo-server-blocker
lcsb is a little tool written in Python 3.8. The purpose is to block specific server regions for cs:go matchmaking (which might work for other Valve games as well).

# How does it work?

This scripts fetches the [gameserver infrastructure provided by Valve](https://github.com/SteamDatabase/SteamTracking/blob/master/Random/NetworkDatagramConfig.json) and does a quick ping measurement for each server region. Then it provides a list of those servers sorted ascending by the latency. You can now select an index. All servers below (and including the index) will be blocked for the specified port regions, which means that CS:GO is going to connect you to servers which are not blocked (the remaining ones).

# F.A.Q.

> Does this one still work?

No, it does not work *yet*. The last thing I am missing are the firewall rules.

> Do I have to be the party leader?

I strongly recommend you to be the party leader. If somebody else searches for a match and finds a server which you have blocked but the leader didn't, you will simply not be able to accept while the others can.

> Why another one?

Well, I don't even know if the other ones are working currently. I feel like I need to learn Python and I thought that would be a nice little project.

> Why only Linux?

I am running Linux-based distributions only, that's why. The firewall rules aren't implemented yet, but I am planning to do so with iptables or ufw. I don't know if you can also do that on apple systems, but it is very likely that changes need to be made.

