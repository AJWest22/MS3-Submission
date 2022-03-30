**MS3 README**

## Table of Content

1. [Overview](#overview)

2. [Site Goals](#site-goals)
    1. [UX Goals](#ux-goals)
    2. [Siteowners Goals](#siteowners-goals)
    3. [User Stories](#user-stories)
    4. [Siteowner Stories](#siteowner-stories)

3. [About The Site](#about-the-site)
    1. [Target Audience](#target-audience)

4. [Code Used](#code-used)
    1. [Frameworks](#frameworks)
    2. [Files Made](#files-made)

5. [The Database](#the-database)

6. [Design](#design)
    1. [Typography](#typography)
    2. [Colors](#colors)
    3. [Images](#images)

7. [Code Features](#code-features)

8. [Features to be Added](#features-to-be-added)

9. [Testing](#testing)
    1. [HTML Validation](#html-validation)
    2. [CSS Validation](#css-validation)
    3. [Python Validation](#python-validation)
    4. [Browser Compatibility](#browser-compatibility)
    5. [Devices Tested On](#devices-tested-on)

10. [Deployment](#deployment)

11. [Credits](#credits)
     1. [Icons](#icons)
     2. [Imagery](#imagery)
     3. [CSS Framework](#css-framework)
     4. [JQuery Framework](#jquery-framework)

12. [Acknowledgements](#acknowledgements)


## **Overview**
 - This site was created for MS3 submission for Code Institute.
 - The site's name is Book Recommendations.
 - The source code can be found on GitHub
 - The site is deployed using Heroku

 - The purpose of this site is to help people find books they might like to read in a particular genre, and leave 
   recommendations on books they have read and would recommend. Users can browse the site and read the books in the dropdown menu
   recommendations, but must be logged in to add a review, edit, and delete a review. 

 - There are currently two types of accounts at the moment:

     **Username**: Reader **Password**: Reader
    and 

    **Username**: Admin **Password** Admin
    Both accounts are test accounts used to test site functionality, for example: Reader was used to check if accounts were showing on the Database, and Admin was used to check if only reviews added by admin could be edited by admin.

    View the site [here](https://flask-genres-books.herokuapp.com/)

    ## **Site Goals**

### **UX Goals**

 - Users can create, edit and delete reviews on books they've read, either books recommended on the site or one they've read themselves, and browse recommendations by others.

 - Users can also leave feedback or ask any questions they may have regarding the site.


### **Siteowners Goals**

 - Provide a service that encourages people to read books and genres they may not normally try, and find good books.

 - Ensure the database continues to accept new data, such as: books, reviews, users, and feedback or questions.


 ### **User Stories**

 - As a user of this site I want to find a good book from a variety of genres

 - As a user I want to know my feedback on the site has been submitted.

 - As a user i want to know if my login was successful or not.

 - As a user I want a easy to use, simple site.

 - As a user I want the ability to edit or delete any of my recommendations


### **Siteowner Stories**

 - As the owner of this site, I want to create a easy to use site that serves a purpose.

 -  As the owner of this site, I want users to know their feedback and any questions have been submitted

 -  As the owner of this site, I want users to come back to this site.

 - As the owner of this site, I want users to be able to have control over their reviews, so edit and delete them as well as the ability to create them. 

 - As the owner of this site I want users login details to be stored safely and securely by encrypting the password on the server.

 - As the owner of this site I want users to know their data is secure. 


## **About The Site**

 - The site has a total of 9 pages. Some are only visible to users who are logged in (profile page for example).
 - Users who are logged in have the option to add, edit and delete their reviews, while those who aren't logged in
 - can only browse other people's reviews. The site's purpose is to help people find books they'd like to read, and users can
 - create, edit and delete recommendations/reviews on books they have read. The genres chosen range from the ones that tend to be - more popular among people (Crime and Thriller) and those that aren't (Fantasy and Horror) so that it caters for a wide array 
 - of audiences. 

### **Target Audience**
 - The site is primarily aimed and adults/young adults who are either big readers and want to find thier next book, or people who want to read more but aren't sure what to read.


## **Code Used**

 The site is build using:
 - *HTML* to provide the site's structure and features, for example the contact form.

 - *CSS* to add style to the site, for example the font of the typography.

 - *PYTHON* to add the backend functionality to the site, for example sending data to the database.

 - *JQUERY* to offer interactivity to the site, for example dropdown menus.


### **Frameworks**

 - *MATERIALIZE CSS* is used to help style the site, and add some features to the site using JQUERY. The code used by Materialize is marked. I chose to work with Materialize, as it incorporated bootstrap, that helps with the making the site mobile 
 friendly, and also to challenge myself with learning a new framework. Materialize may help with styling, but there can be some
 speificity issues when using it. For example some issues I had with using it included: trying to size images in the carousel, and the header images on the home and reviews pages. (The former has been resolved, but the latter is still not fullwidth). 

 - *FLASK* is a framework and is used to help with the structuring of Python, and can be seen in the site using the for loops on the homepage that get the books from the server {% for books in books2 %}

 - *Jinja Template* is used to render the templates and write code similar to Python. For example: render_template(signup.html)


### **Files Made**

 - There were 9 HTML files made in this project, 2 python files, a JavaScript file, a CSS file, a Procfile and requirements.txt file. 

 - Most can be viewed on GitHUb, however the env.py file, that was created to connnect the database with the site, contains 
   sensitve information, and has not been pushed to GitHub.

 - The HTML files are stored in the templates folder, as they form the basis of the site, and it helps structure and organise 
   the code. 

 - The static folder contains the JavaScript and CSS files, and is used to help structure the code files, and keep things orderly.

 - The app.py file provides the backend code that handles the data of the site. It is used for submitting data to the database and pulling information from the database. 

 - The env.py file that was created contains information regarding the database and has not been pushed to GitHub.