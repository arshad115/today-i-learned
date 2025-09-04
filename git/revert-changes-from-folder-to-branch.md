# Revert Changes from Folder to Branch

Here are the manual commands and steps you can use in the future to revert changes in a specific folder back to the main branch version:

## Manual Commands to Revert a Folder to Main Branch

### Step 1: Check what changes exist
```bash
# Navigate to your repository
cd /path/to/your/repo

# Check current git status
git status

# See what changes were made in the specific folder compared to main
git diff origin/main...HEAD -- foldername/
```

### Step 2: Revert the folder to main branch version
```bash
# Reset the folder to match exactly what's in the main branch
git checkout origin/main -- foldername/

# Alternative: if you want to specify a different branch
git checkout origin/some-other-branch -- foldername/
```

### Step 3: Check what was changed
```bash
# See what files were modified
git status

# Review the changes that will be committed
git diff --staged
```

### Step 4: Commit the reversion
```bash
# Commit the reverted changes
git commit -m "Revert foldername/ to main branch version"
```

### Step 5: Clean up any new files (if needed)
```bash
# If there were new files added that don't exist in main, remove them
git rm path/to/new/file

# Commit the removal
git commit -m "Remove files that were added and don't exist in main"
```

### Step 6: Verify the reversion
```bash
# Confirm no differences exist between your folder and main
git diff origin/main...HEAD -- foldername/

# Should show no output if fully reverted
```

### Step 7: Push changes (optional)
```bash
# Push to your remote branch
git push origin your-branch-name
```

## Alternative Methods

### Method 1: Using git restore (Git 2.23+)
```bash
# Restore files from main branch
git restore --source=origin/main -- foldername/

# Commit the changes
git add -A
git commit -m "Revert foldername/ to main branch version"
```

### Method 2: Reset specific commits affecting the folder
```bash
# Find commits that affected the folder
git log --oneline -- foldername/

# Reset to a specific commit (interactive rebase)
git rebase -i HEAD~n  # where n is number of commits back

# Or create a revert commit for specific commits
git revert <commit-hash>
```

### Method 3: Cherry-pick from main
```bash
# If you want specific commits from main that affect the folder
git cherry-pick <commit-hash>
```


## Pro Tips

1. **Always check differences first**: Use `git diff origin/main...HEAD -- foldername/` to see what will be reverted
2. **Stage changes gradually**: You can revert individual files if needed: `git checkout origin/main -- specific/file.go`
3. **Use interactive staging**: `git add -p` to selectively stage parts of files
4. **Create a backup branch**: Before major changes, create a backup: `git checkout -b backup-branch`
5. **Verify with clean diff**: Always end with `git diff origin/main...HEAD -- foldername/` showing no output

These commands will work for any folder or file you want to revert to match another branch!