## Testing Issues and Fixes

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


- FIX: Made use of the function to find whether a composer already existed and the above mentioned project method. This gets the object IDassociated with said composer name, and gets the related composer_image. This is then inserted into the work as an object. Additionally, I added this into the edit work part of app.py. This way, if a composer only receives an image after already being entered to the database via a work, the admin can just click edit and save on the work, and the image will update. In the meantime, there will be a placeholder of a Cello.


# User Testing

The user lands on the home page, logged out, with a brief description of the site's purpose. A direction to 'register' or 'log in', redirects to these respective pages.

Once logged in, the user lands on their home page with their own uploads displayed (or just a note saying 'this is all we could find for you', with a redirect prompt to the browse page).

In the browse page, the user can see what other people have uploaded to the site by browsing the carousel. There is a link to add their own pieces at the top of the page, and a search function to search by genre or composer, under the carousel. 

If they wish to add a piece and change their mind, there is a back to browse button at the top of the page. Otherwise they will be prompted to fill in the form (only the genre, composer and work name fields are necessary to proceed). The add button is a brightly coloured plus at the bottom of the screen.

Once their piece is added, they will return to the browse screen. There, they can see their piece as part of the library, and edit or delete details as necessary.

The user does not need to worry about adding an image for the composer. If the composer exists in the database with an image, that image will automatically populate the image div in the browse section. Otherwise, a placeholder image of a cello will be used.

If the choose to delete, they will be redirected to an 'are you sure' prompt, to ensure no accidental deleteions. The edit screen resembles the add screen with the information to edit already populated.

To search, they can input a composer or genre name in the search bar at the bottom. To undo the search, they can press, 'See All'.

If a user has uploaded a faulty link to listen to the piece, or no link at all, the spotify button will redirect to a custom 404 page in a new tab, with a prompt to open spotify and search for the piece, or return to the browse page.


# User Feedback and fixes

Two people tested the app for functionality and UX feedback.

User issues noted: 

Difficult to read with color scheme 

- Fix: changed to monochromatic colour scheme outside of buttons and nav/footer. 

Edit/delete buttons don't work on mobile if in same latitude as scroll buttons 

- Fix: as above in testing section

Browse unavailable to non users which causes an error

- Fix: removed browse from logged out navbar. 

Carousel keeps randomly collapsing, particularly on mobile.

- Carousel has been given a min height in CSS. This seems to be working. However, as this issue was intermittent, it is possible that this has not completely fixed the issue.

Edit and Delete functions not showing when search has been implemented. 

- Fix: in App.py "username" was added as a variable in `@app.route("/search")`. The edit and delete options are available based on the user that added that work. Therefore the username needed to still be read after the search.

Delete function dropdown not working for every composer/work. Often deleting incorrect ObjectId.

- Fix: The dropdown option only showed up for the final 4 works/composers and was not linked to the displayed work/composer. I cannot figure out why this was, but as the edit functions were working perfectly, I reformatted the delete option to match. That is, redirecting to a different page to ask if the user is sure, and adding a "POST" method to the delete confirmation button.

Flash messages stay unless you move to a different page or refresh. This is annoying and in the way.

- Fix: using a hint from [Stack Overflow](https://stackoverflow.com/questions/21949948/let-flash-messages-disappear-in-the-same-page-in-rails), a timer was set in my script.js file to remove the flash message after a second.

404 page is offputting.

- Fix: A custom 404 page using the flask error handler function.

If no string value for spotify url, the new tab opens at the start of the browse instead of the 404 page.

- Fix: changed button to only display if there is any value in the string associated with the URL in the database.

If piece is edited without composer image uploaded in the meantime, no image displays (this is because, now the composer exists in the database but still has no related image. But as the object now exists in the work part of the database, it is providing an empty string as the image information.)

- Fix: as for the spotify link issue, changed non-cello image to only display if there is any value in the string associated with the image in the database, instead of only displaying if the object doesn't exist.

Home page is cluttered and uninteresting

- Fix: A simplified home page with a brief site description under a hero image and a call to action button.

New visitor to the site should be able to see the library, to have an idea of what the site is about.

- Fix: User can browse the library, but not search or alter it in any way. A prompt above the library carousel tells them these functions are available when logged in. 

"Choose Genre" is not an obvious form field to add a work. This is causing confusion when trying to add a work.

- Fix:  This was a difficult one to fix technically. As it is a dropdown menu, by default there is always a 'selected' option. The only solution I could come up with, was to mark required fields with an asterisk and put a 'required field' key at the top of the form.

# Lighthouse Reports

[HomePageLoggedIn](https://github.com/Shinners888/MS3MusicLibrary/blob/master/assets/lighthouseReports/HomeLoggedInLighthouse.png)

[HomePageLoggedOut](https://github.com/Shinners888/MS3MusicLibrary/blob/master/assets/lighthouseReports/HomeLoggedOutLighthouse.png)

[Browse](https://github.com/Shinners888/MS3MusicLibrary/blob/master/assets/lighthouseReports/BrowseLighthouse.png)

[Login](https://github.com/Shinners888/MS3MusicLibrary/blob/master/assets/lighthouseReports/LogInLighthouse.png)

[Register](https://github.com/Shinners888/MS3MusicLibrary/blob/master/assets/lighthouseReports/RegisterLighthouse.png)

[Add Work](https://github.com/Shinners888/MS3MusicLibrary/blob/master/assets/lighthouseReports/AddPieceLighthouse.png)

[Edit Work](https://github.com/Shinners888/MS3MusicLibrary/blob/master/assets/lighthouseReports/EditPieceLighthouse.png)

[Composers](https://github.com/Shinners888/MS3MusicLibrary/blob/master/assets/lighthouseReports/ComposersLighthouse.png)

[Edit Composer](https://github.com/Shinners888/MS3MusicLibrary/blob/master/assets/lighthouseReports/EditComposerLighthouse.png)

