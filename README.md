![Delicious Daily](/static/images/readme/logo.png "Restaurant Website")

# Welcome to Delicious Daily,

Delicious Daily is a restaurant website offering individual table bookings for their customers. Users interested in booking a table via the online form need to register for free first. Once logged in the users can book tables and manage their reservations (update information on date, time, number of guests, number of child seats, edit the comment field) and delete them if they are no longer needed.

![Delicious Daily Screens](/static/images/responsive.png "Responsive Screens")


On the admin side, restaurant managers and waitresses can manage bookings (view bookings, filter bookings, change bookings) and manage tables (add tables, change number of seats, set tables to private booths whenever they are rearranged) 

![Admin Screen](/static/images/admin_side.png "Admin Screen")

 
# User Experience

## Strategy Plane
### Core Functionality and User Groups
The core functionality is to book and manage table reservations at the restaurant Delicious Daily. The two main user groups are:
* The restaurant admins (restaurant manager and waiters/waitresses) needing to access bookings for on-sight table management
* guests wanting to reserve a table for a certain time, date and number of people

For the guests the website's main goal is to provide a clear and direct navigation through the booking process as well as the managing booking process.
Besides adding and managing reservations, the restaurant admins have the ability to manage the tables at the restaurant. E.g. their number, number of seats and wether they are in a private booth or not.


### Agile Development Method

Following agile development practices, I created the user stories for the project in the Canban tool of Github.

![Delicious Daily](/static/images/readme/agiledevelopement.png "Restaurant Website")

Thereby I followed **two-week-sprints**:

Sprint 1: Designing the project (strategy, goals, user groups, user stories, wireframes)

Sprint 2: Setting up the project (Gitpod, Heroku, SQL, Django, setting up Canban in Github)  

Sprint 3: Create Admin functionality in Django Backend (create models as well as display and filter methods)

Sprint 4: Create Login and Registration functionality

Sprint 5: Create basic user form functionality (entered data is sent to the sql database)


Due to my initial approach to set up a form without the use of a forms.py file and also neglecing the idea of Generic Views I soon realized the limitations I had put onto myself. As time for project submission was running out, I had to hand in an unfinished project, determined to change my approach for the second submission.

This time I followed shorter sprints of **1 week** per sprint:

Sprint 6: Re-write the code to work with forms.py and Generic views

Sprint 7: Create booking form with basic functionality (enter data and send it to SQL)

Sprint 8: Data Validation of booking form (date and time format, no bookings in the past)

Sprint 9: Bootstrap, CSS and images added for design

Sprint 10: No Double Booking functionality

Sprint 11: Debugging of form validation

Sprint 12: Debugging CSS and finalizing of the project


For me personally, it felt like a better approach to have small workpakages in a shorter amount of time. It felt more efficient and targeted than the previous sprints. 


## Scope Plane
As already shortly elaborated in the strategy the main functionality and features of the project should revolve around table booking management for admins and guests of a restaurant.
It was a clear criteria from the start that the guest users need to be logged in, in order to book a table or manage their bookings.
This is clearly stated on the starting page for users to know at first glance.

I detailed the scope of the project by deciding on the user stories.

### User Stories for the admin users
* As an admin I can check the tables booked online and get a quick overview.

* As an admin I can manually change bookings (date, time, number of seats) to serve customer requests received via phone or email.

* As an admin I can manually delete bookings to serve customer requests.

* As an admin I can administrate the waiting list for reserved tables to balance out cancelled bookings.

### User Stories for the guest users

* As a user I can reserve a table so that I can eat at my favorite restaurant on my preferable date, time and capacity (number of seats).

* As a user I can check if my table is available on my desired date and time.

* As a user I can select the number of seats at the table.

* As a registered user I can change or cancel my booking online saving me the hazzle of calling or writing emails.

* As a user I can register prior to my booking in order to change or cancel my booking later.

#### Future User Functionalities

* As a user I can register for the waiting list in case my table is currently not available at the desired time, date and capacity. It might work out due to another one's cancellation.

* As a user I get a list of available tables based on my booking inquiry and can pick my favorite table according to characteristics (private booth, picture of the table).

* The booking slot now is 1 hour per reservation. The user could be asked in the form how long he intends to stay approx., this could help for occations like birthday parties where longer times are usually required. The user should be given a choice of less than two hours or more than two hours and according to his answer the system blocks the alloted time.


## Structure Plane
The front-end has 6 main pages:
1. Homepage: welcoming the user and telling them what the page is about
2. Menu: Showing which kind of food the restaurant visitors can enjoy
3. Register: An AllAuth backed page
4. Login: An AllAuth backed page
5. Booking Page: To book a table
6. Manage Booking: to change reservations
7. List Bookings: to view done bookings

Plus 5 redirects to confirm actions have taken place:
1. confirmation for the booking
2. confirmation for the booking update
3. asking for confirmation before deletion
4. confirmation deletion
5. asking for confirmation before sign out


## Skeleton Plane

To get a deeper understanding of the website I intend to build, I first sketched the database models and their according fields.
In this design phase it was crucial for me to start thinking about concrete features because the features I had in mind would in turn define the database fields I would need.

### The Database Models

For the design of the database models I had both user groups in mind: the restaurant admins and the guests of the restaurant.
While the guests would work with data connected to their reservation only, the admins for sure would like to do table management as well. E.g. be able to adjust the number of tables available and the number of seats per table.

