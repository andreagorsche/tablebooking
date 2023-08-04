# Testing
## Manual Testing
With every sprint manual tests of the intendent funcitonalities and design features were done. The tests were based on acceptance criteria directly derived from the user stories. For documentation an excel sheet was used addressing each user story with according acceptance criteria, tasks and bug fixes.



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

To test the **form validation functionality** wrong data was entered intentionally to stress test the system:

* Users enter wrong data format and/or time format
* Users enter strings instead of time or date
* Users enter past date
* Users enter a date that is a monday (closed on mondays)
* Users enter a date outside of opening times
* Users don't enter number of guests
* Users enter more than 300 characters of text in the comments field

To test that users can't book the **same date and time** twice the following tests were performed:

* User can't double book a booking he or she has done
* User can't double book a booking another user has done
* User can't update a booking to a date and time another user already booked
* User can't update a booking to a date and time they themself have already booked

To test the functionalities of the **admin side** the following test cases were looked at:

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
For me the easiest parts included setting up the admin page and create the models. Troubles started with creating the views and wiring them up with the urls. The following issues came up and were solved by me:

The urlspatterns were missing commas
in the urls path the name attribute was missing, therefore the wiring was not complete
After adding AllAuth I had some troubles wiring up the Menu and Book a Table into the nav bar (only visible if authentificated)

The biggest issue by far was and is the wiring of the form with the database. I became aware of the issue by entering test data to the form and checking the backend for entries but not finding any. Then I started to integrate print statements into my views function to get behind the issue. I solved a minor identation problem in the settings.py file and realized that the POST request is not even started proberly, because the first print statement after the request was already completely ignored. 
I was able to solve major issues already, like missing capitalization of POST in the HTML and views file and unaligned naming of form input fields. Currently, I am trying to figure out how to address a foreign key in a database (private_booth is part of the model Table and needs to be requested by model Reservation).

## Validators
For HTML and CSS the W3 Validators were used. In the first instance there were still bugs showing that are eloborated about in the section above "Debugging". After the debugging was finished no further Validation errors showed.

## HTML Validator

![HTML Validator](/static/images/readme/validators/HTMLValidator.png "HTML Validation")

The above picture is one example of this website passing the HTML validator. The validations were done for all subpages. Since the screens would all look the same, I decided to not copy them all in here.

## CSS Validator

![CSS Validator](/static/images/readme/validators/CSSValidator.png "CSS Validation")

### Pep 8
For the Python files the Pep8 install was used to ensure the code is according to PEP 8 conventions.

## Lighthouse
To test the overall performance of the website Lighthouse was used:

![Lighthouse](/static/images/readme/validators/Lighthouse.png "Lighthouse")