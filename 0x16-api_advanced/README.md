# Reddit API Advanced Tasks :rocket:

This repository contains Python scripts for interacting with the Reddit API to perform advanced tasks. Below is a list of tasks, along with descriptions and links to the respective scripts.

## Table of Contents :bookmark_tabs:

- [0-subs.py](#0-subs.py)
- [1-top_ten.py](#1-top_ten.py)
- [100-count.py](#100-count.py)
- [2-recurse.py](#2-recurse.py)

---

## 0-subs.py :bar_chart:

![Python](https://img.shields.io/badge/Python-3.4%20%7C%203.8%20%7C%203.9-blue)

This Python script, `0-subs.py`, queries the Reddit API and retrieves the number of subscribers (total subscribers, not active users) for a given subreddit. It checks for the validity of the subreddit and returns the count, or 0 if the subreddit is invalid.

:arrow_right: [0-subs.py Script](0-subs.py)

---

## 1-top_ten.py :fire:

![Python](https://img.shields.io/badge/Python-3.4%20%7C%203.8%20%7C%203.9-blue)

The Python script, `1-top_ten.py`, queries the Reddit API to retrieve and print the titles of the first 10 hot posts listed for a specified subreddit. It adheres to the requirements of not following redirects for invalid subreddits.

:arrow_right: [1-top_ten.py Script](1-top_ten.py)

---

## 100-count.py :bar_chart:

![Python](https://img.shields.io/badge/Python-3.4%20%7C%203.8%20%7C%203.9-blue)

`100-count.py` is a Python script that uses recursive functions to query the Reddit API, parse the titles of hot articles, and print a sorted count of specified keywords. The code counts the keywords based on their occurrences in post titles, and the results are printed in descending order by count, and alphabetically for keywords with the same count.

:arrow_right: [100-count.py Script](100-count.py)

---

## 2-recurse.py :repeat:

![Python](https://img.shields.io/badge/Python-3.4%20%7C%203.8%20%7C%203.9-blue)

The Python script `2-recurse.py` is designed to recursively query the Reddit API and retrieve information about all hot articles in a subreddit. It returns a list of dictionaries, each representing an article's title, hotness score, number of comments, and unique identifier.

:arrow_right: [2-recurse.py Script](2-recurse.py)

---

These scripts provide various functionalities for interacting with the Reddit API and can be used to retrieve information about subreddits and their posts, making them useful tools for working with Reddit data. Enjoy exploring and using them!

:memo: _This README was generated with ❤️ using markdown._


