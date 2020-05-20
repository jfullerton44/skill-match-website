# SkillMatch
Welcome to SkillMatch! If you've ever been in a class and didn't know anyone you could reach out to study with, you've come to the right place. This is a Facebook / LinkedIn / Instagram-esque site where you can find study buddies for your classes through our message board and friends list systems!

# How to get started
We'd prefer if you used our actual website link up on Heroku:
	
`http://skillmatch13.herokuapp.com/`

Just point your web browser to that link and get started!

## Local Use
If you want to run the local development server, follow these steps:

- Clone the repo using a terminal and navigate your terminal into the root of the repository.
	
	`git clone https://github.com/UVA-CS3240-S19/project-103-thirteen-reasons-why.git`
	`cd project-103-thirteen-reasons-why.git`

- Run the development server.

	`python3 manage.py runserver`

- Open up a web browser and point it to the following url.

	`http://127.0.0.1:8000/`

You're set up for local browsing! Do note that the database needed by this site will be completely empty though - it won't be very exciting browsing on a completely empty website.

# Navigating through the site
Our site is divided up into a few main sections when you first jump in - more things are visible if you log into the website. The site really opens up once you log in with either the button on the top or in the side bar. Here's how you log in:

- Click the **Log In** button.
- You'll be redirected to a Google login page - use some form of Google email you might have, like a **.virginia.edu** email or **.gmail.com** email.

Anyway, we've got these for you if you just want to browse:

## Discover
Check out the students / professors who've signed up! You can see their skills, classes they've taken, classes they are taking, and study buddies they might already have.

## Posts 
This is the 'forum' part of our site - users can write 'looking for group' - type messages to recruit study buddies, not unlike something you'd see on a large Facebook page.

## Search Bar
Up in the top right, we have a search bar that you can use to look up students, classes, or skills - just type what you want in and the search will return a list of users, classes, and skills that match your query.

## Side Bar
The side bar (click the top right corner) mostly has all of the things above in it.

# After logging in
Upon logging in, notice these changes:

- There's an **Add Friend** button on other peoples' user cards in the **Discover** section. This is how you network with other students.
- A **Your Profile** button appears on top which you can use to edit your profile.
- When you search friends, classes or skills, you'll be able to add them to your list from the search results.
- In the **Posts** section, you'll be able to comment on other peoples' posts or create posts of your own.
- You can filter posts to show only what your friends are sending, or all posts in the database.

The side bar will also receive the same changes.

## Editing your profile
After hitting the **Your Profile** button, you'll be directed to your user profile. Here, you can add classes, skills, and edit your details with one of the appropriately named buttons down (**Edit Profile**, **Add Class**, **Add Skill**) at the bottom. Pick the one you want, and start updating!

## Don't see a class or a skill?
When you hit either **Add Class** or **Add Skill**, you'll be directed to a list of existing classes and skills in our database. If you don't see what you're looking for in this list, hit the button at the top of the list titled **Create New Class** or **Create New Skill**. Here, you can create a new skill by typing in the name of the skill, or create a class. One caveat is that with creating classes, you should adhere to the following format:

- **Prefix**: 2 - 5 character abbreviation of class name, such as ENGR / ENWR.
- **Course Number**: The number of the course you signed up as defined on Lou's List.
- **Professor**: You can enter the professor's whole name, but we'd prefer if you'd use the last name only.
- **Semester**: The season of the semester followed by the year. For instance, Spring 2019 becomes S19.

## How to use the posting system
If you want to recruit buddies, you're going to need to make use of the posting system we've got. 

First, navigate to the **Posts** section. Here, you can respond to other peoples' posts via comments - check for the **Add Comment** button. By default, the posts shown are from your friends, but you can toggle this to all users by clicking the **Show All Posts** button. It'll change to **Show Friend Posts** after this so you can toggle it back.

You can also create your own posts by clicking the **Create Post** button and filling out the form.

# Suggestions?
That's all we've got for our site at present - if you've got more features you'd like us to add, or improvements you'd like us to make, let us know via a private message. Thanks for browsing!

