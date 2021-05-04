# Testing

[back to README.md file](https://github.com/Gmanprodev/Renovate-it/blob/master/README.md)

## Table of Content

1. [DevTools](#devtools)
2. [Manual Testing](#manual-testing)
3. [Automated Testing](#automated-testing)
    * [Code Validation](#code-validation)
    * [Browser Validation](#browser-validation)
    * [Lighthouse Audit](#lighthouse-audit)
4. [User testing](#user-testing)
    * [My Mentor](#my-mentor)
    * [Peer-code-review](#peer-code-review)
    * [User review](#user-review)



## DevTools

* Testing the responsiveness of the web app.
    * As an outcome I added a number of media queries in order to ensure the website is still user friendly on different screen sizes.
    * I used Materialize to ensure I have reactive columns on different screen sizes.
* Testing that the css is targeting the relevant html code.
    * As an outcome the webiste is responsive on all screen sizes.
* Console Debugging
    * As an outcome I was able to see whether my Javascript functions were being called and were executing properly by displaying a console.log value in my console.
    * I noted that a the Favicon wasn't displaying properly and was able to fix this by editing the url code.
    * I noted that when reducing the size of the screen in DevTools the page would randomly become significantly smaller than the device page. I couldn't recreate this probelm on any real devices and therefore believe it's just a problem with the DevTools responsive device displays.


## Manual Testing

* Home Page
   * Verify that the links in the navbar work and the navbar is fixed when on scroll.

   ![Navbar Links](https://github.com/Gmanprodev/Renovate-it/blob/master/documentation/testing/test_images/home_navbar_links.gif?raw=true) 


   * Verify that the links in the footer work and the social media icons wobble on `hover`.

   ![Footer Links](https://github.com/Gmanprodev/Renovate-it/blob/master/documentation/testing/test_images/home_footer_links.gif?raw=true) 


   * Verify that all the buttons work as they should.

   ![Buttons](https://github.com/Gmanprodev/Renovate-it/blob/master/documentation/testing/test_images/home_buttons.gif?raw=true)


   * Verify that the Home Page is responsive.

   ![Responsive Home Page](https://github.com/Gmanprodev/Renovate-it/blob/master/documentation/testing/test_images/home_page_responsive.gif?raw=true)


* Top Tips Page
   * Verify that the search function works.
   * Verify that the Read More buttons work.
   * Verify that the Back To Top button works.
   * Verify that the Top Tips page is responsive.

   ![Search Function](https://github.com/Gmanprodev/Renovate-it/blob/master/documentation/testing/test_images/tips_search.gif?raw=true)

   ![Read More Button](https://github.com/Gmanprodev/Renovate-it/blob/master/documentation/testing/test_images/read_more.gif?raw=true)

   ![Back To Top Button](https://github.com/Gmanprodev/Renovate-it/blob/master/documentation/testing/test_images/back_to_top.gif?raw=true)

   ![Responsive Top Tips Page](https://github.com/Gmanprodev/Renovate-it/blob/master/documentation/testing/test_images/tips_page_responsive.gif?raw=true)


* Sign Up Page
   * Verify that the requirements tooltips work.
   * Verify that the empty fields tooltips work.
   * Verify that the sign up button links to the Profile page, displays the username, displays flash message "signup successful" and text "you haven't added any tips yet".
   * Verify that the login button links to the Login page.
   * Verify that the sign up page is responsive.

   ![Requirements Tooltips](https://github.com/Gmanprodev/Renovate-it/blob/master/documentation/testing/test_images/requirements_tooltips.gif?raw=true)

   ![Empty Field Tooltip](https://github.com/Gmanprodev/Renovate-it/blob/master/documentation/testing/test_images/empty_field_tooltips.gif?raw=true)

   ![Sign Up Button](https://github.com/Gmanprodev/Renovate-it/blob/master/documentation/testing/test_images/signup_button.gif?raw=true)

   ![Login Button](https://github.com/Gmanprodev/Renovate-it/blob/master/documentation/testing/test_images/signup_login_button.gif?raw=true)

   ![Responsive Sign Up Page](https://github.com/Gmanprodev/Renovate-it/blob/master/documentation/testing/test_images/signup_page_responsive.gif?raw=true)


* Login Page
   * Verify that the empty fields tooltips work.
   * Verify that the Login button links to the Profile page, displays the username, displays flash message "welcome {username}".
   * Verify that the sign up button links to the Sign Up page.
   * Verify that the Login page is responsive.

   ![Empty Field Tooltip](https://github.com/Gmanprodev/Renovate-it/blob/master/documentation/testing/test_images/login_empty_fields.gif?raw=true)

   ![Login Button](https://github.com/Gmanprodev/Renovate-it/blob/master/documentation/testing/test_images/login_button.gif?raw=true)

   ![Sign Up Button](https://github.com/Gmanprodev/Renovate-it/blob/master/documentation/testing/test_images/login_signup_button.gif?raw=true)

   ![Responsive Login Page](https://github.com/Gmanprodev/Renovate-it/blob/master/documentation/testing/test_images/login_page_responsive.gif?raw=true)


* Profile Page
   * Verify that the when a user is logged in the page only displays tips added by that user.
   * Verify that the correct tip information is displaying and the Read More pop up card panel works.
   * Verify that the Edit button works.
   * Verify that the Delete button works.
   * Verify that the Back To Top button works.
   * Verify that the Profile page is responsive.

   ![User Tips Displayed](https://github.com/Gmanprodev/Renovate-it/blob/master/documentation/testing/test_images/profile_page.gif?raw=true)

   ![Read More Button](https://github.com/Gmanprodev/Renovate-it/blob/master/documentation/testing/test_images/profile_readmore_button.gif?raw=true)

   ![Edit Button](https://github.com/Gmanprodev/Renovate-it/blob/master/documentation/testing/test_images/profile_edit_button.gif?raw=true)

   ![Delete Button](https://github.com/Gmanprodev/Renovate-it/blob/master/documentation/testing/test_images/profile_delete_button.gif?raw=true)

   ![Back To Top Button](https://github.com/Gmanprodev/Renovate-it/blob/master/documentation/testing/test_images/profile_backtotop_button.gif?raw=true)

   ![Responsive Profile Page](https://github.com/Gmanprodev/Renovate-it/blob/master/documentation/testing/test_images/profile_page_responsive.gif?raw=true)


* Add Tips Page
   * Verify that the empty fields tooltips work.
   * Verify that the Add Tip button links to the public Top Tips page, displays the tip that was added and displays flash message "tip successfully added".
   * Verify that the Login page is responsive.

   ![Empty Field Tooltips](https://github.com/Gmanprodev/Renovate-it/blob/master/documentation/testing/test_images/addtip_empty_fields.gif?raw=true)

   ![Add Tip Button](https://github.com/Gmanprodev/Renovate-it/blob/master/documentation/testing/test_images/addtip_tip_page.gif?raw=true)

   ![Responsive Add Tips Page](https://github.com/Gmanprodev/Renovate-it/blob/master/documentation/testing/test_images/addtip_page_responsive.gif?raw=true)



#### Conclusion

   * I found that the Add Tips page doesn't work as it should whilst using the DevTools responsive window or smaller phone devices as the content continues to get smaller than the device window. I found that if you hard refresh the content then fills the window in the way that it should. I tested this on multiple real mobile devices and didn't encounter any problems.
   * I didn't find any further issues.



## Automated Testing

### Code Validation

   * I used the [W3C Markup Validation Service](https://validator.w3.org/) to validate my html code. The errors that exist are for Headers and for input fields, which I believe stem from using Jinja templating.

   ![index.html Validation](https://github.com/Gmanprodev/Renovate-it/blob/master/documentation/testing/test_images/index.html_test_validation.png?raw=true)

   ![tips.html Validation](https://github.com/Gmanprodev/Renovate-it/blob/master/documentation/testing/test_images/tips.html_test_validation.png?raw=true)
   
   ![signup.html Validation](https://github.com/Gmanprodev/Renovate-it/blob/master/documentation/testing/test_images/signup.html_test_validation.png?raw=true)

   ![profile.html Validation](https://github.com/Gmanprodev/Renovate-it/blob/master/documentation/testing/test_images/profile.html_test_validation.png?raw=true)

   ![login.html Validation](https://github.com/Gmanprodev/Renovate-it/blob/master/documentation/testing/test_images/login.html_test_validation.png?raw=true)

   ![edit_tips.html Validation](https://github.com/Gmanprodev/Renovate-it/blob/master/documentation/testing/test_images/edit_tips.html_test_validation.png?raw=true)

   ![add_tips.html Validation](https://github.com/Gmanprodev/Renovate-it/blob/master/documentation/testing/test_images/add_tips.html_test_validation.png?raw=true)


   * I used the [W3C CSS Validation Service](https://jigsaw.w3.org/) to validate my css code.

   ![CSS Validation](https://github.com/Gmanprodev/Renovate-it/blob/master/documentation/testing/test_images/css_test_validation.png?raw=true)


   * I used the [jshint](https://jshint.com/) website to validate my Javascript code.

   ![Javascript Validation](https://github.com/Gmanprodev/SerenAppy-Web-App/blob/master/documentation/testing/test-images/javascript_validation.jpg?raw=true)

   * I used the [Free Formatter](https://www.freeformatter.com/) to format my html, css and javascript code.


### Browser Validation

   * Chrome - works correctly.
   * Edge - works correctly.
   * Safari - works correctly.
   * Firefox - works correctly.
   * Opera - works correctly.

### Lighthouse Audit

   * Click [here](https://github.com/Gmanprodev/Renovate-it/blob/master/documentation/testing/test_images/lighthouse_report.png?raw=true) for the report.
   * No reccommendations in this report have been implemented in the first release but will be looked at in future releases.

#### Conclusion

   * The code validators highlighted these errors which I do not feel is neccessary to fix now as I believe they are due to the Jinja templating:
      * Using page headers.
      * Input field selections.
      * Showing that I have one unused variable (hideFunction), however I am actually using.
   * The web app works correctly in all five major browsers. I have tested on various devices and five different browsers.
   * The Lighthouse report scores are all really high apart from the performance. Thsi is due to the image hosting which I will rectify in the second release.



## User testing

### My Mentor

Akshat was very impressed with the web app and all of the documentation to go along with it. He liked the flow of the app how easy it was to navigate, he also mentioned that he could see the general public using the app in real life situations.

#### Suggested Improvements

* Remove text shadow from headers - implemented.
* Compress the size of the images and host them on a more up to date platform - will do on second release.

### Peer-Code-Review

The feedback was all very positive and everyone like the look and feel of the app.

#### Suggested Improvements:

   * To have username and password requirements on the sign up form - I implemented this on the first release.


### User Review

The web app was tested by Code Institute students and mentors, friends and family. The majority of testing carried on real devices were on Iphone and Samsung mobiles. The feedback was really positive, most people commenting on how they would continue to use the web app moving forward.


#### Conclusion

   * I am aware that I need to implement a greater line of security on the login details.
   * I will use an analytics platform on the next release, such as [Hotjar](https://www.hotjar.com/), to collect feedback form a larger range of users and use that data to implement changes related to the way users navigate the site.