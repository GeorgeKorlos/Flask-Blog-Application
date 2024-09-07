# Flask Blog Application

This Flask application fetches blog posts from an external API and displays them on a webpage. Users can view a list of posts or click on individual posts to see more details.

## Features
- Fetches blog posts from a remote API using the `requests` library.
- Displays all blog posts on the homepage.
- Allows users to click on a blog post to view more details about it.

## Setup Instructions

### Requirements
- Python 3.x
- Flask
- Requests library

### Install Dependencies
To install the required libraries, run:
  ```bash
  pip install Flask requests
  ```

##Running the Application##
1. Clone or download the project to your local machine.
2.Run the Flask application by executing:
  ```bash

  python main.py
  ```
3. Open a web browser and navigate to `http://127.0.0.1:5000/` to view the blog posts.
   
##Application Structure##
- The app fetches blog posts from a JSON API using the URL https://api.npoint.io/c790b4d5cab58020d391.
- On the home page (/), it displays a list of all the posts.
- Each post has an ID, and users can access a specific post by navigating to `/post_id`, e.g., `/1` to view the first post.

###Templates###
`index.html`
This template displays the list of all blog posts with links to view individual posts.

`post.html`
This template shows the details of a single blog post when clicked from the main page.

###External API###
The blog posts are fetched from https://api.npoint.io/c790b4d5cab58020d391
