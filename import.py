# Adds book information to a table from a CSV file.

import csv
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine(os.getenv("DATABASE_URL"))    # Export to terminal.
db = scoped_session(sessionmaker(bind=engine))


def main():

    counter = 0

    f = open("books.csv")    # Open CSV file.
    reader = csv.reader(f)    # Read file 'f'.
    next(reader, None)    # Skip CSV file headers.

    # Loop over the reader. Call first column isbn, etc.
    for isbn, title, author, year in reader:
        # Insert data (: represents placeholder).
        db.execute("INSERT INTO cs50w_books (isbn, title, author, year) VALUES (:isbn, :title, :author, :year)", {
                   "isbn": isbn, "title": title, "author": author, "year": year})
        counter = counter + 1

        # Print when entry added to database. Remove for speed.
        print(f"Counter = {counter}. {title} ({year}), {author}. ISBN: {isbn}. Successfully added to database!")

    # Save changes.
    db.commit()

    print(f"{counter} books added to database table 'cs50w_books'.")


if __name__ == "__main__":
    main()
