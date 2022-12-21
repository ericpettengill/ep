---
title: Running Python Scripts from Batch File
author: ''
date: '2020-07-11'
slug: running-python-scripts-from-batch-files
categories: []
tags: []
Description: ''
Tags: []
Categories: []
DisableComments: no
---

How to run python scritps from batch file using other python files as imports

Folder structure:

```
└── temp
    ├── Module
    │   ├── moduleA.py
    │   └── moduleB.py
    └── Schedule
        └── schedule.bat
```

### moduleA.py

```python
def add_numbers(x, y):
    return x + y
```

### moduleB.py

```python
from Module import moduleA


if __name__ == '__main__':
    print(moduleA.add_numbers(4, 10))
```

### schedule.bat

Step 1: change to the parent directory of the project you're working in: `cd "path/to/project"`.
This does a couple things, 

1. allows relative file paths to be used correctly from within the python files and 
2. allows importing custom scripts/files, eg, `moduleA`

Step 2: provide the path to the `python.exe` with the `-m` flag and specify the `Module.submodule`
to run: `"path/to/python.exe" -m Module.moduleB`. [See here](https://stackoverflow.com/a/22250157) for 
more information on using the `-m` flag.

```shell script
cd "path/to/project"
"path/to/python.exe" -m Module.moduleB
```

#### More on "path/to/python.exe" and environments

Often times you'll see a particular project will have its own environment(conda/venv/etc..) 
or want to create an environment to use for a project. This environment must be activated before 
running the python script from the batch file. I've found that on Windows, must use `call activate ENVIRONMENT`
from the batch file versus `activate ENVIRONMENT` normally used from the command line.

```shell script
cd "path/to/project"
call activate ENVIRONMENT
"path/to/python.exe" -m Module.moduleB
```
