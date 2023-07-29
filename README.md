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



## Status Unfinished
Currently, the website is unfinished due to major debugs that took their time. So basically I ran out of time and had to hand in an unfinished project.

### Debugging

For me the easiest parts included setting up the admin page and create the models. Troubles started with creating the views and wiring them up with the urls. The following issues came up and were solved by me:

The urlspatterns were missing commas
in the urls path the name attribute was missing, therefore the wiring was not complete
After adding AllAuth I had some troubles wiring up the Menu and Book a Table into the nav bar (only visible if authentificated)

The biggest issue by far was and is the wiring of the form with the database. I became aware of the issue by entering test data to the form and checking the backend for entries but not finding any. Then I started to integrate print statements into my views function to get behind the issue. I solved a minor identation problem in the settings.py file and realized that the POST request is not even started proberly, because the first print statement after the request was already completely ignored. 
I was able to solve major issues already, like missing capitalization of POST in the HTML and views file and unaligned naming of form input fields. Currently, I am trying to figure out how to address a foreign key in a database (private_booth is part of the model Table and needs to be requested by model Reservation).



### Next steps
The next steps of my programming will include:
1. Fix the existing booking form bug (data is not send to database yet; inability to access foreign key)
2. Add full CRUD functionality
3. Adding tests
4. Adding bootstrap, CSS and JavaScript for the looks of the website
5. Manage Booking: to change reservations
6. Add up on the Read me File


 
