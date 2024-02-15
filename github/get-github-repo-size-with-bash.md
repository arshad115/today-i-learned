# Get Github Repository size with BASH

If you want to know the Github repo size before cloning it or for some other reason; you can use the [Github REST API](https://docs.github.com/en/rest?apiVersion=2022-11-28) with [jq](https://jqlang.github.io/jq/) and [numfmt](https://formulae.brew.sh/formula/coreutils):

**Bash command**:
```bash
curl 'https://api.github.com/repos/git/git' | jq '.size' | numfmt --to=iec --from-unit=1024
```
- Replace `git\git` with the `user` and the `repository_name`

**Explanation**:
- We use the `curl` command to get the json data from the API
- The json data is passed to the [jq](https://jqlang.github.io/jq/) module and then we get the `size` property in which we are interested.
- Then we use the [numfmt](https://formulae.brew.sh/formula/coreutils) to convert the size from integer to a human readable size. `numfmt --to=iec` command converts the bytes in integer format to a *human readable size*. Based on the [Github REST API](https://docs.github.com/en/rest?apiVersion=2022-11-28) documentation, the `size` is returned in Kbs. Knowing this we inform the `numfmt` with `--from-unit=1024` command that we are passing the integer in Kbs and not in bytes. 


Got the numfmt command `--from-unit=1024` [here](https://jay.gooby.org/2021/01/22/calculating-rss-size-in-mb)

