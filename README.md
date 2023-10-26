# Bookstore
**Still in progress**

This repository contains the source code for a dynamic e-commerce website built for a fictional bookstore. The project is implemented using Django, a Python web framework, and incorporates features such as book listings, user authentication, shopping cart functionality, and book recommendations.

## Table of Contents
- [Installation](#how-to-install-and-run-the-project)
- [Docker](#docker)
- [Overview](#project-overview)
- [Features](#features)
- [Tools](#technologies-and-frameworks)
- [Tests](#tests)
- [Future plans](#future-plans)

## How to install and run the project?
1. Clone the repository

` git clone https://github.com/Ewa-Anna/Bookstore `

2. Install dependencies

` pip install -r requirements.txt `

3. Change the directory

` cd bookstore `

4. Run the project

` python manage.py runserver `

Project will run on http://127.0.0.1:8000/

## Docker
Building Docker Image
<br>
` docker build -t bookstore . `
<br>
Running Docker Container
<br>
` docker run -p 8000:8000 bookstore `

## Project overview
<div style="text-align: justify;">
The Bookstore is a web-based application developed using Python (Django) for backend and HTML (jinja2), CSS (bootstrap), and JavaScript for frontend to create a user-friendly and feature-rich online bookstore. 
<br>
PostgreSQL is used as the primary database to store core data, such as books, user profiles, and orders and manages critical data. Additionally, Redis is utilized for enhancing user experience through personalized book recommendations tailored to individual interests.
<br>
Its primary purpose is to serve as an online bookstore, offering a range of core functionalities.
</div>

## Features & Future plans
1.	**Book Catalog**: Users can view a list of available books for purchase. Each book is presented with basic information. Users can click on individual books to access detailed information about them, such as the book's description, author, price, and reviews from other users. :heavy_check_mark:
2.	**User Reviews**: Registered users can post reviews and ratings for books they have read. These reviews help other users make informed decisions about their purchases. :heavy_check_mark:
3.	**Search**: User can perform simple search. :heavy_check_mark:
4.	**Tag System**: The project includes a tagging system that allows books to be categorized based on tags. Users can search for books with similar tags, enhancing their browsing experience. :heavy_check_mark:
5. **User Profile**: User can now access basic profile with option to edit their data. :heavy_check_mark:
6.	**Cart**: Users can add books to their shopping cart while browsing the catalog. The cart displays the selected books, their quantities, and the total cost. Users can review and modify their cart contents before proceeding to checkout. :heavy_check_mark:
7. **Order Summary**: A summary of the order is displayed, showing the total cost, quantity and price of the books. Users can review the order details one last time before confirming the purchase. :heavy_check_mark:
1.	**Advanced Search**: Implement an advanced search feature that allows users to filter books by various criteria such as genre, price range, author, and publication date.
2. **Order Confirmation**: Once the user clicks "Submit order" the system processes the transaction, verifies payment information, and generates an order confirmation. Users receive an email confirmation with details of their purchase.
3.	**Advanced User Profiles**: User authentication functionality is implemented, enabling users to create accounts and maintain profiles. In their profiles, users can view their order history and other account-related information.
4.	**Wishlist**: Enable users to create a wishlist where they can save books they intend to purchase later.
5.	**Book Ratings**: Allow users to rate books on a scale and provide detailed feedback. :heavy_check_mark: Display average ratings  :heavy_check_mark: and sort search results by user ratings.
6.	**Social Media Sharing**: Implement social sharing buttons to encourage users to share their favorite books, reviews, and recommendations on social media platforms.
7.	**Discounts and Promotions**: Run promotional campaigns, offer discounts, and provide coupon codes during special events or holidays to attract more users and boost sales.
8.	**Multi-Language Support**: Enable users to access the website in their preferred language. Implement a language selection feature and provide translations for book details and user interface elements.
9.	**Author Pages**: Create dedicated pages for authors, showcasing their biography, other works, and a list of books authored by them. Users can explore books by their favorite authors.
10.	**Book Bundles**: Offer book bundles or sets at discounted prices, encouraging users to purchase multiple related books together.
11.	**Book Availability Notification**: Allow users to subscribe to notifications for out-of-stock books. When a book becomes available, users receive an alert to purchase it.
12.	**Recommendation Engine**: Enhance the book recommendation system by incorporating machine learning algorithms. Provide personalized book suggestions based on users' reading history, preferences, and ratings.


## Technologies and frameworks
- Backend
    
    [![Python](https://skillicons.dev/icons?i=python)](https://skillicons.dev) 
    [![Django](https://skillicons.dev/icons?i=django)](https://skillicons.dev)

- Frontend
    
    [![HTML](https://skillicons.dev/icons?i=html)](https://skillicons.dev)
    [![CSS](https://skillicons.dev/icons?i=css)](https://skillicons.dev) 
    [![JS](https://skillicons.dev/icons?i=javascript)](https://skillicons.dev)

- Databases

    [![PostgreSQL](https://skillicons.dev/icons?i=postgres)](https://skillicons.dev)
    [![Redis](https://skillicons.dev/icons?i=redis)](https://skillicons.dev)

- Other

    [![GitHub](https://skillicons.dev/icons?i=github)](https://skillicons.dev)
    [![VisualStudio](https://skillicons.dev/icons?i=vscode)](https://skillicons.dev)
    [![Docker](https://skillicons.dev/icons?i=docker)](https://skillicons.dev)

## Tests
Run all tests
<br>
``python manage.py test``
