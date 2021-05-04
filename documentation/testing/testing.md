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

   ![Back To Top Button]()



   * Verify that all the function buttons change background colour and text colour on `hover` and when clicked.

   ![Function Buttons](https://github.com/Gmanprodev/SerenAppy-Web-App/blob/master/documentation/testing/test-images/function_buttons.gif?raw=true)


   * Verify that by clicking the Play button the timer starts counting down and the audio starts playing, also the text on the button changes to Pause.
   * Verify that by clicking the Pause button the timer and the audio pauses, also the text on the button changes to Play.

   ![Play/Pause Button](https://github.com/Gmanprodev/SerenAppy-Web-App/blob/master/documentation/testing/test-images/play-pause_button.gif?raw=true)


   * Verify that the Reset button resets the audio and the timer to the original time, also that the Play/Pause button displays the text Play.

   ![Reset Button](https://github.com/Gmanprodev/SerenAppy-Web-App/blob/master/documentation/testing/test-images/reset_button.gif?raw=true)


   * Verify that the Main Menu button takes the user back to the landing page.

   ![Main Menu Button](https://github.com/Gmanprodev/SerenAppy-Web-App/blob/master/documentation/testing/test-images/main-menu_button.gif?raw=true)


   * Verify that when the timer gets to zero the timer resets to the original starting time, the Play/Pause button text displays Play, the audio is reset and a bleep sound plays to signify the end of the meditation session.

   ![Timer Ends](https://github.com/Gmanprodev/SerenAppy-Web-App/blob/master/documentation/testing/test-images/timer_ends.gif?raw=true)


   * Verify that the Main Menu button moves below the other two buttons on smaller screen sizes.

   ![Button Positions](https://github.com/Gmanprodev/SerenAppy-Web-App/blob/master/documentation/testing/test-images/button_positions.gif?raw=true)


   * Verify that the page is responsive.
   
   ![Responsive Page](https://github.com/Gmanprodev/SerenAppy-Web-App/blob/master/documentation/testing/test-images/responsive_page2.gif?raw=true)


#### Conclusion

   * In my original mock ups and in my first attemp at building the countdown timer (before any conducted any testing) I included a moving circle track which moved in tandem with the timer. I decided to remove this from my design for two reasons, one being that it clogged up the page and the other being that it became too complicated for someone of my experience - this issue has been fixed for the first release.
   * I found that when the timer got to zero if the user clicked the play button again the timer started counting into minus numbers, I added a function which reset the timer and buttons upon reaching zero - this issue has been fixed for the first release.
   * I found that the time format wasn't displaying correctly so I built a Jasmine test to solve the problem - this issue has been fixed for the first release.
   * During testing I found unused code in my index.html and style.css files, relating to the SVG countdown track - I removed this for the first release. 



## Automated Testing

### Code Validation

   * I used the [W3C Markup Validation Service](https://validator.w3.org/) to validate my html code.

   ![Html Validation](https://github.com/Gmanprodev/SerenAppy-Web-App/blob/master/documentation/testing/test-images/index.html_validation.jpg?raw=true)

   ![Html Validation](https://github.com/Gmanprodev/SerenAppy-Web-App/blob/master/documentation/testing/test-images/test.html_validation.jpg?raw=true)
   
   ![Html Validation](https://github.com/Gmanprodev/SerenAppy-Web-App/blob/master/documentation/testing/test-images/404.html_validation.jpg?raw=true)


   * I used the [W3C CSS Validation Service](https://jigsaw.w3.org/) to validate my css code.

   ![CSS Validation](https://github.com/Gmanprodev/SerenAppy-Web-App/blob/master/documentation/testing/test-images/css_validation.jpg?raw=true)


   * I used the [jshint](https://jshint.com/) website to validate my Javascript code.

   ![Javascript Validation](https://github.com/Gmanprodev/SerenAppy-Web-App/blob/master/documentation/testing/test-images/javascript_validation.jpg?raw=true)

   * I used the [Free Formatter](https://www.freeformatter.com/) to format my html, css and javascript code.
   
   * I used TDD and built my own Jasmine test to test my formatTime() Javascript function, which you can access [here](https://github.com/Gmanprodev/SerenAppy-Web-App/tree/master/documentation/testing/jasmine_testing)


### Browser Validation

   * Chrome - works correctly. Click [here](test-images/chrome_test.jpg) for the test image.
   * Edge - works correctly. Click [here](test-images/edge_test.jpg) for the test image.
   * Safari - works correctly. Click [here](test-images/safari_test.png) for the test image.
   * Firefox - works correctly. Click [here](test-images/firefox_test.png) for the test image.
   * Opera - works correctly. Click [here](test-images/opera_test.png) for the test image.

### Lighthouse Audit

   * Click [here](test-images/lighthouse_report.pdf) for the full report.
   * No reccommendations in this report have been implemented in the first release but will be looked at in future releases.

#### Conclusion

   * The code validators highlighted these errors which have been fixed for the first release:
      * Using "labelledby" rather than "aria-label".
      * Missing / in a </script> tag.
      * Missing 4 semicolons in my javascript code.
      * Showing that I have one unused variable (hideFunction), however I am actually using.
   * The web app works correctly in all five major browsers.
   * The suggestions given in the Lighthouse report will be implemented in the second release.



## User testing

### My Mentor

Seun was very impressed with the web app and all of the documentation to go along with it. She said that she had been using the web app before bed to get into a calm state of mind and her favourite season option was Winter. She liked the fact that this had a real world application.

#### Suggested Improvements

* Have the selection buttons move into one column on smaller screen sizes - implemented.
* Reduce the amount of empty space on larger screen sizes - haven't implemented as I was not in agreement.
* Reduce the size of the header (navbar) on smaller screen heights (laptops) so that more content can fit on the page - this will be implemented in future releases as the majority of users will be viewing the web app on a mobile device.
* On big screen sizes the background image on the meditation pages becomes larger than the screen and some of the image is cut off. However this isn't very noticable and the images remain defined and clear - this will be implemented in future releases as the majority of users will be viewing the web app on a mobile device.
* Using emailjs to also send an email to the user to confirm their email has been received - this will be implemented in future releases as the user alreday gets a pop up informing them that the email has successfully been sent - this will be implemented in future releases.
* When the SWAL alert appears after submitting the contact form, the contact form should automatically close down - I implemented this after all of the documented testing above and the contact form modal now closes automatically after the fields have been validated and the submit button is clicked.
* The contact form modal is currently accessed via the @ icon in the footer, to complement this have a "contact us" button in the navbar which links to the same modal - this will be implemented in future releases.

### Peer-Code-Review

The feedback was that this is an application that could be used in the real world right now. Everyone enjoyed using the web app due to the way it interacted with the user and the way it was always giving feedback on users actions. 

#### Suggested Improvements:

   * Although the sound quality is pretty good the length of the audio files mean that there are too many stop and start points whilst the audio is playing. This leads to a disturbance for the user during their meditation sessions. These audio files will be updated in future releases.
   * Footer Social Media links all go to the generic login pages and not the company pages - I've left this for a later release as SerenAppy doesn't have a Social Media footprint.
   * Increase colour contrast due to possible accessability issues - Will look to make changes in the future releases.
   * Have the selection buttons move into one column on smaller screen sizes - implemented.


### User Review

The web app was tested by Code Institute students and mentors, friends and family. The majority of testing carried on real devices were on Iphone and Samsung mobiles. The feedback was really positive, most people commenting on how they would continue to use the web app for everday use.


#### Suggested Improvements:

   * Although the sound quality is pretty good the length of the audio files mean that there are too many stop and start points whilst the audio is playing. This leads to a disturbance for the user during their meditation sessions. These audio files will be updated in future releases.

#### Conclusion

   * I am aware that I need to replace the audio files with audio that constantly flows rather than stoping and starting, so users can experience a distraction free meditation session when using the web app.
   * I will use an analytics platform on the next release, such as [Hotjar](https://www.hotjar.com/), to collect feedback form a larger range of users and use that data to implement changes related to the way users navigate the site.