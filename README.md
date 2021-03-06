# shl
[![Build Status](https://travis-ci.org/p-netm/shl.svg?branch=challenge2)](https://travis-ci.org/p-netm/shl)
[![Coverage Status](https://coveralls.io/repos/github/p-netm/shl/badge.svg?branch=challenge2)](https://coveralls.io/github/p-netm/shl?branch=challenge2)
[![Code Climate](https://codeclimate.com/github/p-netm/shl//badges/gpa.svg)](https://codeclimate.com/github/p-netm/shl/)
[![Test Coverage](https://codeclimate.com/github/p-netm/shl/badges/coverage.svg)](https://codeclimate.com/github/p-netm/shl/)
[![Issue Count](https://codeclimate.com/github/p-netm/shl//badges/issue_count.svg)](https://codeclimate.com/github/p-netm/shl/)

***
 > a shopping list web based application that allows users to create , track their shopping needs as well as share their
  shopping lists with others

***

### Description
    > The innovative -----shopping list app----- is an application that  -----allows users  
    > to record and share things they want to spend money on ----- meeting the needs of -----keeping track of their shopping lists -----.
### Requirements
    > Users create accounts
    > Users can log in
    > Users create, view, update and delete shopping lists. 
    > Users can add, update, view or delete items in a shopping list

### Interface:

###### the home page
![index](https://user-images.githubusercontent.com/28119869/30607767-cf8cc600-9d7e-11e7-9b25-844e97275227.png)

## Installation

### Dependencies
    1. Flask
    2. Flask-wtf
    3. flask-login
    4. Flask-Moment
    5. Flask-Script
  

### process:
 * Download python version 3.4.3 or above and install and make sure you have git installed too
 * open command line; install virtualEnv
     > pip install VirtualEnv
 * clone repository from git
     > git clone https://github.com/p-netm/shl.git
 * create a virtual environment; <venv-name> is a placeholder for any arbitrary name
     > VirtualEnv <venv-name>
 * install all the dependencies
     > pip install -r requirements.txt
 * Testing:
     > nosetests
     
### Configurations
#### configuration variables

    
        format on windows:
        set KEY=<value>
        on unix:
        export KEY=<value>
    
    key                 value-options
    ----                ------
    SECRET_KEY          <surprise me>
    CONFIGURATION       {'development', 'production', 'testing', 'default'='development'}
    
### Deploy

    > Python manage.py runserver
        * Restarting with stat
        * Debugger is active!
        * Debugger PIN: ###-###-###
        * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
    
## USE and FEATURES
***
##### first page and login page for unkown users
![auth/login](https://user-images.githubusercontent.com/28119869/30535854-5adfc626-9c6c-11e7-9be6-682efbc0794b.png)

##### registration page
![auth/register](https://user-images.githubusercontent.com/28119869/30535853-5ad9343c-9c6c-11e7-8d53-d3c350c932ea.png)

##### add new list
> Enables user to add a new list with a unique name each time
![add_list](https://user-images.githubusercontent.com/28119869/30997075-f9a43e18-a4cd-11e7-99bb-5edd8a63c6cd.png)
![add_list modal](https://user-images.githubusercontent.com/28119869/30997074-f6302d96-a4cd-11e7-9526-0d3eb919d5e9.png)

##### add a new item 
> A user can add an item to an active list: the add_item link is on the navigation and pops up the modal shown below
![add item modal](https://user-images.githubusercontent.com/28119869/30997192-b929c35c-a4ce-11e7-87e2-6cd4b0a0abaf.png)

##### Modification
> a User can modify each and every aspect of a shopping list or an item. such fields are however limited to all that require user input

### Viewing Public ShoppingLists
 ***
 Given that a user may know the user_name of another user. Hir can create a url that displays the second
 users shopping lists. However the first user cannot edit or delete these or any other lists that they do not own(create)
 ![2017-09-29 04_21_08-shopping-list com home](https://user-images.githubusercontent.com/28119869/30997076-fd623d2a-a4cd-11e7-9a53-094587a5692d.png)
 
### Aknowledgements
All of this would have never been possible without the support of my two LFAs Boswell and Dennis, they were instrumental in
providing very useful feedback and help. Special thanks goes to my team
    
    * Rahma 
    * Gatana
    * Leo
    * Abdul
    * and me
who always reminded and showed me what true collaboration means and feels like.