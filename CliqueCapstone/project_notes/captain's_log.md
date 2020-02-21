*CAPTAINS LOG*
THOUGHTS, ERRORS, IDEAS

**StarDate 01/09/2020**
    - ERROR Figure out authenticate for home page, also figure out ID situation *** FIXED (user = id)
    - Do I need to forloop/Iterate over the object to get it to print? - If you want all the posts from a model from different users

    - BACKGROUND IMAGE for home page, have fixed image, scroll down to view home, or button clicked.

    *CREATING INBOX IDEAS*
        - InboxDB
            - user = ManytoOne
            - directs = 'individual directmsgs fom directmsgDB'
        - DirectMsgDB
            - User = OnetoOne
            - to = OnetoOne
        - EmailsDB
            - Subject
            - Body
            - Time
        InboxDB -> DirectMsgDB -> EmailsDB
    
**StarDate 01/10/2020**
    - Migrated DB, I only need two DB's for the Inbox, Try and figure out how to associate the two users PK's
    - Need to add Data to inboxDB's.
    - Did some frontend work

**StarDate 01/11/2020 - 01/12/2020** 
    - Figure out how to get the Inbox created for the user when signup, just like profile.
    - Figure out how to add subject ot messages
    - When user clicks on Inbox, make a view to filter all his messages

    - On the base template add a filter setting

    - import both db's to both templates, had them kind of set up like the profile just to test the data ** ERROR DONT DO THIS LOL **
    - When you import one at a time you dont get an error
    - make a link on the user-inbox that is a query to the InboxDB to grab your msg, then when clicked displays the next view display all msgs.
        - Actually this is kind of redundant, Maybe use the first user-inbox like an authentication to make sure they have one, and move directly to the display of all current users messages.
        - I dont think i need the inbox view, as its only going to show that every HAS an inbox. I think i just need to query it with the current user, and get their direct messages..
    - When you do get() its sending two id's, receiver, and sender. Filter Accepts both and works. But that means you have to loop over the query set. So how do we keep it to only displaying selected msgs? and not msgs to other users
    - FIXED** So to fix the issue of getting two id's, each message created in the DB with two users gets saved as and id in the DB, so msg user to user2 has id of 2
    which is fine, it works for filtering to get the list of msgs, but filter gives back a list of objects, so to be able to click on one we needed to set it as get(id=id)
    to get the specific msg and be able to query through it **FIXED

    - WORK ON THIS 
        - How to get inbox created when user created. JUST LIKE PROFILE

    - **HOLD UP ERROR**
        - With only one DB that gives a sender-receiver one ID. Will that Cause issues with inboxes? would it be better to still have two DB's?
            - One DB that gives a user a Inbox ID
            - and then another ID for the sender and receiver, but it uses their inbox id as Primary.
            - REEVALUATE INBOX
            
            - ON THE VIEWS I MAY HAVE FOUND SOLUTION, YOU MUST ADD TO THE CONTEXT AND LOOK FOR MATCHES OF receiver=id AND sender=id
            - MUST DO THIS VIEW TO GET THE ONES SENT TO YOU AND ONES YOUVE SENT
    
    - IF API NEEDED FOR GRAD, user map API and share city or state location

    - Check out mixins - LoginRequiredMixins and UserPassesTestMixins for account security on forms. Do i ad this func to all models?
     # security mixins, add to all models?
    def test_func(self):
        msg = self.get_object()
        if self.request.user == msg.author:
            return True
        return False

**StarDate 01.13.2020**
    - NOTES FOR INBOX MODELS
        - So with the 2nd model, it all worked out, 
            - Im able to user self.conversation.receiver
            - AND it doesnt let you duplicate the msg that is FROM and TO
                - HOWEVER This causes an error*** If you switch it up and to TO and FROM, it makes another. So its still a duplicate if both users switch.


    - Working on Welcome Screen picture when user not logged in **ERROR importing picture

    - Figure out the Inbox Model, How do i grab two different uses and have them direct posts to each other?? WOnt the id's keep changing every message?

