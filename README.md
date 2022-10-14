# shortner
URL Shortner in Python


## Please follow steps below in order

First, we will initialize the current directory. This action will create required directories in the local folder. For production system this should not be required.
> `make init`

We will build the image locally, requires internet connection as it pulls varies images like python3.8, postgres and few pip install, it might ask to enter the password
> `make build`

Once build is ready, proceed to run the server using
> `make dev`

Then visit http://localhost:8000/ to make sure that Basic Django project is up and running.

Now, run migration so that we can start using Django Admin.
> `make migrate`

Let's create a super user to log into Djagno Admin
>`make createsuperuser`


Visit http://localhost:8000/admin/ and login using newly created credentials.

