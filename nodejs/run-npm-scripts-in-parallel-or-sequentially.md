# Running NPM Scripts in Parallel or Sequentially

When working with Node.js projects, you might need to run multiple NPM scripts either in parallel or sequentially. Here’s how you can achieve both.

## Running Scripts Sequentially

To run scripts one after another, you can use the `&&` operator. For example:

```json
{
    "scripts": {
        "script1": "echo 'Running script 1'",
        "script2": "echo 'Running script 2'",
        "start": "npm run script1 && npm run script2"
    }
}
```

In this example, `script2` will only run after `script1` has completed successfully.

## Running Scripts in Parallel
To run scripts simultaneously, you can use the `&` operator. For example:

```json
{
    "scripts": {
        "script1": "echo 'Running script 1'",
        "script2": "echo 'Running script 2'",
        "start": "npm run script1 & npm run script2"
    }
}
```

In this example, `script1` and `script2` will run at the same time.

## Conclusion

Using these methods, you can easily manage the execution order of your NPM scripts to fit your project's needs.
