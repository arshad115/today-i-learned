# Executing remote commands with SSH

Run commands on a remote server without opening an interactive shell. Syntax: `ssh [options] user@hostname "command"`

## Basic syntax

```bash
ssh user@hostname "command"
ssh user@hostname command  # Command is optional
```

Return to local shell immediately after execution.

## Simple examples

```bash
ssh user@hostname "ls -la /tmp"
ssh user@hostname "pwd"
ssh user@hostname "whoami"
```

## Multiple commands

Use semicolons or `&&` (depends on success):

```bash
ssh user@hostname "cd /tmp && ls -la"
ssh user@hostname "uptime; df -h"
```

Or with newlines in a multi-line string:

```bash
ssh user@hostname << 'EOF'
cd /tmp
ls -la
whoami
EOF
```

## Capture output locally

```bash
ssh user@hostname "ls -la /tmp" > local-file.txt
ssh user@hostname "cat /var/log/syslog" | grep "error"
```

## Useful patterns

**Check if service is running:**

```bash
ssh user@hostname "systemctl is-active nginx"
```

**Run with custom port and key:**

```bash
ssh -i ~/.ssh/id_ed25519 -p 2222 user@hostname "df -h"
```

**Execute script on remote:**

```bash
ssh user@hostname < local-script.sh
```

**Run with sudo (prompts for password):**

```bash
ssh user@hostname "sudo systemctl restart nginx"
```

**Background task (agent/daemon):**

```bash
ssh user@hostname "nohup long-running-command > output.log 2>&1 &"
```

## Important notes

- Command runs **non-interactively** — no interactive prompts
- **No shell history** recorded on remote
- **Input/output** fully controlled by local shell
- **Permissions** depend on the ssh user
- **Environment variables** may differ from interactive shell

## SSH key authentication

```bash
# With specific key
ssh -i ~/.ssh/custom_key user@hostname "ls"

# Uses default key (~/.ssh/id_rsa or id_ed25519) if `-i` omitted
ssh user@hostname "ls"
```

## Timeout and error handling

```bash
# Timeout after 5 seconds
ssh -o ConnectTimeout=5 user@hostname "sleep 10"

# Fail if command exits with error (useful in scripts)
ssh user@hostname "false" && echo "Success" || echo "Failed"
```

