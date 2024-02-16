# land-cover-challenge

Example code for the UoE land cover time series challenge with Space Intelligence.

## Set up

The `example_notebooks` has most of what you need to get started. It will show basic information about the data we are going to give you and how to access it and work with it in the microsoft planetary computer. 

You will need a SAS token to access some of the data (hosted in Axure blob). The notebooks will walk you through how to download, but before this you need to install `python-dotenv` (`pip install python-dotenv`) and create a file in the root of the `land-cover-challenge` folder called `.env`. In this file you can put the token as:

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

## Study area - Bolivia

We propose you look at [Bolivia](https://www.fao.org/forestry/country/57478/en/bol/), a beautiful country with a diverse range of ecosystems. It's forests are mostly tropical deciduous, so the signal measured by the sensors will vary seasonally in time. Some areas have also experienced heavy deforestation.

There's a lot of questions you can potentially answer after mapping land cover, a few of these to get you started are:

1. Where is deforestation happen? 
2. What is the trend in the past years, has it been reduced or is it speeding up?
3. What are the main drivers of deforestation?
4. How can we use the data to inform policy makers and help them make better decisions?

