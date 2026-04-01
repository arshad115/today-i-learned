# File transfers using scp with remote locations

`scp` (Secure Copy Protocol) transfers files over SSH. Syntax: `scp [options] source destination`

## Local to remote

Copy a file to a remote server:

```bash
scp ./local-file.txt user@hostname:/path/to/remote/
```

Copy a folder recursively:

```bash
scp -r ./local-folder user@hostname:/path/to/remote/
```

## Remote to local

Download a file from remote:

```bash
scp user@hostname:/path/to/remote/file.txt ./local-folder/
```

Download a folder recursively:

```bash
scp -r user@hostname:/path/to/remote/folder ./local-folder/
```

## Remote to remote

Copy between two remote servers:

```bash
scp user1@host1:/path/file.txt user2@host2:/path/destination/
```

With custom SSH key:

```bash
scp -i ~/path/to/key.pem user@hostname:/path/to/file.txt ./local/
```

## Common options

- `-r` — Recursive (folders)
- `-P port` — Custom SSH port (note: capital P)
- `-i keyfile` — Specific private key
- `-p` — Preserve file permissions and times
- `-v` — Verbose output

## Note

If hostname uses a custom SSH port, specify it with `-P`:

```bash
scp -P 2222 user@hostname:/path/file.txt ./local/
```