#### Basic fields
The reservation model would take in typical fields required for every reservation: date, time, a comment field. Since this form would be about restaurant reservations the number of people matters as well. And the table number would be connected as a foreign key.
The table, on the other hand, would have a number and a number of guests in its basic set up. 
But I wanted to add that little extra for both tables and considered USPs relevant in restaurant reservations.

#### Adding USP
##### The extra mile for families
Being a mother myself, I thought it would be a convenient service to add the number of child seats to the model. This way, families booking a table would
a) See that there are child seats at the restaurant and
b) Have the security that they will actually have an available child seat with their booking
The restaurant admins on the other hand can react in case they see a shorthand of child seats for a certain date and react accordingly. – A win-win and good service of the restaurant. Especially with very basic services like bookings at restaurants there is only so much you can do and offer. Adding little small services like the child seat options can turn in a nice little USP that lets families pick Delicious Daily over other restaurants not being so considered in their booking form.

##### The extra mile for couples and small parties
A second guest target group I had in mind were couples. They may prefer a more private setting for their lovey-dovey brunches or romantic dinners. Also people who intend to celebrate a birthday may prefer a more secluded spot in the restaurant. Thus, I added the models field private booth to the tables model.

##### The extra mile to smoothen disappointment
Sometimes it happens that you have the perfect breakfast, lunch or dinner plans and your mind is set on a certain restaurant. Thus, the disappointment is big, if there are no available tables left at the required date or time. This seems especially unfair, considering that people who actually booked sometimes don’t show up or need to cancel their plans last minute. With waiting list functionality I wanted to address this issue and provide the guest with the prospect of a potential table. This extra effort of the restaurant to make their guests wishes true will leave a positive feeling with guest and even if the desired date stays unavailable the guest is more likely to return for another booking because they see the effort.
This feature also provides a relevant benefit for restaurant managers. After all an empty table is equal to missing revenue. So restaurant managers will appreciate the ability to fill up cancellations with waiting reservations.

##### Future functionalities and the data models
I initially planned the waiting list as its own model with the table number and reservation number as foreign keys. But my mentor advised me to add this characteristic to the reservation model directly as a Boolean field called “is_waitlisted”. My mentor also advised me to focus on basic functionality first and write this waiting list feature down for later. Still I decided to integrate this idea in my database model right away, to avoid a re-set up to add the field later.

Like already described in the Scope Plane I came up with one additional feature idea about showing pictures of the available tables and letting the user pic the table themselves. Sadly, I didn’t come up with that idea in the initial design concept but later in the development process, thus an image field in the table model is not integrated in this version of the code. But it is planned for a future version.

### The database model design
Following my above description, I designed the following database model structure for my project Delicious Daily: 

![Database Models](/static/images/readme/database_models.png "Database Models")


### Wireframing

A big part of the skeleton design phase was the wireframing. I decided to do low-fidelty wireframes in the design tool Figma. 

For every page and every interaction with the user I design a separate page.

In order to create a full-stack application I designed a **starting page** that has a delicious food pic at its center. And a note telling the user that he or she is able to book a table after free registration. Thus, advertising the main functionality of the page at first glance.
 At the top is a header with the restaurant logo, linking back to the main page from every page, and a menu with basic functionality for checking the menu, registration and login. At the bottom is a footer with the copyright in place.

![Main Screen](/static/images/readme/Wireframes/mainscreen.png "Main Screen")


A page with breakfast, lunch and dinner menus gives the user a taste of what Delicious Daily has to offer and motivate their free registration to book a table.

![Menu](/static/images/readme/wireframes/menu.png "Menu")

The registration page for first-time users should offer a fast way to enter details and proceed to the booking features. The design of this page, as well as of the login page is intentionally minimalistic. After all data entry requires focus on the entered data. Too much design or animation around the form only distracts and confuses.

![Register](/static/images/readme/wireframes/register.png "Register")

The Login page is designed in similar pattern giving the recurring user the chance to log back in.

![Login](/static/images/readme/wireframes/login.png "Login")

Once a user is registered and logged in new menu options present themselves: book a table, view bookings and logout. 

![RegisteredUser](/static/images/readme/wireframes/registereduser.png "RegisteredUser")

The book a table page is a page of central interest to the user. Therefore the green background of the form is bigger and the background pic is more like a frame to add some visual touch without being to distracting. 
That way the user can focus on the data entry. Still the grey background of the cafe is a repeated image for recognition purposes.

![Book a Table](/static/images/readme/wireframes/bookatable.png "Book a Table")

After clicking the Book button. The user is directed to a feedback page confirming the booking was successful.

![Booking Confirmation](/static/images/readme/wireframes/bookingconfirmation.png "Booking Confirmation")

The booking list page follows the same design principle as the book a table page. A big green background highlights the information at center - the booked reservations. These are organized in a list with two possible actions "manage booking" and "delete booking". Part of the green background frame are the buttons "next" and "previous" in case the user has more than 3 bookings.

![View Bookings](/static/images/readme/wireframes/viewbookings.png "View Bookings")

When the user wants to update a table booking they press the manage booking button and are directed to the booking form to edit their reservation entry. 

![Update a Table](/static/images/readme/wireframes/updateatable.png "Update a Table")

After making the necessary changes, by clicking the button "Update Booking" they are then directed to a page confirming the update.

