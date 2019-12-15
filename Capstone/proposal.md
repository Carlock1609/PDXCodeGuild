# **Capstone Project**

## **Name:** clique.com

#
## **Project Overview**

### Discription:
- This is an application to bring Photographers and Influencers into one social media application. The purpose of this application is to make it easier for Influencers and Photographers to connect, gain experience and build both their portfolios. Instead of having to go through private messages, random DM's, and business queries that could be about anything--Everyone in this application is here for the same reason, an easier way to connect and **FIXTHIS**.

- Photographers can filter through a list of influencers by their follower count, and Influencers can filter through a list of Photographers based on their past portfolios, collaborations and linked pages. Once one is found, the user can message directly for connections or to collaborate.

- The idea for this application is to help new Photographers and Influencers get their start, by inticing them to work with newer users rather than collaborating with users who have already made it.

    ### Libraries/Frameworks

    - BeautifulSoup4 - Will be used to scrape linked social media accounts for follower ammounts.
    - Django - will be used for the web framework. Also user-to-user messaging.
    - Leaflet, MapBoxing - Will be used to plot out local spots perfect for taking photos.
    - Bootstrap4 - This will be pretty heavy in frontend.
#

## **Functionality**

### PLAY-BY-PLAY ----
### USER:
- Welcome Page-- mission statement, screen transitions upwards to Sign-up page when button clicked.

- User Sign-up Page-- in the form, they must check-mark whether they are a Influencer or Photographer.
    - Data will be stored in seperate tables under the User table (Influencer/Photographer).
    - When submited the page will transition to Profile page.

### USER/Influencer:
- Profile Page-- User can customize their page. A profile pic, experience form, photo library, about form, portfolio links and body posts.
    - Main function will be asking the user for their Social media accounts, and using beautifulsoup to scrape accounts for follower amounts, and Displaying follower amounts on their profile.
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
- Photographer can gain points for working with Influencers with lower follower amounts to get there portfolio on the main website feed.

### Functions:
- User Signup form. **MVP
- User Authentication. **MVP
- Profile Customization.
    - Saving User Profile and bringing it back when authenticated. **MVP
    - Other Users are able to post on other users profile Body. **MVP
- Search page, able to search through User Database (photographer or incluencer). **MVP
    - User is able to filter preferences. (Follower amounts/Experience).
- Direct messaging. **MVP
- Community Board.
- User manaully enters follower count on profile. **MVP
    - WebScraper to obtain follower counts - BeautifulSoup4.
- User rank system to intice users to work with newer users, and display top users on main feed.

## Project Ideas:
#### Photo Location marker:
 - When photos are used, a suggestion comes up to share location so it will be plotted on a map, so other Users can find cool spots to take pictures.
#### Rank System:
- Influencer can gain more points for working with photographers with less experience.
- Photographer can gain points for working with Influencers with lower follower count to get there portfolio on the main website feed.
#

## **Data Model**
- USER MODEL and PROFILE MODEL is One to One
- MESSAGES MODEL is One to Many

- User MODEL:
    Credentials **MVP
    - Username 
    - Password
    - Email
    - Social Media Accounts - Instagram, Facebook
- Profile MODEL:
    - Profile Info 
    - Pictures **MVP
    - Body Posts
    - Portfolio links **MVP
    - Follower amounts **MVP
    - Display (ability to customize profile)
    - Experience forms **MVP
- Messages MODEL: django user-to-user system
    - Private messages **MVP
    - Community board messages.
- Map locations MODEL: 
    - Local markers locations for Map.

#
## MVP BY TIME OF PRESENTATION
- User Model
- Profile Model
- Messages Model

- User Signup form. 
- User Authentication. 
- User Profile 
    - Saving User Profile and bringing it back when authenticated. 
    - Other Users are able to post on profile Body. 
- Search page, able to search through User Database (photographer or incluencer).
- Direct messaging.
- User will manaully enter follower amounts on profile. 

#
## **Schedule**
1. WEEK:
    - User Model-- Day Mon-Wed 
    - Porfile Model-- Day Wed-Fri 
    - Messages Model-- Day Fri-Sun
2. WEEK:
    - User Signup form-- Day Mon-Tues
    - User Authentication-- Day Tues-Fri 
    - User Profile-- Day Fri-Sun
3. WEEK:
    - Direct Messaging-- Day Mon-Thu
    - Search Page function-- Day Thu-Sun
4. WEEK:
    - Heavy Front-end-- Day Mon-Fri 
    - Beautifulsoup4 function-- Day Fri-Sun

#


