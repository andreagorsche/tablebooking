# Testing
## Manual Testing
With every sprint, manual tests of the intended functionalities and design features were done. The tests were based on acceptance criteria directly derived from the user stories. For documentation an excel sheet was used addressing each user story with according acceptance criteria, tasks and bug fixes.

### User Story 1 

**As a user I can register prior to my booking in order to change or cancel my booking later.**

The overview table for user story one sums up the tested acceptance criteria, the performed tasks and the bug fixes that took place.

![User Story 1](/static/images/readme/testing/1_user_story/userstory1withacceptancecriteria.png "User Story 1, with Acceptance Criteria, Tasks and Debug Fixes")

Starting Page of Delicious Daily, Starting Point of Manual Testing:
![Start Manual Testing](/static/images/readme/testing/1_user_story/testing/1_start.png "Starting Page for Manual Testing")

Acceptance Criteria 1_1:
Navigation leads first-time user to the registration form.

![AC 1_1](/static/images/readme/testing/1_user_story/testing/ac1_1.png "User Story 1, AC 1_1")

Acceptance Criteria 1_2:
Navigation leads recurring user to the login form.

![AC 1_2](/static/images/readme/testing/1_user_story/testing/ac1_2.png "User Story 1, AC 1_2")

Acceptance Criteria 1_3:
User can fill the registration form with data.

![AC 1_3](/static/images/readme/testing/1_user_story/testing/ac1_3.png "User Story 1, AC 1_3")

Acceptance Criteria 1_4:
User can fill the login form with data.

![AC 1_4](/static/images/readme/testing/1_user_story/testing/ac1_4.png "User Story 1, AC 1_4")

Acceptance Criteria 1_5:
User - who wants to register - gets feedback if email does not fulfill required format.

![AC 1_5](/static/images/readme/testing/1_user_story/testing/ac1_5.png "User Story 1, AC 1_5")

Acceptance Criteria 1_6:
User - who wants to register - gets feedback if password fulfills requirements

![AC 1_6](/static/images/readme/testing/1_user_story/testing/ac1_6.png "User Story 1, AC 1_6")

Acceptance Criteria 1_6b:
User - who wants to register - gets feedback if password is too common.

![AC 1_6b](/static/images/readme/testing/1_user_story/testing/ac1_6b.png "User Story 1, AC 1_6b")

Acceptance Criteria 1_6c:
User - who wants to sign in -  sees that username and/or password are not correct.

![AC 1_6c](/static/images/readme/testing/1_user_story/testing/ac1_6c.png "User Story 1, AC 1_6c")

Acceptance Criteria 1_7:
User sees that login was successful.

![AC 1_7](/static/images/readme/testing/1_user_story/testing/login_success.png "User Story 1, AC 1_7")

Acceptance Criteria 1_8:
User sees that logout was successful.

![AC 1_8](/static/images/readme/testing/1_user_story/testing/ac1_7.png "User Story 1, AC 1_8")

Acceptance Criteria 1_9:
User sees when password is not the same while registering

![AC 1_9](/static/images/readme/testing/1_user_story/testing/ac1_9.png "User Story 1, AC 1_9")

## Debugging in context with User Story 1
The following bugs occured while working on the tasks for user story 1:

Bug 1: tablebooking.views has no attribute login
![User Story 1, Bug 1](/static/images/readme/testing/1_user_story/debug/d1_1.png "User Story 1, Bug 1")

Fix for Bug 1:
In the urls.py file the path for the menu had the views.login instead of views.base, so I changed it to views.base.

Bug 2: When a user tries to access a URL that requires a login, the redirection leads to a sign in page without the according form, leading to one extra click for the user (bad user experience)
![User Story 1, Bug 2](/static/images/readme/testing/1_user_story/debug/d1_2.png "User Story 1, Bug 2")

Fix for Bug 2: I had created a custom login view thus overwriting the Django sign in page. The bug was fixed as soon as I deleted the custom login page and  wired up with Django login in page instead.

Bug 3: When the user authentificated, the content was not displayed, instead a Template Syntax Error showed. 

