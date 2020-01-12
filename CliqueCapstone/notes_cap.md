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

**01/11/2020**
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