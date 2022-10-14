# URL Shortner

## Pre-requisite
This application uses containerized setup.
Please make sure you have installed docker, docker-compose and make.

Makefile is used to fire repetitive commands in fewer words.

Type `make --version` to make sure that you have make command working.
Alternatively, entire project can be run using an virtual environment and psql database but I have not tested it, hence focus is only on docker setup.

Make sure that port 8000 is available and no other services are running. It is best to stop+remove all running containers before going ahead.

### This setup is verified under
1. Host OS is `Ubuntu 20.04.5 LTS`
2. Docker version `20.10.17, build 100c701`
3. docker-compose version `1.29.2, build 5becea4c`


## Please follow the steps in given order

First, we will initialize the current directory. This action will create required directories in the local folder. For production system this should not be required.
> `make init`

We will build the image locally, it requires internet connection as it pulls varies images like python3.8, postgres and few pip install, it might ask to enter the password
> `make build`

Once build is ready, proceed to run the server using
> `make dev`

Now, run migration so that we can start using Django Admin.
> `make migrate`

Let's create a super user to log into Djagno Admin
>`make createsuperuser`


Then visit http://localhost:8000/ to make sure that Basic Django project is up and running.

Visit http://localhost:8000/admin/ and login using newly created credentials.

Visit http://localhost:8000/api/v1/makeshort to start adding data in Database

You can see the data created on above page.

Visit http://localhost:8000/admin/urlshort/urlshort/ to see all data records till now.
Search using slug value on admin panel.


### Project Structure
- Simple Djnago project setup is used for assignment purpose.
- "omnicommon" contains all common code across the app
    - I am using [HakiBenita's blog](https://hakibenita.com/how-to-add-a-text-filter-to-django-admin) to enhance the admin panel's search bar
    - Abstract models and base classes should go in omnicommon
- requirements folder is broken into multiple files as per environment
- "omnihr" is the main django entry-point app.
    - It has settings and local_settings.
    - URLs are configured on api/v1 key.
    - INSTALLED_APPS is divided into sections to better understanding.
- urlshort is django app that has models and services.
    - Models are DB tables.
    - api.py is data layer, gets and creates DB records.
    - interface.py holds Contract for Slug Services to be bound to
    - services.py implements different techniques for generating the slug/short_key
    - views.py contains simple API endpoints

### Improvements I would like to make
- Logging is not done across the application
- Controller pattern could be used as mentioned in TODO section in views.py
- More services can be added to generate most unique slug
- cache can be implemented (LRU cache from functools)
- Auxiliary information like visited count can be stored and maintained (but adds complexity)
- Unit tests per service can be added
- Integration tests for entire data flow can be added
- Add API documentation.

### Applicaion tear down
To stop the service and remove containers
> `make clean`

> `sudo chown -R $USER postgres-data/`

> `rm -rf postgres-data/` (removes all application's data)

### Re-running the application without build
> Make sure that you did the teardown steps completely
> `make dev`

### Re-running the application with build
> `make build`
> `make dev`


## FAQ
#### How to monitor server logs?

To follow application logs for dev purposes (uses "follow", you will have to use ctrl+c to come back to shell)
> `make logs`


#### How to access the django application inside container?
> `make bash`

Alternatively run `make shellplus` or `make shell` to enter Django shell.





