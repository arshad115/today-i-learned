# Fresh Start: Backing Up Main Branch and Creating Clean Main

## Overview
Sometimes you need to start fresh with your main branch while preserving the existing code history. This guide shows how to backup your current main branch to another branch and create a clean, empty main branch.

## Step-by-Step Process

### 1. Backup Current Main Branch

First, create a backup of your current main branch:

```bash
# Switch to main branch
git checkout main

# Create a backup branch from current main
git checkout -b main-backup

# Push the backup branch to remote
git push -u origin main-backup
```

### 2. Alternative: Create Named Backup Branch

You can also create a more descriptive backup branch name:

```bash
# Create backup with timestamp or version
git checkout -b main-backup-$(date +%Y%m%d)
# or
git checkout -b main-v1-backup

# Push to remote
git push -u origin main-backup-$(date +%Y%m%d)
```

### 3. Create Clean Main Branch

Now create a fresh, empty main branch:

```bash
# Create a new orphan branch (no history)
git checkout --orphan new-main

# Remove all files from staging
git rm -rf .

# Create initial commit with empty repository
git commit --allow-empty -m "Initial commit - fresh start"

# Delete old main branch locally
git branch -D main

# Rename new-main to main
git branch -m new-main main
```

### 4. Force Push New Main Branch

⚠️ **Warning**: This will overwrite the remote main branch. Make sure your backup is pushed first!

```bash
# Force push the new empty main branch
git push -f origin main
```

### 5. Verify Backup and Clean Main

```bash
# Check that backup branch exists
git branch -a

# Verify main is clean
git log --oneline

# Check backup branch has your old code
git checkout main-backup
git log --oneline
```

## Alternative Approach: Using git reset

If you want to keep some history but start from a specific clean commit:

```bash
# Backup current main
git checkout main
git checkout -b main-backup
git push -u origin main-backup

# Reset main to initial commit (or any clean commit)
git checkout main
git reset --hard <initial-commit-hash>

# Force push the reset main
git push -f origin main
```

## Best Practices

### Before Starting
- [ ] Ensure all important work is committed and pushed
- [ ] Notify team members about the main branch reset
- [ ] Consider creating tags for important releases before backup

### Backup Verification
- [ ] Verify backup branch contains all expected code
- [ ] Test that backup branch builds/runs correctly
- [ ] Document the backup branch location and purpose

### Communication
- [ ] Update team about the new main branch structure
- [ ] Update CI/CD pipelines if needed
- [ ] Update documentation referencing old main branch

## Recovery Process

If you need to restore from backup:

```bash
# Switch to backup branch
git checkout main-backup

# Create new main from backup
git checkout -b new-main

# Delete current main
git branch -D main

# Rename to main
git branch -m new-main main

# Force push restored main
git push -f origin main
```

## Use Cases

This approach is useful when:
- Starting a major refactor or rewrite
- Migrating to a completely different technology stack
- Cleaning up a repository with sensitive data in history
- Creating a demo repository from an existing project
- Separating different versions of a project

## Security Considerations

- **Sensitive Data**: If backing up due to sensitive data in history, ensure the backup branch is properly secured
- **Access Control**: Consider who has access to backup branches
- **Cleanup**: Remove backup branches when no longer needed

## Notes

- The original commit history is preserved in the backup branch
- Contributors will need to re-clone or reset their local repositories
- Any open pull requests targeting main will need to be updated
- Consider using `git filter-branch` or `git filter-repo` if you need to remove specific files from history before backup