![User Story 1, Bug 3](/static/images/readme/testing/1_user_story/debug/d1_3.png "User Story 1, Bug 3")

Fix for Bug 3: There was an end if missing in the template code.

Bug 4: When adding the Django status messages, to the code, the div for django message stayed displayed after the message was already disolved.

![User Story 1, Bug 4](/static/images/readme/testing/1_user_story/debug/d1_4.png "User Story 1, Bug 4")

Fix for Bug 4: Javascript needed to be properly imported and code had typos. 

### User Story 2 

**As a user I can check if my table is available on my desired date and time.**

The overview table for user story two sums up the tested acceptance criteria, the performed tasks and the bug fixes that took place.

![User Story 2](/static/images/readme/testing/2_userstory/userstory2withacceptancecriteria.png "User Story 2, with Acceptance Criteria, Tasks and Debug Fixes")

Acceptance Criteria 2_1: The user is getting a confirmation if the booking at the desired date and time was possible.

![AC 2_1](/static/images/readme/testing/2_userstory/a2_1.png "User Story 2, AC 2_1")

Acceptance Criteria 2_2: The user gets an error message if there is no table available at the desired date and time.

![AC 2_2](/static/images/readme/testing/2_userstory/a2_2.png  "User Story 2, AC 2_2")

## Debugging in context with User Story 2
The following bugs occured while working on the tasks for user story 2:

Bug 1: When entering wrong data in the booking form, error messages were not showing.

![User Story 2, Bug 1](/static/images/readme/testing/2_userstory/d2_1.png "User Story 2, Bug 1")

Fix for Bug 1:
The displaying of errors in the html template was missing.

Bug 2: Double booking is possible despite a check in the code that should forbid a double booking.

![User Story 2, Bug 2](/static/images/readme/testing/2_userstory/d2_2.png "User Story 2, Bug 2")

Fix for Bug 2:
The check for double bookings was written in the forms.py instead of the views file. Once the code was transfered it worked properly.

### User Story 3
**As a user I can reserve a table so that I can eat at my favorite restaurant on my preferable date, time and capacity (number of seats).**

The overview table for user story three sums up the tested acceptance criteria, the performed tasks and the bug fixes that took place.

![User Story 3](/static/images/readme/testing/3_userstory/userstory3withacceptancecriteria.png "User Story 3, with Acceptance Criteria, Tasks and Debug Fixes")

Acceptance Criteria 3_1: User can navigate to the booking form.

![AC 3_1](/static/images/readme/testing/3_userstory/a3_1.png "User Story 3, AC 3_1")

Acceptance Criteria 3_2: User can enter data into the form.

![AC 3_2](/static/images/readme/testing/3_userstory/a3_2.png "User Story 3, AC 3_2")

Acceptance Criteria 3_3: User can sent data.

![AC 3_3](/static/images/readme/testing/3_userstory/a3_3.png "User Story 3, AC 3_3")

Acceptance Criteria 3_4-3_6: User is informed if they enter the wrong date format. User is informed if they enter the wrong time format. User is informed if number of guests is not >0.

![AC 3_4](/static/images/readme/testing/3_userstory/a3_4.png "User Story 3, AC 3_4")

Acceptance Criteria 3_7: User is informed if the date they choose is in the past.

![AC 3_5](/static/images/readme/testing/3_userstory/a3_5.png "User Story 3, AC 3_5")

Acceptance Criteria 3_8: User is informed if they enter a date that is a monday, because monday the restaurant is closed.

![AC 3_6](/static/images/readme/testing/3_userstory/a3_6.png "User Story 3, AC 3_6")

Acceptance Criteria 3_9: User is informed if they try to book outside of opening hours.

![AC 3_7](/static/images/readme/testing/3_userstory/a3_7.png "User Story 3, AC 3_7")

Acceptance Criteria 3_10: User is informed if comment has more than 300 characters.

![AC 3_8](/static/images/readme/testing/3_userstory/a3_8.png "User Story 3, AC 3_8")

## Debugging in context with User Story 3
The following bug occured while working on the tasks for user story 3:

Bug 1: In a second iteration, the error messages regarding form validation didn't work AGAIN. 

