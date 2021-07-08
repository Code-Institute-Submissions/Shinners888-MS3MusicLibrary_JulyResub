# Music Library Collaboration

## Data-Centric Development Project MS3 - Code Institute

MUSO - The Misanthropic Unicorns Symphony Orchestra presents "Bringing Classic Back"

A community built collection of favourites in the various classical/art music genres, to reignite a love of the music.

Features include:
- The ability to browse favourites uploaded by other users
- The ability to upload information about your own favourite pieces
- Admin can update/delete on a case by case basis
- The ability to search by composer or genre
- Discounts to performances by the symphony orchestra for registered users

## Goals

To build a community of people who like classical music and recommend music to those who are new to the genre and may find it overwhelming. The symphony orchestra will let the most popular pieces on the website dictate what is performed every few months, and discounts will be available to members of the community for those concerts.

## UX

This is for people who would like to listen to more classical music but don't know where to begin, or classical music lovers who want to share their favourite pieces. The orchestra notes what new additions there are, and if possible, will perform them at upcoming concerts.

It is a basic layout, easy to follow. The 'create' and 'update' pages are not available from the navbar and have 'go back' buttons easily visible at the top of the page.

#### Not logged in

 - You will land on the MUSO page which will tell you a little bit about the orchestra's site and direct you to register or login.

 - Register to create an account/log in.

#### Logged in

 - You will be taken immediately to the home page which is where upcoming concerts will be listed

 - Browse what others have uploaded and follow the spotify link to listen. This will open in a new tab or the app, so the user can continue to browse while listening.

 - Under the browse is a prompt to add to the library. If the user knows a piece they think the others might like, they can follow the link.

 - If the piece has been added by the current user, they have the option to update or delete the piece. The admin user also has these privileges, in case a user misspells or duplicates anything. The delete button contains a dropdown 

 - Below again is a search bar where users can search by composer or genre, with a button to clear search options. 

 #### Admin

 As well as editing or deleting works, an admin can edit composer information. If a new composer has been entered into the database, they will not yet have a related photo. The admin can upload a photo in the composers page. They can then click edit and save on any works by that composer to have the image displayed.

### Aesthetic

In honour of the unsociable unicorns after which the site is named, the navbar, buttons and footer are made up of bright, almost psychadelic ,colours traditionally associated with unicorns, around a dark monochrome website.



# CRUD

 - Create

Create a user name and password which will be stored in the database with a password hash for security.

Add your favourite piece with some prompted information, and a link to listen to teh piece/work, to be displayed in the browse section

 - Read

The Browse page reads and displays all infomation in the works collection, gathers descriptive information from the genres collection, and displays edit/delete buttons to the admin or the user who originally created the related work.

 - Update

Pieces can be edited by the admin, or the same user that created them. All 'work' information can be updated.

 - Delete

A user who created a work, or the admin can delete said work. They will be prompted with a dropdown button to ensure they did not hit delete by accident.

# Execution

This project was created using:

 - HTML (Note: my own class/id names are created in camelCase while materialize is hyphenated. Python variables are created with snake_case)
 - CSS
 - JQuery
 - Python
 - Flask
 - MongoDB (flask_pymongo)
 - Materialize 
 - Font Awesome
 - Google Fonts
 - VSCode editor for Github

