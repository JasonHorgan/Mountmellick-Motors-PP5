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

The finance page is broken up into 3 pages, Finance info, Finance application and finance success. I initially wanted all users of the site to be able to access this site, which in turn will generate more leads for the car dealership, however this was causing an error, so I changed it so that only logged in users can access the finance pages. I included buttons to the finance application form on the stock page for logged in users to drive more traffic and increase leads. 

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

**Authentication**

Description:

Ensure a user can sign up to the website

Steps:

1. Navigate to [Mountmellick Motors Sign Up](https://mountmellick-motors-59b177d11415.herokuapp.com/accounts/signup/) 
2. Enter email, username and password
3. Enter Password again
4. Click Sign up

Expected:

Another page pops up advising a confirmation email has been sent to the email entered.

An email is then sent to the email address entered in preivious screen. There are different emails that are sent based on the circumstances:

Account already exists with the email entered email template.
Account confirmation email sent to the email entered which includes a link that the user clicks on to complete account registration. 

Result:

Working as expected.
<hr>

Description:

Ensure that registered users are able to log in.

Steps:
1. Navigate to [Mountmellick Motors Log in](https://mountmellick-motors-59b177d11415.herokuapp.com/accounts/login/) 
2. Enter login details
3. Click login

Expected:

User is successfully logged in and redirected to the home page with a toast messaging advising successful login, but if their log in details are incorrect, they see an error message letting them know their username or password is wrong

Result:

Working as expected.

![wrong password]<img src="/static/images/readme-images/wrong_pw.png">
![Login Success]<img src="/static/images/readme-images/login_success.png">

<br>

Description:

User's can sign out

Steps:

1. User logs into their account
2. User clicks the sign out button
3. User clicks sign out button again when asked to reconfirm

Expected:

User is logged out and brought back to home page and a toast message is shown advising they have logged out.

Result:

Working as expected

![logout success]<img src="/static/images/readme-images/logout_success.png">

Description:

Logged out users can purchase a vehicle

Steps:

1. Navigate to [Stock]( https://mountmellick-motors-59b177d11415.herokuapp.com/stock/ ) 
2. Click on the vehicle you want to purchase so the stock info page opens
3. Click Add to bag
4. Click Shopping bag icon on the top right of the page to open the bag
5. Click Secure Checkout button to open checkout page
6. Fill in all required info 
7. Checkout Success page opens with an order number and order summary
8. Confirmation email is received 

Expected:

Order is successful and user receives confirmation email

Result:

Working as expected

![Order Success]<img src="/static/images/readme-images/order_success.png">


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

I initially wanted all users of the site to be able to access this site, which in turn will generate more leads for the car dealership, however this was causing an error, so I changed it so that only logged in users can access the finance pages. I also changed the nav bar so that finance is only shown to logged in users.

# Deployment

### Creating a Database

Below you will find all of the steps for creating a database using PostgreSQL from Code Institute:

- Navigate to PostgreSQL from Code Institute
- Enter your student email address in the input field provided
- Click Submit
- Wait while the database is created
- Your database is successfully created! Please review the email sent to your student email inbox

Now that we have a new database instance created, in the next step we’ll create a Heroku app to connect to.

Let’s create this app now. Log into Heroku and go to the Dashboard.

1: Click New to create a new app
2: Give your app a name and select the region closest to you. When you’re done, click Create app to confirm
3: Open the Settings tab
4: Add the config var DATABASE_URL, and for the value, copy in your database url from your PostgreSQL from Code Institute email. It should look something like this

<img src="/static/images/readme-images/config-var.png">

5: Leave this tab open as well, we’ll return here shortly

Now we can set up our project to connect to our PostgreSQL from Code Institute database, create our database tables by running migrations, add our shops fixtures, and confirm that it all works by creating a superuser.

Open up your IDE tab and follow the steps below.

1: In the terminal, install dj_database_url and psycopg2, both of these are needed to connect to your external database.

2: Update your requirements.txt file with the newly installed packages

3: In your settings.py file, import dj_database_url underneath the import for os

4: Scroll to the DATABASES section and update it to the following code, so that the original connection to sqlite3 is commented out and we connect to the new database instead. Paste in the database URL from your PostgreSQL from Code Institute email in the position indicated

<img src="/static/images/readme-images/database_instructions.png">

5: In the terminal, run the showmigrations command to confirm you are connected to the external database

6: If you are, you should see a list of all migrations, but none of them are checked off

7: Migrate your database models to your new database

8: Load in the fixtures.

9: Create a superuser for your new database

<img src="/static/images/readme-images/create_superuser.png">

10: Finally, to prevent exposing our database when we push to GitHub, we will delete it again from our settings.py - we’ll set it up again using an environment variable shortly - and reconnect to our local sqlite database. For now, your DATABASE setting in the settings.py file should look like this

<img src="/static/images/readme-images/database_instructions_2.png">


### Deploying to Heroku

In these text-based steps, we will configure and deploy our e-commerce application to the web.

It is not secure to have your SECRET_KEY variable committed to GitHub, so we will create a new secret key and hide it in our environment.

Add the following code to env.py in the root directory of your project. You can use a service such as https://randomkeygen.com/ to generate secret keys.

"os.environ.setdefault('SECRET_KEY', 'Your secret key here')"

In settings.py, update the SECRET_KEY value to the following code. This code will access the SECRET_KEY variable from the environment instead of hard-coding it into our settings.py file.

"SECRET_KEY = os.environ.get('SECRET_KEY')"

If you don't already have an env.py file, you will also need to:

import os at the top of the env.py file.
import env at the top of the settings.py file.

#### Preparing our project for deployment

1. In settings.py, locate the DATABASES settings

2. Update the code to this:

if 'DATABASE_URL' in os.environ:
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    }
else: 
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

This code will ensure that our development environment can continue to access our local SQLite database and that our deployed site can simultaneously access the separate database we created in the last topic.

3. Next, locate where the env module is imported into settings.py.

4. As your env.py file is not committed to Git (in order to keep your environment variables secret), your Heroku app will not be able to access this file and will throw an error. To prevent this, update the code to check if the file exists in the environment first before trying to import it:

Note: Your Heroku app will access its environment variables from the Heroku Config Vars.

5. Next, we need to create a Procfile in the root directory of our project.

Important: The Procfile must start with a capital P, and it has no file extension.

6. Inside the Procfile

we will tell Heroku to create a web dyno and run gunicorn to serve our Django app:

web: gunicorn mountmellick_motors.wsgi

This declaration assumes that your the main django project folder for your app is named mountmellick_motors, this will need to be updated to your project name 
Note: the space after the colon
Note: gunicorn mountmellick_motors.wsgi is the command Heroku will use to start the server. It works similarly to python3 manage.py runserver.
Note: gunicorn is a production equivalent of the manage.py runserver used in development but with speed and security optimisation.

7. To ensure that Heroku uses the correct version of Python to work with all the project's dependencies, add a runtime.txt file to the root directory. Inside it, add the following line of code with whichever version of Python you are using:

python-3.11.11

8. A final change we need to make to settings.py is to add our Heroku app hostname. To get this, return to your Heroku app dashboard, and click the Open app button.

9. Copy the URL for your app.

10. In settings.py, add the URL for your app to the ALLOWED_HOSTS.

Important: Remove https:// from the start of the URL, and the trailing slash from the end of the URL:

#### Installing gunicorn 

1. In the terminal, install gunicorn:

pip3 install gunicorn (or pip install gunicorn, depending on your operating system)

2. Freeze your updated dependencies into the requirements file with:

pip3 freeze --local > requirements.txt

3. Save, commit and push all your changes to GitHub.

#### Preparing Heroku settings for deployment

1. In your Heroku application, navigate to the app settings.

2. Open the Config Vars.

3. Create a new environment variable called DISABLE_COLLECTSTATIC, and give it a value of 1.

For our initial deployment, we need to temporarily disable Heroku from collecting static files from our project. This step prevents Heroku from uploading static files, such as CSS and JS, during the build. In a future topic, we'll set up an AWS account to manage these files. For now, the DISABLE_COLLECTSTATIC environment variable will prevent deployment errors, allowing us to successfully deploy our site without accessing static files.

4. Create a new environment variable called SECRET_KEY, and set its value to a random string. Your Heroku secret key should not be the same as the one set in your env.py file. You can use a service such as https://randomkeygen.com/ to generate secret keys.

#### Deploying the app

1. On your Heroku app dashboard, select the Deploy tab.

2. Here, we will connect our Heroku app to our GitHub repository and deploy our project. Scroll to the Deployment method and select GitHub

3. Search for your repository name, then click Connect

4. Click the Enable Automatic Deploys button. This will ensure that any time you push new code to your GitHub repository, Heroku will deploy the updated application.

5. Click Deploy Branch to deploy your project.

6. Watch the build log as it runs. You can view the build output in the application's Activity tab in the dashboard. This build may take several minutes to complete.

7. Click the Open app button at the top of the page to open your app. It will look odd without the static files connected, but the links should work. If you navigate to a shop category, you should be able to see product images.

#### Conditionally setting DEBUG

1. Once you confirm that your project has deployed—albeit without the static files connected—we'll conditionally set DEBUG to True only in the development environment.

Important: Setting DEBUG to True leaves your site vulnerable to security issues. Therefore, it must be set to False when deployed.

In settings.py, update the DEBUG value to True only if an environment variable named DEVELOPMENT is present.

DEBUG = 'DEVELOPMENT' in os.environ

2. In env.py, add a new environment variable for DEVELOPMENT and set it to '1'

os.environ.setdefault('DEVELOPMENT', '1')
Then, commit and push your changes to GitHub.

Note: Your product images will no longer show on Heroku now that DEBUG is set to False. Don't worry; in the next section, we'll host them with AWS.

#### Removing paid-for Postgres add-on

Due to a Heroku automation, Heroku automatically assigns you a paid-for Postgres database add-on despite the fact that you are not using their database service for your application. To prevent getting charged for this add-on, you can remove it with the following steps:

1. In your Heroku app dashboard, click the Resources tab:

2. Next to Heroku Postgres, click the chevron button on the far right.

3. Select Delete Add-on

4. Type your app name, then click Remove add-on


In the next topic, we'll get an AWS account set up and start configuring S3 to host our static files and product images.

### Amazon Web Services

We will use Amazon web services to host our static files. Here are the steps on how to set this up and connect it to the project:

#### Step 1:

- Sign in or create an account on  [AWS](https://signin.aws.amazon.com/)

1. Type ‘s3’ into the search bar
2. Click on S3
3. Click the "Create a new bucket button"

To create the new bucket:

1. Enter a bucket name
2. Select ‘ACLs enabled’
3. Select ‘Bucket owner preferred’
4. Deselect ‘Block all public access’
5. Check the box to acknowledge the risk of public access
6. Leave the other options unchanged and click ‘create bucket’

#### Step 2 - Enable static website hosting

When the bucket is created, click on the bucket name to view the bucket details:
Click on the ‘Properties’ tab:
Scroll down to the ‘static website hosting’ section and click ‘Edit’:
1. Click ‘Enable’
2. Enter ‘index.html’ (without quotes) into the Index document input
3. Enter ‘error.html’ (without quotes) into the Error document input
4. Click ‘Save changes’

#### Step 3 - Change CORS configuration

Click on the permissions tab:
Scroll down to the Cross-origin resource sharing (CORS) section and click ‘Edit’

1. Add the following code for the CORS settings

[
{
"AllowedHeaders": ["Authorization"],
"AllowedMethods": ["GET"],
"AllowedOrigins": ["*"],
"ExposeHeaders": []
}
]

2. Click ‘Save changes’


#### Step 4 - Add a bucket policy

On the Permissions tab of your S3 bucket, scroll to the ‘Bucket policy’ section and click ‘Edit’:
Click ‘Policy Generator’:
This will open in a new tab.

1. For the policy type you can select ‘S3 Bucket Policy’
2. For the principal you can enter “*” without quotes
3. For the Action select ‘GetObject’ from the dropdown

Then go back to the bucket policy editor in the other tab and click the copy button to copy the ARN:

Then go back to the Policy Generator in the other tab
1. Paste the ARN into the ARN input
2. Click ‘Add Statement

Scroll down and click ‘Generate Policy’:

Copy all of the text in the popup:

Go back to the policy editor in the other tab and paste in the policy code.

Edit the ‘Resource’ value by adding /* to the end, to allow access to all objects within the bucket

It should look like this, but instead of YOUR_ARN you will have your actual ARN:

It should look like this, but instead of YOUR_ARN you will have your actual ARN:
{
"Version": "2012-10-17",
"Id": "Policy1720032710777",
"Statement": [
{
"Sid": "Stmt1720024120521",
"Effect": "Allow",
"Principal": "*",
"Action": "s3:GetObject",
"Resource": "YOUR_ARN/*"
}
]
}

Scroll to the bottom and click ‘Save Changes’:

#### Step 5 - Edit the Access Control List (ACL)

Back on the Permissions tab, scroll down to the Access control list section and click ‘Edit’:
On the ‘Edit Access control list’ page:
1. Click ‘List’ in the Everyone (public access)
2. Click the checkbox to indicate that you understand the effects of the changes
3. Click ‘Save changes’


#### Creating AWS Groups, Policies and Users

#### Step 1 - Create a user group

1. Search for ‘iam’ in the search bar at the top
2. Click on ‘IAM’

Click ‘User Groups’ on the left:
Click ‘Create Group’:
Enter a group name: (here I’ve used ‘manage-test-bucket’ as the name of the bucket is
‘test-bucket’)
Scroll down to the bottom and click ‘Create user group’:

#### Step 2 - Create a Policy

Click ‘Policies’ in the menu to the left:
Click ‘Create Policy’:
1. Click the ‘JSON’ tab
2. Click the ‘Actions’ dropdown
3. Click ‘Import policy’

1. Search for ‘s3’
2. Select ‘AmazonS3FullAccess’
3. Click ‘Import Policy’

1. Search for ‘s3’ at the top
2. Right click ‘S3’
3. Click ‘Open in a new tab’

In the new tab:
1. Select your bucket
2. Click ‘Copy ARN’

Go back to the previous tab and add your ARN in quotes to the ‘Resource’ list twice, for the
second one add /* after the ARN.
For example my ARN is
arn:aws:s3:::test-bucket-demo-2024

so the two lines I’ve added are:
"arn:aws:s3:::test-bucket-demo-2024",
"arn:aws:s3:::test-bucket-demo-2024/*"

Scroll to the bottom and click ‘Next’:

Enter a policy name and description:

Scroll down and click ‘Create policy’:

You’ll see a success message.

#### Step 3 - Attach the policy to the group

Click ‘User groups’ in the menu to the left:

Click your group:
1. Click the ‘Permissions’ tab
2. Click the ‘Add permissions’ dropdown
3. Click ‘Attach policies’

1. Search for your policy (you can search for the policy name or description that you
entered previously)
2. Select the checkbox beside your policy
3. Click ‘Attach policies’

#### Step 4 - Create a User

1. Click ‘Users’ in the menu to the left
2. Click ‘Create user’

1. Enter a user name
2. Click ‘Next’

1. Select the group you created previously
2. Click ‘Next’

Scroll down and click ‘Create user’:

#### Step 5 - Create an Access Key

Click on your new user:
Click ‘Security credentials’:
Scroll down to the ‘Access keys’ section and click ‘Create access key’:
1. Select ‘Application running outside AWS’
2. Click ‘Next’

Click ‘Create access key’:

1. Scroll down and click ‘Download .csv file’
2. Click ‘Done’

Open the .csv file in any text editor (such as Notepad on Windows, TextEdit on Mac). 

Note that the values are separated by a comma, a common mistake is to see the forward slash
as separating the values, but it’s actually part of the last value:

Use the values as your AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY heroku
config vars:

install boto3
install django-storages
freeze to requirements.txt
add storages to installed apps in settings.py:

if "USE_AWS" in os.environ:
    # Bucket Config
    AWS_STORAGE_BUCKET_NAME = "mountmellick-motors-pp5"
    AWS_S3_REGION_NAME = "eu-north-1"
    AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
    AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com"


Go to heroku to set up enviromental variables
open CSV file downloaded earlier and copy each variable into heroku Settings

AWS_STORAGE_BUCKET_NAME AWS_ACCESS_KEY_ID from csv AWS_SECRET_ACCESS_KEY from csv USE_AWS = True remove DISABLE_COLLECTSTATIC variable from heroku

Create file in root directory custom_storages.py:

from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage

Go to settings.py, add the AWS settings

To load the media files to S3 bucket
Go to your S3 bucket page on AWS. Create new folder "media"
go to the media folder and click Upload


# Credits

# Resources

- Project setup and general skeleton and functionality of the site was based on the CI boutique ado walkthrough.
- Bootstrap 4 library was used for this project's general HTML layout. 
- I used [STACK OVERFLOW](https://stackoverflow.com/) for help with debugging errors throughout the project.
- [W3SCHOOLS](https://w3schools.com/) was used as a guide to help me understand Django and its features.
- CI Slack channel student chat as a troubleshooting/general source of info
- [OpenAI](https://openai.com/) - Troubleshooting bugs, text for website and for help with media queries/CSS
- Photos of cars for sale were taken from public adverts on [Done Deal](https://www.donedeal.ie/motor) 
- Deployment section of readme was written step by step using the deployment section of the boutique ado walkthrough along with its step by step guides for setting up AWS.



### Media

- Text sections derived from [OpenAI](https://openai.com/dall-e-2) and then tweaked to sound more natural.
- Privacy Policy generated from [Privacy Policy Generator](https://privacypolicygenerator.info/).
- Favicon was taken from [Wikipedia](https://it.m.wikipedia.org/wiki/File:Mountmellick_Coat_of_Arms.png) and then resized 

### Acknowledgements

I want to thank code institute staff for all their help throughout the year but especially to my Mentor Graham who offered a lot of much needed support throughout the year. Thank you to my cohort facillitator Marko for all of his guidance through the year too and also to the CI mentor and Student care team. Finally to my family for keeping me on track throughout the year to ensure I stayed focused and got it complete. 


