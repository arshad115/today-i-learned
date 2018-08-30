# Disable closing the dialog on clicking outside the dialog window in Angular

When you are opening your dialog, open it with this paramter:
```ts
this.dialog.open(AppDialogComponent, {
      disableClose: true
    });
```

It will disable closing the dialog, on clicks outside the dialog. 
