# **Capstone Project**

## **Name:** AchieveSTATUS.com

#
## **Project Overview**

### Discription:
- This is an application to bring Photographers and Influencers into one social media application. The purpose of this application is to make it easier for Influencers and Photographers to connect, gain experience and build both portfolios. Instead of having to go through private messages, random DM's, and business queries that could be about anything--Everyone in this application is here for the same reason, an easier way to connect and to Achieve STATUS.

- Photographers can filter through a list of influencers by their follower count, and Influencers can filter through a list of Photographers based on their past portfolios, collaborations and linked pages. Once one is found, the user can message directly for connections or to collaborate.

- The idea for this application is to help new Photographers and Influencers get their start, by inticing them to work with newer users rather than collaborating with users who have already made it.

    ### Libraries/Frameworks

    - BeautifulSoup4 - Will be used to scrape linked social media account for follower counts.
    - Django - will be used for web framework.
    - Leaflet, MapBoxing - Will be used to plot out local spots perfect for taking photos.
    - Bootstrap4 - This will be pretty heavy in frontend.
#

## **Functionality**

### PLAY-BY-PLAY ----
### USER:
- Welcome Page-- mission statement, screen transitions upwards to Sign-up page when button clicked.

- User Sign-up Page-- in the form, they check-mark whether they are a model or photographer.
    - Data will be stored in seperate tables under the User table (Influencer/Photographer).
    - When submited the page will transition to Profile page.

### USER/Influencer:
- Profile Page-- User can customize their page. A profile pic, experience form, photo library, about form, portfolio links and body posts.
    - Main function will be asking the user for their Social media accounts, and using beautifulsoup to scrape accounts for follower amounts, and Displaying follower counts on profile.
- Direct messaging.

### USER/Photographer:
- Profile Page-- User can customize their page. A profile pic, experience form, photo library, about form, portfolio links and body posts.
    - User will be able to link their own personal portfolios
- Direct messaging.

### USER/BOTH:
- Search Page-- Influencer/Photographer will use the search page to search through a list of other photographers or influencers on the application database.
- User can set different filters for better results, (follower count/work experience)
- Once user clicks on another user, they are able checkout their profile and send direct messages/Make body posts.
### PLAY-BY-PLAY-end ----
## (Listed items that contain **MVP at the end is what I want to be done by the capstone.)
### PAGES:
- Welcome Page **MVP
- Sign-up Page **MVP
- Profile Page **MVP
- Search Page **MVP
- Direct Messaging Page **MVP
- Community Board Page
- Main Feed Page (will be used for rank system ideas)

### Rank System:
- Influencer can gain more points for working with photographers with less experience.
- Photographer can gain points for working with Influencers with lower follower count to get there portfolio on the main website feed.

### Functions:
- User Signup form. **MVP
- User Authentication. **MVP
- Profile Customization.
    - Saving User Profile and bringing it back when authenticated. **MVP
    - Other Users able to post on profile Body. **MVP
- Search page, able to search through User Database (photographer or incluencer). **MVP
    - User is able to filter preferences. (Follower count/Experience).
- Direct messaging. **MVP
- Community Board.
- User manaully enters follower count on profile. **MVP
    - WebScraper to obtain follower counts - BeautifulSoup4.
- User rank system to intice users to work with lessers, and display top users on main feed.

### Function Ideas:
- Photo Location marker - When photos are used, a suggestion comes up to share location so it will be plotted on a map, so other Users can find cool spots to take pictures.
#

## **Data Model**
(Models with two attributes with sub attributes? Better organization?)
(Should I rather make two seperate models (Credentials and Profile)?)
- User MODEL:
    - Credentials **MVP
        - Username 
        - Password
        - Email
    - Profile Info 
        - Pictures **MVP
        - Body Posts
        - Portfolio links **MVP
        - Follower counts **MVP
        - Display (ability to customize profile)
        - Experience forms **MVP
- Messages MODEL: 
    - Private messages **MVP
    - Community board messages.
- Map locations MODEL: 
    - Local markers locations for Map.

#
## MVP
- User Signup form. **MVP
- User Authentication. **MVP
- User Profile **MVP
    - Saving User Profile and bringing it back when authenticated. MVP**
    - Other Users able to post on profile Body. **MVP
- Search page, able to search through User Database (photographer or incluencer). **MVP
- Direct messaging. **MVP
- User manaully enters follower count on profile. **MVP
### Stored Data MVP's
- User - Login information, Profile Info(photos, portfolios, follower counts, display, experience forms). **MVP
- Messages - private messages, Community bord messages. **MVP

#
## **Schedule**
- Complete this

#



<!-- FIGURE out how to store images on another server, and keep app seperate -->
<!-- That’s what django.contrib.staticfiles is for: it collects static files from each of your applications (and any other places you specify) into a single location that can easily be served in production. -->