A quick Python3 class to query the new governance proposals and get Discord alerts for Terra and the blockchains listed on Mintscan.

Requires <code>terra-sdk</code> and <code>discord-webhook</code>
(Other modules are normally installed by default)

The Discord webhook address must be specified at line 16.

Systemd service is provided, just update the path to the script (and Python executable if required), as well as the arguments (e.g. COSMOS DESMOS SIFCHAIN).<br>
These arguments (upper or lowercase, doesn't matter) should match exactly the blockchain's name, i.e. "SIFCHAIN" and not "SIF".<br>
Then move to <code>/etc/systemd/system/</code> and run <code>systemctl enable discord_governance_alerts.service && systemctl start discord_governance_alerts.service</code> -- for Debian-based systems.
<br>
Otherwise just run with <code>nohup python3 standalone_governance_alerts.py BLOCKCHAIN_1 BLOCKCHAIN_2 ... BLOCKCHAIN_X &</code>
<br>
(if the program stops running, upon next start it will not pick up the proposals submitted in the meantime however).



