---
title: Parallelizing API calls using python
author: ''
date: '2020-07-09'
slug: parallelizing-api-calls-using-python
categories: []
tags: []
Description: ''
Tags: []
Categories: []
DisableComments: no
---

This comes from a project where I had to make many GET requests on an api. 
Each request was structured the same but with different parameters. 
To speed this up I utilized the `concurrent.futures` python module to parallelize requests.

To start, I created a dataframe of all the parameters needed for each request and put them into a list as 
the method I used within `concurrent.futures` requires a list(more on this later). Also created helper functions 
to form the api URL and make the request. To make the GET requests, 
I utilized the [Requests](https://requests.readthedocs.io/en/master/) module.

```python
import pandas as pd
import requests
import concurrent.futures


df = pd.DataFrame({
    'param_1': ['x', 'y', 'z'],
    'param_2': ['123', '456', '789']
})

rows = df.to_dict('records')
# rows = [
#   {'param_1': 'x', 'param_2': '123'}, 
#   {'param_1': 'y', 'param_2': '456'}, 
#   {'param_1': 'z', 'param_2': '789'}
#   ]


def form_url(row):
    p_1, p_2 = row['param_1'], row['param_2']
    url = f'fancy_api.com/?param1={p_1}&param_2={p_2}'
    return url

        
def get_request(url):
    r = requests.get(url)
    return r.json()

      
def main():
    final = []
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for result in executor.map(get_request, rows):
            final.append(result)
    print(final)


if __name__ == '__main__':
    main()
```

The `concurrent.futures` module works very similar to a for loop but rather than iterating one at a time this module allows the ability to parallelize functions.

```python
# for loop
for row in rows:
    print(form_url(row))

# fancy_api.com/?param1=x&param_2=123
# fancy_api.com/?param1=y&param_2=456
# fancy_api.com/?param1=z&param_2=789
    
# in parallel
map(form_url, rows)
```

This is just an example of how to parallelize things and not one that can be directly ran in python as is, see below for one! Note also that the `requests` module supports supplying the parameters via a `request.get(url, params=p)` argument so this could be modified to supply the params that way, however, for my particular use case I went with this route due to some internal restrictions.


### A runnable example:

This will print `[1,25,16,4]`, ie, the square of each element in `[1,5,4,2]`

```python
import concurrent.futures


def f(a):
    return a**2


def main():
    final = []
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for result in executor.map(f, [1,5,4,2]):
            final.append(result)
    print(final)


if __name__ == '__main__':
    main()
```

