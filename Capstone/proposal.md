# **Capstone Project**

## **Name:** AchieveSTATUS.com

#
## **Project Overview**

### Discription:
- This is an application to bring Photographers and Influencers into one social media application. 
The purpose of the application is to make it easier for Influencers and Photographers to gain experience, and build both portfolios.
Instead of having to go through private messages, random DM's, and business queries that could be about anything--Everyone in this application is here for the same reason, to Achieve STATUS.

- Photographers can filter through a list of influencers by their follower count, and Influencers
can filter through a list of Photographers based on their past portfolios, collaborations and linked pages.
Once one is found, the user can message directly for connections or to collaborate.

- The idea for this application is to help new Photographers and Influencers get their start, by inticing them to work with newer users rather than collaborting with users who have already made it.

    ### Libraries/Frameworks

    - BeautifulSoup4 - Will be used to scrape linked social media accounts for follower counts.
    - Django - will be used to authenticate users and make sure they have actual social media accounts. And to store their profiles properly in a DB.
    - Leaflet, MapBoxing - Will be used to plot out local spots perfect for taking photos.
    - Bootstrap4 - This will be pretty heavy in frontend
#

## **Functionality**

### USER:
- Welcome Page, screen transitions upwards to Sign-up page when button clicked.

- User Sign-up Page, in the form they check whether they are a model or photographer.
    - Data will be stored in seperate tables under the User table (Influencer/Photographer).
    - When submited the page will transition to Profile page.

### USER/Influencer:
- Profile Page, User can customize their page. A profile pic, experience form, photo library, about, links, body posts.
    - Main function will be asking the user for their Social media accounts, and using beautifulsoup to scrape accounts for user Amounts. And Displaying follower counts on profile.
    - Direct messaging.
    - Search for photographer.

### USER/Photographer:
- User must signup and upload portfolio/experience and other collaborations to their profile.
- User can set filter on search to get a list that meets the preffered follower count criteria.
- User can send message to Influencer to collaborate.


### Rank System:
- User can gain more points for working with photographers with less experience.
- User can gain points for working with Influencers with lower follower count to get there portfolio on the main website feed.

### Functions:
- User Signup Form
- User Authentication

- WebScraper to obtain follower counts - BeautifulSoup4
- User Rank system that intices users to work with other users who need more experience and there foot in the door. Rank system gives extra points for that.
- Chat system
    - Direct Messaging 
    - Group Messaging
    - Community boards

### Function Ideas:
- Photo Location marker - When photos are used, a suggestion comes up to share location so it will be plotted on a map, so other Users can find cool spots to take pictures.
#

## **Data Model**

- User - Login information, Profile Info, photos, portfolios, follower counts, display
- Messages - private messages, Community board messages
- Map locatoions - local markers locations for Map

#
## **Schedule**
- Complete this

#



<!-- 

### Influencer:
- User must signup and are also required to link their social media accounts to get their follower counts.
- User will have the follower count displayed on their profile for each application and total follower count combined aswell.
- User can set filter on Photographer based on experience and search a list that matches.
- User can send message to Photographer to collaborate -->