![Update Confirmation](/static/images/readme/wireframes/updateconfirmation.png "Login")

If a user clicks the "delete booking" button, they are directed to a subpage asking to confirm the deletion.

![Delete Question](/static/images/readme/wireframes/deletequestion.png "Delete Question")

If they confirm the deletion they are directed to user feedback page stating that the booking was deleted successfully.

![Confirmation Delete](/static/images/readme/wireframes/confirmationdelete.png "Confirmation Delete")

Once the user wants to log out they click on Logout in the top menu and are directed to a page where they have to confirm there logout.

![Logout Question](/static/images/readme/wireframes/logoutquestion.png "Logout Question")

In general, I followed a  minimalist approach for user feedback pages (like e.g. your booking has been confirmed, deletion is confirmed, booking update is confirmed) and for interaction pages (e.g. please confirm deletion, do you really want to log out).

### User Flow
Wireframing is always closely linked to the user flow. After all, if I don't know how the user navigates to the page and which touchpoints he or she has, how should I consideratley design the wireframing?
Thus, with the wireframes designed I created a typical user flow for recurring users and first time users in one graphic.

![User Flow Delicious Daily](/static/images/readme/userflow_deliciousdaily.png "User Flow")

#### First-time users

First-time users enter the page, browse the menu, register, book a table, list their booking. They eventuelly may adapt their booking or delete it. Ultimately they log out.

#### Recurring users

Recurring users enter the page, browse the menu, login in, book a table and/or list their previous bookings. They might update or delete previous bookings and eventually log back out.

## Surface Plane

Each surface design for me starts with the color scheme. After all it determines the imagery used and also the typography.

### Color Scheme
Since by definition imagery of food tends to be colorful and should be at the center of page, the color scheme I choose was subtle and down to earth. No screaming colors but colors that go well as supporting colors.

#### Main color
For the header, footer, logo as well as the background blocks of forms and lists I choose the color cadetblue to frame the rich imagery and information displayed.

![Main Color - Cadet Blue](/static/images/readme/colorscheme/cadetblue.png "Main Color - Cadet Blue")

#### Supporting color
As supporting colors I choose Alice Blue to create a nice supporting contrast to the cadetblue main color. As further supporting colors I used dark charcoal and white.

![Supporting Color - Alice Blue](/static/images/readme/colorscheme/aliceblue.png "Main Color - Alice Blue")
![Supporting Color - Dark Charcoal](/static/images/readme/colorscheme/dark_charcoal.png "Main Color - Dark Charcoal")
![Supporting Color - White](/static/images/readme/colorscheme/white.png "Main Color - White")

### Typography
For the font I decided to go with Cormorant Garamond as the main font. It is very good to read and still has some unique touch to it. The font Pacifico is more playful and used for special nuances like the quote of the Chef or the logo.

### Imagery
The imagery chosen show the delight and deliciousness of eating. It is more than just a process of eating to fill an empty stomach. It is a celebration of taste and touches all senses.

#### Key Visual
The key visual is the picture of the restaurant from outsite. It appears to be drawn but is actually an edited picture. This effect together with the colors of the visual give a softer touch compared to a pure photograph. 
The key visual is used in a black-and-white version as a background whenever the user has to enter information or is given information. This way a pattern is visible to the user that makes him or her recognize he is still on the right website and was not redirected somewhere else.
Furthermore, it undermines the role of the key visual as something recurring and recognizeable, similar to the logo.

![Key Visual](/static/images/readme/startingpage/starting_page_1.png "Key Visual")


#### Food pictures
For the menus breakfast, lunch and dinner one symbol picture each was used. Like described before with the color scheme, the food pics are supposed to look delicious and inviting to eat at the restaurant. The pics are colorful and very distinct from each other to suggest different tasts and looks depending on the time of day you eat at Delicious Daily.

![Key Visual](/static/images/readme/startingpage/starting_page_4.png "Key Visual")


#### Picture of the restaurants chef
There is nothing more welcoming than a friendly face. So the restaurant chef himself decided to appear on the main page - doing what he does best: prepare delicious food. A quote about the joy of eating is adding to the overall feeling that eating is a delicious act. 

![Key Visual](/static/images/readme/startingpage/starting_page_2.png "Key Visual")


# Features
Like already elaborated in the Skeleton Plane the main features and functionalities revolve around the basics of a restaurant table booking system plus individual USPs added to give the user an even better experience.

## CRUD
The main functionality I focused on in the initial developement process was the CRUD functionality:
* Create table bookings
* Read table bookings
* Update table bookings and
* Delete table bookings

### Create a booking
In order to create a booking the user first has to register. Once logged in the user clicks on "Book a table" in the menu to get to the booking form. The user is required to enter the date, time, number of people and number of child seats required. The commed field is optional. On clicking the Book button the data entry is checked through form validation. If the data entry was correct the user is informed that the booking was successful. Otherwise error messages inform the user about the problem with the entered data.
 
#### Form Validation
The form validation checks if:
* The date is entered in the format DD/MM/YYYY
* The time is entered in the format HH:MM
* The date is not in the past
* The time is within opening hours
* The date is not a monday
* The number of guests is bigger than 0
* The comment is no more than 300 characters

#### Double Booking
The user is informed in case there is no table available for the requested date, time and number of guests.

