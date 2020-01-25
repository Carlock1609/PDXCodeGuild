DataBase APi
    - A self-contained packaging of a database that accepts and returns structures requests according to an applications business logic.


Core Responsibilites of a DB
    - Consolidating data operations in the 'main' application
        - (rails, php, node, etc)
    - Converting them insto dedicated stored procedures in the database
        - rather than quertinf with literal SQL (via or ORM)

    This resultsin code that is:
        - Executing faster
        - coded simpler
        - organized better


A dbAPI accepts requestis and returns responses in a stanardized way using exlisovely stored procedures.


implementaion:1,2,3
    1. Strictly all interaction by any and all clients must be done exclusively through prescrived 'delegate functions' in the database
    2. Delegate functions accept and return data in a structured and standardized form.
    3. Dedicted user accounts are made for axxes to the database and have resutructed privilages: only access to delegate functions. These accounts are used for all client connections
        - Security is layered
        

Advantages of postgres
    - Execution speed
    - Data integrity and process Optimization
    - security
    - transactional control
    - Error handling and diagnostics
    - Separation of concern
    - Functional testing 


Look up 'apix' examples

the dbAPI is kind of like JSON and how to post data that way