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
Needs to be accomplished.


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




