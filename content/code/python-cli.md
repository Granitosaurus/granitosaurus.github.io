Title: Tutorial: Design, produce and publish a cli app on linux using python
Date: 2017-10-07
Tags: python, linux, guide, cli
Slug: python-cli
Summary: A lengthy guide that on how to design, make and publish a command line interface appliction for *nix.
Status: Draft

#Intro

In this guide we'll design, create and finally publish a command line
interface application for linux!
We'll replicate a tiny app I made recently that converts one amount of currency to another.
In other words it does this:

    $ curr 100usd eur
    85.42

you can find the app and it's source code here:
https://github.com/Granitosaurus/curr


#Design

Before we head on to code we should have a quick run-through of how
should we do this, what resources we should use and what we want from our application.

In this guide our goal is:
__An application that converts one currency value to another__

##Understanding Command Line Interface (CLI)
First we should understand how cli application functions. Here's how standard
cli application might look like this:

    person run start finish --speed 100 -v

Breaking down the components:

* `person` - name of program; this is how you call the program
* `run` - command of a program; usually programs have multiple commands that perform different functions.
In this case our `person` program could have multiple commands like `run`, `walk`, `dance`
* `start` and `finish` - are arguments of a command `run`;
every command has their own arguments and they can be either mandatory or optional
* `--speed` and `-v` - are called options, they are always optional, belong to commands and come in two forms:
short (like our `-v`) and long (like our `--speed`). The difference is pretty self explanatory:
short options are easier to type but long ones are more explicit and self documenting.

##CLI in python

Python modules (the `.py`) files can receive command arguments
very easily without much of additional code.
Python has `sys` module which contains operating system functions.
In this case we can use it to get program arguments:

    # foo.py
    import sys
    print(sys.argv)

If we run it, we can see that sys.argv gets populated with our input:

    $ python foo.py one two --three
    ['foo.py', 'one', 'two', '--three']

However we still need to parse this to find out which of these are
commands, options or arguments; as well as add appropriate errors and help texts.
Fortunately for us there are already plenty of packages that manage that for you.
We'll be using one of the most popular ones called [click](https://github.com/pallets/click)

`click` allows you to put decorators on your functions that parse the command arguments and pass them to your function:

    # pi.py
    import click
    @click.command()
    @click.argument('number', type=click.INT)
    def myapp(number):
        """This app multiples number by 3.14"""
        print(number * 3.14)
    if __name__ == '__main__':
        myapp()

If we run it:

    $ python pi.py --help
    Usage: pi.py [OPTIONS] NUMBER

      This app multiples number by 3.14

    Options:
      --help  Show this message and exit.
    $ python pi.py 11
    34.54

You can get `click` from `pypi` by `pip install click` command.

## Finding a Data Source

Our goal is to get _up to date_ currency conversions.
So we need to find some internet resource that can provide this data we need.

If you google "currency data json" (json is a file format that is very similar to python dictionaries) you'll get quite a bit of results.
We'll use http://fixer.io/ in this example since it doesn't require any authentication and is very straight-forward.

## Choosing Config Format

Just like every great program ours should have a config file!
There are lot of different config file types. There are `.ini`,`json`,`xml` or even `.py` files can be used!
Since we're developing app for *nix systems we should stick to something that is similar to good ol' `rc` files.

