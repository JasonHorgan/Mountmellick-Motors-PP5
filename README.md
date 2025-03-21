# Mountmellick Motors
### Car dealership E-Commerce Business

### [Link to the live site](https://mountmellick-motors-59b177d11415.herokuapp.com/)


### Overview

For my final project of this course I have decided to build a Car Dealership E-Commerce site. I decided to build a car dealership site as the company I currently work for builds websites for Irish Car dealers and I felt this would be a good way to showcase the skills I have learned throughout the year at the code institute. Although purchasing a car outright is not something we would typically do online, I felt this would be a fun take on an e-commerce store and is easily customisable to fit a real world scenario. 

<img src="/static/images/readme-images/mockup.png">


## Site User Goals
The main goals for users of my site would be to browse a wide range of cars for sale in the midlands so they can purchase a new car in their local area without having to travel too far to a bigger city. 
They would also be looking for flexible financing options and the ability to test drive the car so they can be sure they want to buy it and are happy with how it performs which in turn gives them peace of mind.
They also want to be able to simply browse vehicles without having to create an account but can also stay up to date by easily signing up to a newsletter informing them immediately when new stock is available


## Site Owner Goals
The main goals for the site owner are to provide an easy-to-navigate platform where users can browse a diverse range of cars for sale in the Midlands,just as they could in a bigger city.

They also want to be able to offer finance options to make their vehicles more accesible to a cariety of customers, which will help them sell more cars and in turn, generate a greater profit. Facilitating test drives of the cars also shows transparency and builds trust with their local community. 

The site owner also wants to make the site easy for staff to use with the integration of a product management section for superusers, so that staff members can upload new vehicles for sale easily with little room for user error. 

Finally, the site owner wants to keep generating traffic via the newsletter. If the newsletter is easy to sign up to, then users are likely to return when they are notified of new stock on site. 


### Brand Identity & Colour Palette

The brand identity of Mountmellick Motors is supposed to feel local, but professional. The colour scheme used is simple but also maintains a feel of professionalism that a user would expect from a car dealership. I included the Mountmellick crest as the favicon to really hammer home the feeling of a local business but maintain sleekness with the colour scheme used throughout the site and with the hero image. 


### Wireframes

I made a few basic wireframes on Balsamiq so I would have a rough idea of what I wanted the site to look like. Although I did not stick to them entirely, they did give me a good foundation to work with. 

<img src="static/images/readme-images/wireframe.png">
<img src="static/images/readme-images/wireframe2.png">
<img src="static/images/readme-images/wireframe3.png">


## Data Structure
I created a rough data structure on paper first so I would have an idea of how I wanted my models to relate to each other and this really helped me to keep things organised. I have also attempted to complete one online so you can visualise what I was aiming for:



# Agile Development

I did my best to follow the Agile development method by using Github User stories, issues, Kanban board, the Moscow system and milestones. This was a great help in terms of keeping me on track and being able to clearly visualize what work I had completed and what was left to do, as well as planning future implementations.


# User Stories

As mentioned above, I used Github projects to help me keep track of user stories, which can be found here - 

Here are some of the most important user stories:

- #### Set up workspace
As a Developer I can set up my workspace so that I can write my code and follow along to the botique ado walkthrough with ease.

- #### Set up folders and file paths
As a Developer I can set up folders and ensure file paths are correct so that everything works as intended

- #### Create 3 custom models
As a developer I can set up 3 custom models so that I am meeting the minimum pass criteria for this assignment

- #### Set up allauth
As a Developer I can install and set up allauth so that users of my site can create an account and log in

- #### Set up Stripe
As a Developer I can set up Stripe so that users of my site can securely make payments


# Features

I wanted the site to be as easy to use and accessible as possible, so the only pages that require the user to log in or create an account are the test drives bookingpage and the profile page. Only superusers can access the product management page and have access to edit stock on the site. 

## Base

