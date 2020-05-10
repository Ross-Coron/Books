# CS50W - Project 1: Books

Hello, World! This is my submission for CS50W's [Project 1: Books](https://docs.cs50.net/web/2019/x/projects/1/project1.html).

This website is for reviewing books. The application allows users to register / login / logout, search for books, leave a review for individual books, and see reviews made by other people. The application also allows users to see book information and reviews made by other people using the Goodreads API. Finally, book details and reviews can be queried programmatically via a custom API.

A short video demonstrating the website can be found [here](https://www.youtube.com/watch?v=OM04rpB4_1o&t=1s).

## Getting Started:

 1. Set `api_key` environment variable to your Goodreads API key.
 2. Set `secret_key` environment variable to your Flask secret key.
 3. Set `DATABASE_URL` environment variable to the address of your Heroku database.
 4. When in the same directory as `application.py`, execute `flask run` to launch the application.

## Files

 - All files stored within the `project1` directory.
 - CSS and image files stored within the `static` directory.
 - HTML files stored within the `templates` directory.
 - Website Flask / Python code stored within `application.py`.
 - `books_tables`: SQL code for three database tables.
 - `books.csv`: CSV file of 5000 books
 - `import.py:` Python code to upload CSV file contents to a database table.

## API

To view a book's details in JSON format, navigate to `.../api/ISBN_NUMBER`. JSON returns data in the following format:

```
{
    "title": "Memory",
    "author": "Doug Lloyd",
    "year": 2015,
    "isbn": "1632168146",
    "review_count": 28,
    "average_score": 5.0
}
```
##