This Project was deployed using [Heroku](https://www.heroku.com/about)

# Resources

 - Code Institute mini project lessons
 - Slack
 - StackOverflow
 - [MongoDB Documentation](https://docs.mongodb.com/manual/)
 - [Werkzeug Password Hashing](https://werkzeug.palletsprojects.com/en/1.0.x/utils/#general-helpers)
 - [Unsplash](https://unsplash.com/)
 - [Favicon.io](https://favicon.io/)
 - [Clipart Key](https://www.clipartkey.com/view/bhiwTb_illustration/)
 - [Spotify](https://open.spotify.com/)

# Wireframes

[Desktop1](https://github.com/Shinners888/MS3MusicLibrary/blob/master/assets/wireframes/MUSODesktop.jpg)

[Desktop2](https://github.com/Shinners888/MS3MusicLibrary/blob/master/assets/wireframes/MUSODesktop1.jpg)

[Desktop3](https://github.com/Shinners888/MS3MusicLibrary/blob/master/assets/wireframes/MUSODesktop2.jpg)

[Desktop4](https://github.com/Shinners888/MS3MusicLibrary/blob/master/assets/wireframes/MUSODesktop3.jpg)

[Desktop5](https://github.com/Shinners888/MS3MusicLibrary/blob/master/assets/wireframes/MUSODesktop4.jpg)
[Mobile](https://github.com/Shinners888/MS3MusicLibrary/blob/master/assets/wireframes/MUSOMobile.jpg)

Please note these were early sketches and some elements do not represent the working website

# Data Diagram

[Data Diagram](https://github.com/Shinners888/MS3MusicLibrary/tree/master/assets/MUSO1.png)

Please note this was an early sketch of the relationships between the various types of data. In implementing the project, it became prudent to slightly alter how the collections interacted with one another.

# Creation and testing

### Database Creation

In MongoDB I created a music library database with four collections: composers, genres, site_users and works. Works is the main collection and gathers data in some shape or form from each other collection. 

- Genres

Each genre has it's own info. And to sort them chronologically in the site, each has an Int ID depending on when that period of classical music occurs. This provides a reference of a time period when a user is uploading a new piece, for those who may not be sure of the classical music eras.

- Site_users

This simply contains a username and password. The user that creates each work will be stored in the work collection so they can edit or delete what they have uploaded if they wish. The passwords are encrypted using the werkzeug password hash

- Composers

Another simple collection. This contains just composer names and their corresponding images. When a user adds a new work, this collection is scanned to see if the user already exists. If it does, no new composer is created. If it exists and has a corresponding image, the ObjectId and composer image url will be imported into the created works object as a nested object. This will allow the composer image to display under any of their works.

- Works

The main collection of this project. The objects in this collection contain at a minimum, the composer name, the name of the work, the genre and the username of the object creator. There should also be a short description and a url to redirect the user to listen to the piece/s. The $text Index search function acts on this collection, querying the composer and genre fields.


### Creation 
1. Initial Commits: Imported flask, flask_pymongo, dnspython, and os, linked to Heroku and MongoDB, tested that an HTML page would display print from app.py. Created a base HTML page.

2. Added Registration and login pages linked to site_users collection in MongoDB. Styled base html, added flash messages and a method to display them (in base.html) Checked all git push commands deployed to Heroku.

3. Added logout function to pop user from system. Checked application system cookies and verified that session user was gone after logout.

4. Added browse page with carousel. The carousel iterates through the works in the database and diplays each, one after the other, featuring elements of each work.

5. Created the add_work function. This gives the user a selection of genres with their rough timelines for reference. The rest of the data is filled in themselves.

6. Removed autocomplete from some aspects of the form as it was not aesthetically pleasant, particularly in the login section. It is helpful in adding a composer or searching.

7. Altered JS for the carousel as clicking any buttons on it were overridden by the carousels inbuilt turn function.

8. Created index text search via python3 - from app import mongo. Will search the works collection for a composer name or genre.

9. Added and wired up edit and delete functions, only available to the user that added that work_id, or to the admin.

10. Styled and changed general layout of site. Discarded pointless pages, added a modal to confirm logout request, and dropdown to confirm delete request.

11. Added functionality within add and edit work functions, to read the composer name, find the composers unique ID, get the composer image from said ID if it already exists, and populate an image object with the _id and composer image fields.

12. Added method to delete composer. It is possible that duplicates would happen due to spelling errors. The admin can update incorrect spelling in the work and remove the incorrect/duplicate composers.

13. Tidied code and commented.

14. Set debug to False

# Deployment

- Create env.py file with the following fields:

import os

os.environ.setdefault("IP", "0.0.0.0")<br>
os.environ.setdefault("PORT", "5000")<br>
os.environ.setdefault("SECRET_KEY", "")<br>
os.environ.setdefault("MONGO_URI", "")<br>
os.environ.setdefault("MONGO_DBNAME", "CLUSTER NAME HERE")

- push env.py to gitignore with __pycache_/

- Type "pip3 freeze --local > requirements.txt" in the terminal (so Heroku will know what is required to run the app)

- Use pip3 to install flask, flask_pymongo and dnspython

- The app can now be run locally by typing python3 app.py in the terminal

Heroku Deployment

Deployment was executed early on, with commits and pushes updateing the app.This ensured there was nothing missing early on that would cause issues later.

- Following creation of requirements.txt above, create a Procfile by typing "echo web: python app.py > Procfile" in the terminal

In Heroku:
- Create new app

- Choose an app name and your country and click create app

- Go to the deploy tab and choose "Connect to Github"

- Connect to project repository

- Go to settings > reveal config vars.

Copy in the key, value pairs to match those in env.py

- If requirements.txt and Procfile are committed, go to the deploy tab in Heroku and Enable Automatic Deployment

Deploy Branch. This will take a few minutes. Anything you push from Github now will automatically update in the Heroku App


### Testing

Genre would not upload genre_name from the add_work function. Appeared as 'null' or '1' in MongoDB

- Fixed by assigning value to select option in html, that matched the value selected.

Spotify button on carousel wasn't working. They would push to the next carousel page instead of redirecting to spotify.

- Fixed by redesigning the navigation for the carousel based on [this](https://stackoverflow.com/questions/46454964/how-can-i-put-the-prev-and-next-arrow-in-materialize-carousel) fix in StackOverflow

Nav buttons interfered with edit, delete or spotify buttons on mobile screen. If buttons were in the same latitude as the nav buttons, the slider center overrode them. 

- This was hidden for small screens and decorative arrows were put in place to indicate to the user to swipe.

Nested for-loops causing an issue in the carousel.
The aim was to get the composer name from the displayed work, match this to a composer name in the composers collection and get the image from that ID. If the composers loop was the inside loop, only the first carousel would display an image. Even if that composer name appeared again. If the composer loop was the outside loop and the work loop inside, the image would appear for the first carousel item, and any further instance of that composer in the carousel. However, this then blocked the search function from working at all, for any type of search request. The carousel would appear completely blank.

Fix attempts included:
-  using the [project](https://docs.mongodb.com/manual/tutorial/project-fields-from-query-results/) method to gather the information from the composer ID and create a separate image filed in the work document. The result of this was, upon creating a new work, instead of having an _id: ObjectId key, value, it had an "image": "composer_image" key, value. 


- FIX: Made use of the function to find whether a composer already existed and the above mentioned project method. Got the composer ID from this and could extract the composer image. This is then inserted into the work as an object. Additionally, I added this into the edit work part of app.py. This way, if a composer only receives an image after already being entered to the database via a work, the admin can just click edit and save on the work, and the image will update. In the meantime, there will be a placeholder of a Cello

# Lighthouse Reports

[HomePageLoggedIn](https://github.com/Shinners888/MS3MusicLibrary/blob/master/assets/lighthouseReports/HomeLoggedInLighthouse.png)

[HomePageLoggedOut](https://github.com/Shinners888/MS3MusicLibrary/blob/master/assets/lighthouseReports/HomeLoggedOutLighthouse.png)

[Browse](https://github.com/Shinners888/MS3MusicLibrary/blob/master/assets/lighthouseReports/BrowseLighthouse.png)

[Login](https://github.com/Shinners888/MS3MusicLibrary/blob/master/assets/lighthouseReports/LogInLighthouse.png)

[Register](https://github.com/Shinners888/MS3MusicLibrary/blob/master/assets/lighthouseReports/RegisterLighthouse.png)

[Add Work](https://github.com/Shinners888/MS3MusicLibrary/blob/master/assets/lighthouseReports/AddPieceLighthouse.png)

[Edit Work](https://github.com/Shinners888/MS3MusicLibrary/blob/master/assets/lighthouseReports/EditPieceLighthouse.png)

[Composers](https://github.com/Shinners888/MS3MusicLibrary/blob/master/assets/lighthouseReports/ComposersLighthouse.png)

[Add Composer]()

[Edit Composer](https://github.com/Shinners888/MS3MusicLibrary/blob/master/assets/lighthouseReports/EditComposerLighthouse.png)

# User Testing
User issues noted: 

Difficult to read with color scheme 

- Fix: changed to monochromatic colour scheme outside of buttons and nav/footer. 

Edit/delete buttons don't work on mobile if in same latitude as scroll buttons 

- Fix: as above in testing section

Delete button dropdown hidden behind delete button. 

- Fix: JQuery: "coverTrigger: False"

Browse unavailable to non users which causes an error

- Fix: removed browse from logged out navbar. 

Carousel keeps randomly collapsing, particularly on mobile.

- Carousel has been given a min height in CSS. This seems to be working. However, as this issue was intermittent, it is possible that this has not completely fixed the issue.

Edit and Delete functions not showing when search has been implemented. 

- Fix: in App.py "username" was added as a variable in @app.route("/search"). The edit and delete options are available based on the user that added that work. Therefore the username needed to still be read after the search.

Delete function dropdown not working for every composer/work. Often deleting incorrect ObjectId.

- Fix: The dropdown option only showed up for the final 4 works/composers and was not linked to the displayed work/composer. I cannot figure out why this was, but as the edit functions were working perfectly, I reformatted the delete option to match. That is, redirecting to a different page to ask if the user is sure, and adding a "POST" method to the delete confirmation button.

Flash messages stay unless you move to a different page or refresh. This is annoying and in the way.

- Fix: using a hint from [Stack Overflow](https://stackoverflow.com/questions/21949948/let-flash-messages-disappear-in-the-same-page-in-rails), a timer was set in my script.js file to remove the flash message after a second.

# Possible Future Features

An upvote downvote system, with a possibility to search by votes.

A comments section to discuss the pieces.


# Credits

Orchestra Image: [Arindam Mahanta on Unsplash](https://unsplash.com/photos/VEOk8qUl9DU)

Cello Image: [Dominic Scythe on Unsplash](https://unsplash.com/photos/lDKmtwvrZZs)

Unicorn Favicon: [Clipart Key](https://www.clipartkey.com/view/bhiwTb_illustration/)

# Acknowledgments

I'd like to thank my mentor Nishant Kumar for continuing support thoughout the project and the course as a whole. And my tester Eileen for her critical UX eye!