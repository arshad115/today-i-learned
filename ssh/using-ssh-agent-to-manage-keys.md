# Using SSH agent to manage keys

SSH agent is a background process that holds your decrypted SSH keys in memory, so you don't need to enter your passphrase repeatedly.

## How it works

1. **Start the agent** (usually automatic in modern shells):

```bash
eval "$(ssh-agent -s)"
```

2. **Add your key once** (prompts for passphrase):

```bash
ssh-add ~/.ssh/id_ed25519
# Enter passphrase once
```

3. **Use SSH without entering passphrase**:

```bash
ssh user@hostname  # Agent automatically provides the key
ssh user2@host2    # Still no passphrase needed
```

4. **Agent forgets the key when you logout** → automatic cleanup

## Key commands

```bash
ssh-agent -s           # Start agent and output shell commands
ssh-add ~/.ssh/id_ed25519  # Add key (prompts for passphrase)
ssh-add -l             # List all loaded keys
ssh-add ~/.ssh/id_rsa  # Add another key
ssh-add -d ~/.ssh/id_ed25519  # Remove specific key
ssh-add -D             # Remove all keys
```

## Why use SSH agent?

| Method | Passphrase needed? | Visible in history? | Security |
|--------|-------------------|---------------------|----------|
| Direct SSH | Every connection | ❌ | Good |
| SSH agent | Once per session | ❌ | Excellent (recommended) |
| sshpass | No (stored in command) | ⚠️ Yes | Poor |
| Unencrypted key | No | ❌ | Very poor |

## Check if agent is running

```bash
echo $SSH_AUTH_SOCK
# If output is empty, agent not running
```

## Automatic setup in ~/.zprofile or ~/.bash_profile

For convenience, add to your shell profile:

```bash
if [ -z "$SSH_AUTH_SOCK" ]; then
  eval "$(ssh-agent -s)"
fi
ssh-add ~/.ssh/id_ed25519 2>/dev/null
```

This starts the agent automatically and loads your key on login (you'll be prompted for the passphrase once).