![User Story 3, Bug 1](/static/images/readme/testing/3_userstory/d3_1.png "User Story 3, Bug 1")

Fix for Bug 1: This time the issue was due to a change I made while testing my code with the html validator. There it stated that nesting button tags in anchor tags is bad practice. Although shown in class, I decided to change it. Thereby I created a logic error in the code. On button click I linked to the confirmation page directly instead of submitting the form data and the success url being the confirmation page. - This case showed me that features that already worked, can stop working, if code is altered and that causes are sometimes very hidden and not in the obvious context (e.g. form validation does not work, so form validation logic is wrong - sometimes it is some html template error that causes the problem.)

### User Story 4

**As a user I can select the number of seats at the table.**

The overview table for user story four sums up the tested acceptance criteria, the performed tasks and the bug fixes that took place.


![User Story 4](/static/images/readme/testing/4_userstory/userstory4withacceptancecriteria.png "User Story 4, with Acceptance Criteria, Tasks and Debug Fixes")

Acceptance Criteria 4_1:
User can enter the number of seats he or she wishes to occupy with the booking.

![AC 4_1](/static/images/readme/testing/4_userstory/a4_1.png "User Story 4, AC 4_1")

Acceptance Criteria 4_2:
User is informed if number of guests is <=0

![AC 4_2](/static/images/readme/testing/4_userstory/a4_2.png "User Story 4, AC 4_2")

## Debugging in context with User Story 4
The following bug occured while working on the tasks for user story 4:

Bug 1: Error messages not showing when wrong data is entered into the form.

![User Story 4, Bug 1](/static/images/readme/testing/3_userstory/d3_1.png "User Story 4, Bug 1")

Fix for Bug 1: This bug occured in 2 iternations. The first time the issue was due to the error messages not being integrated in the html template. And the second time the html template of the create booking were altered wrongly (nested button within link tag) --> see Bug 1 in User Story 2 and 3.

### User Story 5

**As a registered user I can change or cancel my booking online saving me the hazzle of calling or writing emails.**

The overview table for user story five sums up the tested acceptance criteria, the performed tasks and the bug fixes that took place.


![User Story 5](/static/images/readme/testing/5_userstory/userstory5withacceptancecriteria.png "User Story 5, with Acceptance Criteria, Tasks and Debug Fixes")

Acceptance Criteria 5_1:
User can navigate to the existing bookings.

![AC 5_1](/static/images/readme/testing/5_userstory/a5.1.png "User Story 5, AC 5_1")

Acceptance Criteria 5_2:
User is informed if there are no current bookings available.

![AC 5_2](/static/images/readme/testing/5_userstory/a5.2.png "User Story 5, AC 5_2")

Acceptance Criteria 5_3:
User is shown a list of current bookings, if they exist.

![AC 5_3](/static/images/readme/testing/5_userstory/a5.1.png "User Story 5, AC 5_3")

Acceptance Criteria 5_4:
User can navigate between the bookings.

Previous:
![AC 5_4_1](/static/images/readme/testing/5_userstory/a5.4_1.png "User Story 5, AC 5_4_1")

Next:
![AC 5_4_2](/static/images/readme/testing/5_userstory/a5.4_2.png "User Story 5, AC 5_4_2")

Acceptance Criteria 5_5:
User can navigate to the update booking form.

![AC 5_5](/static/images/readme/testing/5_userstory/a5.5.png "User Story 5, AC 5_5")

Acceptance Criteria 5_6:
User is informed if the update is not possible (error messages according to form validation - see user story 3).

![AC 5_6](/static/images/readme/testing/5_userstory/a5.6.png "User Story 5, AC 5_6")

Acceptance Criteria 5_7:
User is informed if the booking update at the selected time and date is not possible anymore (avoid double booking).

![AC 5_7](/static/images/readme/testing/5_userstory/a5.7.png "User Story 5, AC 5_7")

Acceptance Criteria 5_8:
User is informed that update was successful.

![AC 5_8](/static/images/readme/testing/5_userstory/a5.8.png "User Story 5, AC 5_8")

Acceptance Criteria 5_9:
User can navigate to delete a booking on mouse-click.

