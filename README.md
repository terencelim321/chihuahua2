# Food Recommendation Flask API

## Flask API Endpoints

### GET /api/v0.1/recommend

Returns list of recommended restaurants based on provided list of restaurant IDs.

Parameters
- **ids**: Compulsory. List of IDs (comma separated) to be used to generate recommendations.
- **top**: Default = 5. Returns this number of recommendations based on descending score.
- **prices**: Optional. Only recommends restaurants with these prices (comma separated, valid values: 1=$, 2=$$, 3=$$$, 4=$$$).
- **zip_codes**: Optional. Only recommends restaurants with these zip_codes (comma separated).

Output
- **total**: Total recommendations returned
- **recommendations**: List of recommendations with score ranging from 0 to 1 (higher the score, more relevant the recommendation).
- **input_ids**: Details associated with IDs provided
- **rejected**: Rejected IDs

Example
- http://<host>:<port>/api/v0.1/recommend?ids=1,4&top=2&price=2,3&zip_codes=012345,712345
```
{ 
	"total": 2, 
  	"recommendations": [
  		{ "id":"2", "name":"Chicken Rice", "price":"$$", "zip_code":"012345", "tags": ["restaurant"], "score":0.6435643 },
  		{ "id":"9", "name":"Bak Kut Teh", "price":"$$", "zip_code":"712345", "tags": ["restaurant"], "score":0.543154 }	
  	],
  	"input_ids": [
  		{ "id":"1", "name":"Tze Char", "price":"$$", "zip_code":"543210", "tags": ["restaurant"] }
  	]
  	"rejected_ids": [
  		"4"
  	]
}
```

### POST /api/v0.1/recommend

Same as GET method, but also assumes provided restaurant IDs are user's preference & stores them in database.
- Additional "user_id" parameter required. 
- All other parameters & output same as GET.


## Running Flask API Service

### 1. Create Heroku App & Heroku Postgres

Prerequisite
- Heroku account
- Install postgreSQL (to use "psql" in command line)

Steps
1. Login to Heroku via web browser.
2. Create new app from Heroku dashboard.
3. Install Heroku Postgres add-on.
4. On Heroku Postgres add-on page, click on "Settings" > "View Credentials"
5. Declare local environment variable based on these credentials.
```
export DATABASE="<to be filled in>"
export DATABASE_HOST="<to be filled in>"
export DATABASE_PORT="<to be filled in>"
export DATABASE_USER="<to be filled in>"
export DATABASE_PASS="<to be filled in>"
export DATABASE_URL="postgresql://${DATABASE_USER}:${DATABASE_PASS}@${DATABASE_HOST}:${DATABASE_PORT}/${DATABASE}"
```
6. Connect to Heroku Postgres with following psql command
```
cd <project folder>
PGPASSWORD=$DATABASE_PASS psql -h $DATABASE_HOST -U $DATABASE_USER $DATABASE
```
7. Execute following commands to create the required tables
```
\i postgres/create_restn.sql
\i postgres/create_restn_tags.sql
\i postgres/create_restn_user_rating.sql
```
8. Confirm that tables have been created
```
\dt
```

### 2a. Deploy App to Heroku

Prerequisite
- Git
- [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)
- Created Heroku App & Heroku Postgres (instructions above)

Steps
1. Login to Heroku via web browser.
2. Click on created app on Heroku dashboard.
3. Click on "Settings" > "Reveal Config Vars".
4. Add the following configuration variable (there should be a DATABASE_URL variable already present).
```
KEY = APP_SETTINGS, VALUE = config.ProductionConfig
```
5. Click on "Deploy" > "Deploy using Heroku Git" section.
6. Following instructions to push codes to Heroku App.

### 2b. Running Locally

#### Setting up python virtual environment

Prerequisite
- Python >=3.6 ("python --version" to check)

Steps
1. Change to project folder.
```
cd <project folder>
```
2. Create python virtual environment.
```
python -m venv venv
```
3. Activate virtual environment. "(venv)" will appear at command prompt if activated.
```
venv\Scripts\activate (for windows) OR venv/bin/activate (for mac)
```
4. Install required python packages.
```
pip install -r requirements.txt
```

#### Running python script

Prerequisite
- Setup of python virtual environment (instructions above)
- Created Heroku App & Heroku Postgres (instructions above)

Steps
1. If not activated yet, activate virtual environment ("(venv)" will appear at command prompt if activated).
```
cd <project folder>
venv\Scripts\activate (for windows) OR venv/bin/activate (for mac)
```
2. Add local environment variable.
```
export APP_SETTINGS="config.DevelopmentConfig"
```
3. Run python script.
```
cd <project folder>
python run.py
```
