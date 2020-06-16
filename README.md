# scorer
Python 3+ required

## Description

A simple web service to calculate live averages

* Scores stored under UIDs
* Mean average for each UID
* Average of UID averages


## Installing Dependencies

    pip install -r requirements.txt

## Run
The app can be run locally for development with 
    python app.py

This will run it on localhost:5000. The server will be accessible from your laptop.

For a production env, the app would need to be packaged and run with gunicorn or equivalent package manager.


The persistence layer for this app is plain vanilla JSON file with the name 'scores.json'

This is not suitable for data intensive environments. A good noSQL (or SQL) DB would suffice. I was thinking of implementing it using SQlite but as it has AVG functions but ended up doing a vanilla implementation.


## Endpoints

| Method | Path | JSON-encoded Payload | Description |
|--------|------|----------------------|-------------|
|POST|/uid_scores/|{"uid": $string,"points":$integer}|Uploads a new score and returns average for UID|
|GET|/group_averager||Returns group average for all UIDs|


The get method does not require a payload or any inputs. I thought the endpoint name would be self sufficient.


