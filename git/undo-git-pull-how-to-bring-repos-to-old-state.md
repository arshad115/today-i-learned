# Undo git pull

### With Head
```
git reset --hard 'HEAD@{1}'
```

### With time
```
git reset --hard master@{"10 minutes ago"}
```
or
```
git reset --hard master@{8:30}
```

For more details, go here: [Stackoverflow](https://stackoverflow.com/questions/1223354/undo-git-pull-how-to-bring-repos-to-old-state)