### Read table booking
When clicking the "view bookings" button the user can check all bookings they did so far. In case there aren't any bookings yet the user is informed through a message. If there are bookings listed the user is free to manage the booking or delete it through the provided buttons.
Many table booking forms are just basic contact forms sending the restaurant email for reservation requests. But Delicious Daily offers a database-based solution that allows users to not only book but also manage and delete their bookings easily and fast.

### Update and delete table booking 
Sometimes plans change and the user needs to update or delete their booking. If the reservation request was send via a contact form the user would be required to write an email or call. If the phone is busy or the restaurant closed at the time this easy task of updating or deleting a booking can be tedious. Not with Delicious Daily. Here each customer can manage their reservations themselves giving them maximum flexibility and ease-of-access. 
When updating the booking, the user is required to update the data he or she already entered in the form and then pressing the button update. An immediate message confirms the changes.
When deleting a booking, the user is requried to press the according button in the actions column of the table listing all reservations. The user is then asked once more if he or she is sure they want to cancel. Then in a last step the cancellation is confirmed.

## USP

### Child Seat Feature
Families don't have to worry whether their little ones will have their own child seats available at the restaurant, because they can be booked with the table - individually and easily. The information about required child seats is also passed to the restaurant admin and therefore a shortage is made visible fast and can be acted on.


# Technologies Used
To reach the functionalities described above in the features section, I worked with the MTV (Model-Template-Views) framework Django. For the models, views and form I used Python. To create my templates I used HTML. And to style it I used CSS and Bootstrap.
For file storage cloudinary was used, to store the database Elephant SQL was used. Whitenoise was installed to handle the transfer of the static files between Django, Cloudinary and Heroku.

A full list of libraries used you can find in the list below.

asgiref==3.6.0
cloudinary==1.33.0
dj-database-url==0.5.0
dj3-cloudinary-storage==0.0.6
Django==3.2.18
django-allauth==0.52.0
django-summernote==0.8.20.0
gunicorn==20.1.0
oauthlib==3.2.2
psycopg2==2.9.5
PyJWT==2.6.0
python3-openid==3.2.0
pytz==2022.7.1
requests-oauthlib==1.3.1
sqlparse==0.4.3
urllib3==1.26.15
whitenoise==6.5.0

# Debugging
For me the easiest parts included setting up the admin page and create the models. Troubles started with creating the views and wiring them up with the urls. The following issues came up and were solved by me:

The urlspatterns were missing commas
in the urls path the name attribute was missing, therefore the wiring was not complete
After adding AllAuth I had some troubles wiring up the Menu and Book a Table into the nav bar (only visible if authentificated)

The biggest issue by far was and is the wiring of the form with the database. I became aware of the issue by entering test data to the form and checking the backend for entries but not finding any. Then I started to integrate print statements into my views function to get behind the issue. I solved a minor identation problem in the settings.py file and realized that the POST request is not even started proberly, because the first print statement after the request was already completely ignored. 
I was able to solve major issues already, like missing capitalization of POST in the HTML and views file and unaligned naming of form input fields. Currently, I am trying to figure out how to address a foreign key in a database (private_booth is part of the model Table and needs to be requested by model Reservation).

# Testing
## Manual Testing
With every sprint manual tests of the intendent funcitonalities and design features were done. These tests were documented in test cases stated in the file [Testing.md](Testing.md).

### Test Cases

To test the **login and registration** functionalities, the following test cases were tested:
* The user can register
* The registered user can re-login with the same credentials
* The user can't get past the registration by entering the URL

To test the **CRUD functionalites** of the application the follwoing test cases were looked at:
* Users can create a booking
* Users can list (read) their bookings - only theirs and not that of other users. 
* Users can update their booking
* Users can delete a booking
   
To test the **form validation** functionality wrong data was entered intentionally to stress test the system:
* Users enter wrong data format and/or time format
* Users enter strings instead of time or date
* Users enter past date
* Users enter a date that is a monday (closed on mondays)
* Users enter a date outside of opening times
* Users don't enter number of guests
* Users enter more than 300 characters of text in the comments field

To test that users **can't book the same date and time twice** the following tests were performed:
* User can't double book a booking he or she has done
* User can't double book a booking another user has done
* User can't update a booking to a date and time another user already booked
* User can't update a booking to a date and time they themself have already booked

To test the functionalities of the admin side the following test cases were looked at:
* The admin can create tables
* The admin can change table characteristics (e.g. number of seats, private booth or not)
* The admin can delete tables
* the admin can filter tables by table number, number of seats, private booth (Boolean)
* The admin can create reservations
* The admin can change reservations (e.g. date, time, number of guests)
* The admin can waitlist a reservation
* The admin can delete a reservation
* The admin can filter reservations by table, date, number of guests, is_waitlisted (Boolean)

## Debugging

## Validators

For HTML and CSS the W3 Validators were used. In the first instance there were still bugs showing that are eloborated about in the section above "Debugging". After the debugging was finished no further Validation errors showed.

![HTML Validator](/static/images/readme/validators/htmlvalidation.png "HTML Validator")

The above picture is one example of this website passing the HTML validator. The validations were done for all subpages. Since the screens would all look the same, I decided to not copy them all in here.

![CSS Validator](/static/images/readme/validators/cssvalidation.png "CSS Validator")

For the Python files the Pep8 install was used to ensure the code is according to PEP 8 conventions.

To test the overall performance of the website Lighthouse was used:

