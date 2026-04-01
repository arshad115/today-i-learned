# SSH connection basics: password, keys, and parameters

Basic SSH syntax: `ssh [options] [user@]hostname`

## Password authentication

```bash
ssh user@hostname
# Prompts for password
```

## Key-based authentication

Use a specific private key:

```bash
ssh -i ~/.ssh/id_rsa user@hostname
```

With custom key location:

```bash
ssh -i /path/to/private/key user@hostname
```

Common key paths:
- `~/.ssh/id_rsa` — RSA key
- `~/.ssh/id_ed25519` — Ed25519 key (recommended)
- `~/.ssh/id_ecdsa` — ECDSA key

## Useful parameters

| Option | Purpose |
|--------|---------|
| `-p port` | Custom SSH port (default 22) |
| `-i keyfile` | Specify private key file |
| `-v` | Verbose output (debug connection issues) |
| `-vv` or `-vvv` | More verbose |
| `-X` | Enable X11 forwarding |
| `-L local:remote` | Local port forwarding |
| `-R remote:local` | Remote port forwarding |
| `-N` | Don't open shell (useful with port forwarding) |
| `-f` | Run in background |
| `-t` | Force pseudo-terminal allocation |

## Examples

Connect on custom port with specific key:

```bash
ssh -i ~/.ssh/id_ed25519 -p 2222 user@hostname
```

Run remote command and exit (no shell):

```bash
ssh user@hostname "ls -la /tmp"
```

Port forwarding (local):

```bash
ssh -L 8080:localhost:3000 user@hostname -N -f
# Maps localhost:8080 → remote:3000
```

Verbose debugging:

```bash
ssh -vvv user@hostname
```

## SSH key best practices

- Use Ed25519 keys (`ssh-keygen -t ed25519`)
- Protect with passphrase
- Store in `~/.ssh/` with restricted permissions (`chmod 600`)
- Use SSH agent for convenience
