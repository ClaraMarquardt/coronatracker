# CoronaTracker

CoronaTracker is a Flask app that provides users with information about the number of confirmed Corona cases and deaths in different countries. 

## Quickstart 

### Live  (AWS Elasticbeanstalk)
```
http://flaskenv3.eba-jrrppwrc.us-east-2.elasticbeanstalk.com/home
```

### Local

1. Clone the repository

```
git clone https://github.com/ClaraMarquardt/coronatracker.git
cd coronatracker/Session4_IntegrationDeployment
```
pip install -U Flask
pip install geopy numpy pandas

2. Launch the Flask app
```
python application.py
```

3. Open http://127.0.0.1:5000/home in your browser