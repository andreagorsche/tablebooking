![Delicious Daily](/static/images/readme/Logo.png "Restaurant Website")

# Welcome to Delicious Daily,

The restaurant website is designed to allow registered users to book tables, delete and change bookings.
On the admin side the same functionality applies. The front-end has 5 main pages:
1. Homepage: welcoming the user and telling them what the page is about
2. Menu: Showing which kind of food the restaurant visitors can enjoy
3. Register/Login: An AllAuth backed page
4. Booking Page: To book a table
5. Manage Booking: to change reservations

The admin page has the following functionalities:
add reservations, delete reservations
add tables and delete tables
 
# User Experience 
I took the user experience (especially for the front-end) into consideration and drafted the pages I wanted to create. See below.

## Agile Developement
Through out the project I followed agile development practices.

### User Stories
At the beginning of the project I created the following User Stories in my Github project as issues: 
As a user I can reserve a table so that I can eat at my favorite restaurant on my preferable date, time and capacity (number of seats).

As a user I can check if my table is available on my desired date and time.

As a user I can select the number of seats at the table.

As a user I can register for the waiting list in case my table is currently not available at the desired time, date and capacity. It might work out due to another one's cancellation.

As a registered user I can change or cancel my booking online saving me the hazzle of calling or writing emails.

As a user I can register prior to my booking in order to change or cancel my booking later.

As an admin I can check the tables booked online and get a quick overview.

As an admin I can manually change bookings (date, time, number of seats) to serve customer requests received via phone or email.

As an admin I can manually delete bookings to serve customer requests.

As an admin I can administrate the waiting list for reserved tables to balance out cancelled bookings.

### Sketching Database Models
Before writing the models I drafted them and consider the relationship of the needed tables.

#### Reservation
Foreign Key 	Table Nr		    integer
Foreign Key	    User			    user model
Many to Many	Date 			    date
Many to Many 	Time			    time
Many to Many 	Number of people    integer (max value 10)

After this first draft I took on the models and decided that having the functionality of a child seat choice, a private booth option and an option to be waitlisted, in case the table is currently book at the desired time and date, would add value. Leading to my final version of models in the models.py file.




### Debugging

For me the easiest parts included setting up the admin page and create the models. Troubles started with creating the views and wiring them up with the urls. The following issues came up and were solved by me:

The urlspatterns were missing commas
in the urls path the name attribute was missing, therefore the wiring was not complete
After adding AllAuth I had some troubles wiring up the Menu and Book a Table into the nav bar (only visible if authentificated)

The biggest issue by far was and is the wiring of the form with the database. I became aware of the issue by entering test data to the form and checking the backend for entries but not finding any. Then I started to integrate print statements into my views function to get behind the issue. I solved a minor identation problem in the settings.py file and realized that the POST request is not even started proberly, because the first print statement after the request was already completely ignored. 
I was able to solve major issues already, like missing capitalization of POST in the HTML and views file and unaligned naming of form input fields. Currently, I am trying to figure out how to address a foreign key in a database (private_booth is part of the model Table and needs to be requested by model Reservation).

# Features

# Deployment
## Initial Deployment
The deployment was done in 2 phases. The first deployment was done when I first set up the django project and connected everything to Heroku.

The steps I took were:

### 1) Set up Gitpod workspace with Django
a. Create a new repository in Github
b. Initialize a new Gitpod workspace
c. Install Django and gunicorn to the workspace
d. Install supporting libraries: dj_database_url==0.5.0 and    
   psycopg2
e. Create requirements file
f. Create Django project (deliciousdaily)
g. Create App (tablebooking)
h. Add installed App name in the installed Apps in settings.py
i. run migrations
j. runserver and add host name to the allowed hosts in settings.py

### 2) Create Heroku App and Elephant SQL database
a. Log in to Heroku and click button "New" and select "Create new app
b. Name the new App and choose the region
c. Click "Create App" button
c. Login to Elephant SQL and click button "Create new instance"
d. Name instance and choose region
e. Go to the next step "Review" and Click "Create instance"

### 3) Connect Django Project with Heroko and SQL
a. Copy the database Url von Elephant SQL and insert it as a 
    Config Var in the Heroku App and as an environmental variable in the env.py file in Gitpod
