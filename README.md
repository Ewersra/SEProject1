Project 6 Information

#
Project 6 installation information <br>

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
Log in to your open AI account, click on your profile icon to open a dropdown menu, select API Keys, select "+ Create new secret key" (verify phone number first if needed),
copy the key and save it somewhere for safe keeping, add it to the code in run.py where it says "key =" (a key is included in the code already)
```

##
Run the program on the command line
(urls.txt can be found in the Data folder)

```
python run.py
```

##
run.py will run a loop, sending each link to module_1 to get the website data, to module_2 to get the page HTML, module_3 to get the comments and remove HTML tages, module_4 sends the comments to ChatGPT to get the sentiments, and module_5 creates the graphs. <br>
The data folder will contain the different outputs: raw will have the page html, processed will have the comments, sentiments will have the sentiment files, and plots will have the graphs.
