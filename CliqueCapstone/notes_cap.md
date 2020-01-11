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