![Lighthouse](/static/images/readme/validators/lighthouse.png "Lighthouse")



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


 

![Delicious Daily](/static/images/readme/logo.png "Restaurant Website")

# Welcome to Delicious Daily,

Delicious Daily is a restaurant website offering individual table bookings for their customers. Users interested in booking a table via the online form need to register for free first. Once logged in the users can book tables and manage their reservations (update information on date, time, number of guests, number of child seats, edit the comment field) and delete them if they are no longer needed.

On the admin side, restaurant managers and waitresses can manage bookings (view bookings, filter bookings, change bookings) and manage tables (add tables, change number of seats, set tables to private booths whenever they are rearranged) 
 
# User Experience

## Strategy Plane
### Core Functionality and User Groups
The core functionality is to book and manage table reservations at the restaurant Delicious Daily. The two main user groups are:
* The restaurant admins (restaurant manager and waiters/waitresses) needing to access bookings for on-sight table management
* guests wanting to reserve a table for a certain time, date and number of people

For the guests the website's main goal is to provide a clear and direct navigation through the booking process as well as the managing booking process.
Besides adding and managing reservations, the restaurant admins have the ability to manage the tables at the restaurant. E.g. their number, number of seats and wether they are in a private booth or not.


### Agile Development Method

Following agile development practices, I created the user stories for the project in the Canban tool of Github.

![Delicious Daily](/static/images/readme/AgileDevelopement.png "Restaurant Website")

Thereby I followed **two-week-sprints**:

Sprint 1: Designing the project (strategy, goals, user groups, user stories, wireframes)

Sprint 2: Setting up the project (Gitpod, Heroku, SQL, Django, setting up Canban in Github)  

Sprint 3: Create Admin functionality in Django Backend (create models as well as display and filter methods)

Sprint 4: Create Login and Registration functionality

Sprint 5: Create basic user form functionality (entered data is sent to the sql database)


Due to my initial approach to set up a form without the use of a forms.py file and also neglecing the idea of Generic Views I soon realized the limitations I had put onto myself. As time for project submission was running out, I had to hand in an unfinished project, determined to change my approach for the second submission.

This time I followed shorter sprints of **1 week** per sprint:

Sprint 6: Re-write the code to work with forms.py and Generic views

Sprint 7: Create booking form with basic functionality (enter data and send it to SQL)

Sprint 8: Data Validation of booking form (date and time format, no bookings in the past)

Sprint 9: Bootstrap, CSS and images added for design

Sprint 10: No Double Booking functionality

Sprint 11: Debugging of form validation

Sprint 12: Debugging CSS and finalizing of the project


For me personally, it felt like a better approach to have small workpakages in a shorter amount of time. It felt more efficient and targeted than the previous sprints. 


## Scope Plane
As already shortly elaborated in the strategy the main functionality and features of the project should revolve around table booking management for admins and guests of a restaurant.
It was a clear criteria from the start that the guest users need to be logged in, in order to book a table or manage their bookings.
This is clearly stated on the starting page for users to know at first glance.

I detailed the scope of the project by deciding on the user stories.

### User Stories for the admin users
* As an admin I can check the tables booked online and get a quick overview.

* As an admin I can manually change bookings (date, time, number of seats) to serve customer requests received via phone or email.

* As an admin I can manually delete bookings to serve customer requests.

* As an admin I can administrate the waiting list for reserved tables to balance out cancelled bookings.

### User Stories for the guest users

* As a user I can reserve a table so that I can eat at my favorite restaurant on my preferable date, time and capacity (number of seats).

* As a user I can check if my table is available on my desired date and time.

* As a user I can select the number of seats at the table.

* As a registered user I can change or cancel my booking online saving me the hazzle of calling or writing emails.

* As a user I can register prior to my booking in order to change or cancel my booking later.

#### Future User Functionalities

* As a user I can register for the waiting list in case my table is currently not available at the desired time, date and capacity. It might work out due to another one's cancellation.

* As a user I get a list of available tables based on my booking inquiry and can pick my favorite table according to characteristics (private booth, picture of the table).

* The booking slot now is 1 hour per reservation. The user could be asked in the form how long he intends to stay approx., this could help for occations like birthday parties where longer times are usually required. The user should be given a choice of less than two hours or more than two hours and according to his answer the system blocks the alloted time.


## Structure Plane
The front-end has 6 main pages:
1. Homepage: welcoming the user and telling them what the page is about
2. Menu: Showing which kind of food the restaurant visitors can enjoy
3. Register: An AllAuth backed page
4. Login: An AllAuth backed page
5. Booking Page: To book a table
6. Manage Booking: to change reservations
7. List Bookings: to view done bookings

Plus 5 redirects to confirm actions have taken place:
1. confirmation for the booking
2. confirmation for the booking update
3. asking for confirmation before deletion
4. confirmation deletion
5. asking for confirmation before sign out


## Skeleton Plane

To get a deeper understanding of the website I intend to build, I first sketched the database models and their according fields.
In this design phase it was crucial for me to start thinking about concrete features because the features I had in mind would in turn define the database fields I would need.

### The Database Models

For the design of the database models I had both user groups in mind: the restaurant admins and the guests of the restaurant.
While the guests would work with data connected to their reservation only, the admins for sure would like to do table management as well. E.g. be able to adjust the number of tables available and the number of seats per table.

