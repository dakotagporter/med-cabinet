# Med Cabinet

## Description
Help patients find specific cannabis strains to help battle any medical conditions or ailments. Allow users to provide various inputs as search parameters. A search bar allows for specific retrieval of a strain of choice. Check boxes and dropdowns on the side allow for a more generalized searching experience. More specfically, a description box grants a user the power to search strains that are as similar as possible to their desires.

## API
A Flask micro-framework API runs on the backend to provide functionality to our web application. No database has been used for this project. Having only small amounts of data, we have decided to store and parse JSON data instead.

## Models
Natural Language Processing is implemented to take a user's description input and process it to be compared and visualized with the description of the strain currently in our data. A clustering algorithm is able to then return the most closely related strains using their input.

## Accessability and Installation
Our web application will soon be deployed on Heroku.
