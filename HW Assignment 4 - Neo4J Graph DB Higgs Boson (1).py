#!/usr/bin/env python
# coding: utf-8

# In[1]:


from neo4j import GraphDatabase

host = 'ec2-54-67-89-95.us-west-1.compute.amazonaws.com'
port = '9232'

uri = "bolt://" + host + ':' + port

driver = GraphDatabase.driver(uri, auth=("neo4j", "password"), encrypted=False)

session = driver.session()


# In[49]:


with session.begin_transaction() as tx:
    #Q1
    print('Q1 - How many total nodes with Label :User are there in the database?')
    for q1 in tx.run('match (:User) return count(*) as User_Count'):
        print('Answer: Total nodes with Label :User are', q1[0])
    
    #Q2
    print('Q2 - How many Social Network relationships are there in the database ?')
    for q2 in tx.run('match ()-[follows:Follows]->() return count(follows)'):
        print('Answer: Total Social Network relationships are',q2[0])
    
    #Q3
    print('Q3 - How many Social Network followers does user 89805 have ?')
    for q3 in tx.run('match (follower)-[:Follows]->(:User{user:89805}) return count(follower)'):
        print('Answer: User 89805 has',q3[0], 'followers in total.')
    
    #Q4
    print('Q4 - How many total times did users in this network retweet ?')
    for q4 in tx.run('match (:User)-[retweets:Retweets]->() return count(retweets)'):
        print('Answer: The users retweeted', q4[0], 'times in total.')
    
    #Q5
    print("Q5 - How many times did users in this network reply to other users' tweets?")
    for q5 in tx.run('match (:User)-[replies:Replys]->() return count(replies)'):
        print('Answer: The users replied', q5[0], 'times in total.')
    
    #Q6
    print('How many times did users in this network mention other users in their tweets?')
    for q6 in tx.run('match (:User)-[mentions:Mentions]->() return count(mentions)'):
        print('Answer: The users mentioned other users', q6[0], 'times in their tweets.')
    
    #Q7
    print('Q7 - How many users follow user 89805 ?')
    for q7 in tx.run('match (follower)-[:Follows]->(:User{user:89805}) return count(follower)'):
        print('Answer: User 89805:', q7[0], 'followers in total.')
    
    #Q8
    print('Q8 - How many users does user 89805 follow ?')
    for q8 in tx.run('match (:User{user:89805})-[follows:Follows]->() return count(follows)'):
        print('Answer: User 89805 follows', q8[0],'users in total.')
    
    #Q9
    print('Q9 - Did user 14907 ever retweet user 89805?')
    for q9 in tx.run('match (:User{user:14907})-[retweets:Retweets]->(:User{user:89805}) return count(retweets)'):
        print('Answer: No, User 14907 has retweeted user 89805 -',q9[0],'time(s).')
    
    #Q10
    print('Q10 - Did user 89805 ever retweet user 14907 ?')
    for q10 in tx.run('match (:User{user:89805})-[retweets:Retweets]->(:User{user:14907}) return count(retweets)'):
        print('Answer: Yes, user 89805 has retweeted user 14907 -', q10[0], 'time(s) in total.')
    
    #Q11
    print('Q11 - Find out the top 5 users with the highest number of followers ? ')
    print('Answer:')
    print('The top 5 users with the highest number of followers are listed below,')
    for q11 in tx.run('match (follower)-[:Follows]->(user:User) return user, count(follower) ORDER BY count(follower) DESC LIMIT 5'):
        print(q11[0])
    
    #Q12
    print('Q12 - What is the total count of followers of followers of user 89805 ?')
    for q12 in tx.run('match (followers)-[:Follows] ->(follower)-[:Follows] ->(:User{user:89805}) return count(followers)'):
        print('Answer: The total count of followers of user 89805s followers are', q12[0])
    
    #Q13
    print('Q13 - Explore and find some interesting statistic from the data. Print out what you found.')
    for a1 in tx.run('match (:User{user:206})-[follows:Follows]->() return count(follows)'):
        print('1. User 206 is following', a1[0],'user(s) in total.')
    for a2 in tx.run('match (follower)-[:Follows]->(:User{user:206}) return count(follower)'):
        print('2. User 206 has',a2[0],'follower(s) in total.')
    for a3 in tx.run('match (retweets)-[:Retweets]->(:User{user:206}) return count(retweets)'):
        print('3. User 206 retweeted', a3[0],'time(s) in total.')
    for a4 in tx.run('match (replies)-[:Replys]->(:User{user:206}) return count(replies)'):
        print('4. User 206 has replied', a4[0],'time(s) in total.')
    for a5 in tx.run('match (:User)-[mentions:Mentions]->(:User{user:206}) return count(mentions)'):
        print('5. User 206 were mentioned', a5[0],'time(s) in other users tweets.')
    for a6 in tx.run('match (:User{user:206})-[retweets:Retweets]->(:User{user:1503}) return count(retweets)'):
        print('6. User 206 has retweeted user 1503 -', a6[0], 'time(s) in total.')
        


# In[ ]:




