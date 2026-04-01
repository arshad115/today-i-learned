# SSH connection without welcome message or banner

Suppress SSH banners, welcome messages, and diagnostic output using the `-q` (quiet) flag.

## Quiet mode: `-q` flag

```bash
ssh -q user@hostname
ssh -q user@hostname "command"
```

Suppresses:
- Banner messages
- Warning messages
- Diagnostic output

## Multiple verbose levels

```bash
ssh -q user@hostname       # Quiet (minimal output)
ssh user@hostname          # Normal (default)
ssh -v user@hostname       # Verbose (debug info)
ssh -vv user@hostname      # More verbose
ssh -vvv user@hostname     # Maximum verbose
```

## SSH config file approach

For persistent suppression, add to `~/.ssh/config`:

```
Host myserver
    Hostname example.com
    User myuser
    LogLevel QUIET
```

Then use:

```bash
ssh myserver
```

## Disable banner specifically

The server sends banner in `/etc/ssh/banner` or configured location. To suppress:

```bash
ssh -q user@hostname  # Quiet mode
ssh -o "LogLevel=QUIET" user@hostname  # Explicit log level
ssh -o "Banner=none" user@hostname  # Disable banner (if server allows)
```

## With commands (clean output)

Useful for scripts/automation where you only want command output:

```bash
ssh -q user@hostname "ls -la /tmp"
output=$(ssh -q user@hostname "cat file.txt")
```

## Combined with other options

```bash
ssh -q -i ~/.ssh/key -p 2222 user@hostname
ssh -q -o ConnectTimeout=5 user@hostname "echo test"
ssh -q -T user@hostname < script.sh
```

## Note

The `-q` flag controls **local** SSH client messages, not server-side banner. If the server sends a banner, you may still see it. For full suppression at server level, the admin must configure `/etc/ssh/sshd_config` with `Banner none`.

