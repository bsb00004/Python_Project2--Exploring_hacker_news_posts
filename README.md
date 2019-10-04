# Python_Project2--Exploring_hacker_news_posts
### Exploring Hackers News Posts¶
In this project, we'll compare two different types of posts from Hacker News, a popular site where technology related stories (or 'posts') are voted and commented upon. 
![image](https://s3.amazonaws.com/dq-content/354/hacker_news.jpg)

The two types of posts we'll explore begin with either Ask HN or Show HN.imageUsers submit Ask HN posts to ask the Hacker News community a specific question, such as "What is the best online course you've ever taken?" Likewise, users submit Show HN posts to show the Hacker News community a project, product, or just generally something interesting.

We'll specifically compare these two types of posts to determine the following:

- Do Ask HN or Show HN receive more comments on average?
- Do posts created at a certain time receive more comments on average?

It should be noted that the data set we're working with was reduced from almost 300,000 rows to approximately 20,000 rows by removing all submissions that did not receive any comments, and then randomly sampling from the remaining submissions.

Below are descriptions of the columns:

- <font color=red>id</font>: The unique identifier from Hacker News for the post
- <font color=red>title</font>: The title of the post
- <font color=red>url</font>: The URL that the posts links to, if it the post has a URL
- <font color=red>num_points</font>: The number of points the post acquired, calculated as the total number of upvotes minus the total number of downvotes
- <font color=red>num_comments</font>: The number of comments that were made on the post
- <font color=red>author</font>: The username of the person who submitted the post
- <font color=red>created_at</font>: The date and time at which the post was submited