#### Basic fields
The reservation model would take in typical fields required for every reservation: date, time, a comment field. Since this form would be about restaurant reservations the number of people matters as well. And the table number would be connected as a foreign key.
The table, on the other hand, would have a number and a number of guests in its basic set up. 
But I wanted to add that little extra for both tables and considered USPs relevant in restaurant reservations.

#### Adding USP
##### The extra mile for families
Being a mother myself, I thought it would be a convenient service to add the number of child seats to the model. This way, families booking a table would
a) See that there are child seats at the restaurant and
b) Have the security that they will actually have an available child seat with their booking
The restaurant admins on the other hand can react in case they see a shorthand of child seats for a certain date and react accordingly. – A win-win and good service of the restaurant. Especially with very basic services like bookings at restaurants there is only so much you can do and offer. Adding little small services like the child seat options can turn in a nice little USP that lets families pick Delicious Daily over other restaurants not being so considered in their booking form.

##### The extra mile for couples and small parties
A second guest target group I had in mind were couples. They may prefer a more private setting for their lovey-dovey brunches or romantic dinners. Also people who intend to celebrate a birthday may prefer a more secluded spot in the restaurant. Thus, I added the models field private booth to the tables model.

##### The extra mile to smoothen disappointment
Sometimes it happens that you have the perfect breakfast, lunch or dinner plans and your mind is set on a certain restaurant. Thus, the disappointment is big, if there are no available tables left at the required date or time. This seems especially unfair, considering that people who actually booked sometimes don’t show up or need to cancel their plans last minute. With waiting list functionality I wanted to address this issue and provide the guest with the prospect of a potential table. This extra effort of the restaurant to make their guests wishes true will leave a positive feeling with guest and even if the desired date stays unavailable the guest is more likely to return for another booking because they see the effort.
This feature also provides a relevant benefit for restaurant managers. After all an empty table is equal to missing revenue. So restaurant managers will appreciate the ability to fill up cancellations with waiting reservations.

##### Future functionalities and the data models
I initially planned the waiting list as its own model with the table number and reservation number as foreign keys. But my mentor advised me to add this characteristic to the reservation model directly as a Boolean field called “is_waitlisted”. My mentor also advised me to focus on basic functionality first and write this waiting list feature down for later. Still I decided to integrate this idea in my database model right away, to avoid a re-set up to add the field later.

Like already described in the Scope Plane I came up with one additional feature idea about showing pictures of the available tables and letting the user pic the table themselves. Sadly, I didn’t come up with that idea in the initial design concept but later in the development process, thus an image field in the table model is not integrated in this version of the code. But it is planned for a future version.

### The database model design
Following my above description, I designed the following database model structure for my project Delicious Daily: 

![Database Models](/static/images/readme/Database_Models.png "Database Models")


### Wireframing

A big part of the skeleton design phase was the wireframing. I decided to do low-fidelty wireframes in the design tool Figma. 

For every page and every interaction with the user I design a separate page.

In order to create a full-stack application I designed a **starting page** that has a delicious food pic at its center. And a note telling the user that he or she is able to book a table after free registration. Thus, advertising the main functionality of the page at first glance.
 At the top is a header with the restaurant logo, linking back to the main page from every page, and a menu with basic functionality for checking the menu, registration and login. At the bottom is a footer with the copyright in place.

![Main Screen](/static/images/readme/Wireframes/MainScreen.png "Main Screen")


A page with breakfast, lunch and dinner menus gives the user a taste of what Delicious Daily has to offer and motivate their free registration to book a table.

![Menu](/static/images/readme/Wireframes/Menu.png "Menu")

The registration page for first-time users should offer a fast way to enter details and proceed to the booking features. The design of this page, as well as of the login page is intentionally minimalistic. After all data entry requires focus on the entered data. Too much design or animation around the form only distracts and confuses.

![Register](/static/images/readme/Wireframes/Register.png "Register")

The Login page is designed in similar pattern giving the recurring user the chance to log back in.

![Login](/static/images/readme/Wireframes/Login.png "Login")

Once a user is registered and logged in new menu options present themselves: book a table, view bookings and logout. 

![RegisteredUser](/static/images/readme/Wireframes/RegisteredUser.png "RegisteredUser")

The book a table page is a page of central interest to the user. Therefore the green background of the form is bigger and the background pic is more like a frame to add some visual touch without being to distracting. 
That way the user can focus on the data entry. Still the grey background of the cafe is a repeated image for recognition purposes.

![Book a Table](/static/images/readme/Wireframes/BookATable.png "Book a Table")

After clicking the Book button. The user is directed to a feedback page confirming the booking was successful.

![Booking Confirmation](/static/images/readme/Wireframes/BookingConfirmation.png "Booking Confirmation")

The booking list page follows the same design principle as the book a table page. A big green background highlights the information at center - the booked reservations. These are organized in a list with two possible actions "manage booking" and "delete booking". Part of the green background frame are the buttons "next" and "previous" in case the user has more than 3 bookings.

![View Bookings](/static/images/readme/Wireframes/ViewBookings.png "View Bookings")

When the user wants to update a table booking they press the manage booking button and are directed to the booking form to edit their reservation entry. 

![Update a Table](/static/images/readme/Wireframes/UpdateATable.png "Update a Table")

After making the necessary changes, by clicking the button "Update Booking" they are then directed to a page confirming the update.

