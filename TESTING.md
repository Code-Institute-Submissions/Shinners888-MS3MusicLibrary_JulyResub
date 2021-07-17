## Testing

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