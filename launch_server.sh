#! /bin/bash
run_server () {
	export FLASK_APP=tiny-dashboard
	export FLASK_ENV=development
	cd dashboard
	flask run
	exit 0
}

if [[ $# -eq 1 && $1 == '--no-docker' ]]
	then
		run_server
fi

if [ `docker ps -f name=mongodb | wc -l` -eq 1 ]
	then
		docker run -d -v `pwd`/firebase_backup.mongo:/data/db --name mongodb -p 27017-27019:27017-27019 mongo; docker ps --quiet
fi
run_server

