# Fail2ban for SSH

Fail2ban helps protect SSH by monitoring auth logs and banning IPs after repeated failed login attempts.

## Install

Ubuntu/Debian:

```bash
sudo apt update
sudo apt install -y fail2ban
```

RHEL/CentOS:

```bash
sudo dnf install -y fail2ban
```

## Enable and start

```bash
sudo systemctl enable fail2ban
sudo systemctl start fail2ban
sudo systemctl status fail2ban
```

## Configure SSH jail (recommended: use jail.local)

Create or edit `/etc/fail2ban/jail.local`:

```ini
[sshd]
enabled = true
port = ssh
logpath = /var/log/auth.log
backend = systemd
maxretry = 5
findtime = 10m
bantime = 1h
```

For RHEL-like systems, `logpath` is usually `/var/log/secure`.

## Apply changes

```bash
sudo systemctl restart fail2ban
```

## Check status and banned IPs

```bash
sudo fail2ban-client status
sudo fail2ban-client status sshd
```

## Unban an IP

```bash
sudo fail2ban-client set sshd unbanip <IP_ADDRESS>
```

## Useful notes

- Keep your own admin/VPN IP in `ignoreip` to avoid locking yourself out.
- Fail2ban is a layer, not a replacement: also use SSH keys and disable password login when possible.
- Test with `maxretry` and `findtime` values that match your server's risk profile.

