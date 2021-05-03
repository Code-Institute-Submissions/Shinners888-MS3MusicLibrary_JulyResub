# Music Library Collaboration

## Data-Centric Development Project MS3 - Code Institute

MUSO - The Misanthropic Unicorns Symphony Orchestra presents "Bringing Classic Back"

A community built collection of favourites in the various classical/art music genres, to reignite a love of the music.

Features include:
- The ability to browse favourites uploaded by other users
- The ability to upload information about your own favourite pieces
- A way to inform the admin that there are duplicates/incorrect information
- Admin can update/delete on a case by case basis
- The ability to search by composer, genre, piece etc...
- Discounts to performances by the symphony orchestra for registered users

## Goals

To build a community of people who like classical music and recommend music to those who are new to the genre and may find it overwhelming. The symphony orchestra will let the most popular pieces on the website dictate what is performed every few months and discounts will be available to members of the community for those concerts.

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

# CRUD

 - Create

Create a user name and password which will be stored in the database with a password hash for security
Add your favourite piece with information and a link, to be displayed in the browse section

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
 - Javascript/JQuery
 - Python
 - Flask
 - MongoDB (flask_pymongo)
 - Materialize 
 - Font Awesome
 - Google Fonts
 - VSCode editor for Github

This Project was deployed using Heroku

# Resources

 - Code Institute mini project lessons
 - Slack
 - StackOverflow
 - MongoDB Documentation
 - [Werkzeug Password Hashing](https://werkzeug.palletsprojects.com/en/1.0.x/utils/#general-helpers)
 - [Unsplash](https://unsplash.com/)
 - [Favicon.io](https://favicon.io/)
 - [Clipart Key](https://www.clipartkey.com/view/bhiwTb_illustration/)
 - Spotify

# Notes

added text search - python3 - mongo app - genre_text_composer_text

Resources


# Creation and testing

### Creation 
1. Initial Commits: Imported flask, flask_pymongo, dnspython, and os, linked to Heroku and MongoDB, tested that an HTML page would display print from app.py. Created a base HTML page.

2. Added Registration and login pages linked to site_users collection in MongoDB. Styled base html, added flash messages and a method to display them (in base.html)

3. Added logout function to pop user from system. Checked application system cookies and verified that session user was gone after logout.

4. Added browse page with carousel. The carousel iterates through the works in the database and diplays each, one after the other, featuring elements of each work.

5. Created the add_work function. This gives the user a selection of genres with their rough timelines for reference. The rest of the data is filled in themselves.

6. Removed autocomplete from some aspects of the form as it was not aesthetically pleasant, particularly in the login section. It is helpful in adding a composer or searching.

7. Altered JS for the carousel as clicking any buttons on it were overridden by the carousels inbuilt turn function.

8. Added index text search via python3 - mongo app. Will search the works collection for a composer name or genre

9. Added and wired up edit and delete functions, only available to the user that added that work_id, or to the admin

10. Styled and changed general layout of site. Discarded pointless pages, added a modal to confirm logout request, and dropdown to confirm delete request.

11. Tidied code

### Testing

- Genre would not upload genre name from the add_work function. Appeared as 'null' or '1' in MongoDB

Fixed by assigning value to select option that matched the value selected.

- Spotify button on carousel wasn't working. They would push to the next carousel page instead of redirecting to spotify.

Fixed by redesigning the navigation for the carousel based on [this](https://stackoverflow.com/questions/46454964/how-can-i-put-the-prev-and-next-arrow-in-materialize-carousel) fix in StackOverflow

- Nav buttons interfered with edit, delete or spotify buttons on mobile screen. If buttons were in the same latitude as the nav buttons, the slider center overrode them. 

This was removed for small screens and decorative arrows were put in place to indicate to the user to swipe.

- Nested for-loops causing an issue in the carousel.
The aim was to get the composer name from the displayed work, match this to a composer name in the composers collection and get the image from that ID. If the composers loop was the inside loop, only the first carousel would display an image. Even if that composer name appeared again. If the composer loop was the outside loop and the work loop inside, the image would appear for the first carousel item, and any further instance of that composer in the carousel. However, this then blocked the search function from working at all, for any type of search request. The carousel would appear completely blank.

Fix attempts included:
-  using the [project](https://docs.mongodb.com/manual/tutorial/project-fields-from-query-results/) method to gather the information from the composer ID and create a separate image filed in the work document. The result of this was, upon creating a new work, instead of having an _id: ObjectId key, value, it had an "image": "composer_image" key, value. 

- trying to create a composer object within the work object, populated from the composers collection. This showed the most promise but as yet, I have not successfully implemented this.


# User Testing
User issues noted: 

- Difficult to read with color scheme 

Fix: changed to monochromatic colour scheme outside of buttons and nav/footer. 

- Edit/delete buttons don't work on mobile if in same latitude as scroll buttons 

Fix: as above in testing section

- Delete button dropdown hidden behind delete button. 

Fix: JQuery: "coverTrigger: False"

- Browse unavailable to non users which causes an error

Fix: removed browse from logged out navbar. 




# Credits

Orchestra Image: [Arindam Mahanta on Unsplash](https://unsplash.com/photos/VEOk8qUl9DU)
Cello Image: [Dominic Scythe on Unsplash](https://unsplash.com/photos/lDKmtwvrZZs)
Unicorn Favicon: [Clipart Key](https://www.clipartkey.com/view/bhiwTb_illustration/)

# Acknowledgments

I'd like to thank my mentor Nishant Kumar for continuing support thoughout the project and the course as a whole. And my tester Eileen for her critical UX eye!