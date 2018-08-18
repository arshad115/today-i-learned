# Setting up jekyll/Github Pages environment

I assume, you have already setup the jekyll/Github pages on your local computer using git and you run the commands in the prompt. To run a jekyll site on your local computer you can follow the following steps:

1. Install Ruby. 
    First thing we need is Ruby. If you are using Windows then you can get the [Ruby installer](https://rubyinstaller.org/downloads/). Download the dev kit version and nsttall it with toolchain.
2. Install [Bundler](https://bundler.io/) gem.
    In Ruby the packages are called gems, so we need to install the bundler gem. You only need to do it once. After Ruby is installed you can open command prompt and run the following command:
    ```
    gem install bundler
    ```
3. Install dependencies.
    To install the dependencies, run the following command. It is similar to `npm install`.
    ```
    bundle install
    ```
4. Run dev environment
    Now you are all set to run the app.
    ```
    bundle exec jekyll serve
    ```

---

To build the app:

    ```
    bundle exec jekyll build
    ```