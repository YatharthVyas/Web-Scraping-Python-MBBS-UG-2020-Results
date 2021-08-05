# Web-Scraping-Python-MBBS-UG-2020-Results

An automated script to fetch automate the process of fetching results of MBBS Undergrad 2020 students using their Seat Numbers.

The code uses string manipulation and doesn't rely on any external library.

It loops over the Seat Numbers to send POST requests to the Form page and then uses string indexes to obtain the necessary information from the response markup.
This is then stored in a dataframe and exported as a csv

Run this Script Online: https://replit.com/@YatharthVyas/Python-POST-form#main.py
