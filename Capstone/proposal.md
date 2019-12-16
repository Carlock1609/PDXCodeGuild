# **Capstone Project**

## **Name:** clique.com

#
## **PROJECT OVERVIEW**

### Discription:
- This is an application to bring Photographers and Influencers into one social media application. The purpose of this application is to make it easier for Influencers and Photographers to connect, gain experience and build both their portfolios. Instead of having to go through private messages, random DM's, and business queries that could be about anything--Everyone on this website will be looking for the same thing, experience and connecting. There are numorous Influencers on social media who need portfolios for their pages or marketing, however they may not want to sign-up on Modeling Agencies to find that. This application is built towards them. 

- Photographers can filter through a list of influencers by their follower amount, and Influencers can filter through a list of Photographers based on their experience. Once one is found, the user can message directly for connections or to collaborate.

- The idea for this application is to help new Photographers and Influencers get their start, by inticing them to work with newer users rather than collaborating with users who have already made it.

    ### Libraries/Frameworks

    - BeautifulSoup4 - Will be used to scrape linked social media accounts for follower ammounts.
    - Django - will be used for the web framework. Also user-to-user messaging.
    - Leaflet, MapBoxing - Will be used to plot out local spots perfect for taking photos.
    - Bootstrap4 - This will be pretty heavy in frontend.
#

## **FUNCTIONALITY**

### PLAY-BY-PLAY ----
### USER:
1. Welcome Page-- A centered mission statement, and a button on bottom of page that transitions upward to Sign-up page.

2. User Sign-up Page-- in the form, they must check-mark whether they are a Influencer or Photographer.
    - Data will be stored in User Model when the form is submited.
    - The page will then transition to Profile page.

### USER/Influencer:
3. Profile Page-- User can customize their page. A profile pic, experience form, photo library, about form, portfolio links and body posts.
    - Forms will be stored in Profile Model.
    - Main function will be asking the user for their Social media accounts, and using beautifulsoup to scrape accounts for follower amounts, and Displaying follower amounts on their profile.
- User can use Direct messaging.

### USER/Photographer:
4. Profile Page-- User can customize their page. A profile pic, experience form, photo library, about form, portfolio links and body posts.
    - Forms will be stored in Profile Model.
    - User will be able to link their own personal portfolios.
- User can use Direct messaging.

### USER/BOTH:
5. Search Page-- Influencer/Photographer will use the search page to search through a list of other photographers or influencers from the User Model.
6. User can set different filters for better results, (follower count/work experience)
7. Once user clicks on another user, they are able checkout their profile and send direct messages/Make body posts.
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

### Functions:
- User Signup form. **MVP
- User Authentication. **MVP
- Profile Customization.
    - Saving to Profile Model and bringing it back when User authenticated. **MVP
    - Other Users are able to post on other Users profile Body. **MVP
- Search page, able to search through User Model (photographer or incluencer). **MVP
    - User is able to filter preferences. (Follower amounts/Experience).
- Direct messaging. **MVP
- Community Board.
- User manaully enters follower count on profile. **MVP
    - WebScraper to obtain follower counts - BeautifulSoup4.
- User rank system to intice users to work with newer users, and display top users on main feed.

## Project Ideas:
#### Photo Location marker:
 - When photos are used, a suggestion comes up to share location so it will be plotted on a map, so other Users can find local scenenic spots to take pictures.
#### Rank System:
- Influencer can gain more points for working with photographers with less experience.
- Photographer can gain points for working with Influencers with lower follower count to get there portfolio on the main website feed.
#

## **DATA MODEL**
- USER MODEL and PROFILE MODEL is One to One
- MESSAGES MODEL is One to Many

- User MODEL:
    - Username 
    - Password
    - Email
    - Social Media Accounts - Facebook, Instagram
- Profile MODEL:
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
## **SCHEDULE**
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

After Presentation

5. WEEK:
    - BeautifulSoup4 function-- Day Mon-Fri
    - Community Board-- Day Fri-Sun
6. WEEK: 
    - Community Board-- Day Mon-Wed
    - Rank System-- Day Wed-Sat
    - Main Page-- Day Sun-Mon
7. WEEK: 
    - Photo Location function-- Day Mon-Sun
8. WEEK:
    - Frontend styling-- Day Mon-Sun

#


