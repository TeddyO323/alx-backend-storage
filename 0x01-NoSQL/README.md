# 0x01. NoSQL

## Back-end | NoSQL | MongoDB

## Resources
Read or watch:
- [NoSQL Databases Explained](https://www.youtube.com/watch?v=7S_tz1z_5bA)
- [What is NoSQL?](https://www.mongodb.com/nosql-explained)
- [MongoDB with Python Crash Course - Tutorial for Beginners](https://www.youtube.com/watch?v=E-1xI85Zog8)
- [MongoDB Tutorial 2 : Insert, Update, Remove, Query](https://www.youtube.com/watch?v=85WjOh9Q5Wg)
- [Aggregation](https://docs.mongodb.com/manual/aggregation/)
- [Introduction to MongoDB and Python](https://www.mongodb.com/blog/post/getting-started-with-python-and-mongodb)
- [mongo Shell Methods](https://docs.mongodb.com/manual/reference/method/)
- [Mongosh](https://www.mongodb.com/mongosh)

## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### General
- What NoSQL means
- What is the difference between SQL and NoSQL
- What is ACID
- What is a document storage
- What are the NoSQL types
- What are the benefits of a NoSQL database
- How to query information from a NoSQL database
- How to insert/update/delete information from a NoSQL database
- How to use MongoDB

## Requirements
### MongoDB Command File
- All your files will be interpreted/compiled on Ubuntu 18.04 LTS using MongoDB (version 4.2)
- All your files should end with a new line
- The first line of all your files should be a comment: `// my comment`
- A `README.md` file, at the root of the folder of the project, is mandatory
- The length of your files will be tested using `wc`

### Python Scripts
- All your files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7) and PyMongo (version 3.10)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/env python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle style (version 2.5.*)
- The length of your files will be tested using `wc`
- All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All your functions should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'`)
- Your code should not be executed when imported (by using `if __name__ == "__main__":`)

## More Info
- [Install MongoDB 4.2 in Ubuntu 18.04](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/)
- [Official installation guide](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/)

```bash
$ wget -qO - https://www.mongodb.org/static/pgp/server-4.2.asc | apt-key add -
$ echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.2 multiverse" > /etc/apt/sources.list.d/mongodb-org-4.2.list
$ sudo apt-get update
$ sudo apt-get install -y mongodb-org
...
$  sudo service mongod status
mongod start/running, process 3627
$ mongo --version
MongoDB shell version v4.2.8
git version: 43d25964249164d76d5e04dd6cf38f6111e21f5f
OpenSSL version: OpenSSL 1.1.1  11 Sep 2018
allocator: tcmalloc
modules: none
build environment:
    distmod: ubuntu1804
    distarch: x86_64
    target_arch: x86_64
$  
$ pip3 install pymongo
$ python3
>>> import pymongo
>>> pymongo.__version__
'3.10.1'
```
---

### Tasks

1. **List All Databases**
   - **Description:** Write a script that lists all databases in MongoDB.
   - **Usage:** `cat 0-list_databases | mongo`
   - **Example Output:**
     ```
     MongoDB shell version v3.6.3
     connecting to: mongodb://127.0.0.1:27017
     MongoDB server version: 3.6.3
     admin        0.000GB
     config       0.000GB
     local        0.000GB
     logs         0.005GB
     bye
     ```

2. **Create a Database**
   - **Description:** Write a script that creates or uses the database my_db.
   - **Usage:** `cat 1-use_or_create_database | mongo`
   - **Example Output:**
     ```
     MongoDB shell version v3.6.3
     connecting to: mongodb://127.0.0.1:27017
     MongoDB server version: 3.6.3
     switched to db my_db
     bye
     ```

3. **Insert Document**
   - **Description:** Write a script that inserts a document in the collection school.
   - **Usage:** `cat 2-insert | mongo my_db`
   - **Example Output:**
     ```
     MongoDB shell version v3.6.3
     connecting to: mongodb://127.0.0.1:27017/my_db
     MongoDB server version: 3.6.3
     WriteResult({ "nInserted" : 1 })
     bye
     ```

4. **List All Documents**
   - **Description:** Write a script that lists all documents in the collection school.
   - **Usage:** `cat 3-all | mongo my_db`
   - **Example Output:**
     ```
     MongoDB shell version v3.6.3
     connecting to: mongodb://127.0.0.1:27017/my_db
     MongoDB server version: 3.6.3
     { "_id" : ObjectId("5a8fad532b69437b63252406"), "name" : "Holberton school" }
     bye
     ```

5. **List Matched Documents**
   - **Description:** Write a script that lists all documents with name="Holberton school" in the collection school.
   - **Usage:** `cat 4-match | mongo my_db`
   - **Example Output:**
     ```
     MongoDB shell version v3.6.3
     connecting to: mongodb://127.0.0.1:27017/my_db
     MongoDB server version: 3.6.3
     { "_id" : ObjectId("5a8fad532b69437b63252406"), "name" : "Holberton school" }
     bye
     ```

6. **Count Documents**
   - **Description:** Write a script that displays the number of documents in the collection school.
   - **Usage:** `cat 5-count | mongo my_db`
   - **Example Output:**
     ```
     MongoDB shell version v3.6.3
     connecting to: mongodb://127.0.0.1:27017/my_db
     MongoDB server version: 3.6.3
     1
     bye
     ```

7. **Update Document**
   - **Description:** Write a script that adds a new attribute to a document in the collection school.
   - **Usage:** `cat 6-update | mongo my_db`
   - **Example Output:**
     ```
     MongoDB shell version v3.6.3
     connecting to: mongodb://127.0.0.1:27017/my_db
     MongoDB server version: 3.6.3
     WriteResult({ "nMatched" : 1, "nUpserted" : 0, "nModified" : 1 })
     bye
     ```

8. **Delete Matched Documents**
   - **Description:** Write a script that deletes all documents with name="Holberton school" in the collection school.
   - **Usage:** `cat 7-delete | mongo my_db`
   - **Example Output:**
     ```
     MongoDB shell version v3.6.3
     connecting to: mongodb://127.0.0.1:27017/my_db
     MongoDB server version: 3.6.3
     { "acknowledged" : true, "deletedCount" : 1 }
     bye
     ```

9. **List All Documents in Python**
   - **Description:** Write a Python function that lists all documents in a collection.
   - **Usage:** `./8-main.py`
   - **Example Output:**
     ```
     [5a8f60cfd4321e1403ba7ab9] Holberton school
     [5a8f60cfd4321e1403ba7aba] UCSD
     ```

10. **Insert a Document in Python**
    - **Description:** Write a Python function that inserts a new document in a collection based on kwargs.
    - **Usage:** `./9-main.py`
    - **Example Output:**
      ```
      New school created: 5a8f60cfd4321e1403ba7abb
      [5a8f60cfd4321e1403ba7ab9] Holberton school
      [5a8f60cfd4321e1403ba7aba] UCSD
      [5a8f60cfd4321e1403ba7abb] UCSF 505 Parnassus Ave
      ```

11. **Update Topics in a Document**
    - **Description:** Write a Python function that changes all topics of a school document based on the name.
    - **Prototype:** `def update_topics(mongo_collection, name, topics):`
      - `mongo_collection`: The pymongo collection object.
      - `name` (string): The school name to update.
      - `topics` (list of strings): The list of topics approached in the school.
    - **Usage:** `./10-update_topics.py`
    - **Example Output:**
      ```
      [5a8f60cfd4321e1403ba7ab9] Holberton school ['Sys admin', 'AI', 'Algorithm']
      [5a8f60cfd4321e1403ba7aba] UCSD
      [5a8f60cfd4321e1403ba7abb] UCSF 505 Parnassus Ave
      [5a8f60cfd4321e1403ba7ab9] Holberton school ['iOS']
      ```

12. **Schools by Topic**
    - **Description:** Write a Python function that returns the list of schools having a specific topic.
    - **Prototype:** `def schools_by_topic(mongo_collection, topic):`
      - `mongo_collection`: The pymongo collection object.
      - `topic` (string): The topic searched.
    - **Usage:** `./11-schools_by_topic.py`
    - **Example Output:**
      ```
      [5a90731fd4321e1e5a3f53e3] Holberton school ['Algo', 'C', 'Python', 'React']
      [5a90731fd4321e1e5a3f53e5] UCLA ['C', 'Python']
      ```

13. **Log Stats**
    - **Description:** Write a Python script that provides some stats about Nginx logs stored in MongoDB.
    - **Prototype:** `./12-log_stats.py`
    - **Example Output:**
      ```
      94778 logs
      Methods:
          method GET: 93842
          method POST: 229
          method PUT: 0
          method PATCH: 0
          method DELETE: 0
      47415 status check
      ```

14. **Regex Filter**
    - **Description:** Write a script that lists all documents with a name starting with Holberton in the collection school.
    - **Usage:** `./100-find | mongo my_db`
    - **Example Output:**
      ```
      { "_id" : ObjectId("5a90731fd4321e1e5a3f53e3"), "name" : "Holberton school" }
      { "_id" : ObjectId("5a90731fd4321e1e5a3f53e3"), "name" : "Holberton School" }
      { "_id" : ObjectId("5a90731fd4321e1e5a3f53e3"), "name" : "Holberton-school" }
      ```

15. **Top Students**
    - **Description:** Write a Python function that returns all students sorted by average score.
    - **Prototype:** `def top_students(mongo_collection):`
      - `mongo_collection`: The pymongo collection object.
    - **Usage:** `./101-main.py`
    - **Example Output:**
      ```
      [5a90776bd4321e1ec94fc40a] Sonia => 13.1
      [5a90776bd4321e1ec94fc40c] Julia => 10.266666666666666
      [5a90776bd4321e1ec94fc408] John => 9.533333333333333
      [5a90776bd4321e1ec94fc40b] Amy => 9.366666666666665
      [5a90776bd4321e1ec94fc409] Bob => 6.066666666666667
      ```

16. **Log Stats - New Version**
    - **Description:** Improve 12-log_stats.py by adding the top 10 of the most present IPs in the collection nginx of the database logs.
    - **Usage:** `./102-log_stats.py`
    - **Example Output:**
      ```
      IPs:
          172.31.63.67: 15805
          172.31.2.14: 15805
          172.31.29.194: 15805
          69.162.124.230: 529
          64.124.26.109: 408
          64.62.224.29: 217
          34.207.121.61: 183
          47.88.100.4: 166
          45.249.84.250: 160
          216.244.66.228: 150
