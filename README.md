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
You need to create two config files: one for the database parameters and the other for flask.
Final project outline:
```
.
├── dashboard
│   ├── config.py
│   ├── instance
│   │   └── config.py
│   └── tiny-dashboard
│       └── ...
├── launch_server.sh
├── README.md
└── requirements.txt
```

**dashboard/config.py**
```
mongoURL = 'mongodb://localhost:27017/'
db_name = 'database_name'
```

**dashboard/instance/config.py**
```
SECRET_KEY = 'my_flask_secret_key'
DEBUG = True
```

## Running 

By default, the mongo database will be inside a docker container, so the launcher will check if the container is running, and if not, it will run the container

### Without docker
If you don't want to use docker, execute the script with the flag `--no-docker`
```
chmod +x launch_server.sh
./launch_server.sh --no-docker
```

### Default execution
```
chmod +x launch_server.sh
./launch_server.sh
```

You can edit the script to specify the location for the database in the local machine. This is the used to maintain the persistence for the database inside the container.