![AC 5_9](/static/images/readme/testing/5_userstory/a5.1.png "User Story 5, AC 5_9")

Acceptance Criteria 5_10:
User is asked to confirm deletion.

![AC 5_10](/static/images/readme/testing/5_userstory/a5.10.png "User Story 5, AC 5_10")

Acceptance Criteria 5_11:
User is informed about successful deletion.

![AC 5_11](/static/images/readme/testing/5_userstory/a5.11.png "User Story 5, AC 5_11")

### User Story 6

**As an admin I can check the tables booked online and get a quick overview.**

The overview table for user story six sums up the tested acceptance criteria, the performed tasks and the bug fixes that took place.


![User Story 6](/static/images/readme/testing/6_userstory/userstory6withacceptancecriteria.png "User Story 6, with Acceptance Criteria, Tasks and Debug Fixes")

Acceptance Criteria 6_1:
Admin can access a list of all bookings/reservations.

![AC 6_1](/static/images/readme/testing/6_userstory/a6_1.png "User Story 6, AC 6_1")

Acceptance Criteria 6_2:
Admin can filter the reservations by characteristics like table, date, number of guests.

![AC 6_2](/static/images/readme/testing/6_userstory/a6_2.png "User Story 6, AC 6_2")


### User Story 7

**As an admin I can manually change bookings (date, time, number of seats) to serve customer requests received via phone or email.**

The overview table for user story seven sums up the tested acceptance criteria, the performed tasks and the bug fixes that took place.

![User Story 7](/static/images/readme/testing/7_userstory/userstory7withacceptancecriteria.png "User Story 7, with Acceptance Criteria, Tasks and Debug Fixes")

Acceptance Criteria 7_1:
Admin is able to access and edit reservations.

![AC 7_1](/static/images/readme/testing/7_userstory/a7_1.png "User Story 7, AC 7_1")

Acceptance Criteria 7_2:
Admin is able to delete reservations.

![AC 7_2](/static/images/readme/testing/7_userstory/a7_2.png "User Story 7, AC 7_2")


Acceptance Criteria 7_3:
Admin is able to add tables.

![AC 7_3](/static/images/readme/testing/7_userstory/a7_4.png "User Story 7, AC 7_3")

Acceptance Criteria 7_4:
Admin is able to delete tables.

![AC 7_4](/static/images/readme/testing/7_userstory/a7_5.png "User Story 7, AC 7_4")

Acceptance Criteria 7_5:
Admin is able to edit tables.

![AC 7_5](/static/images/readme/testing/7_userstory/a7_3.png "User Story 7, AC 7_5")

### User Story 8

**As an admin I can administrate the waiting list for reserved tables to balance out cancelled bookings.**

The overview table for user story eight sums up the tested acceptance criteria, the performed tasks and the bug fixes that took place.

![User Story 8](/static/images/readme/testing/8_userstory/userstory8withacceptancecriteria.png "User Story 8, with Acceptance Criteria, Tasks and Debug Fixes")

Acceptance Criteria 8_1:
Admin can tick waitlisted on and off in reservation.

![AC 8_1](/static/images/readme/testing/8_userstory/a8_1.png "User Story 8, AC 8_1")


### Acceptance Criteria - Assessment of 1st submission

In order to work through the assessment of the 1st submission I created a table with acceptance criteria, tasks and bugs, as for the user stories.

![Assessment 1st submission](/static/images/readme/assessment/acceptance_criteria_assessment.png "Assessment 1st submission")

Acceptance Criteria 1: Favicon added

![Favicon](/static/images/readme/assessment/favicon.png "Favicon")

Acceptance Criteria 2: Error pages added

![Error pages](/static/images/readme/assessment/errorpages.png "Error pages")

Acceptance Criteria 3: Frontend Design is completed
![Front End Design](/static/images/readme/testing/1_user_story/testing/1_start.png "Front End Design")

Acceptance Criteria 4: user stories are more detailed with acceptance criteria

![acceptance criteria](/static/images/readme/testing/1_user_story/userstory1withacceptancecriteria.png "acceptance criteria")

