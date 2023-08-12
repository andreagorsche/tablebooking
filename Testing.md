# Testing
## Manual Testing
With every sprint manual tests of the intendent funcitonalities and design features were done. The tests were based on acceptance criteria directly derived from the user stories. For documentation an excel sheet was used addressing each user story with according acceptance criteria, tasks and bug fixes.

### User Story 1 

**As a user I can register prior to my booking in order to change or cancel my booking later.**

The overview table for user story one sums up the tested acceptance criteria, the performed tasks and the bug fixes that took place.

![User Story 1](/static/images/readme/Testing/1_UserStory/UserStory1WithAcceptanceCriteria.png "User Story 1, with Acceptance Criteria, Tasks and Debug Fixes")

Starting Page of Delicious Daily, Starting Point of Manual Testing:
![Start Manual Testing](/static/images/readme/Testing/1_UserStory/Testing/1_Start.PNG "Starting Page for Manual Testing")

Acceptance Criteria 1_1:
Navigation leads first-time user to the registration form.

![AC 1_1](/static/images/readme/Testing/1_UserStory/Testing/AC1_1.PNG "User Story 1, AC 1_1")

Acceptance Criteria 1_2:
Navigation leads recurring user to the login form.

![AC 1_2](/static/images/readme/Testing/1_UserStory/Testing/AC1_2.PNG "User Story 1, AC 1_2")

Acceptance Criteria 1_3:
User can fill the registration form with data.

![AC 1_3](/static/images/readme/Testing/1_UserStory/Testing/AC1_3.PNG "User Story 1, AC 1_3")

Acceptance Criteria 1_4:
User can fill the login form with data.

![AC 1_4](/static/images/readme/Testing/1_UserStory/Testing/AC1_4.PNG "User Story 1, AC 1_4")

Acceptance Criteria 1_5:
User gets feedback if email does not fulfill required format.

![AC 1_5](/static/images/readme/Testing/1_UserStory/Testing/AC1_5.PNG "User Story 1, AC 1_5")

Acceptance Criteria 1_6:
User gets feedback if password fulfills requirements

![AC 1_6](/static/images/readme/Testing/1_UserStory/Testing/AC1_6.PNG "User Story 1, AC 1_6")

Acceptance Criteria 1_6b:
User gets feedback if password is too common

![AC 1_6b](/static/images/readme/Testing/1_UserStory/Testing/AC1_6b.PNG "User Story 1, AC 1_6b")

Acceptance Criteria 1_6c:
User sees that username and/or password are not correct.

![AC 1_6c](/static/images/readme/Testing/1_UserStory/Testing/AC1_6c.PNG "User Story 1, AC 1_6c")

Acceptance Criteria 1_7:
User sees that login was successful.

![AC 1_7](/static/images/readme/Testing/1_UserStory/Testing/AC1_7.PNG "User Story 1, AC 1_7")

Acceptance Criteria 1_8:
User sees that logout was successful.

![AC 1_8](/static/images/readme/Testing/1_UserStory/Testing/AC1_8.PNG "User Story 1, AC 1_8")

Acceptance Criteria 1_9:
User sees when password is not the same while registering

![AC 1_9](/static/images/readme/Testing/1_UserStory/Testing/AC1_9.PNG "User Story 1, AC 1_9")

## Debugging in context with User Story 1
The following bugs occured while working on the tasks for user story 1:

Bug 1: tablebooking.views has no attribute login
![Delicious Daily](/static/images/readme/Testing/1_UserStory/Debug/D1_1.PNG "Starting Page")

Fix for Bug 1:
In the urls.py file the path for the menu had the views.login instead of views.base, so I canged it to views.base.

Bug 2: When a user tries to access a URL that requires a login, the redirection leads to a sign in page without the according form, leading to one extra click for the user (bad user experience)
![Delicious Daily](/static/images/readme/Testing/1_UserStory/Debug/D1_2.PNG "Starting Page")

Fix for Bug 2: I had created a custom login view thus overwriting the Django sign in page. The bug was fixed as soon as I deleted the custom login page and  wired up with Django login in page instead.

Bug 3: When the user authentificated, the content was not displayed, instead a Template Syntax Error showed. 

![Delicious Daily](/static/images/readme/Testing/1_UserStory/Debug/D1_3.PNG "Starting Page")

Fix for Bug 3: There was an end if missing in the template code.

Bug 4: When adding the Django status messages, to the code, the div for django message stayed displayed after the message was already disolved.

![Delicious Daily](/static/images/readme/Testing/1_UserStory/Debug/D1_4.PNG "Starting Page")

Fix for Bug 4: Javascript needed to be properly imported and code had typos. 





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