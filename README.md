# Music Library Collaboration

## Data-Centric Development Project MS3 - Code Institute
![Display](assets/projectImages/screensimage.png)

MUSO - The Misanthropic Unicorns Symphony Orchestra presents "Bringing Classic Back"

A community built collection of favourites in the various classical/art music genres, to reignite a love of the music and repopularise it.

Features include:
- The ability to browse favourites uploaded by other users
- The ability to upload/edit/delete information about your own favourite pieces
- Admin can update/delete works and composers on a case by case basis
- The ability to search by composer or genre
- Discounts to performances by the symphony orchestra for registered users

[View the live project here](http://bringing-classic-back.herokuapp.com/home)

## Goals

To gather a community of people who like classical music, and recommend music to those who are new to the genre and may find it overwhelming. The symphony orchestra will incorporate new uploads to the site in performances, and discounts will be available to members of the community for those concerts.

## UX

This is for people who would like to listen to more classical music but don't know where to begin, or classical music lovers who want to share their favourite pieces. The orchestra notes what new additions there are, and if possible, will perform them at upcoming concerts.

It is a basic layout, easy to follow. The 'create' and 'update' pages are not available from the navbar and have 'go back' buttons easily visible at the top of the page.

#### Not logged in

 - You will land on the MUSO page which will tell you a little bit about the orchestra's site and direct you to register or login.

 - Register to create an account/log in.

#### Logged in

 - You will be taken immediately to the home page.

 - Browse what others have uploaded and follow the spotify link to listen. This will open in a new tab or the app, so the user can continue to browse while listening.

 - On the browse page is a prompt to add to the library. If the user knows a piece they think others might like, they can follow the link.

 - If the piece has been added by the current user, they have the option to update or delete the piece. The admin user also has these privileges, in case a user misspells or duplicates anything. The delete button contains a dropdown 

 - Below again is a search bar where users can search by composer or genre, with a button to clear search options. 

 #### Admin

 As well as editing or deleting works, an admin can edit composer information. If a new composer has been entered into the database, they will not yet have a related photo. The admin can upload a photo in the composers page. They can then click edit and save on any works by that composer to have the image displayed.

### Aesthetic

In honour of the unsociable unicorns after which the site is named, the navbar, buttons and footer are made up of bright, psychadelic colours traditionally associated with unicorns, around a dark monochrome website.



# CRUD

 - Create

Create a user name and password which will be stored in the database with a password hash for security.

Add your favourite piece with some prompted information, and a link to listen to the piece/work, to be displayed in the browse section carousel

 - Read

The Browse page reads and displays all infomation in the works collection, gathers descriptive information from the genres collection, and displays edit/delete buttons to the admin or the user who originally created the related work.

For the Admin, the composers page has a list of all composers in the database.

 - Update

Pieces can be edited by the admin, or the same user that created them. All 'work' information can be updated.

The admin can edit composer information, adding an image or correctine spelling issues which could lead to duplicates of a composer.

 - Delete

A user who created a work, or the admin can delete said work. They will be redirected to an 'are you sure you want to delete "X work"' page to ensure they do not accidentally delete anything. 

The admin can delete composers from the composer page. This is handy incase someone creates a duplicate by misspelling. Similarly they will be redirected to an 'are you sure you want to delete "X composer"' page. 



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

[Desktop Home/Sign In](https://github.com/Shinners888/MS3MusicLibrary/blob/master/assets/wireframes/MUSODesktop.jpg)

[Desktop Browse](https://github.com/Shinners888/MS3MusicLibrary/blob/master/assets/wireframes/MUSODesktop2.jpg)

[Desktop Search](https://github.com/Shinners888/MS3MusicLibrary/blob/master/assets/wireframes/MUSODesktop3.jpg)

[Desktop Register/ Login](https://github.com/Shinners888/MS3MusicLibrary/blob/master/assets/wireframes/MUSODesktop4.jpg)

[Mobile](https://github.com/Shinners888/MS3MusicLibrary/blob/master/assets/wireframes/MUSOMobile.jpg)

Please note these were early sketches and some elements do not represent the working website

# Data Diagram 

[Data Diagram - dbdiagram.io](https://dbdiagram.io/d/607a0563ef1b8f6b3dd5ac4e)

![Database layout image](assets/projectImages/DBMUSO.png)




# Creation and testing

## Database Creation

In MongoDB I created a music library database with four collections: 'genres', 'site_users', 'composers' and 'works'. 'Works' is the main collection and gathers data from each other collection. 

-------------
### 1. GENRES

Each genre has it's own information. To display them chronologically in the site, each has an Int ID depending on when that period of classical music occurs. This provides a reference of a time period when a user is uploading a new piece, for those who may not be sure of the classical music eras.

|  | | Genre | Chronological Genre Number (as genre_id) | Timeline |
| -- | -- | --- | ----------- | -----------------|
| Format | ObjectId | String | Int | String |
| Example | _id1 | Medieval | 1 | c.500 to 1400 |
| Example | _id2 | Renaissance | 2 | c.1400 to 1600 |
| Example | _id3 | Romantic | 5 | c.1800 to 1910 |

![Database layout image](assets/projectImages/genresdb.png)
--------------------

### 2. SITE USERS


This simply contains a username and password. The user that creates each work will be stored in the work collection so they can edit or delete what they have uploaded if they wish. The passwords are encrypted using the werkzeug password hash

| | User ID| Username | Password Hash |
| - | - | --- | ----------- |
| Format | ObjectId | String (created by user) | String |
| Example | _id | admin | scrambledPasswordHash | 

-------------------

### 3. COMPOSERS


Another simple collection. This contains just composer names and their corresponding images. When a user adds a new work, this collection is scanned to see if the user already exists. If it does, no new composer is created. If it exists and has a corresponding image, the ObjectId and composer image url will be imported into the created works object as a nested object. This will allow the composer image to display under any of their works.

| | Composer ID | Composer Name | Composer Image |
| - | --- | --- | ----------- |
| Format | ObjectId | String | URL String |
| Example | _id | Composer Name | Image URL | 

![Database layout image](assets/projectImages/composersdb.png)
---------

### 4. WORKS

The main collection of this project. The objects in this collection contain at a minimum, the composer name, the name of the work, the genre and the username of the object creator. There should also be a short description and a url to redirect the user to listen to the piece/s. The $text Index search function acts on this collection, querying the composer and genre fields.

|| Work ID | Genre | Composer | Work Name | Description | URL to listen | Added by User | Image |
| - | - | --- | ----------- | --- | --- | --- | --- | --- |
| Format | ObjectId | String (dropdown menu 'genres') | String | String | String | String URL | String from 'site_users' | Object (if Composer is in 'composers', get related cSymphony | Description | Spotify Link | Username from site_users |  {"ObjectId": _id for Beethoven in 'composers'(see above),                                          "composer_image": image from related composer_id,} |


![Database layout image](assets/projectImages/worksdb.png)
------------------

## Creation 
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

## Deployment

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


# Possible Future Features

An upvote downvote system, with a possibility to search by votes.

A comments section to discuss the pieces.

# Testing and User Testing

[Testing.md](https://github.com/Shinners888/MS3MusicLibrary/blob/master/TESTING.md)


# Credits

Orchestra Image: [Arindam Mahanta on Unsplash](https://unsplash.com/photos/VEOk8qUl9DU)

Cello Image: [Dominic Scythe on Unsplash](https://unsplash.com/photos/lDKmtwvrZZs)

Unicorn Favicon: [Clipart Key](https://www.clipartkey.com/view/bhiwTb_illustration/)

# Acknowledgments

I'd like to thank my mentor Nishant Kumar for continuing support thoughout the project and the course as a whole. And my tester Eileen for her critical UX eye!

