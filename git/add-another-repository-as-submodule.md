# Add or link another git repository as a submodule

Many a times you want to use code or resources from multiple repositories, but may be you dont want to link to another folder. You want to keep the projects separately but you want to use them together. You want the code or a library from another repo in the your orignal repo. 

Well, worry no more. Now you can use `git submodule`

### What is Submodule
From git-scm website:
> Submodules allow you to keep a Git repository as a subdirectory of another Git repository. This lets you clone another repository into your project and keep your commits separate.

### How to use Submodule
You can open the git terminal in the repository where you would like to link another repository. Then run the following command to add a submodule.
```
git submodule add https://github.com/username/RepositoryName
```

### How to update a Submodule
If you want to check for new work in a submodule, you can go into the directory and run ~~`git fetch` and `git merge`~~ `git submodule foreach git pull origin master` the upstream branch to update the local code.

That's pretty much it! 

For more details, go here: [https://git-scm.com/book/en/v2/Git-Tools-Submodules](https://git-scm.com/book/en/v2/Git-Tools-Submodules)
