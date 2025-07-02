# Avium Labs Python Application Template

This git repository is designed to be a "getting started" template.

The rest of this document provides the details for using this template 
to begin development of a Python application or library.


## Design 

The src/app directory is bind mounted into the Docker container and the 
container provides the Python runtime environment.   

The project provides two different starting points for Python development:
* app.py - when developing a Python application such as a web application
* server.py - when developing a Python library 

There are two supporting scripts that provide `aliases` for running python 
commands in the docker container:  
* .appdev - supports macOS and Linux  
* .appdev.ps1 - supports Windows

The three aliases are:  
* pip  
* python  
* pytest  

If you need to run `pip`, `python`, or `pytest` in the container, source one 
of the script files prior to running the command. I.e.,  

```shell
. ./.appdev
```

```PowerShell
. .\.appdev.ps1
```


The included `requirements.txt` file includes the following python packages 
and their dependencies:

* google-cloud-bigquery
* google-cloud-storage
* fuzzywuzzy
* pandas
* pytest

This file may be deleted and recreated with project specific requirements.  

There are two methods for adding additional packages.

1. Directly editing requirements.txt.
2. Running pip install.

**To install Python packages with pip:**
* Modify `compose.yaml` to run server.py
* Source the included .appdev file in a shell session
* Run pip install <package>
* Run pip freeze to export application requirements
* Run docker compose build to rebuild the image
* Modify `compose.yaml` to run app.py
* Continue with coding

```shell
. ./.appdev
```
```shell
pip install <package>
```
```shell
pip freeze > requirements.txt
```

The appdev PowerShell script has not been tested. Please file an 
issue if it does not work.

```PowerShell
. .\.appdev.ps1
```
```PowerShell
pip install <package>
```
```PowerShell
pip freeze > requirements.txt
```

## Development Environment

To continue developing after initializing a new project, use the 
`docker compose` command. 

**Important**

Modify the compose.yaml file and set the image name and version 
`aviumlabs/app:0.1.0` to the name and version of the application your are 
developing. 

Modify the pyproject.toml file to meet your requirements. 

**Recommendation is to not use spaces or special characters in the name and keep it short.**

1. Build the Docker image
```shell
docker compose build
```

Note: After adding new dependencies, rebuild the image.

2. Run the Docker container in the foreground
```shell
docker compose up
```

or Run the container in the background

```shell
docker compose up -d
```

To view the container logs (when running in the background)

```shell
docker compose logs -f app
```

### Saving Data

There are multiple ways to save data during the execution of your application;  
including Google Cloud Storage, Docker volumes, databases, etc. This is left 
to the developer to decide.  


### Google Service Account Access Key

To access google cloud services; obtain a service account access key.  

Copy the json credential to `.secret-app.json` in the root of the project 
directory. 

Uncomment the following lines in the `compose.yaml` file:

```
#secrets:
    #  - appsecret 

#secrets:
#  appsecret:
#    file: ./.secret-app.json
```

By default this file is not tracked in git. __DO NOT__ add this file to git.

The included `.env` file automtically sets the `GOOGLE_APPLICATION_CREDENTIALS` 
environment variable making the credential available to your application code.

This file also sets the PROJECT_ID environment variable to a default value of 
`aviumlabs` - change this to your **project_id**.


### Coding

All of the code for the application is in the `src/app` directory and it is 
stored on your computer's local filesystem and not in the docker container.

Use your favorite editor to write your application code.


### Build a Package

The environment has built in support for building a package. The `dist` 
directory is bind mounted into the container, and running `build` will 
create a python package in the `dist` directory on your local filesystem. 

```shell
. ./.appdev
```
```shell
python -m build
```

### Pytest Integrated

The environment has integrated support for `pytest`. Create your **test** 
files in the test directory and run pytest in the docker container.

```shell
. ./.appdev
```
```shell
pytest 
```

To print output:  
```shell
pytest -s
```

To run specific test file with output:  
```shell
pytest -s ../tests/test_<file_name>.py
```