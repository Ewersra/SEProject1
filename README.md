#
Project 1 installation information <br>
The given url for this is provided, and goes to r/mildlyinteresting post: "They have baguette vending machines in France."

##
Clone the Repo

```
git clone https://github.com/Ewersra/SEProject1
```

##
Install the Conda Environment, activate it

```
conda env update -name project1_env --file requirements.yaml
conda activate project1_env
```

##
Run the first program on the command line

```
python Project1.py https://old.reddit.com/r/mildlyinteresting/comments/16lr7xk/they_have_baguette_vending_machines_in_france/
``` 

The program will output the scraped page to output.txt

##
Run the second program on the command line

```
python Project2.py output.txt
```

if Reddit blocked program one from scraping the page, an html file of the page is provided to use for project two, if it is needed, execute this instead:
```
python Project2.py html.txt
```

the output from program two will be comments.txt