**StarDate 01.14.2020**
    - For bottom Navbar figure outa btter way of having fixed buttom, or if im able to when the user scrolls past a certain point it scrolls with it.




**StarDate 01.15.2020**
    - Figure out flow of website pages, curretly running into an issue with the login page, you cannot simply add the login form to the home page because of the auth.contrib.urls in the mysite urls. Maybe try making the users the default page instead of home
        - Currently when user tries to go to homepage without authenticating, user gets redirected to login page. Get rid of the home pages login/signup tages.
        - Figure out css scroll effect


    - Work on getting s3 buckets set up

    - PROFILE TWEAKS** 
        - Have more items on left side in smaller tags.
        - Create a button that when clicked lets you update file. Make room for photos.
        - Make dropdown for extra profile info to save room


**StarDate 01.16.2020**
    - S3 buckets working and deployed.
    - Decoupling figured out and working.

**StarDate 01.17.2020**
    - Do research on incorporating CDN's
    - Do more research on S3 bucckets

    - Figure out profile_bg 
        - Do i need another model for the profile posts? and just use that to also get random photos to home page?
        - See if you can add profile_bg to that same resizing.

    - Figure out how to set default images for profile and cover

    - For profile template, Kindof like FB, i want to have the profile pic with border in the bottom left of jumbotron

    - WORK ON HOME MODEL

    - If your unable to have the two forms on one page, consider making another view/template to submit multiple photos-- Screw that if your only doing one photo at a time.

**StarDate 01.18.2020** 
    - working on twitter allauth in another project, then see about the easiest way of implementing with class
    - Almost finished tutorial on allauth for twitter, had to submit review to get an API key, finish from there.

**StarDate 01.19.2020**
    - For Multiple image posts, were going to make two or three more models, a Post and a Image that is OnetoOne with post.
    
**StarDate 01.20.2020**
    - FOLLOWED A STUPID-BUTT TUTORIAL THAT TOOK FOREVER TO DO AND IN THE ND SHE LEFT OUT STUFF. COME ON.
        - Got it to work on the TwitterAllauth_2.0... Only took a few minutes. (Faceslap)
    
    - INTEGRATE ALLAUTH AT SOME POINT
        - When User authenticated, it looks like it actually got extra data in a ATT, and it has everything from there followers. Try using that foir the API

    - Work on forms now

    - Getting error when creating new user and going directly to profile. it says there is no default image set
        - FIGURED OUT WHERE ERROR IS COMING FROM. When deleting the .url it then loads correctly but with image.******** figure this out

    - Allauth was succesful, check admin to see what user does when they sign up that way. Will they be missing other data that the custom users do?
        - On the user Model, no Email is associated it looks like. nothing to click on
            - The only difference is they Cant put there first name or Email. 
                - Should i change there first name then?

**StarDate 01.21.2020**
    - HOMEPAGE, get random posts from users posting photos to their profile. 
        - Eventaully only get the ones that have the most likes
            - Or Users that have the most likes 

    - Succesful on getting threee different images and posting them to S3
        - Try to make them seperate and specific to a user, So i can for loop users library?
            - On s3 there was something a little weird, said that own was Carlock1609 and carlock906 is logged in? look into this

    - Figure out why Navbar js disappear on scroll only works when user logged in
        - Actually only works on profile page?
        - FIXED** had to move navbar script to top

    - TRYING to get allauth user an email on signin, and using the ACCOUNT_EMAIL_REQUIRED it gives me an error
        - Except when you get it in retains the email? maybe it just didnt post to db?

    - Fucked up navbar but i have a new look now.
    - Change buttons to wide faded out squares
        - Fixed navbar and buttons

    - I decided to put a Search link in the nav to click
        - Make model and view for search, and make the template have the search bar in middle of screen

