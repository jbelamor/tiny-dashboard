# tiny-dashboard

A dashboard to view and modify the data from a mongo database.

## Instalation
First steps
```
git clone https://github.com/jbelamor/tiny-dashboard.git
cd tiny-dashboard
```

### Using virtual enviroments
Use virtual enviroments to install the requiremnts:
```
pip3 install --user virtualenv
virtualenv --python=python3 .env
source .env/bin/activate
```

### Common part
```
pip3 install -r requirements.txt --user
```

## Configuration
You need to create fill the file `dashboard/config.py` with the following structure and information:
```
mongoURL = 'mongodb://localhost:27017/'
db_name = 'database_name'
SECRET_KEY = 'the_secret_key_of_your_server'
DEBUG = True
```

In this file you should include all the parameters to connect to the database and for the flask server.

## Running 

This dashboard was designed to be executed along mongo inside a docker container.

### Without docker
Execute the script with the flag `--no-docker`
```
chmod +x launch_server.sh
./launch_server.sh --no-docker
```

### Default execution
```
chmod +x launch_server.sh
./launch_server.sh
```
