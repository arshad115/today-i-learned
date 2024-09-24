# Fixing Detached HEAD in a Git Submodule

When working with Git submodules, you might encounter a situation where the submodule is in a detached HEAD state. This can be problematic if you need to make changes and commit them. Here’s how you can fix it:

## Steps to Fix Detached HEAD

1. **Navigate to the Submodule Directory**
    ```sh
    cd path/to/your/submodule
    ```

2. **Check the Current Status**
    ```sh
    # if the master branch already exists locally:
    git branch -u <origin>/<branch> <branch>
    # else:
    git checkout -b <branch> --track <origin>/<branch>
    ```

## source
[I am a helpful link](https://stackoverflow.com/questions/18770545/why-is-my-git-submodule-head-detached-from-master)
