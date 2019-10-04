#!/usr/bin/env python
# coding: utf-8

# Project1-Exploring Hackers News Posts¶
# First, we'll read in the data and remove the headers.

import csv
from datetime import datetime

# read in the data
file = open("hacker_news.csv")
data = csv.reader(file)
hn = list(data)

hn[0:5]#display first 5 rows

headers = hn[0]#First assigning header to variable headers
hn = hn[1:]# Remove the headers

print(headers)
print(hn[0:5])#printing to make sure header is removed

# Identify posts that begin with either `Ask HN` or `Show HN` and separate the data into different lists.
ask_posts = []#creating empty list for Ask HN
show_posts = []#creating empty list for Ask HN
other_posts = []#creating empty list for Ask HN

for item in hn:#looping through each rom in title column
    title = item[1]#titile column is 2nd column
    if title.lower().startswith("ask hn"):
        ask_posts.append(item)
    elif title.lower().startswith("show hn"):
        show_posts.append(item)
    else:
        other_posts.append(item)
        
print(len(ask_posts))
print(len(show_posts))
print(len(other_posts))

# Calculate the average number of comments `Ask HN` posts receive.
total_ask_comments = 0
for item in ask_posts:
    total_ask_comments += int(item[4])
    
avg_ask_comments = total_ask_comments / len(ask_posts)
avg_ask_comments

# Calculate the average number of comments `Show HN` posts receive.
total_show_comments = 0

for post in show_posts:
    total_show_comments += int(post[4])
    
avg_show_comments = total_show_comments / len(show_posts)
print(avg_show_comments)

# Calculate the amount of ask posts created during each hour of day and the number of comments received.
import datetime as dt

result_list = []

for post in ask_posts:
    result_list.append(
        [post[6], int(post[4])]
    )

comments_by_hour = {}
counts_by_hour = {}
date_format = "%m/%d/%Y %H:%M"

for each_row in result_list:
    date = each_row[0]
    comment = each_row[1]
    time = dt.datetime.strptime(date, date_format).strftime("%H")
    if time in counts_by_hour:
        comments_by_hour[time] += comment
        counts_by_hour[time] += 1
    else:
        comments_by_hour[time] = comment
        counts_by_hour[time] = 1

comments_by_hour

# Calculate the average amount of comments `Ask HN` posts created at each hour of the day receive.
avg_by_hour = []

for hr in comments_by_hour:
    avg_by_hour.append([hr, comments_by_hour[hr] / counts_by_hour[hr]])

avg_by_hour


# Sorting and Printing Values from a List of Lists

swap_avg_by_hour = []# Create a empty list that equals avg_by_hour with swapped columns.

#Iterate over the rows of avg_by_hour and append to swap_avg_by_hour...
#...a list whose first element is the second element of the row, 
#...and whose second element is the first element of the row.
for row in avg_by_hour:
    swap_avg_by_hour.append([row[1], row[0]])
    
print(swap_avg_by_hour)

# Using the sorted() function to sort swap_avg_by_hour in descending order. 
#Since the first column of this list is the average number of comments,..
#..sorting the list will sort by the average number of comments.
sorted_swap = sorted(swap_avg_by_hour, reverse=True)

sorted_swap

# Sort the values and print the the 5 hours with the highest average comments.

print("Top 5 Hours for 'Ask HN' Comments")
for avg, hr in sorted_swap[:5]:
    print(
        "{}: {:.2f} average comments per post".format(
            dt.datetime.strptime(hr, "%H").strftime("%H:%M"),avg
        )
    )

