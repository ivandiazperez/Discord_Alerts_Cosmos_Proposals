# Discord_Alerts_Terra_Proposals

A quick Python class to query the new Terra governance proposals and get Discord alerts.

Requires <code>terra-sdk discord-webhook</code>

The Discord webhook address must be specified at line 13.

Systemd service is provided, just update the path to the script (and Python executable if required) then move to <code>/etc/systemd/system/</code>
and run <code>systemctl enable discord_governance_alerts.service && systemctl start discord_governance_alerts.service</code> -- for Debian-based systems.
