# Fortune500-Scraper

This code queries the Fortune 500 API, saving the results of the F500 list, including company rank and name to a CSV file.

## Requirements

The code is designed to run in Python, using the following libraries:

- json
- httplib2


## Code Examples

After cloning the code (`git clone https://github.com/jmausolf/Fortune500-Scraper`) and navigating to the repo `cd Fortune500-Scraper`, do the following:

```bash
#Collect the Fortune 500
$ python main.py
```


```bash
#Collect the Fortune 1000
$ python main.py -n 1000
```

> *Note:* If python3 is not your default version or python, you will need to amend the commands to include your python3 alias, e.g. `python3 main.py -n 1000`

---

## Acknowledgements

The repository was originally created courtesy of @LegendL3n. Numerous modifications have been made to make the code compatible with Python 3.5+ and to write the results to a CSV. Command line arguments have been added to allow specifying the Fortune 500 or Fortune 1000 among other possibilities. Regular expressions replace non-ascii text (notably non-ascii single/double quotes to avoid issues in code relying on the created CSV's.)

