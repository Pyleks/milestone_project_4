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
7. [Testing Summary](#Testing-Summary)
8. [Deployment](#Deployment)
9. [Credits](#Credits)
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


![Main Page Desktop](https://github.com/Pyleks/Milestone-Project-3/blob/master/static/wireframes/Main%20Page%20Desktop.png)
![Main Page Tablet](https://github.com/Pyleks/Milestone-Project-3/blob/master/static/wireframes/Main%20Page%20Tablet.png)
![Main Page Phone](https://github.com/Pyleks/Milestone-Project-3/blob/master/static/wireframes/Main%20Page%20Phone.png)

</details>

<details>
<summary>Product Page</summary>
<br>

![Recipe Page Desktop](https://github.com/Pyleks/Milestone-Project-3/blob/master/static/wireframes/Recipe%20Page%20Desktop.png)
![Recipe Page Tablet](https://github.com/Pyleks/Milestone-Project-3/blob/master/static/wireframes/Recipe%20Page%20Tablet.png)
![Recipe Page Phone](https://github.com/Pyleks/Milestone-Project-3/blob/master/static/wireframes/Recipe%20Page%20Phone.png)

</details>

<details>
<summary>Profile Page</summary>
<br>

![Profile Page Desktop](https://github.com/Pyleks/Milestone-Project-3/blob/master/static/wireframes/Profile%20Page%20Desktop.png)
![Profile Page Tablet](https://github.com/Pyleks/Milestone-Project-3/blob/master/static/wireframes/Profile%20Page%20Tablet.png)
![Profile Page Phone](https://github.com/Pyleks/Milestone-Project-3/blob/master/static/wireframes/Profile%20Page%20Phone.png)

</details>

<details>
<summary>Administrator Page</summary>
<br>

![Administrator Page Desktop](https://github.com/Pyleks/Milestone-Project-3/blob/master/static/wireframes/Administrator%20%20Desktop.png)
![Administrator Page Tablet](https://github.com/Pyleks/Milestone-Project-3/blob/master/static/wireframes/Administrator%20Page%20Tablet.png)
![Administrator Page Phone](https://github.com/Pyleks/Milestone-Project-3/blob/master/static/wireframes/Administrator%20Page%20Mobile.png)

</details>

<details>
<summary>Create Recipe</summary>
<br>
<p>I overhauled this page, adding 2 new text areas, to add recipe ingredients easier.</p>

![Create Recipe Desktop](https://github.com/Pyleks/Milestone-Project-3/blob/master/static/wireframes/Create%20Recipe%20Page%20Desktop.png)
![Create Recipe Tablet](https://github.com/Pyleks/Milestone-Project-3/blob/master/static/wireframes/Create%20Recipe%20Page%20Tablet.png)
![Create Recipe Phone](https://github.com/Pyleks/Milestone-Project-3/blob/master/static/wireframes/Create%20Recipe%20Page%20Mobile.png)


## Design Decisions
The design decisions here is following the Django Code Institute tutorial quite closely to get as much as possible
working properly in the final product, but everything is simplified enough to make the user experience very
straight forward, allowing for quick navigation.

#### Color Scheme

Need to add color scheme

The current set of colors are all very bland but contrasting to make sure all the buttons and navigation is easy to
identify for the visitor, and to make sure no colors "drown" out as they navigate through everything.

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
- W3 HTML Validator using URL and copy/paste code
- W3 CSS Validator
- JS Hint
- PEP8





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
   </ol>

