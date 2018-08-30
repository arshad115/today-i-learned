# Close Dialog from typescript

Use this code:

```ts
  //constructor
  constructor(public dialogRef: MatDialogRef<any>) {
  }
  //method to close
  close() {
    this.dialogRef.close();
  }
```
