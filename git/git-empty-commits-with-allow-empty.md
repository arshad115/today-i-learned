# Git empty commits with --allow-empty

Use this when you want a commit even if there are no staged file changes:

```bash
git commit --allow-empty -m "Your commit message"
```

## How it works

- `--allow-empty`: tells Git to create a commit even when there are no staged changes.
- Normally, Git prevents commits with no changes.
- This flag bypasses that restriction.

## When empty commits are useful

1. Trigger CI/CD pipelines: force a rebuild without code changes.
2. Refresh PR/webhooks: force GitHub sync or webhook processing.
3. Mark milestones: add a clear history marker (for example, `Release v1.0.0`).
4. Trigger deployment: some CI systems trigger deployments on every commit.
5. Test CI configuration: verify pipeline behavior without touching source files.

## Example

```bash
# Create an empty commit
git commit --allow-empty -m "Trigger CI rebuild"

# Push it
git push origin your-branch
```