![Update Confirmation](/static/images/readme/Wireframes/UpdateConfirmation.png "Login")

If a user clicks the "delete booking" button, they are directed to a subpage asking to confirm the deletion.

![Delete Question](/static/images/readme/Wireframes/DeleteQuestion.png "Delete Question")

If they confirm the deletion they are directed to user feedback page stating that the booking was deleted successfully.

![Confirmation Delete](/static/images/readme/Wireframes/ConfirmationDelete.png "Confirmation Delete")

Once the user wants to log out they click on Logout in the top menu and are directed to a page where they have to confirm there logout.

![Logout Question](/static/images/readme/Wireframes/LogoutQuestion.png "Logout Question")

In general, I followed a  minimalist approach for user feedback pages (like e.g. your booking has been confirmed, deletion is confirmed, booking update is confirmed) and for interaction pages (e.g. please confirm deletion, do you really want to log out).

### User Flow
Wireframing is always closely linked to the user flow. After all, if I don't know how the user navigates to the page and which touchpoints he or she has, how should I consideratley design the wireframing?
Thus, with the wireframes designed I created a typical user flow for recurring users and first time users in one graphic.

![User Flow Delicious Daily](/static/images/readme/UserFlow_deliciousdaily.png "User Flow")

#### First-time users

First-time users enter the page, browse the menu, register, book a table, list their booking. They eventuelly may adapt their booking or delete it. Ultimately they log out.

#### Recurring users

Recurring users enter the page, browse the menu, login in, book a table and/or list their previous bookings. They might update or delete previous bookings and eventually log back out.

## Surface Plane

Each surface design for me starts with the color scheme. After all it determines the imagery used and also the typography.

### Color Scheme
Since by definition imagery of food tends to be colorful and should be at the center of page, the color scheme I choose was subtle and down to earth. No screaming colors but colors that go well as supporting colors.

#### Main color
For the header, footer, logo as well as the background blocks of forms and lists I choose the color cadetblue to frame the rich imagery and information displayed.

![Main Color - Cadet Blue](/static/images/readme/colorscheme/cadetblue.png "Main Color - Cadet Blue")

#### Supporting color
As supporting colors I choose Alice Blue to create a nice supporting contrast to the cadetblue main color. As further supporting colors I used dark charcoal and white.

![Supporting Color - Alice Blue](/static/images/readme/colorscheme/aliceblue.png "Main Color - Alice Blue")
![Supporting Color - Dark Charcoal](/static/images/readme/colorscheme/dark_charcoal.png "Main Color - Dark Charcoal")
![Supporting Color - White](/static/images/readme/colorscheme/white.png "Main Color - White")

### Typography
For the font I decided to go with Cormorant Garamond as the main font. It is very good to read and still has some unique touch to it. The font Pacifico is more playful and used for special nuances like the quote of the Chef or the logo.

### Imagery
The imagery chosen show the delight and deliciousness of eating. It is more than just a process of eating to fill an empty stomach. It is a celebration of taste and touches all senses.

#### Key Visual
The key visual is the picture of the restaurant from outsite. It appears to be drawn but is actually an edited picture. This effect together with the colors of the visual give a softer touch compared to a pure photograph. 
The key visual is used in a black-and-white version as a background whenever the user has to enter information or is given information. This way a pattern is visible to the user that makes him or her recognize he is still on the right website and was not redirected somewhere else.
Furthermore, it undermines the role of the key visual as something recurring and recognizeable, similar to the logo.

![Key Visual](/static/images/readme/startingpage/starting_page_1.png "Key Visual")


#### Food pictures
For the menus breakfast, lunch and dinner one symbol picture each was used. Like described before with the color scheme, the food pics are supposed to look delicious and inviting to eat at the restaurant. The pics are colorful and very distinct from each other to suggest different tasts and looks depending on the time of day you eat at Delicious Daily.

![Key Visual](/static/images/readme/startingpage/starting_page_4.png "Key Visual")


#### Picture of the restaurants chef
There is nothing more welcoming than a friendly face. So the restaurant chef himself decided to appear on the main page - doing what he does best: prepare delicious food. A quote about the joy of eating is adding to the overall feeling that eating is a delicious act. 

![Key Visual](/static/images/readme/startingpage/starting_page_2.png "Key Visual")


# Features
Like already elaborated in the Skeleton Plane the main features and functionalities revolve around the basics of a restaurant table booking system plus individual USPs added to give the user an even better experience.

## CRUD
The main functionality I focused on in the initial developement process was the CRUD functionality:
* Create table bookings
* Read table bookings
* Update table bookings and
* Delete table bookings

### Create a booking
In order to create a booking the user first has to register. Once logged in the user clicks on "Book a table" in the menu to get to the booking form. The user is required to enter the date, time, number of people and number of child seats required. The commed field is optional. On clicking the Book button the data entry is checked through form validation. If the data entry was correct the user is informed that the booking was successful. Otherwise error messages inform the user about the problem with the entered data.
 
#### Form Validation
The form validation checks if:
* The date is entered in the format DD/MM/YYYY
* The time is entered in the format HH:MM
* The date is not in the past
* The time is within opening hours
* The date is not a monday
* The number of guests is bigger than 0
* The comment is no more than 300 characters

#### Double Booking
The user is informed in case there is no table available for the requested date, time and number of guests.

