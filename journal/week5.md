# Week 5 — DynamoDB and Serverless Caching

# AWS Cloud Bootcamp Week 05
## DynamoDB and Serverless Caching
by: Chris Ruediger 


### My Sumamary

...

### Key Terms
- NoSQL
- DynamoDB: AWS Service implementing NoSQL, includes key-value and document stores
- Access Patterns
- Partition key and primary key and sort key
- GSI (Global Secondary Indexes) vs LSI (Local Secondary Indexes)

### We did...
1)
2)
3)

### Notes:
- NoSQL/Mongo DB
    - Have to some serious data planning
    - Asking the questions about what questions you want to ask
        - What data do we need? When do we need it? and at what velocity?
        - this = how many tables
        - What are you optimizing for?
    - DynamoDB is aimed at preprocessing the data so you "don't have to ask it questions"
    - **Critical Access Patterns**
        - Need to get a list of conversations "I" am invlolved in and sorted by most recent (Pattern B)
        - List of messages in a conversation, sorted by update time in descending order (Pattern A)
        - Create a message (Pattern C)
        - update a message_group for the last message (Pattern D)
    - When doing table design, write queries 
    - Cramming things into a single table
        - Reduces complexity
        - Keeps data together that is related
    - Partition key for Access Pattern A can be message_group_uuid, which would return list of all messages from that group
    - As few GSIs as possible
    - If its not something you're gonna index on, squeeze it into a JSON document

### Questions???
- What is the consequence of immplemeting a schema and changing it after it's deployed?