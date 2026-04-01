# Fix REMOTE HOST IDENTIFICATION HAS CHANGED warning with ssh-keygen -R

When SSH shows this warning:

```text
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@ WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED! @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
IT IS POSSIBLE THAT SOMEONE IS DOING SOMETHING NASTY!
Someone could be eavesdropping on you right now (man-in-the-middle attack)!
It is also possible that a host key has just been changed.
```

your local `known_hosts` entry for that host no longer matches the server key.

## Quick fix

Remove the stale host key entry, then reconnect:

```bash
ssh-keygen -R github.com
```

Or for a custom host/IP:

```bash
ssh-keygen -R <hostname-or-ip>
```

After that, connect again:

```bash
ssh -T git@github.com
```

SSH will prompt you to trust and save the new host key.

## Notes

- This often happens after server rebuilds, host key rotation, or DNS/IP changes.
- Do not ignore this warning blindly for unknown hosts. Verify the fingerprint from a trusted source first.