The base.html page contains all of the header and Footer code that is transferred across the site when it is loaded into other pages, as well as other important pages and info such as Javascript, messages, meta tags etc.
The nav is broken up between main-nav.html and mobile-top-header.html to make them both more customisable without taking up too much space on the base file. 

<img src="static/images/readme-images/mobile-nav.png">
<img src="static/images/readme-images/header.png">

I wanted the footer to contain as much info as possible without feeling cramped and overloaded 

<img src="static/images/readme-images/footer.png">

### Index

The index page AKA the home page, is the landing page for the site. I wanted it to be visually appealling and grab the user's attention immediately hence the flashy BMW as the hero image. The user can then see the button for viewing stock too. The home page also contains the Header and Footer, as do all other pages on the site 

<h1><img src="/static/images/readme-images/home.png"/></h1>

### About

I kept the about page very simple. It just gives a few key details about the dealership and why they should choose mountmellick motors for buying their next vehicle. 

<h1><img src="/static/images/readme-images/about1.png"/></h1>
<h1><img src="/static/images/readme-images/about2.png"/></h1>


### bag

The bag contains all the contents of the users shopping bag. Heavily inspired by the boutique ado walkthrough. 

<h1><img src="/static/images/readme-images/bag.png"/></h1>

### Checkout

The checkout along with stripe implementation were taken directly from the boutique ado walkthrough. I really enjoyed this part of the walkthrough as I know Stripe is a very powerful and uselful tool to know how to work with in my future career as a developer. That said, it was also the most challenging part of the walkthrough for me. 

<h1><img src="/static/images/readme-images/checkout.png"/></h1>

### Finance

The finance page is broken up into 3 pages, Finance info, Finance application and finance success. I wanted all users of the site to be able to access this site, which in turn will generate more leads for the car dealership. If the finance applications were locked behind a sign up process, the dealership may lose leads. This is typical of the automotive industry. I also included buttons to the finance application form on the stock page to drive more traffic and increase leads. 

<h1><img src="/static/images/readme-images/finance.png"/></h1>

### Test Drives
The test drive application form is only available to people with an account on site. This is to ensure that if you have a test drive booked, it is stored on your user profile so you can edit and delete your appointment. I did not want this available to just anyone who accesses the site, as this could lead to a lot of bookings and potential no shows. I wanted only serious buyers to have access to test drives, ensuring higher quality leads. 

<h1><img src="/static/images/readme-images/testdrive.png"/></h1>

### Stock
The stock page is the bread and butter for the site. This is where users can find information about all of the cars in stock on the site. I wanted each vehicle to live inside of a bootstrap card with a button for applying for finance or booking a test drive. I think the bootstrap card layout on this page give is a very neat and proffessional feel. I also added edit and delete buttons for super users so they can edit or delete stock from the site. 

<h1><img src="/static/images/readme-images/stock.png"/></h1>

### Profile
The profile was heavily inspired by the boutique ado walkthrough and then further expanded upon by adding test drives to the bottom of the page where the user can edit and delete their test drive bookings too. Users can also save their address info to the checkout and see previous order history.

<h1><img src="/static/images/readme-images/profile2.png"/></h1>

### Newsletter
The newsletter was placed at the top of the footer so it is easily visible. I only wanted one required field of email so this made it really accessible for people to sign up to so they can stay up to date with new stock on the site and in turn increase traffic to the site with returning users. 

<h1><img src="/static/images/readme-images/newsletter.png"/></h1>

### Privacy Policy

I generated a standard privacy policy and linked this in the footer. 

<h1><img src="/static/images/readme-images/privacypolicy.png"/></h1>


### Custom 404 page
Custom 404 page is thrown when a user enters a wrong or invalid link on site

<h1><img src="/static/images/readme-images/404.png"/></h1>

## Features Left To Implement

There are a number of features I would like to implement for future sprints on this site:

