# Test

## INTRODUCTION
This API contains endpoints populate user data, as well as endpoint which tell you if a number is spam, or allow you to find a person’s name by searching for their phone number 


# How to run the application
To load in all python dependencies, go to the project directory name "test"
* pip install -r requirements.txt (Python 2), 
* pip3 install -r requirements.txt (Python 3)


### migrate the database, run the following command in the command prompt
py manage.py makemigrations
py manage.py migrate

### start Django server
py manage.py runserver
* use the link below for direct access to the endpoints
* http://127.0.0.1/api/endpoint/

### endpoint to follow in working around the application
* sign-up
* login
* contact
* spam
* search-number
* search-name