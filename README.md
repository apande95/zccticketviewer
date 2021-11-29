# Zendesk Ticket Viewer
![GitHub](https://img.shields.io/github/license/apande95/zccticketviewer)\
![Github](https://img.shields.io/badge/language-python-red.svg)\
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
4. Once all the requirements are installed, you will have to ```cd``` into the ```src``` folder. Once in the ```src``` folder, use the shell sh command to run the ```setup.sh``` file.
```
cd src

For Mac/ Unix based
sh ./setup.sh

```