- A wishlist so users can save cars they are considering purchasing
- A reviews section which would be linked to an active google profile 
- a searchbar so users can search for specific items or categories
- An accessories tab in the store so users can purchase car accessories
- form validation on test drives booking form so users can only book for a future date
- Instead of paying the full amount for the vehicle, the user pays a deposit to secure the vehicle

# Web Marketing Strategies

In the web marketing module of the course we were tasked with creating a list of questions to consider when creating a marketing plan for our E-Commerce store.

- Who is the target audience for the site?
- Where does the target audience for the site usually look when buying a new car?
- Do they typically use social media?
- What is most important to potential users when buying a new car?
- What do people typically search for when buying a new car?

Short-Tail Keywords:
- Used Cars
- Car Dealership
- Car Finance
- Test Drive
- Buy a Car
- Midlands Cars
- Car Loans
- Affordable Cars
- Best Car Deals
- New Cars

Long-Tail Phrases:
- Used Cars for Sale in the Midlands
- Best Car Dealership in Mountmellick
- Affordable Car Finance Options Ireland
- Test Drive a Car Near Me
- Buy a Reliable Second-Hand Car Locally
- Car Loans for First-Time Buyers Ireland
- Car Finance in the Midlands
- Best Family Cars for Sale in Laois
- How to Apply for Car Finance in Ireland
- Where to Find the Best Car Deals Near Me

## Meta Data

<img src="/static/images/readme-images/meta.png"> 

## Sitemap

I used XML-Sitemaps to generate a sitemap file. I downloaded the xml and included in the repository as advised in the course content.

## Robots

I included a robots.txt file. 

## Social Media Marketing

I created a mockup of a business facebook page for the dealership. I think Facebook is best suited as potential buyers may typically search Facebook marketplace when searching for a new car to purchase

<h1><img src="/static/images/readme-images/facebook.jpg"/></h1>

## Email Marketing
I used Mailchimp to create a newsletter sign up which was then integrated into the footer of the project with only an email address as the required field, to make signing up easy. 

<h1><img src="/static/images/readme-images/newsletter.png"/></h1>

# Technology

- Html 
- CSS 
- Font Awesome 
- Google Fonts 
- Bootstrap 
- Javascript
- Python 
- Django Framework
- GitHub 
- Heroku


# Testing

- HTML Validation

  HTML Code passed validation with no warnings or errors on all pages. All pages gave the same result as in the below screenshot 

  <img src="/static/images/readme-images/HTML_valid_1.png">

- CSS Validation

  CSS code passed through the validator without any issues

  <img src="/static/images/readme-images/css_valid.png">

- Pyhton Linter
  All my .py files passed through the linter without issue. I used the black extension to re-format them all, then manually tested them all one-by-one and manually fixed a few that black did not catch and now they all pass validation. 

  <img src="/static/images/readme-images/pylinter.png">

## Lighthouse testing

My site passed lighthouse testing with no issues that I could find. There was an accessibility issue where the "Privacy policy" text in the footer was blue so it wasn't readable. I changed the text colour to white and re-deployed and then re-tested and now it works and passes lighthouse testing. 

<img src="/static/images/readme-images/lighthouse1.png">
<img src="/static/images/readme-images/lighthouse2.png">
<img src="/static/images/readme-images/lighthouse3.png">

## Manual Testing

I tested all elements of the site myself manually and found no issues. Further details found below 

### Account Registration

| Test |Result  |
|--|--|
| User can create a profile | Pass |
| User receives confirmation email | Pass |
| User can log in | Pass |
| User can log out | Pass |

### User Navigation Tests

| Test | Result  |
|--|--|
| User can access each page | Pass |
| SuperUser can access admin page | Pass |
| Each page on the site is accessible as intended | Pass |

#### Account Authorisation Tests

| Test | Result  |
|--|--|
| Only Superuser can access admin page | Pass |
| Only Superuser can add, update and delete stock | Pass |
| Only superusers can access product management | Pass|

#### Profile

