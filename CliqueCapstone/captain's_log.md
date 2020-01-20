*CAPTAINS LOG*
THOUGHTS, ERRORS, IDEAS

**01/09/2020**
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
    
**01/10/2020**
    - Migrated DB, I only need two DB's for the Inbox, Try and figure out how to associate the two users PK's
    - Need to add Data to inboxDB's.
    - Did some frontend work

**01/11/2020 - 01/12/2020** 
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

**01.13.2020**
    - NOTES FOR INBOX MODELS
        - So with the 2nd model, it all worked out, 
            - Im able to user self.conversation.receiver
            - AND it doesnt let you duplicate the msg that is FROM and TO
                - HOWEVER This causes an error*** If you switch it up and to TO and FROM, it makes another. So its still a duplicate if both users switch.


    - Working on Welcome Screen picture when user not logged in **ERROR importing picture

    - Figure out the Inbox Model, How do i grab two different uses and have them direct posts to each other?? WOnt the id's keep changing every message?

**01.14.2020**
    - For bottom Navbar figure outa btter way of having fixed buttom, or if im able to when the user scrolls past a certain point it scrolls with it.




**01.15.2020**
    - Figure out flow of website pages, curretly running into an issue with the login page, you cannot simply add the login form to the home page because of the auth.contrib.urls in the mysite urls. Maybe try making the users the default page instead of home
        - Currently when user tries to go to homepage without authenticating, user gets redirected to login page. Get rid of the home pages login/signup tages.
        - Figure out css scroll effect


    - Work on getting s3 buckets set up

    - PROFILE TWEAKS** 
        - Have more items on left side in smaller tags.
        - Create a button that when clicked lets you update file. Make room for photos.
        - Make dropdown for extra profile info to save room


**01.16.2020**
    - S3 buckets working and deployed.
    - Decoupling figured out and working.

**01.17.2020**
    - Do research on incorporating CDN's
    - Do more research on S3 bucckets

    - Figure out profile_bg 
        - Do i need another model for the profile posts? and just use that to also get random photos to home page?
        - See if you can add profile_bg to that same resizing.

    - Figure out how to set default images for profile and cover

    - For profile template, Kindof like FB, i want to have the profile pic with border in the bottom left of jumbotron

    - WORK ON HOME MODEL

    - If your unable to have the two forms on one page, consider making another view/template to submit multiple photos-- Screw that if your only doing one photo at a time.

**01.18.2020** 
    - working on twitter allauth in another project, then see about the easiest way of implementing with class
    - Almost finished tutorial on allauth for twitter, had to submit review to get an API key, finish from there.

**01.19.2020**
    - For Multiple image posts, were going to make two or three more models, a Post and a Image that is OnetoOne with post.
    
**01.20.2020**
    - FOLLOWED A STUPID-BUTT TUTORIAL THAT TOOK FOREVER TO DO AND IN THE ND SHE LEFT OUT STUFF. COME ON.
        - Got it to work on the TwitterAllauth_2.0... Only took a few minutes. (Faceslap)
    
    - INTEGRATE ALLAUTH AT SOME POINT
        - When User authenticated, it looks like it actually got extra data in a ATT, and it has everything from there followers. Try using that foir the API

    - Work on forms now

    - Getting error when creating new user and going directly to profile. it says there is no default image set
        - FIGURED OUT WHERE ERROR IS COMING FROM. When deleting the .url it then loads correctly but with image.******** figure this out