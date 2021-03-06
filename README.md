# Threads

Welcome to Threads, a e-commerce website with the hottest brands for hoodies and shorts on the market, 1 click away from
finding your next favorite clothing piece.

## Contents
1. [UX](#UX)
2. [Design Decisions](#Design-Decisions)
3. [Database](#Database)
4. [Features](#Features)
5. [Technologies](#Technologies)
6. [Testing](#Testing)
8. [Deployment](#Deployment)
10. [Disclaimer](#Disclaimer)


## User Experience
This have been designed with the idea of giving the visitor a quick access to our inventory of clothing pieces
for both men and women, simple straight forward design allowing for quick and easy shopping experience.

#### User Stories
> Quick access to your new favorite clothing store.

> Looking for a new shirt with a good brand behind it.

> Want to find mixed brand store for a good variation of clothes.

> Want to show my friends where I bough my new hoodie.

> Looking for a safe page to buy my next clothing article.

> Want to buy a shirt or hoodie from a store that provide Free delivery on high orders.

#### WireFrames
<details>
<summary>Main Page</summary>
<br>


![Main Page Desktop](https://github.com/Pyleks/milestone_project_4/blob/master/wireframes/Landing%20Page%20Desktop.png)
![Main Page Tablet](https://github.com/Pyleks/milestone_project_4/blob/master/wireframes/Landing%20Page%20Tablet.png)
![Main Page Phone](https://github.com/Pyleks/milestone_project_4/blob/master/wireframes/Landing%20Page%20Mobile.png)

</details>

<details>
<summary>Product Page</summary>
<br>

![Product Page Desktop](https://github.com/Pyleks/milestone_project_4/blob/master/wireframes/Product%20Page%20Desktop.png)
![Product Page Tablet](https://github.com/Pyleks/milestone_project_4/blob/master/wireframes/Product%20Page%20Tablet.png)
![Product Page Phone](https://github.com/Pyleks/milestone_project_4/blob/master/wireframes/Product%20Page%20Phone.png)

</details>

<details>
<summary>Product Details</summary>
<br>

![Product Details Desktop](https://github.com/Pyleks/milestone_project_4/blob/master/wireframes/Product%20Details%20Desktop.png)
![Product Details Tablet](https://github.com/Pyleks/milestone_project_4/blob/master/wireframes/Product%20Details%20Page%20Tablet.png)
![Product Details Phone](https://github.com/Pyleks/milestone_project_4/blob/master/wireframes/Product%20Details%20Page%20Phone.png)

</details>

<details>
<summary>Shopping Bag</summary>
<br>

![Shopping Bag Desktop](https://github.com/Pyleks/milestone_project_4/blob/master/wireframes/Shopping%20Bag%20Desktop.png)
![Shopping Bag Tablet](https://github.com/Pyleks/milestone_project_4/blob/master/wireframes/Shopping%20Bag%20Tablet.png)
![Shopping Bag Phone](https://github.com/Pyleks/milestone_project_4/blob/master/wireframes/Shopping%20Bag%20Phone.png)

</details>

<details>
<summary>Checkout</summary>
<br>


![Checkout Desktop](https://github.com/Pyleks/milestone_project_4/blob/master/wireframes/Checkout%20Desktop.png)
![Checkout Tablet](https://github.com/Pyleks/milestone_project_4/blob/master/wireframes/Checkout%20Tablet.png)
![Checkout Phone](https://github.com/Pyleks/milestone_project_4/blob/master/wireframes/Checkout%20Phone.png)

</details>

## Design Decisions
The design decisions here is following the Django Code Institute tutorial quite closely to get as much as possible
working properly in the final product, but everything is simplified enough to make the user experience very
straight forward, allowing for quick navigation.

#### Color Scheme

![alt text](https://github.com/Pyleks/milestone_project_4/blob/master/media/Color-Scheme.png)



The current set of colors are used to make strong contrast to each other, making each element "pop" out
so the visitor have clear defined places to go when navigating the e-commerce website.


#### Typography
I choose to use __Roboto__ for all text, which is the same as previous project, especially since this is a
e-commerce site, making the text easy to read, as well being one of the most common e-commerce fonts used.
[Source](https://www.builderfly.com/7-perfect-font-pairing-for-your-ecommerce-website)

## Database
The databases added this time is the built in sqlite3 database that comes with Django during the development cycle
And once moved to Heroku, this changed to Heroku Postgres for the production environment. 

## Features
The current features of this website (Threads) is the simple process of visiting, browsing and buying the listed 
clothing pieces (Shirt and Hoodies).

#### Landing Page
The landing page of the site mainly provides them with a search field, and a shop now button + their total shopping
amount in top right corner.

#### Product Page
This site is listening pictures of all the products available if you access it through the "shop now" button,
However if you arrive by searching for color, gender, type or brand, it will give you a filtered result.

#### Product Details Page
In here you can see all the products from Name, Price, Description, Rating, Quantity, Picture or the 2 buttons
"Keep Shopping" and "Add to Bag".

#### Shopping Bag Page
In the shopping bag you can see all the products you added, as well the number of each article added to the bag,
and you can see the price for each item as well the combined cost of everything you added to the bag.
If needed this page can also be used for removing items from the bag entirely or simply move onwards to Secure Checkout/Keep Shopping.

#### Checkout Page
The final step, where you enter all your information, including personal details as well your credit card into 
STRIPE payment terminal for a safe and secure checkout process, you can also see a full order summery of everything
you are about to purchase.

#### Search Explained
So this is the place where you can add pretty much any keyword of what you are looking for to bring up an item
related to what you searched for, granted it is in our store, this field work with a wide range of keywords.


### Features I wished I knew how to implement
There is mainly 1 feature I wish was properly implemented, and that is the Profile page, to the same extent
As my previous project. 
- Profile Page

## Technologies

### Languages
| Languages  | Usage |
| :------------- | :------------- |
| [HTML](https://www.w3schools.com/html/)  | Creating the entire foundation for the website.  |
| [CSS](https://www.w3schools.com/css/)  | Applying styling across all pages.  |
| [JavaScript](https://www.w3schools.com/js/)  | Mainly used for Stripe  |
| [Python](https://www.python.org/)  | Runs the entire backend server code, (Django) |

### Libraries

|Libraries  |Usage  |
| :-------------| :-------------|
| [Bootstrap](https://getbootstrap.com/)  | Styling Framework to get a modern feel to the website.  |
| [Font Awesome](https://fontawesome.com/)  | Used for all website icons.  |


### Python Libraries and Framework
This list is longer then previous, so only key Libraries are added below.

|Libraries  |Usage  |
| :-------------| :-------------|
| [Django](https://www.djangoproject.com/)  | Required to run all route operations in the code.  |
| [STRIPE](https://stripe.com/en-ie)  | Handling all Payments  |
| [Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/)  | Handling form logic  |
| [Dj Database](https://pypi.org/project/dj-database-url/0.2.2/)  | Provides support between Django and Heroko Postgres database |
| [Certifi](https://stripe.com/en-ie)  | For safe form handling, and verifying the SSL certificate  |


### Database

|Libraries  |Usage  |
| :-------------| :-------------|
| [Heroku Postgres](https://www.heroku.com/postgres)  | Free tier version of Postgres for all database management in production  |


## Testing
Need to be written

__I have tested the following__
- Intended use (Interactivity)  
- Responsiveness across devices
- At this point there is nothing to test as it's all broke on Heroku anyway.  


### Intended Use on Chrome, Firefox and Edge (Interaction)
#### Landing Page
- Opens correctly, showing everything in correct ratio, all icons appears, mouse cursor changes over the icons.  
- All buttons direct to the intended sites, like shop now, search button, home button.  

#### Product Page
- Everything is showing correctly, hoovering over images provides a light feedback from the website where the user is looking.  
- All buttons direct the user to the correct location  
- Search still working inside the product page.  

#### Product Details Page
- All buttons are showing correct, and provides good feedback when hoovering over them with the cursor.  
- All links works correctly.  
- Quantity field is interactive 

#### Shopping Bag Page
- All icons except "Remove" is working correctly, (To be updated later today)
- The update button is refreshing correctly when used.
- Keep Shopping and Secure checkout work as intended.
- Home button is working from here, same with search.

#### Checkout Page
- All icons works correctly
- In writing moment STRIPE is not showing at all (hopefully fixed very soon)
- All information is shown correctly
- Disclaimer - This page is 95% from CI tutorial on (Will also be mentioned on disclaimer section)

#### Search Function Test
- The function works correctly, added additional search for gender.
- Works correctly from all pages
- Issue: When searching for Women or Men it can bring up both genders.

### Responsiveness
In this test the website was tested to all default device sizes provided my chrome as well responsive
slider across Chrome, Firefox and Edge. (This test have been preformed on all projects)

  <ol>
  <li>360 x 640 Galaxy S5</li>
  <li>375 x 667 iPhone 6/7/8</li>
  <li>375 x 812 iPhone X</li>
  <li>411 x 731 Pixel 2</li>
  <li>411 x 823 Pixel 2 XL</li>
  <li>414 x 736 iPhone 6/7/8 Plus</li>
  <li>768 x 1024 iPad</li>
  <li>1024 x 1366 iPad Pro</li>
  <li>540 x 720 Surface Duo</li>
  <li>280 x 653 Galaxy Fold</li>
   </ol>
   

### Functionality
| Page        | Bugs           | Status  |
|:------------- |:-------------| :-----:|
| Main Page     | No issues found | Good |
| Product Page     | No issues found      | Good |
| product Details | No issues found  | Good |
| Shopping Bag | No issues found     | Good |
| Checkout  | Found    | Bad |
| Search  | No issues found     | Good |

### Big issue found (Not fixed yet)
STRIPE is not displaying at all, But hopefully fixed soon.


### Responsiveness
| Page        | Bugs           | Status  |
|:------------- |:-------------| :-----:|
| Bag page     | After re-written into Boostrap grid, it's not scaling correctly | Not Fixed |
| Search  | Do not have a very pretty way of aligning when scaling     | Not Fixed |


> However this is only on local version, on Heroku, non of these things works at all.

## Deployment
1. Go to [GitHub](https://github.com/Pyleks)
2. Click Repositories.
3. Locate Milestone-Project-3.
4. Open [Milestone-Project-3](https://github.com/Pyleks/Pyleks/milestone_project_4)
5. Click the green button clone to download.
6. Or clone from URL using the following command in terminal: <code>got clone https://github.com/Pyleks/Pyleks/milestone_project_4.git</code>

#### 2. Installing Requirements.
Once you have the project cloned on your computer, you are ready to set everything up.  
1. Open the Terminal and navigate to __Milestone-Project-4__ folder on the computer.  
2. Install the libraries from requirements.txt by typing <code>pip3 install -r requirements.txt</code>  

#### Setting up the database
Make sure create a create a free postgres database on Heroku, and preform the database Migration.
The database will provide you a path automatically in the Config Vars

#### Setting up the vars
DISABLE_COLLECTSTATIC = 1
SECRET_KEY = Include that in the vars as well.

# Disclaimer.
Due to time constraints, A ton of this project have been relying heavily on Code Institute tutorial.
Any code that have {#Code Mostly from Code Insitute#}, is code that is mostly from CI

This is for Educational Purpose, and non of the images/prices/descriptions are representing a real store
that will sell any of this.