[TOML](https://en.wikipedia.org/wiki/TOML) is a popular and easy configuration format and we'll stick to it.
For that we'll use `toml` package from `pypi`, you can install it via `pip install toml` command



#Production

This is the part where we write actual code!
We're already familiar with tools that we'll use: `python3.6` with `click` for interface and `toml` for configuration.

## Interface

First lets design the interface:
We want a user to be able to provide three arguments to our application - `amount`, `currency` and `result_currency`.
Since amount and currency go together we can have them as one argument `amount_and_currency` and later separate it in our program.

We end up with this pattern:  `program amount_and_currency result_currency`
In python and click this would look like:

    # curr.py
    import click
    import re
    @click.command()
    @click.argument('amount_and_currency')
    @click.argument('result_currency')
    def cli(amount_and_currency, result_currency):
        # separate amount and currency
        amount, currency = re.split('(\d+\.*\d*)', amount_and_currency)[1:]
        print(f'amount: {amount}\ncurrency: {currency}\nresult_currency: {result_currency}')
    if __name__ == '__main__':
        cli()

We can already test it:

    $ python curr.py 100USD EUR
    amount: 100
    currency: USD
    result_currency: EUR

Believe it or not that's almost all of the interface code we need!

## Brains!

The brains of our program have to do three things:

1. Download currency data and store it as a file somewhere.
2. Handle user configuration.
3. Make sure currency data stays up to date.

Since all of these things are closely related we'll consider them as one and create a class called `Manager`

    class Manager:
        def load_config():
            """return config dictionary and initiate default directories and files if they don't exist"""

        def get_currency_data(currency):
            """return up-to-date currency data from hard drive"""

### Handling Config

There are standard locations where your app configs and data should reside.
For linux based OS that is defined in [XDG base directory specification](https://specifications.freedesktop.org/basedir-spec/basedir-spec-0.6.html)
For config files that directory is either user set directory in
`$XDG_CONFIG_HOME` environment variable or it defaults to `/home/user/.config/`.

In other words to get config directory we have to use:

    Path(os.path.expanduser(os.environ.get('XDG_CONFIG_HOME') or '~/.config')) / 'curr'

### Serving Data

We want to cache data to reduce amount of requests we need.
Why download the same file every time we want to use the app?
This is where config directory comes in -
we can store data of every currency there! Once user makes conversion
we check the local data, see how dated it is and depending on
that we either update the data or not before we make our calculations.

### Action

We can put this whole logic into one class:



    # 1
    CONFIG = Path(os.path.expanduser(os.environ.get('XDG_CONFIG_HOME') or '~/.config')) / 'curr'

    class ConfigManager:
        # 2
        default_conf = {
            'update_days': 5,
            'output_format': '{result:.2f}',
        }

        def __init__(self, basedir=CONFIG):
            # 3
            self.dir = basedir
            self.rc = self.dir / 'currrc'
            self.conf = self.load_config()

        def load_config(self):
            """return config dictionary and initiate default directories and files if they don't exist"""
            # 4
            conf = self.default_conf
            if not os.path.exists(self.dir):
                os.makedirs(self.dir)
            if os.path.exists(self.rc):
                conf.update(toml.loads(open(self.rc).read()))
            else:
                with open(self.rc, 'w') as f:
                    toml.dump(conf, f)
            return conf

        def get_currency_data(self, currency):
            """update currency data files if outdated"""
            # 5
            currency = currency.upper()
            filename = self.dir / f'{currency}.json'
            if os.path.exists(filename):
                data = json.loads(open(filename).read())
                if (datetime.now() - datetime.strptime(data['date'], '%Y-%m-%d')).days < self.conf['update_days']:
                    return data
            # 6
            try:
                source = request.urlopen(f'http://api.fixer.io/latest?base={currency.upper()}').read()
            except HTTPError as err:
                if err.code == 422:
                    exit(f'ERROR: unknown currency {currency}')
            except (ConnectionError, URLError):  # todo figure out which errors are no internet errors
                if os.path.exists(filename):
                    log.warning(f'No internet connection: outdated currency for {currency}: {data["date"]}')
                    return data
                else:
                    exit(f"Error: No internet connect and cached data doesn't exist")
            else:
                data = json.loads(source)
                log.info(f'updated {currency} @ {data["date"]}')
                with open(self.dir / f'{currency}.json', 'wb') as f:
                    f.write(source)
                return data

        def __getitem__(self, item):
            #7
            return self.conf[item]

This might look like a lot but bear with me - it's surprisingly simple.
Let's dig through 7 comments and see what each bit of code does here:

1. Establishing default config location - one that will be used if not specified by the user.
2. We set up default configuration with default values for user configuration.
We start with `update_days` set to 5, to update every 5 days unless user changes this in the `rc` file.
We also specify `output_format` for how to output the message - this is great idea if our program will be used by some other program to perform some automation.
3. We want the manager to be modular in case the user wants to have
multiple configs - this is a bit of a stretch but nevertheless is a
good practice since it allows much more flexibility and multiple
use-cases for a single application.
4. `load_config` method reads existing rc config file or create
if it doesn't exist.
5. `get_currency_data` returns currency data and updates it before hand
if necessary to make sure that used that is up to date.
6. When updating data we want to handle couple of different failure scenarios:
What if user provides unsupported currency? We want to quit the program with an error message - nothing else we can do.
What if user has no internet connect? Then we want to serve local currency info and warn the user if it's outdated.
7. Magic methods are fun. In this particular case magic method
`__getitem__` allows you to have a nice shortcut of accessing config details straight through our `Manager` object:

        print(Manager()['update_days'])
        5

## Wrap It Up

Finally we wrap the brains with interface:

    @click.command()
    #1
    @click.argument('from_what')
    @click.argument('to_what')
    #2
    @click.option('--basedir', help='directory where configuration and cached data is stored, default:')
    @click.option('-v', '--verbose', help='show info messages', is_flag=True)
    def cli(from_what, to_what, verbose, basedir):
        """
        #3
        Simple currency converter.
        e.g. "curr 100usd eur" -> 85.164
        """
        #4
        if not verbose:
            log.setLevel(logging.ERROR)
        #5
        from_num, from_cur = re.split('(\d+)', from_what)[1:]
        from_cur = from_cur.strip().upper()
        #6
        conf = ConfigManager(basedir=basedir or CONFIG)
        data = conf.get_currency_data(from_cur)
        #7
        output_format = conf['output_format']
        click.echo(output_format.format(result=data['rates'][to_what.upper()] * int(from_num)))
        log.info(f'{from_cur} last updated: {data["date"]}')
    #8
    if __name__ == '__main__':
        cli()

Again lets dig through the comments to clarify what's going on here:

1. Define two mandatory arguments for our app: `from_what`
 which contains some numbers and currency while `to_what` only contains currency.
2. Define some optional flags: `--basedir` to allow user to provide their own config directory
and `--verbose` in case user wants to see logging info for debugging.
3. Define docstring - which will also be caught by click and used as `--help` text.
4. If user doesn't specify `--verbose` flag - we want to mute logging by default - people shouldn't be spammed with non-critical information.
5. Convert user supplied arguments to computer parsable data.
6. Load up configure file and retrieve currency information.
7. Do the math and print results!
8. Make it so if the `.py` is being ran directly it starts with our cli function.

Combining both parts we now have an a full working application.
See this github file for easy access:

And try running it:

    $ python curr.py --help
    Usage: curr [OPTIONS] FROM_WHAT TO_WHAT

      Simple currency converter. e.g. "curr 100usd eur" -> 85.164

    Options:
      -v, --verbose  show info messages
      --help         Show this message and exit.
    $ curr 100usd eur
    85.42


# Packaging

In this case there are two ways we can deliver our program to the userbase:

## As a script

Since our program is contained in a single `.py` file... #todo

* First we add this [shebang](https://en.wikipedia.org/wiki/Shebang_(Unix))
    to our file so the user's system would know explicitly what to use to run our program

        #!/usr/bin/env python3

* Now we can get rid of `.py` extensions since we already have an indicator inside of the file.

        mv curr.py curr

* Finally we can add our program to our system's `PATH`:

        $ chmod +x curr
        $ echo $PATH
        /usr/lib/jvm/default/bin:/usr/local/sbin:/usr/local/bin:/usr/bin:/usr/bin/site_perl:/usr/bin/vendor_perl:/usr/bin/core_perl:/home/youruser/bin:/home/youruser/.local/bin:/home/youruser/bin
        $ cp curr ~/.local/bin  # one of the locations from the above
        $ curr --help
        Usage: curr [OPTIONS] FROM_WHAT TO_WHAT

This is great for small programs that you __don't intend to publish__. As you can see this
approach expects the user to get his hands dirty and handle dependencies
and installation manually.

## As a package

The proper way to share programs is to turn them into packages, so various package managers
can install them without any input required by user.
Python has it's own packaging manager called `pip`, it's allows complex setup scenarios
that require minimal user interaction.

For that we need to add few more files to our project directory

    $ tree
    .
    ├── curr.py
    ├── readme.md
    ├── requirements.txt
    └── setup.py














