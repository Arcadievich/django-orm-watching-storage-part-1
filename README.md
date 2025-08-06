# Bank Security Console

This is an internal repository for employees of Radiance Bank. If you got into this repository by accident, you will not be able to run it, since you do not have access to the database, but you can freely use the layout code or see how database queries are implemented.

## How to install

Python3 should be already installed. Then use pip (or pip3, if there is a conflict with Python2) to install dependencies:

`pip install -r requirements.txt`

You also need to create a file `.env` in the same folder where the file is located `main.py`. In it, you must declare 3 environment variables: `SECRET_KEY`, `ADDRESS` and `PASSWORD`.


- `ADDRESS` - Your website address.
- `PORT` - Specify the connection port
- `NAME` - Database name
- `USER` - Username
- `PASSWORD` - The password for the database on the website.
- `SECRET_KEY` - It must contain the secret key to your website.

## An example of a successful script launch

![example](https://pouch.jumpshare.com/preview/7B9TmhLTEKVBxIt5N3hPprryWJJ-Hhe1cIDOPm63d5yTZn1nJeINkZ2IKxOZRWzHyCmXxW0aX77REwSJma5eRdDtWqSUXyOovbeVHxgnKOo)
