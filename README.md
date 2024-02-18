# land-cover-challenge

Example code for the UoE land cover time series challenge with Space Intelligence.


## Study area - Bolivia

<img width="200" alt="bolivia-screenshot" src="https://github.com/KBodolai/land-cover-challenge/assets/69843715/32bfeb63-9e2a-4540-9e31-a275177112da">

We propose you look at [Bolivia](https://www.fao.org/forestry/country/57478/en/bol/), a beautiful country with a diverse range of ecosystems. It's forests are mostly tropical deciduous, so the signal measured by the sensors will vary seasonally in time. Some areas have also experienced heavy deforestation, with Global Forest Watch estimating a [primary forest loss of over 9% in the past 20 years](https://www.globalforestwatch.org/dashboards/country/BOL).

There's a lot of questions you can potentially answer after mapping land cover, a few of these to get you started are:

1. Where is deforestation happening? 
2. What is the trend in the past years, has it been reduced or is it speeding up?
3. What are the main drivers of deforestation?
4. How could you use the historical data to inform policy?

## Set up

### Notebooks

The `example_notebooks` folder has most of what you need to get started. It will show basic information about the data we are going to give you and how to access it and work with it in the microsoft planetary computer. We suggest you run them in numerical order. To access them you only need to open a terminal in the planetary computer (or your local machine) and run.

`git clone https://github.com/KBodolai/land-cover-challenge.git`

You should see a folder named land-cover-challenge appear on the home folder of your planetary computer jupyter server.

### Git in the planetary computer

We recommend that you use github in your team to version control and share things with each other. You can fork the [land-cover-challenge](https://github.com/KBodolai/land-cover-challenge) repo and work with a public or a private repo.

If you work with a private repo, you will need some way of authentication to clone and push your changes to github, you can do this with ssh:

1. Run `ssh-keygen` in a terminal your planetary computer instance and follow the steps (all defaults is good)
2. Copy the public part of the key (you can get it in the terminal if you run `cat ~/.ssh/id_rsa.pub` if you used default values)
3. Modify the permissions of the private file by running `chmod 400 ~/.ssh/id_rsa`. You will need to do this every time you start your server again. 
4. In your github account in the browser, go to settings -> SSH and GPG keys -> New ssh key, add a title and paste the key.

You should now be able to clone things from public or private repos authenticating via ssh by doing:

```
git clone git@github.com:<ACCOUNT-WHERE-REPO-LIVES>/<REPO-NAME>.git
```

We also recommend some care around working together with notebooks. Notebooks are notoriously difficult to version control, so if you're going to run somebody else's notebooks, it might be best to follow some kind of convention, like NUMBER-INITIALS-NAME (e.g. 01-kb-EDA.ipynb), to avoid creating big diffs and merge conflicts.

### Accessing the lc-challenge blob storage

You will need a SAS token to access some of the data (hosted in Azure blob). The notebooks will walk you through how to download, but before this you need to install `python-dotenv` (`pip install python-dotenv`, you will need to do this every time you restart your server) and create a file in the root of the `land-cover-challenge` folder called `.env`. In this file you can put the token as:

```
SAS_TOKEN='<paste token>'
```

And you will be able to read it in python with:
```python
import os
from dotenv import load_dotenv

load_dotenv()

token = os.environ['SAS_TOKEN']
```

`.env` is ignored in `.gitignore` so you don't accidentally push the private token out in the open.



