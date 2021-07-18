# Music Library Collaborative

## Data-Centric Development Project MS3 - Code Institute
![Display](assets/projectImages/screensimage1.png)

MUSO - The Misanthropic Unicorns Symphony Orchestra's Music Library Collaborative

A community built collection of favourite works in the various classical/art music genres, to repopularise classical music in the 21st Century.

Features include:
- The ability to browse favourites uploaded by other users
- The ability to upload/edit/delete information about your own favourite pieces
- Admin can update/delete works and composers on a case by case basis
- The ability to search by composer or genre
- Discounts to performances by the symphony orchestra for registered users

[View the live project here](http://bringing-classic-back.herokuapp.com/home)

## Goals

To provide a place for a community of people who like classical music, and recommend music to those who are new to the genre and may find it overwhelming. The symphony orchestra will make a point of performing user favourites at their concerts, and discounts will be available to members of the community for those concerts.

## User Stories

- I am a fan of classical music and am looking to find new suggestions for good pieces to hear.

- I am new to classical music and trying to find more pieces to listen to, to appreciate the genre.

- I am a fan of the orchestra and would like to bring my favourite pieces to their attention, with the intention that they will someday perform these pieces.

I want a simple site with a library of pieces to listen to. I would like the option to browse the library, without needing to register or log in. I understand that this has limited features and if I wish to avail of more features, be able to engage with the site, or get discounts to the orchestra concerts, I need to register and log in.

# UX
### Design

In honour of the unsociable unicorns after which the site is named, the navbar, buttons and footer are made up of bright, psychadelic colours traditionally associated with unicorns, around a dark monochrome website.

### Not logged in

 - You will land on the MUSO page which will tell you a little bit about the orchestra's site and direct you to register or login. There is a call to action to browse the library. Here you can see what has been uploaded, but you cannot add to it or search. For this, you must be logged in.

 - Register to create an account/log in.

### Logged in

 - You will be taken immediately to your 'My Music' page, where your own uploads are listed. There is a prompt to go to the full library to browse.

 - Browse what others have uploaded and follow the spotify link to listen. These will open in a new tab, so the user can continue to browse while listening. If the link is faulty, an error page will direct you to return to browse, or open spotify and search for yourself.

 - On the browse page is a prompt to add to the library. If the user knows a piece they think others might like, they can follow the link.

 - If the piece has been added by the current user, they have the option to update or delete the piece from the library carousel. The admin user also has these privileges, in case a user misspells or duplicates anything. The delete button redirects to a confirmation page, to ensure they intended to delete.

 - Below again is a search bar where users can search by composer or genre, with a button - "see all" - to clear search options. 

 - There is a log out button on the navbar, this prompts a confirmation of intent in case it was pressed accidentally.

 - There is a navbar available at all times to the user, and most pages have a 'return to browse' button, as 'Browse' is the feature page of the site.

 #### Admin

 - As well as editing or deleting works, an admin can edit composer information. If a new composer has been entered into the database, they will not yet have a related photo. The admin can upload a photo in the composers page. They can then click edit-and-save for any works by the respective composer, in order to have the new image displayed.


[User Testing](https://github.com/Shinners888/MS3MusicLibrary/blob/master/TESTING.md)

# Technologies and Resources Used

## Technologies 
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

## Resources

 - Code Institute mini project lessons
 - Slack
 - StackOverflow
 - [MongoDB Documentation](https://docs.mongodb.com/manual/)
 - [Werkzeug Password Hashing](https://werkzeug.palletsprojects.com/en/1.0.x/utils/#general-helpers)
 - [Unsplash](https://unsplash.com/)
 - [Favicon.io](https://favicon.io/)
 - [Clipart Key](https://www.clipartkey.com/view/bhiwTb_illustration/)
 - [Spotify](https://open.spotify.com/)
 - [Am I Responsive](http://ami.responsivedesign.is/)
 - [Python Validator](http://pep8online.com/)
 - [Nu Validator](https://validator.w3.org/nu/?doc=http%3A%2F%2Fbringing-classic-back.herokuapp.com%2Fhome)


# Wireframes

[Desktop Home/Sign In](https://github.com/Shinners888/MS3MusicLibrary/blob/master/assets/wireframes/MUSODesktop.jpg)

[Desktop Browse](https://github.com/Shinners888/MS3MusicLibrary/blob/master/assets/wireframes/MUSODesktop2.jpg)

[Desktop Search](https://github.com/Shinners888/MS3MusicLibrary/blob/master/assets/wireframes/MUSODesktop3.jpg)

[Desktop Register/ Login](https://github.com/Shinners888/MS3MusicLibrary/blob/master/assets/wireframes/MUSODesktop4.jpg)

[Mobile](https://github.com/Shinners888/MS3MusicLibrary/blob/master/assets/wireframes/MUSOMobile.jpg)

Please note these were early sketches and some elements do not represent the working website

# CRUD, Data Diagram and Database

## Crud 

 - Create

Create a user name and password which will be stored in the database with a password hash for security.

Add your favourite piece with some prompted information (a star denotes the required fields), and a link to listen to the piece/work, to be displayed in the browsing carousel

 - Read

The Browse page reads and displays all infomation in the works collection, gathers descriptive information from the genres collection, images from the composer collection, and displays edit/delete buttons to the admin or the user who originally created the related work.

For the Admin, the composers page has a list of all composers in the database.

 - Update

Pieces can be edited by the admin, or the same user that created them. All 'works' information can be updated.

The admin can edit composer information, adding an image or correcting spelling issues, which could lead to duplicates of a composer.

 - Delete

A user who created a work, or the admin, can delete said work. They will be redirected to an 'are you sure you want to delete "X work"' page to ensure they do not accidentally delete anything. 

The admin can delete composers from the composer page. This is handy in case someone creates a duplicate by misspelling. Similarly they will be redirected to an 'are you sure you want to delete "X composer"' page. 


## Data Diagram 

[Data Diagram - dbdiagram.io](https://dbdiagram.io/d/607a0563ef1b8f6b3dd5ac4e)

![Database layout image](assets/projectImages/DBMUSO.png)



## Database Creation

In MongoDB I created a music library database with four collections: 'genres', 'site_users', 'composers' and 'works'. 'Works' is the main collection and gathers data from all other collections. 

-------------
### 1. GENRES

Each genre has its own information. To display them chronologically in the site, each has an Int ID depending on when that period of classical music occurs. This provides a reference of a time period when a user is uploading a new piece, for those who may not be sure of the classical music eras.

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

# Application Creation 
1. Initial Commits: Imported flask, flask_pymongo, dnspython, and os, linked to Heroku and MongoDB, tested that an HTML page would display print from app.py. Created a base HTML page.

2. Added Registration and login pages linked to site_users collection in MongoDB. Styled base html, added flash messages and a method to display them (in base.html) Checked all git push commands deployed to Heroku.

3. Added logout function to pop user from system. Checked application system cookies and verified that session user was gone after logout.

4. Added browse page with carousel. The carousel iterates through the works in the database and diplays each, one after the other, featuring elements of each work.

5. Created the add_work function. This gives the user a selection of genres with their rough timelines for reference. The rest of the data is filled in by the user.

6. Removed autocomplete from some aspects of the form as it was not aesthetically pleasing, particularly in the login section. It is helpful in adding a composer or searching.

7. Altered JS for the carousel as clicking any buttons on it were overridden by the carousels inbuilt turn function.

8. Created index text search via python3 - from app import mongo. This allows the user to search the works collection for a composer name or genre.

9. Added functional edit and delete functions, only available to the user that added that work_id, or to the admin.

10. Styled and changed general layout of site. Discarded pointless pages, added a modal to confirm logout request, and dropdown to confirm delete request.

11. Added functionality within add and edit work functions, to read the composer name, find the composers unique ID, get the composer image from said ID if it already exists, and populate an image object with the _id and composer image fields.

12. Added method to delete composer. It is possible that duplicates would happen due to spelling errors. The admin can update incorrect spelling in the work and remove the incorrect/duplicate composers.

13. Tidied code and commented.

14. Included username as a variable in the search function in app.py. As the edit and delete buttons are displayed based on the username of the person browsing, these buttons were not showing up when the search function was implemented.

15. Set a minimum height for the carousel as it was collapsing intermittently, blocking information and buttons fron the users view.

16. Changed delete button from a dropdown menu to a 'redirect to confirm' page.

17. Changed home page for both logged out and logged in to be more aesthetically pleasing, with a CTA button to browse the library.

18. Changed session user 'home' page to a 'my music' page, displaying what said user has uploaded to the library.

19. Added flash message in case there are no search results.

20. Set debug to False

# Deployment
## Git Deployment

- Create env.py file with the following fields:

import os

os.environ.setdefault("IP", "0.0.0.0")<br>
os.environ.setdefault("PORT", "5000")<br>
os.environ.setdefault("SECRET_KEY", "secret_key_here")<br>
os.environ.setdefault("MONGO_URI", "mongodb+srv://shinners:pword@cluster0.hsdbq.mongodb.net/music_library?retryWrites=true&w=majority")<br>
os.environ.setdefault("MONGO_DBNAME", "music_library")

- push 'env.py' to gitignore with `__pycache__/`

- Type `pip3 freeze --local > requirements.txt` in the terminal so Heroku, (deployment instructions below) will know what is required to run the app

- Use pip3 to install flask, flask_pymongo and dnspython

- The app can now be run locally by typing python3 app.py in the terminal


## Heroku Deployment

Deployment was executed early on, with commits and pushes updating the app. This ensured there was nothing missing early on that would cause issues later.

To deploy the app to heroku:

- Ensure `requirements.txt` was created as outlined above.

- Following creation of `requirements.txt` above, create a Procfile by typing `echo web: python app.py > Procfile` in the terminal

- Add and commit the requirements and Procfile, and push to GitHub.

- Create a new app on the [Heroku website](https://dashboard.heroku.com/apps) by clicking the "New" button in your dashboard. Name your app and set your region.

- From the heroku dashboard in your new app, click on "Deploy" then "Deployment method" and pick GitHub.

- Type the name of the Github Repository that the app is being built in, and confirm.

- In the heroku dashboard for the application, click on "Settings" > "Reveal Config Vars".

- Set the config vars to match those in env.py above:

- To get your MONGO_URI read the MongoDB Atlas documentation [here](https://docs.atlas.mongodb.com/)

- In the heroku dashboard, click "Deploy".

- In the "Manual Deployment" section of this page, select master branch and then click "Deploy Branch".

- This may take some time, but the site is now successfully deployed. Any further changes commited to the repository will update in Heroku.

# Fork and Clone
Fork

- Login or Sign Up to [GitHub](https://github.com/).
- On GitHub, go to [MS3 Music Library](https://github.com/Shinners888/MS3MusicLibrary).
- On the top right of the screen, click "Fork".
- Create an env.py file with your own values, as above
- in the terminal, type:
- - `pip3 install flask`
- - `pip3 install flask_pymongo`
- - `pip3 install dnspython`
- - `install -r requirements.txt`
- - `python3 app.py` (to run project locally, your version may require a different command)

Cloning

- Login or Sign Up to [GitHub](https://github.com/).
- On GitHub, go to [MS3 Music Library](https://github.com/Shinners888/MS3MusicLibrary).
- Beside the green gitpod button, click "Code".
- Here you can copy the link to clone using HTTPS.
- Open Git Bash.
- Change the current working directory to the new location, where you want the cloned directory to be.
- Type `git clone`, and then paste the HTTPS URL from above
- Press Enter, and your local clone will be created.
- As in the fork steps, create the env.py file and install all requirements etc.
Check [Github Docs](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository-from-github/cloning-a-repository#cloning-a-repository-to-github-desktop) for further information.


# Possible Future Features

An upvote downvote system, with a possibility to search by popularity.

A comments section to discuss the pieces.

# Testing and User Testing

[Testing.md](https://github.com/Shinners888/MS3MusicLibrary/blob/master/TESTING.md)


# Credits

Orchestra Image: [Arindam Mahanta on Unsplash](https://unsplash.com/photos/VEOk8qUl9DU)

Silhouette Image [Photo by Alberto Bigoni on Unsplash](https://unsplash.com/photos/AAnoZVR6vm8)

Cello Image: [Dominic Scythe on Unsplash](https://unsplash.com/photos/lDKmtwvrZZs)

Unicorn Favicon: [Clipart Key](https://www.clipartkey.com/view/bhiwTb_illustration/)

README based on [CI Sample README](https://github.com/Code-Institute-Solutions/SampleREADME)

# Acknowledgments

I would like to thank my mentor Nishant Kumar for his continued support thoughout the project and the course as a whole. I would also like to thank Declan and Eileen, for testing the app for functionality and UX.

