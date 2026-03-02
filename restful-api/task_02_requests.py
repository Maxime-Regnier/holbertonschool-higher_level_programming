#!/usr/bin/python3
import requests
import csv
def fetch_and_print_posts():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    print(f"Status Code: {response.status_code}")
    if response.status_code == 200:
        data = response.json()
        for post in data:
            print(post["title"])
def fetch_and_save_posts():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    if response.status_code == 200:
        data = response.json()
        data_list = [{"id": post["id"], "title": post["title"], "body": post["body"]} for post in data]
        with open("posts.csv", "w", newline="") as csvfile:
            fieldnames = ["id", "title", "body"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data_list)