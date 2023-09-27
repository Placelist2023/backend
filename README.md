## GET STARTED

* Open terminal
* Run `$ cp local/template.env local/.env`
* Run `$ docker-compose build`.
* Run `./local/admin.sh migrate`
* Run `./local/admin.sh createsuperuser` and answer the prompts with `admin@placelist.com` / `thisisapword`
* Run `docker-compose up`
* Go to `http://localhost:1337/health-check` and check the response is 200.
* Go to `http://localhost:1337/admin` and login with the credentials you set above.
* This is a viewer for you to navigate your local database. Click on `Users` and you should see your admin user.
* To stop the app, press `ctrl + c` in the terminal.


# API CALLS TO SIGN UP AND LOGIN

Run the app using `docker-compose up`. Then (in another terminal window) run the following commands to test the api 
calls (replace the ? with actual values):

## Sign up:
* `curl -X POST -d "email=?&password=?&password2=?&first_name=?&last_name=?" http://localhost:1337/users/register`

Once you have run this, refresh the page in the admin app and you should see the new user.

## Login:
* `curl -X POST -d "email=?&password=?" http://localhost:1337/auth/token`

This will return two tokens. Copy the `access` token. 

## Get user details

Replace the ? with the `access` token above.

# `curl --header "Authorization: Bearer ?" http://localhost:1337/users/me`

This should return the full user info.