**StarDate 01.21.2020**
    - Figure out why navbar disappears when smaller
    - Figure out login page twittter button not center

**StarDate 01.23.2020**
    - Figured out INBOX kinda THOROUGLY TEST
        - You need to figure out distinct instead of doing subject
        - So even though you change the subject, itll still work goign to the same user, but in the list it is not unique

        - So testing using only one persons profile works great! It posts in order as well
        - For distinct, The subject will work. I'm going to user their usernames which will be UNIQUE and work. HOWEVER
            - There will be Two threads possibly. 
            - If one user sends an email to another, itll be "userone and usertwo's Conversation" for one thread and vice versa if they make another. 
                - THEY DONT HAVE TO THOUGH, if users keep posting on same thread. not too big of a biggie, Possibly make statement too-
                    - Check to see if its a polynomal?

        - Figure out how to add sender - reciever names to list
        
**StarDate 01.24.2020**
    - Figure out flow of inbox.
        - What im thinking is, user looks up user profile, there is a button to send message, when clicked user goes directly to message detail screen instead of list, AND
            - AND after initiating that it gets add to inbox
            - FIGURE OUT HOW TO PASS THOSE PARAMS IN URL
                - SOLUTION
                    - So I have it working like the profile update.
                    - What needs to happen is whatever profile they're on, it needs to know that profile id. So when you click the button it also fills that out, The Sending Message too title, and the User Inbox ID as well as Conversation name

    - Figured out how to associate user.id to profile as well as User's Profile to pass to create-msg.
        - Users are also now able to visit other users profiles.
    - Figure out permissions for the profile page
        - DONE

    - Figure out how to build custom form and put in default values
        - Sender, Receiver, Profile
        - FORM DONE
    
    - BUG FORM posts correctly and has the correct data as shown in admin. HOWEVER Inbox is showing up empty and nothing shows on template
        - ** RECEIVER GETS THE EMAIL AND IT SHOWS, SENDER HAS EMPTY INBOX UNTIL RECEIVER SENDS EMAIL BACK

**StarDate 01.25.2020**
    - Figure out how to redirect page to same template after posting. On message page

**StarDate 01.26.2020**
    - On message template there is a bug with the names
        - I think the sender and receiver filters are getting confused
            - Figure out a way for when the initial message is set, whenever you reply the sender and receiver will always be the same

    - working on frontend for chat, trying to add receivers picture on left and sender on right to space things

    - WELCOME SCREEN have the title transition in, and then the login screen transitions in

**StarDate 01.27.2020**
    - Inbox finished at a good spot, try to figure out how to float messages right and left.
        - Next step is implementing search function so user can get to a profile to send message
    
    - Work on search function

    - THERE IS A BUG IN UPDATING PROFILE AND USERINBOX. IT IS NOW A COMMUNITY CHAT

**StarDate 01.28.2020**
    - Fixed profile, i was missing the f string syntax for the Redirect

**StarDate 01/30/2020**
    - BUG inbox create msg view, the conversation switches on the third msg
        -fixed

**StarDate 02/2/2020**
    - Changed city and state to location from twitter extradata
        - Search function is slightly different
    - FIX THE DEFAULT IMAGE
    - Add friends list function, already added to model.
    

**StarDate 02/19/2020**
    - Finished Cloudfront
    - CURRENTLY working on photo Library DONE*
        - SAME as profile just more photos
    - THEN work on security and pop this puppy up
    - BUG with photo library and delete FIXED**

    - PHOTO LIBRARY DONE AND SECURE WITH LIMITS AND USERS

    - Work on user Security

**StarDate 02/20/2020**
    - Finished security on messages and list

    - Need to work on user experience and add success messages - NOPE
    - Work on point system for home page
        - FIX display only 10 users on ranked page

    - Figure out how to only get photos from users on the ranked page

**StarDate 02/20/2020**
