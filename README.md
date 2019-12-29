# linux-csgo-server-blocker
lcsb is a little tool written in Python 3.8. The purpose is to block specific server regions for cs:go matchmaking (which might work for other Valve games as well).

# How does it work?

This script fetches the [gameserver infrastructure provided by Valve](https://github.com/SteamDatabase/SteamTracking/blob/master/Random/NetworkDatagramConfig.json) and does a quick ping measurement for each server region. Then it provides a list of those servers sorted ascending by the latency. You can now select an index. All servers below (and including the index) will be blocked for the specified port regions, which means that CS:GO is going to connect you to servers which are not blocked (the remaining ones).

# F.A.Q.

> Does this one still work?

Yes, at the time of writing this script works. If it does not anymore, feel free to contact me.

> Do I have to be the party leader?

I strongly recommend you to be the party leader. If somebody else searches for a match and finds a server which you have blocked but the leader didn't, you will simply not be able to accept while the others can.

> Failed blocking a server in [region], skipping...
>
> Could not enable ufw, are you a privileged user?

Try running the script as root.

> I want to unblock all servers.

The script does not provide a functionality for deletion *yet*. You can delete the rules by hand as of now, they have comments prefixed with `lcsb - `

> I want to unblock a specific server/region.

See the answer above.

> Why another one?

Well, I don't even know if the other ones are working currently. I feel like I need to learn Python and I thought that would be a nice little project.

> Why only Linux?

I am running Linux-based distributions only, that's why. The firewall rules are applied by ufw. I don't know if you can also do that on Apple/BSD/... systems, but it is very likely that changes need to be made.