| Test |Result  |
|--|--|
|User can add items to bag | Pass |
|User can delete items from bag | Pass |
|User can edit quantity of items in bag | Pass |
|User can make a purchase with a test credit card | Pass |
|User receives confirmation email when order is successful | Pass |
|User can see the confirmation page when order is successful | Pass |
|All users can submit a finance application | Pass |
|Logged in user can view and update their address on profile page | Pass |
|Logged in User can view order history on profile page | Pass |
|Logged in User can create test drive bookings | Pass |
|Logged in User can view, edit and delete test drives on profile page | Pass |

### Responsiveness

- The website is fully responsive on all screen sizes due to Bootstrap and CSS media queries


### Browser Testing

Browser | Outcome | Pass/Fail |
--- | --- | --- |
Google Chrome | No issues found (appearance/responsiveness)| Pass |
Safari |  No issues found (appearance/responsiveness) | Pass |
Mozilla Firefox |  No issues found (appearance/responsiveness)| Pass |

### Other Testing

I had some friends and family sign up to the site and try to make purchases with the test card and it seemed to work for everyone with no issues found from their testing 

### Known Issues & Bugs
When I was configuring the send email feature for users creating an account and order confirmations, I was getting an error from Django which was due to the version of Django used in my workspace as I used 3.12.8. The fix for this was to create a new file at the project level of the app called "python-version" which tells heroku to use version 3.11 of Django so that the emails would send. Tutoring helped me debug and fix this issue. 

The main issue present on site at the moment is that when users are booking test drives, they can book a date in the past, which should not be possible. I would like to fix this in a future sprint. 

# Deployment

This project was deployed using Heroku. Full details of deployment seen below:

Part 1 - Create the Heroku app:

Navigate to your Heroku dashboard and create a new app with a unique name in a region close to you.
In your new app’s settings tab, ensure the Config Var DISABLE_COLLECTSTATIC key has a value of 1. You should also set your Stripe keys, secret key and Database URL in your config vars section. 

Part 2 - Update your code for deployment:

Use pip3 to install gunicorn~=20.1 and freeze it to the requirements.txt file.
In the settings.py file, set the DEBUG constant to False and append the '.herokuapp.com' hostname to the ALLOWED_HOSTS list.
Git add, commit and push the code to your GitHub repo.

Part 3 - Deploy to Heroku:

In your new app’s Deploy tab, search for your GitHub repo and connect it to the Heroku app. Manually deploy the main branch of this GitHub repo.
In your new app’s resources tab, ensure you are using an eco dyno and delete any Postgres database Add-on.

# Credits

# Resources

- Project setup and general skeleton and functionality of the site was based on the CI boutique ado walkthrough.
- Bootstrap 4 library was used for this project's general HTML layout. 
- I used [STACK OVERFLOW](https://stackoverflow.com/) for help with debugging errors throughout the project.
- [W3SCHOOLS](https://w3schools.com/) was used as a guide to help me understand Django and its features.
- CI Slack channel student chat as a troubleshooting/general source of info
- [OpenAI](https://openai.com/) - Troubleshooting bugs, text for website and for help with media queries/CSS
- Photos of cars for sale were taken from public adverts on [Done Deal](https://www.donedeal.ie/motor) 



### Media

- Text sections derived from [OpenAI](https://openai.com/dall-e-2) and then tweaked to sound more natural.
- Privacy Policy generated from [Privacy Policy Generator](https://privacypolicygenerator.info/).
- Favicon was taken from [Wikipedia](https://it.m.wikipedia.org/wiki/File:Mountmellick_Coat_of_Arms.png) and then resized 

### Acknowledgements

I want to thank code institute staff for all their help throughout the year but especially to my Mentor Graham who offered a lot of much needed support throughout the year. Thank you to my cohort facillitator Marko for all of his guidance through the year too and also to the CI mentor and Student care team. Finally to my family for keeping me on track throughout the year to ensure I stayed focused and got it complete. 


