# Using rsync for file transfers

`rsync` synchronizes files over SSH, with smart incremental copying (only transfers changed parts). Syntax: `rsync [options] source destination`

**See also:** [Using scp for file transfers](using-scp-for-file-transfers.md) — comparison below.

## Local to remote

Copy a single file to remote:

```bash
rsync -avz ./local-file.txt user@hostname:/path/to/remote/
```

Copy a folder to remote:

```bash
rsync -avz ./local-folder/ user@hostname:/path/to/remote/
```

## Remote to local

Download a single file from remote:

```bash
rsync -avz user@hostname:/path/to/remote/file.txt ./local-folder/
```

Download a folder from remote:

```bash
rsync -avz user@hostname:/path/to/remote/folder/ ./local-folder/
```

## Remote to remote

Sync between two remote servers:

```bash
rsync -avz --rsh=ssh user1@host1:/path/src/ user2@host2:/path/dest/
```

## Common options

- `-a` — Archive mode (preserves permissions, times, etc.)
- `-v` — Verbose
- `-z` — Compress during transfer
- `-r` — Recursive
- `--delete` — Delete files in destination not in source
- `--exclude=pattern` — Skip matching files
- `--dry-run` — Preview without copying

## rsync vs scp

| Feature | rsync | scp |
|---------|-------|-----|
| Incremental | ✅ (only changed parts) | ❌ (full copy) |
| Resume | ✅ (can restart) | ❌ (restarts from beginning) |
| Bandwidth | Better (compression, skips unchanged) | Basic |
| Speed | Faster for repeated syncs | Faster for one-time small files |
| Complexity | More options, steeper learning curve | Simple, straightforward |

Use **rsync** for backups and large repeated syncs. Use **scp** for quick one-off file transfers.

