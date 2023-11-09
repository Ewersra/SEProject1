Project 4 Information

#
Project 4 installation information <br>
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
Create an Open AI account

```
Go to openai.com, click login, and then sign up
```

##
Create an Open AI API Key

```
Log in to your open AI account, click on your profile icon to open a dropdown menu, select API Keys, select "+ Create new secret key", copy the key and save it somewhere for safe keeping, use it in your code
```

##
Run the program on the command line

```
python run.py https://old.reddit.com/r/mildlyinteresting/comments/16lr7xk/they_have_baguette_vending_machines_in_france/
``` 

The final ouput of the program will be in a file called sentiments


##
If main project does not work, we provided just the open AI module on it's own to show we can get the sentiments of the comments from Open AI. It's in it's own folder called "OpenAI_stuff"

```
python project4.py 
``` 