b. Define the Secret Key in env.py and also add it to the 
   Config Var in Heroku
c. Reference the env.py file, the database URL and secret key 
   in the settings.py file
d. Save all files and migrate 
e. Add Heroku Hostname to ALLOWED_HOSTS
f. create the folders static and templates in the Gitpod workspace
g. add the Procfile and add the code: web: gunicorn PROJ_NAME.wsgi
h. save all files and Add, Commit and Push

### 4) Deploy on Heroku
a. Go to the created App and click it
b. Go to deploy section
c. Scroll down and click deploy
d. Click view to check the result 


## Final Deployment
After the functionality of Delicious Daily was tested and confirmed, I re-deployed to Heroku. 
Sadly, no pics and no css seemed to have an effect.

![Deployment without whitenoise](/static/images/readme/deploymenterror_static.png "Deployment without whitenoise")

I started to address the issue by following these steps:
1) Checking Slack if anyone else ever had this problem
2) Finding the right thread and following the steps:
    a) Delete the Config Var DISABLE_COLLECTSTATIC from Heroku
    b) Install whitenoise to gitpod
    c) run the command python3 manage.py collectstatic

This resulted in a second folder with the name 'staticfiles being created in my gitpod directory. At this point I realized that not setting up Cloudinary from the start was a mistake.
Reading about Django not transfering static files to Heroku automatically made me realize how crucial it would have been for me to set up Cloudinary for static file storage upfront. - An important lesson learned for future projects.
At this point, I could only do the set-up of Cloudinary at the end of the project.

Thus, I did the following steps next:
1) Install the Cloudinary libraries
2) Update the requirements.txt file
3) Copy the URL of the cloudinary URL and insert it into the env.py file
4) Insert the cloudinary url als Config Var in Heroku
5) add the Config Var DISABLE_COLLECTSTATIC and set its value to 1 (temporary, will be removed again after cloudinary set up)
6) Add cloudinary libraries to installed apps in settings.py file
7) Tell Django to use Cloudinary to store media and static files with the following code in settings.py:
      STATIC_URL = '/static/'
      STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'
      STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'), ]
      STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
      MEDIA_URL = '/media/'
      DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
8) Link the file to the templates directory in Heroku, placing the following code under the BASE_DIR line
      TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')
9) Change the templates directory to TEMPLATES_DIR, placing the following code within the TEMPLATES array
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
10) Delete the staticfiles folder created before
11) Add, Commit and Push changes

When looking at the development version as well as the deployed version - all CSS styling and all images were gone. To fix this problem I took the following steps:
   1) checking if my Cloudinary URL was copied correctly into Heroku and env.py
   2) if my settings.py file was set up correctly (template directory, static files directory, libraries added to the isntalled apps ...)
   3) I also tried to rename the static root folder because I had read in a slack channel of the course that it worked for one other student - but the basic problem was a different one
   4) Thanks to the guidance of student tutor Joshua, I then followed the following steps:
      a) delete all folders previously created on Cloudinary
      b) Login to Heroku via the command line by running  the command 'heroku login -i' in the terminal of Gitpod
      c) Enable automatic deploy in Heroku

The static files in cloudinary started to rebuild. Leading to the next issue: My relative file paths to images and css files were not funcitonal anymore. So the final step to set-up Cloudinary at the end of the project was: updating the filepaths in the base.html file and the subpages.css. 
While the change of the images in the html template was not the problem, the change in the CSS file proved to be more tricky. Apparently Django-specific template tags like "{% static %}" won't work in CSS files. So checked Slack for possible solutions. Linking directly to the cloudinary URL was recommended by CI tutoring to a fellow student (see screenshot below). So I followed this approach as well.

![CSS Django BG](/static/images/readme/tutor_solution_cssdjangobg.png "Backgroundimage, CSS and Django")




# Credits

#### Find out that the inner-menu-card div was missing for my flip cards to work on the front page 
https://www.w3schools.com/howto/howto_css_flip_card.asp

#### Install whitenoise and collect static files to display images and use css files when deployed to Heroku
https://www.w3schools.com/django/django_static_whitenoise.php
https://www.w3schools.com/django/django_collect_static_files.php


 
