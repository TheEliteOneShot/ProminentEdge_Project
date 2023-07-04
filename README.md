# ProminentEdge_Project

The completed project that satisfied all of the project requirements in a quality way. The CAD files are uploaded into an SQLite database. It is possible to upload more than one CAD file at a single time.

# Installation for Windows (Tested on Windows 11)

- This is just a regular Vue 3 frontend with a Python flask backend using an SQLITE database. There shouldn't be anything that complicated to get working.
  
- Install NPM [https://nodejs.org/en/download] (This app was tested on NPM version 8.5.0)
- Install Python [https://www.python.org/downloads] (This app was tested on python version 3.10.3)

- This app uses a google maps API key and a RAPID API key for the meteos weather API. I am using my own keys with the trial account that I've put into source control for a short time so please feel free to use them while they last. If the desire to change the API keys to your own keys are required, please consult the '.env' file inside the frontend/src directory. This file is part of the VITE build process and will use 'VITE_RAPID_API_KEY', 'VITE_RAPID_API_HOST', 'VITE_GOOGLE_MAPS_API_KEY' to deploy the web application.
  
- Additionally, the backend flask app is using a 'config.py' file location in the backend folder. This will allow configuration of where the sqlite database is initially deployed and may be necessary to configure depending on where python thinks your base path is when the backend has started.

# Startup instructions

- Run **start_backend.ps1** to start up the backend server. This will start the flask app and initialize the database.
- Run **start_frontend.ps1** to start up the frontend server. This will start the frontend Vue server. Follow the localhost link to the web page written to the console when the script has finished starting. (note: if the NPM doesn't automatically download the package.json dependencies it may require typing 'npm install' into the console inside the frontend folder directory.

# Improvements if I had double the time

- I would polish the app further by adding in the Vue router so that I could add another page that showed an event timeline for the entire CAD file. Each event would be clickable and it would automatically scroll to the Google Map Marker that the event was referencing.
- I would polish the Google Map API by removing overlapping Markers. As it currently stands, it's very difficult to read Markers that are very close in physical proximity.

# How much time did I spend on the app

- Well, it should be noted that I do software for a living. Therefore, I am constantly working on things. My primary job responsibility is data analysis using MSSQL. So I had to refresh my full stack skills.
- I spent nearly 10 hours on putting everything together, mostly boiler plate code and reading Google Maps and Vue3 documentation. HOwever, that being said, it should be highlighted that most of the difficult work which requires good software development experience only took me around 4 hours. Therefore...
- Time Spent: 4 hours :)
  
# Images

# 1. Upload any amount of CAD files
  
![1_uploadfiles](https://github.com/TheEliteOneShot/ProminentEdge_Project/assets/45804405/254b8db5-a3f8-425a-a44f-ea179076fe2a)

# 2. Select a single CAD file that has been uploaded to the SQLITE database
  
![2_selectcadfile](https://github.com/TheEliteOneShot/ProminentEdge_Project/assets/45804405/c76697ab-8cc3-438c-9907-796c7160c6a1)

# 3. View locations that were present in the selected CAD file via Google Maps
  
![3_viewlocations](https://github.com/TheEliteOneShot/ProminentEdge_Project/assets/45804405/d3dc0b56-a37f-4769-bcda-8b682dd4d468)

# 4. Click on a Marker present in the Google Maps to see expanded information about that specific event. Additionally, it will call the meteos weather API to get weather details for that day and location.
  
![4_viewinformation](https://github.com/TheEliteOneShot/ProminentEdge_Project/assets/45804405/201a48e9-0320-42f8-a205-ea9580a816eb)
