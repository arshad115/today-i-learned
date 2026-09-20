---
title: Check if local git files are older than remote
---

## Problem

When a repo is copied (not cloned), the local files may be older than the latest remote commit. You need to check before deciding whether to keep local or remote changes.

## Commands

```bash
# Date of last remote commit
git log -1 --format="%ci" origin/main

# Timestamps of all files that differ from remote
git diff --name-only origin/main | while read f; do
  ts=$(stat -f "%Sm" -t "%Y-%m-%d %H:%M:%S" "$f" 2>/dev/null || echo "not found")
  echo "$ts  $f"
done | sort
```

If file timestamps are **before** the remote commit date → your local copy is older, take the remote.

## Syncing a copied repo (no commits yet)

```bash
# Fetch remote history
git fetch origin

# Move local branch pointer to remote (keep working files)
git reset origin/main

# Or discard local and fully match remote
git reset --hard origin/main

# Set upstream so VS Code shows Sync instead of Publish Branch
git branch --set-upstream-to=origin/main main
```

## Files on remote but missing locally

These show as `not found` in the stat loop — they were added in a remote commit after your copy was made.

## References

- [git reset docs](https://git-scm.com/docs/git-reset)
