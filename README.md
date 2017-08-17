# Realty Mogul Interview Assignment

## My Own Notes
Backend
- For MISSING_DATA_ENCODING: using hyphen to separate encoded missing numbers to prevent ambiguity while keeping it in a relatively compressed format
- Caching CSV read from file to prevent redundant work
- Using prettyjson renderer to make json data more human-readable if accessing from browser

Frontend
- Mostly following smart container/dumb component paradigm
- prop-types - for establishing type consistency when passing props to components
- babel-polyfill - allows for new ES6+ features in older browsers
- async-to-generator Babel plugin to allow async func w/in App.js
- jest/enzyme - Snapshot rendering and helper function tests

## Quick Overview
Congratulations! You've passed our initial round of interviews and we're
curious about your technical chops. Our team is in the business of building
web applications and services and we will be testing you with some of the
tehcnology that we use on a day-to-day basis.

Please clone this repo and follow the installation instructions below to get
set up; once you're set up, your goal is to meet the requirements outlined at
the bottom of this readme.

## Installation Instructions
1. Clone this repo to your machine
2. Create any virtualenvs as necessary
3. If you don't have yarn installed on your machine already, run `brew install yarn`. *If you're not working in an OSX environment, please refer to [these docs](https://yarnpkg.com/lang/en/docs/install/#windows-tab)*
4. `cd rm-fs-code-test`
5. Run `pip install -e .`
6. `cd sampleapp_fe`
7. Run `yarn install`

## Development Instructions

### Front End
1. From the root directory, `cd sampleapp_fe` and run `yarn start` to spin up the webpack-dev-server
2. All code changes will automatically be reflected at **localhost:8080** upon saving
3. When you're done with your frontend code and want it to be served via sampleapp_be, run `yarn build`

---
### Back End
1. From the root directory, run `pserve development.ini --reload`
2. All code changes will be reflected at **locahost:9000**

## Requirements
1. Pyramid backend:
    * Render React application at `/` (This has been setup for you already)
    * Parse the provided CSV file in `sampleapp_be/assets/properties.csv` and serve the results as a JSON object at `/data`
    * Results must contain **only properties in California**, and contain the following:
        1. PROP_NAME
        2. ADDRESS
        3. CITY
        4. STATE_ID
        5. ZIP
        6. MISSING_FIELD_COUNT (number of fields in a record that is missing data)
        7. MISSING_DATA_ENCODING - a number where each digit indicates consecutive columns with and without data
            - e.g. [a,b,c,,,d,e] will be 322 (3 columns with data followed by 2 columns with missing data followed by 2 columns with data)

2. React frontend:
    * Render 1 button that fetches data from `/data` when pressed
    * Upon success, render a table of the data
    * Feel free to install other libs as necessary, but be prepared to explain why
    * Must have the following components (NOTE: These are React components that you create):


          <Button />
          <Table />
          <Tr />
          <Td />

