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
    4. Flask-Mail
    5. Flask-Migrate
    6. Flask-Moment
    7. Flask-Script

### pocess:
 * Download python version 3.4.3 or above and install and make sure you have git installed too
 * open command line; install virtualEnv
     > pip install VirtualEnv
 * clone repository from git
     > git clone https://github.com/p-netm/shl.git
 * create a virtual environment; <venv-name> is a placeholder for any arbitrary name
     > VirtualEnv <venv-name>
 * install all the dependencies
     > pip install -r requirements.txt
     
### Configurations
#### configuration variables

    ```
        format on windows:
        set KEY=<value>
        on unix:
        export KEY=<value>
    ````
    key                 value-options
    ----                ------
    SECRET_KEY          <surprise me>
    CONFIGURATION       {'development', 'production', 'testing'}
    
### Deploy

    > Python manage.py runserver
    
## USE and FEATURES
***
##### first page and login page for unkown users
![auth/login](https://user-images.githubusercontent.com/28119869/30535854-5adfc626-9c6c-11e7-9be6-682efbc0794b.png)

##### registration page
![auth/register](https://user-images.githubusercontent.com/28119869/30535853-5ad9343c-9c6c-11e7-8d53-d3c350c932ea.png)

##### add new list
> Enables user to add a new list with a unique name each time

##### add a new item 
> A user can add an item to an active list: the add_item link is on the navigation and pops up the modal shown below

##### Modification
> a User can modify each and every aspect of a shopping list and item

### Viewing Public ShoppingLists
 ***
 Given that a user may know the user_name of another user. Hir can create a url that displays the second
 users shopping lists. However the first user cannot edit or delete these or any other lists that they do not own(create)
 
### Aknowledgements
All of this would have never been possible without the support of my two LFAs Boswell and Dennis, they were instrumental in
providing very useful feedback and help. Special thanks goes to my team
    
    * Rahma 
    * Gatana
    * Leo
    * Abdul
    * and me
who always reminded and showed me what truecollaboration means and feels like.