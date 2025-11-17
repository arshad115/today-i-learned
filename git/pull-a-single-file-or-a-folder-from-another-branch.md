# Pull A single file or a folder from another branch

Sometimes you need to get a specific file or folder from another branch without switching branches or merging everything. Here are several methods to accomplish this.

## Method 1: Using `git restore` (Git 2.23+)

The modern way to restore files from another branch:

```bash
# Restore a single file from another branch
git restore --source=branch-name path/to/file.txt

# Restore a folder from another branch
git restore --source=branch-name path/to/folder/

# Restore multiple files
git restore --source=branch-name file1.txt file2.txt folder/
```

## Method 2: Using `git checkout` (Traditional method)

```bash
# Checkout a single file from another branch
git checkout branch-name -- path/to/file.txt

# Checkout a folder from another branch
git checkout branch-name -- path/to/folder/

# Checkout multiple files/folders
git checkout branch-name -- file1.txt folder/ file2.txt
```

## Method 3: Using `git show` (For single files only)

```bash
# Copy content of a file from another branch
git show branch-name:path/to/file.txt > path/to/file.txt

# View the content without saving (useful for inspection)
git show branch-name:path/to/file.txt
```

## Examples

```bash
# Get package.json from the develop branch
git restore --source=develop package.json

# Get entire src folder from feature branch
git checkout feature-branch -- src/

# Copy config file from main branch
git show main:config/database.yml > config/database.yml
```

## Important Notes

- These commands will overwrite the current version of the file/folder
- Changes are staged automatically and ready to commit
- Use `git status` to see what files were modified
- You can use commit hashes instead of branch names: `git restore --source=abc123 file.txt`