### Read table booking
When clicking the "view bookings" button the user can check all bookings they did so far. In case there aren't any bookings yet the user is informed through a message. If there are bookings listed the user is free to manage the booking or delete it through the provided buttons.
Many table booking forms are just basic contact forms sending the restaurant email for reservation requests. But Delicious Daily offers a database-based solution that allows users to not only book but also manage and delete their bookings easily and fast.

### Update and delete table booking 
Sometimes plans change and the user needs to update or delete their booking. If the reservation request was send via a contact form the user would be required to write an email or call. If the phone is busy or the restaurant closed at the time this easy task of updating or deleting a booking can be tedious. Not with Delicious Daily. Here each customer can manage their reservations themselves giving them maximum flexibility and ease-of-access. 
When updating the booking, the user is required to update the data he or she already entered in the form and then pressing the button update. An immediate message confirms the changes.
When deleting a booking, the user is requried to press the according button in the actions column of the table listing all reservations. The user is then asked once more if he or she is sure they want to cancel. Then in a last step the cancellation is confirmed.

## USP

### Child Seat Feature
Families don't have to worry whether their little ones will have their own child seats available at the restaurant, because they can be booked with the table - individually and easily. The information about required child seats is also passed to the restaurant admin and therefore a shortage is made visible fast and can be acted on.


# Technologies Used
To reach the functionalities described above in the features section, I worked with the MTV (Model-Template-Views) framework Django. For the models, views and form I used Python. To create my templates I used HTML. And to style it I used CSS and Bootstrap.
For file storage cloudinary was used, to store the database Elephant SQL was used. Whitenoise was installed to handle the transfer of the static files between Django, Cloudinary and Heroku.

A full list of libraries used you can find in the list below.

asgiref==3.6.0
cloudinary==1.33.0
dj-database-url==0.5.0
dj3-cloudinary-storage==0.0.6
Django==3.2.18
django-allauth==0.52.0
django-summernote==0.8.20.0
gunicorn==20.1.0
oauthlib==3.2.2
psycopg2==2.9.5
PyJWT==2.6.0
python3-openid==3.2.0
pytz==2022.7.1
requests-oauthlib==1.3.1
sqlparse==0.4.3
urllib3==1.26.15
whitenoise==6.5.0

# Debugging
### Debugging (old)

For me the easiest parts included setting up the admin page and create the models. Troubles started with creating the views and wiring them up with the urls. The following issues came up and were solved by me:

The urlspatterns were missing commas
in the urls path the name attribute was missing, therefore the wiring was not complete
After adding AllAuth I had some troubles wiring up the Menu and Book a Table into the nav bar (only visible if authentificated)

The biggest issue by far was and is the wiring of the form with the database. I became aware of the issue by entering test data to the form and checking the backend for entries but not finding any. Then I started to integrate print statements into my views function to get behind the issue. I solved a minor identation problem in the settings.py file and realized that the POST request is not even started proberly, because the first print statement after the request was already completely ignored. 
I was able to solve major issues already, like missing capitalization of POST in the HTML and views file and unaligned naming of form input fields. Currently, I am trying to figure out how to address a foreign key in a database (private_booth is part of the model Table and needs to be requested by model Reservation).

# Testing
## Manual Testing
### Test Cases
CRUD
   Create
   Read
   Update
   Delete
Form validation
Double Booking

## Validators

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

#### Using the Django authentication system (to restrict access for not logged in users)
https://docs.djangoproject.com/en/dev/topics/http/views/#the-404-page-not-found-view
https://docs.djangoproject.com/en/1.11/topics/auth/default/#the-loginrequired-mixin
https://stackoverflow.com/questions/34217400/function-object-has-no-attribute-as-view
https://stackoverflow.com/questions/17662928/

#### error pages set up
https://www.w3schools.com/django/django_404.php
https://studygyaan.com/django/built-in-error-views-in-django
django-creating-a-custom-500-404-error-page
https://stackoverflow.com/questions/60507625/django-wrong-amount-of-arguments-in-custom-handler
https://stackoverflow.com/questions/60507625/django-wrong-amount-of-arguments-in-custom-handler

#### Find out that the inner-menu-card div was missing for my flip cards to work on the front page 
https://www.w3schools.com/howto/howto_css_flip_card.asp

#### Read more about and follow PEP 8 conventions
https://www.datacamp.com/tutorial/pep8-tutorial-python-code?utm_source=google&utm_medium=paid_search&utm_campaignid=19589720818&utm_adgroupid=143216588777&utm_device=c&utm_keyword=&utm_matchtype=&utm_network=g&utm_adpostion=&utm_creative=661628555465&utm_targetid=dsa-1947282172981&utm_loc_interest_ms=&utm_loc_physical_ms=20047&utm_content=dsa~page~community-tuto&utm_campaign=230119_1-sea~dsa~tutorials_2-b2c_3-n-eu_4-prc_5-na_6-na_7-le_8-pdsh-go_9-na_10-na_11-na&gclid=Cj0KCQjw0IGnBhDUARIsAMwFDLlIxFR_fPQKt4TkcMKSAowINprSfDHmO2iF59yPWU06ECHlYAR5dNEaAuh3EALw_wcB

#### Install whitenoise and collect static files to display images and use css files when deployed to Heroku
https://www.w3schools.com/django/django_static_whitenoise.php
https://www.w3schools.com/django/django_collect_static_files.php


 

