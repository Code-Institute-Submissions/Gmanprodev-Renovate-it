# Renovate.it - a renovation advice sharing web app.

A live demo can be found [here](https://renovate-it.herokuapp.com/)

![Desktop Demo](documentation/testing/test_images/renovate-it_responsive_image.png)

## Introduction

Renovate-it is a public information sharing web app which allows users to share their tips and experiences on renovation based topics. The main purpose of this web app is to give the general public access to a platform where they can search for advice before embarking on their own renovation project and to share their knowledge with others.

The web app can be viewed on Desktop, Tablet and Mobile devices. Click [here](https://renovate-it.herokuapp.com/) to view.


## Table of Content

1. [UX](#ux)
    * [Goals](#goals)
        * [SerenAppy goals](#serenappy-goals)
        * [Business goals](#business-goals)
        * [Customer goals](#customer-goals)
    * [User Stories](#user-stories)
        * [Local Health and Well-being Centre](#local-health-and-well-being-centre)
        * [The potential customer](#the-potential-customer)
         * [The UX designer](#the-ux-designer)
    * [Minimum Viable Product](#minimum-viable-product)
    * [Design](#design)
        * [Colors](#colors)
        * [Font](#font)
    * [Wireframes](#wireframes)
2. [Features](#features)
    * [Existing Features](#existing-features)
        * [Elements seen on the landing page](#elements-seen-on-the-landing-page)
        * [Elements seen on the 404 page](#elements-seen-on-the-404-page)
        * [Elements seen on all meditation pages](#elements-seen-on-all-meditation-pages)
    * [Features left to implement](#features-left-to-implement)
    * [Bugs and Fixes for Future Releases After Testing](#bugs-and-fixes-for-future-releases-after-testing)
3. [Technologies Used](#technologies-used)
4. [Testing](#testing)
5. [Deployment](#deployment)
    * [Hosting on GitHub Pages](#hosting-on-github-pages)
    * [How to run this project locally](#how-to-run-this-project-locally)
6. [Credits](#credits)
    * [Media](#media)
    * [Acknowledgements](#acknowledgements)
        * [Examples and Tutorials and Samples](#examples-and-tutorials-and-samples)
        * [Pages used for information](#pages-used-for-information)
        * [I received advice and encouragement from](#i-received-advice-and-encouragement-from)
7. [Disclaimer](#disclaimer)

## UX

### Goals

#### Renovate-it goals

The goal of this web app is to give the general public a platform to share their advice with others and also gain insights into other peoples experiences before embarking on their own renovation project.

**Target audience is:**

* People who are considering starting a renovation project.
* People who are currently engaged in a renovation project.
* People who have any renovation advice or experiences to share. 
* Any age group.
 

#### Business goals

* Interactive web-app.
* Fully functional web app.
* Intuitive design.
* Easy to navigate.
* To have as many registered users as possible.
* Daily increases in user numbers.
* Daily increases in tips being added.


#### Customer goals

* Easy to navigate.
* Easy to search for specific keywords.
* To easily locate information.
* Easy to add and edit information.

Both business and customer goals are addressed through user stories.


### User Stories

#### Renovate-it business

* As a business, I want my web app to display industrial textured colours.
* As a business, I want my web app to display simple to follow instructions.
* As a business, I want my web app to be responsive on all devices.
* As a business, I want a strong focus on mobile usability as most users will be veiwing the web app on mobile devices.
* As a business, I want my web app to be interactive and offer real time feedback.
* As a business, I want my web app to load quickly.
* As a business, I want my web app to use as little of the users data as possible.
* As a business, I want my web app to allow users to engage with us through different social media routes.
* As a business, I want my web app to display clear high resolution images.
* As a business, I want my web app to be usable for both left and right handed users.
* As a business, I want my web app to have a low risk of accidently clicking more than one button at once on smaller screens sizes.
* As a business, I want my web app to have a search function.
* As a business, I want my web app to have images that are easily recognisable and associated with renovation categories.

#### The potential customer

* As a customer, I want to know how the web app works and easy to follow instructions.
* As a customer, I want to know when I take the wrong action or something doesn't work.
* As a customer, I want the web app to be interactive with real time feedback.
* As a customer, I want the the web app to be easy to use and navigate, particularly on mobile devices.
* As a customer, I want to easily search for keywords relating to top tips.
* As a customer, I want to easily sign up for an account.
* As a customer, I want to know be able to view the tips I have added.
* As a customer, I want to be able to save the tips I'm interested in to view at a later date.
* As a customer, I want to be able to easily edit or delete tips I have added.

#### The UX designer

* As a UX designer, I want to track the user behaviour so that I can improve the user experience.
    * As a UX designer, I want to track the user behaviour so that I can identify the possible user confusion over navigating the web app.
* As a UX designer, I want to focus on the mobile design as most users will be using the web app on a mobile device.
* As a UX designer, I want the web app to be intercative and give real time feedback when a user executes an action.
  



### Minimum Viable Product

All the User Stories have been assessed against value and complexity on the chart below. Due to the relatively short time for the implementation of the web app, only the MVPs will be implemented in the first release of the web app.

[User Stories evaluation](documentation/mvp/user_stories.md)


**Explanation of the chart**

* The top area of the chart has been given the higher priority of implementation because it represents the most important features including:
  * Colour scheme and design.
  * Simple to follow instructions
  * Intercative and showing real time feedback to the user.
  * Easy to use audio and timer function controls.
  * Allowing users to interact with the supplier.
  * Responsive Web app.
* I have addressed all of the high value and high/low complexity in the first release.
* The features with high complexity and low value have been postponed for future updates/releases.

![chart](documentation/mvp/value_chart.jpg)


### Design

#### Colors

Following colours have been used:
* ![#26a69a](https://place-hold.it/20/26a69a/000000?text=+) #26a69a (Teal) 
* ![#1d8882](https://place-hold.it/20/1d8882/000000?text=+) #1d8882 (Turquoise) 
* ![#f7e7ce](https://place-hold.it/20/f7e7ce/000000?text=+) #f7e7ce (Gin Fizz) 
* ![#000000](https://place-hold.it/20/000000/000000?text=+) #000000 (Black)    
* ![#F44336](https://place-hold.it/20/F44336/000000?text=+) #F44336 (Red) 
* ![#9e9e9e](https://place-hold.it/20/9e9e9e/000000?text=+) #9e9e9e (Nobel) 
* ![#fff](https://place-hold.it/20/fff/000000?text=+) #fff (White) 

I used the Materialize Teal colour across every page, including the navbar, footer, majority of the text and buttons. The homepage icons and the all of the forms use the color Gin Fizz. The color white is used for the navbar and footer content and flash messages. The delete buttons, both on the profile page and the confirmation modal, are red to emphasise the warning. Turquoise is used for the icon text on the homepage and Nobel (grey) is used for the form text. The colour black is used for a small amount of text on the tips cards and the forms.

#### Font

The Fonts I used for this project are **Yellowtail** and **Montserrat** with the font weights: 
* 300
* 400
* 500

The [Yellowtail](https://fonts.google.com/specimen/Yellowtail?query=yellow) font was chosen for it's brush stroke appearance to link in with the renovation theme.

### Wireframes

I decided that it would be more helpful to have mockups than simple wireframes. The mockups were built in [figma](https://www.figma.com/). 

Link to the mockups can be found [here](https://www.figma.com/file/fkOYNcpb1G4whUHj7TskjS/Renovate.IT?node-id=0%3A1). The mockups were designed for the mobile first approach. I have produced a desktop, tablet and mobile mockup of the main pages.

If you are unable to access the mockup links above please see the mockup images [here](https://github.com/Gmanprodev/Renovate-it/tree/master/documentation/wireframes).

## Features

### Existing Features

#### Elements seen on the homepage

* **Layout and Style**
    * I wanted the web app to have an appearance that was associated with industrial colours and style. My aim was to have a lot of white and grey to reflect the industrial theme but also to layer on top of that a artistic brush stroke style to soften the look and feel. I kept all of the content in a square format to refelct the blocks that are used in building material.
    * I installed Favicon scripts so that when the web app loads the user sees the R. logo next to the Renovate-it name at the top of the browser tab.

* **Navigation bar**
    * Has a `fixed` position to ensure that the logo can always be seen by the user.
    * A Renovate-it logo in the left corner which also serves as a link to the homepage. This logo moves to the centre of the navbar on smaller screens and links to the Profile page when a user is logged in.
    * The page links are displayed on the right of the navbar. These turn into a burger menu on smaller screens and reveal a side navbar which displays from the right.

* **Footer**
    * Logo displayed on the left of the footer.
    * Logo is linked to the homepage. When a user is logged in it links to the Profile page.
    * Social media links are on the right of the footer - facebook, Twitter and Instagram (linked to relevant login page).
    * All footer text and icons are displayed in the colour white and wobble when on `hover` and clicked.

* **First Parallax**
    * Displays a background image of grey brickwork. On top of the image sits text with two buttons, a welcome message with a Sign Up button and a login message with a login button. Both buttons have waves effects when on `hover` and clicked.

* **Parallax Divider**
    * This divides the top and bottom parallax. It displays four icons on one row and explains the user process. The icons and text gradually move down into one column as the screen get smaller.

* **Second Parallax**
    * Displays a background image of a modern kitchen. On top of the image sits text with a button linking to the public Top Tips page. The button has wave effects when on `hover` and clicked.

#### Elements seen on the 404 and 500 pages

* **Layout and Style**
    * A white page with both a header and button reflecting the same styling.
    * The button links to the Homepage.
    * The button has wave effects when on `hover` and clicked.

#### Elements seen on the Top Tips page

* **Search Bar**
    * A search bar displays at the top of the page. The user can enter any words and the function will search through all the tips stored in the database and return the results. If there are no results the user will see a flash message informing them that no results were found. Below the search bar there are two buttons, search and reset, the search button when clicked starts the function and the reset button restores the Top Tips page and displays all of the tips. Both buttons have waves effects when on `hover` and clicked.

* **Card Panels**
    * Each of the tips are displayed inside a card panel, each card panel has an image which is associated with the tip category and below the image the category, username, location and tip are displayed as text. The Top Tip info is line clamped at one line so that the card panels all remain the same height. At the bottom of each card panel there is a Read More button which, when clicked, displays a secondary pop up card with the full Top Tip text. The button has wave effects when on `hover` and clicked.

* **Back To The Top Button**
    * The button is placed at the bottom of the page to enable the user to return to the top of the page without manually scrolling. I haven't included any pagination because I wanted it to be an infinity scrolling page. The button is Gin Fizz colour and changes to White when on `hover` and clicked.

### Elements seen on the Login page

* **Login Form**
    * The form has a background colour of Gin Fizz, a username and password field and a Login button. The fields will display tooltips advising the user of any errors and the underline for each field will turn red if incorrect and turn green if correct. The Login button has a number of actions, depending on the users input, if the fields are blank "Please fill in", if the input is incorrect "incorrect password and/or username" and if all the inputs are correct it will take the user to their Profile page with a flash message "Welcome {username}. There is also a Sign Up button below the form in case the user isn't registered.

### Elements seen on the Signup page

* **Signup Form**
    * The form has a background colour of Gin Fizz, a username and password field and a Signup button. Below each field there is the text "*requirements", if the user `hover` or clicks on this text it will display a tooltip with the requirements for each field. The user will also see tooltips advising the them of any errors and the underline for each field will turn red if incorrect and turn green if correct. The Signup button has a number of actions, depending on the users input, if the fields are blank "Please fill in" and if all the inputs are correct it will take the user to their Profile page with a flash message "Welcome {username}.. There is also a Login button below the form in case the user is already registered.

### Elements seen on the Profile page

* **Tips added by user**
    * This page displays only the tips that have been added by the user that is logged in, at the bottom of each card panel is a Edit and Delete button. The Edit button links to the Edit page which has the same format as the Add Tips page, giving the user the ability to change any of the information held in the database. The delete button opens a modal which gives the user a secondary confirmation to delete or a close button to stop the delete action.
    
* **Back To The Top Button**
    * The button is placed at the bottom of the page to enable the user to return to the top of the page without manually scrolling. I haven't included any pagination because I wanted it to be an infinity scrolling page. The button is Gin Fizz colour and changes to White when on `hover` and clicked.

### Elements seen on the Edit page

* **Edit Form**
    * The form has a background colour of Gin Fizz, category, location and top tip fields are pre filled with the users original information which can be edited by the logged in user. Below the fields is a Save Changes button, upon clicking the button the changes are saved to the database and the user is redirected to their Profile page with a flash message "Tip Updated".

### Elements seen on the Add Tips page

* **Add Tip Form**
    * The form has a background colour of Gin Fizz with category, location and top tip fields. The category field is a dropdown selection and both the location and top tip fields are text. Below the fields is a Add Tip button, upon clicking the button the information is saved to the database and the user is redirected to their Profile page with a flash message "Tip Successfully Added".

### Logout Function

* **Logout**
    * Upon clicking the Logout link in the navbar the user is redirected to the Login page with a flash message "you are logged out".

### Features left to implement

* **Admin Account** - To allow an admin user to access all of the databse information for editing and deleting purposes.
* **Change Password** - To allow users to change their password.
* **Save Tips** - To enable users to save tips to a project list when logged in so that they can access particular tips rather than searching for them again.
* **Tracking User Behaviour** - Use an analytics tool such as [Hotjar](https://www.hotjar.com/) to view user behaviour.
* **Most and Least Visited Pages on the Site** - Use an analytics tool such as [Hotjar](https://www.hotjar.com/) to understand where the traffic is going on the site.


### Bugs and Fixes for Future Releases After Testing
 
* **Image Size and Hosting** - The Lighthouse Audit Report will show better performance.
* **Social Media Links in Footer** - The social media icons are linked to the correct pages, however these are currently generic login pages. These will direct you to the company specific pages in future releases. They could also do with more space between the icons.

## Technologies Used

### Languages

* HTML - base language for this project.
* CSS - used for styling the HTML code.
* JavaScript/Jquery - used to make the web app interactive.
* Python (flask) - Framework.
* Jinja - templating.

### Database

* MongoDB - document key vaue pairs database.

### Libraries

* [Materialize](https://materializecss.com/getting-started.html) - used for responsive grid system, styling and modals.
* [JQuery](https://jquery.com/) - were used in conjunction with the Materialize library.
* [FontAwseome](https://fontawesome.com/) - used for all icons on the site.
* [Google Fonts](https://fonts.google.com/) - used for the Pacifico fonts.
* [Hover.css](https://ianlunn.github.io/Hover/) - used to animate the social media icons.
* [Unsplash](https://unsplash.com/) - used for all images.
* [Favicon.io](https://favicon.io/) - used for creating a favicon.

### Tools

* [Gitpod](https://www.gitpod.io) - used as IDE for this project.
* [Git](https://git-scm.com/) - used for version control.
* [Github](https://github.com/) - used to host repository.
* [Heroku](https://www.heroku.com/) - used to deploy.
* [Figma](https://www.figma.com/) - used for creation of mockups.
* [Am I Responsive](http://ami.responsivedesign.is/) - used for testing purposes as well as creating the image to display the web pages on different devices.
* [Google Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools) - used for testing and debugging.
* [PageSpeed insights](https://developers.google.com/speed/pagespeed/insights/) - used for testing the loading speed of the site.
* [Lighthouse Audit](https://developers.google.com/web/tools/lighthouse) - used to test whether the site meets the standards expected.
* [w3 html validator](https://validator.w3.org/) - used to test and validate my html code.
* [w3 css validator](https://jigsaw.w3.org/) - used to test and validate my css code.
* [Free Formatter](https://www.freeformatter.com/) - used to format my html, css and javascript code.
* [Browserstack](https://www.browserstack.com/) - used to test my site on different browsers.
* [Color Scheme Designer](http://colorschemedesigner.com/) - used to test colour combinations.
* [jshint](https://jshint.com/) - used to validate my Javascript code.



## Testing

Testing information can be found [here](documentation/testing/testing.md).


## Deployment

This web app was developed in Gitpod and pushed to the remote repository, GitHub and Heroku. The live page is deployed on Heroku. 

### How to clone this project:

* Log In into GitHub and access the repository.
* Click on the "Code" button (near the green "GitPod" one).
* Copy the URL.
* Open Gitbash from your computer.
* Type "git clone", paste the URL and press "enter".

### How to run the code locally:
* Create the required databases. You can do this by accessing Mongo DB. Create a cluster and then create the required collections (as seen in Use of Database). Don't forget to add the value to every key.
* Go to GitPod and install the requirements by typing the following in the terminal: pip3 install -r requirements.txt.
* Add the secret environment variables: create a .gitignore file; then create a env.py file and add it to the .gitignore . In the env.py add the following environment variables:
* At this point you can go back to the terminal and type "python3 app.py" to open the preview of the website.

### How to deploy this project - with Heroku:
* From the terminal: type "pip3 freeze --local > requirements.txt" to update the list of requirements needed to run this application.
* Type " echo web: python app.py > Procfile " to create the Procfile.
* Go to Heroku and if you don't have it create an account.
* Click on "New" on the top right corner and select "Create new app". In the modal, add a name and select the region, then click "Create app".
* The way I decided to use is via GitHub. To select this method click on "connect to GitHub" and select the right repository. Click on connect.
* Before selecting "Enable Automatic Deploys" go to the setting!
* The environment variables are hidden so we will have to write them manually. Do do this, from settings click on "Reveal config vars" and insert your variables.
* Go back to the terminal in GitPod and push both the requirements.txt and the Procfile one at the time, with their respective commits.
* We can now go back to Heroku and click on "Enable Automatic Deployment". Next click on "Deploy Branch".
* The website is now successfully deployed and you can view it by clicking on "Open app".

**Used commands during deployment:**
* `git add .` - to add the files to the staging area.
* `git commit -m "text message here"` - to commit the files.
* `git push` - to push to origin master branch on to GitHub.
* `git status` - to see the current status of the files.

### Hosting on GitHub Pages
* Log into GitHub.
* From the list of repositories choose [Renovate-it](https://github.com/Gmanprodev/Renovate-it).
* Go to settings.
* Scroll down to GitHub Pages section.
* Select as a source **master branch**.
* The page is now automatically refreshed and the project is deployed.
* To access the project scroll down again to GitHub Pages section and click on the provided link.

For more detailed information regarding deployment to GitHub Pages click [here](https://pages.github.com/).

### How to run this project locally

**Clone this project from GitHub:**

* Go to [Renovate-it](https://github.com/Gmanprodev/Renovate-it) GitHub repository.
* Click on "Clone or download" green button.
* Copy the URL to the repository.
* Open the terminal in your IDE.
* Choose the working directory where you would like to have the cloned repository.
* Type git clone, and add the URL you copied from Github.
* Press Enter and your local clone will be created.

For more information regarding cloning of a repository click [here](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository).

## Credits

### Content

All content in this web app was written by me.

### Media

**All Images & Audio**
   * All of the images used in the web app are free and do not require permission to use.



### Acknowledgements

#### Examples and Tutorials and Samples

* [Code Institute](https://codeinstitute.net/) - I used the Task Manager mini project to build my code foundations and then completely cistomised it thereafter.
   

#### Pages used for information

* [W3schools](https://www.w3schools.com/)
* [W3C](https://www.w3.org/)
* [Stack overflow](https://stackoverflow.com/)
* [CSS-Tricks](https://css-tricks.com/)
* [MDN web docs](https://developer.mozilla.org/)
* [Codepen](https://codepen.io/)

#### I received advice and encouragement from
   * Akshat (my mentor)
   * Tutor Support (CI online webchat)
   * SuzanneNL (fellow student)

## Disclaimer

**This web page was created for educational purposes only.** 