Acceptance Criteria 5: python functions have docstrings

![docstrings python](/static/images/readme/assessment/filenames_nocapitalization.png "doc strings python")

Acceptance Criteria 6: python code follows PEP 8 formatting convensionts

**See python code.**
The only exception are 5 too long lines in the settings.py. These are the AUTH_PASSWORD_VALIDATORS. I left them on purpose the way they are.

Acceptance Criteria 7: file names avoid capitalization

![file names](/static/images/readme/assessment/filenames_nocapitalization.png "file names")

Acceptance Criteria 8: key design decisions are clearly documented

**See Readme.md file**

Acceptance Criteria 9: CRUD functionalities of the form are functioning and allowing users to initiate actions

![CRUD functionality](/static/images/readme/testing/5_userstory/a5.6.png "Crud functionality")

Acceptance Criteria 10: Notifications of successful or failed CRUD operations are made to the user

![AC 5_8](/static/images/readme/testing/5_userstory/a5.8.png "User Story 5, AC 5_8")

Acceptance Criteria 11: Backend code for form has foolproof validations to avoid incorrect user inputs

![AC 3_4](/static/images/readme/testing/3_userstory/a3_4.png "User Story 3, AC 3_4")

Acceptance Criteria 12: Non logged in users can't access restricted content and functionality through direct entry of the URL 

![login required](/static/images/readme/assessment/loginrequired.png "login required")


Acceptance Criteria 13: Manual testing of all functionalities has been performed and been documented in the Testing.md file

**See above**

Acceptance Criteria 14: Commit messages are more specific and more frequently done

**See Github commits**


Acceptance Criteria 15: Deployed code equals the deployment code version

**See deployed project**


Acceptance Criteria 16: Deployment process is part of the read me file

**See Readme.md file**

Acceptance Criteria 17: Debug mode is turned off

**See settings.py file**

Acceptance Criteria 18: Template code is not limited to walkthrough projects

**See template code**

Acceptance Criteria 19: code passes validation

**See Readme.md file**

### Adding final USPs

2 USPs I wanted to add to this app but due to my mentors advice they were something for the end of the project, if there is still time.
These 2 USPs I wanted to add to the  booking form and manage booking form are:

* Private Booth option 
* Waitlist option

#### Private Booth Option

The easiest way to offer the user an option for a private booth, was to add this information to the placeholder text of the comments field.
The user is informed that a private booth setting is possible upon requests. It needs to be stated in the comment field.

#### USP Waitlist 

The waiting list implementation was a trial and error issue from start to finish. 

1. My first approach was an own database model WaitingList but my mentor advised me to integrated is_waitlisted in the reservation model instead.

2.  My second approach was to check the booking request for double-bookings and then if there is a double-booking, let the user confirm that they want to be waitlisted. This proofed to be tricky because at the time the data is validated it needs to be sent - so creating a javascript pop up to confirm, did not work, because data was not sent anymore.

3. I created a redirection to a confirmation page, similar to the deletion confirmation page. So the user would enter a date and time into the registration form, would press the button, the data would be validated and throw the double booking error and then the user would be directed to the waiting list confirmation page. If they press confirm the reservation should be saved otherwise not. The problem with this approach was that the sent data for validation was not transferable to the waitlist confirmation page because no data was saved. 

4. I wanted to integrate a check box called "Waitlist" into the reservation form that would only show if the validation says that there is a double booking. Also this approach was tricky because the form would be needed to render and send data twice and this for both cases: booking and managing a reservation.

**The solution**: Thus, I adapted approach number 3 and created the checkbox for the form right away. If there is a double booking the error message informs the user about the option to be waitlisted and asks to check the waitlist checkbox, in case the user wants to be waitlisted.
If the waitlist checkbox is checked, the user is redirected to a waitlist confirmation page. There the user gets the information that the waiting list registration was successful and that they would hear back from the restaurant 24 hrs prior to the desired booking the latest.

![waitlist checkbox](/static/images/readme/usps/waitlistcheckbox.png "waitlist checkbox")

![waitlist confirmed](/static/images/readme/usps/waitlistconfirm.png "waitlist confirmed")

