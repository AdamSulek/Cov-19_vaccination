# Cov-19_vaccination
Covid 19 vaccination registration program

Project created for covid 19 vaccine registration.

The site administrator can add places where the vaccination program is carried out. The user can register for an account in which they have access to submit a vaccination form. The form is only visible for the site administrator and contains information about the user's diseases and health history. The form is connected to a table of the place where the vaccination is to be carried out, and the date of the vaccination is set, not to overlap with other dates of users of the given place.

A patient can only register for a vacant vaccination appointment, except in the case of a priority, in which case the patient will be informed of the need to reschedule. Once the form has been submitted correctly, the user will receive an email notification of the vaccination location and date. Certain fields on the form determine the priority of the vaccination date (thrombosis - risk group, referred for medical consultation, cancer tendency and history of transplantation - generate the priority of the vaccination date).

The table layout that makes up the database is included in the database_scheme.tif file.

This project use SQlite as a backend database with Django.

## Setup
### Setup virtual environment
`virtualenv -p python3 venv/`

`source venv/bin/activate`

### Install packages
`pip3 install -r requirements.txt`

### Migrate and start server
`python3 manage.py migrate`

`python3 manage.py runserver`
