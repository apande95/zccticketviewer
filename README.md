# Zendesk Ticket Viewer
![GitHub](https://img.shields.io/github/license/apande95/zccticketviewer)
![Github](https://img.shields.io/badge/language-python-red.svg)
[![Pytest Testcases](https://github.com/apande95/zccticketviewer/actions/workflows/test_main.yml/badge.svg)](https://github.com/apande95/zccticketviewer/actions/workflows/test_main.yml)
[![codecov](https://codecov.io/gh/apande95/zccticketviewer/branch/main/graph/badge.svg?token=UQGMVTL8L6)](https://codecov.io/gh/apande95/zccticketviewer)\
This application was created for Zendesk Intern Coding Challenge. The application fulfills the following tasks:

- Connect to the Zendesk API
- Request all the tickets for your account
- Display them in a list
- Display individual ticket details
- Page through tickets when more than 25 are returned

:rocket: Installation
---
1. Clone the Github repository to a desired location on your computer. You will need [git](https://git-scm.com/) to be preinstalled on your machine. Once the repository is cloned, you will then ```cd``` into the local repository.
```
git clone https://github.com/apande95/zccticketviewer
cd zccticketviewer
```
2. This project uses Python 3, so make sure that [Python](https://www.python.org/downloads/) and [Pip](https://pip.pypa.io/en/stable/installation/) are preinstalled. All requirements of the project are listed in the ```requirements.txt``` file. Use pip to install all of those. For further isolation please use a virtual environment [ Python3 -m venv . ] and then source the activate file in bin.
```
pip3 install -r requirements.txt
```

3. Create a config.env file in src and save the url and token(API token) of your application inside like below. URL can be changed to your own domain.

```
TOKEN=<API TOKEN>
URL=https://zccapande.zendesk.com
```

4. Once all the requirements are installed, you will have to ```cd``` into the ```src``` folder. Once in the ```src``` folder, use the shell sh command to run the ```setup.sh``` file.
```
cd src

For Mac/ Unix based
sh ./setup.sh

```

:rocket: Demo
---

https://github.com/apande95/zccticketviewer/blob/main/zccTicketViewerDemo.mp4

:rocket: Code Coverage and testing 
---

- Pytest used for testing, workflow is setup which runs all the test cases on git push.
- CodeCov is used for code coverage. Its only ~50 for now but will be imporved if time permits.
- Please see https://github.com/apande95/zccticketviewer/blob/main/src/test_ticketviewer.py file for test cases. 

