#!/bin/bash

MARKER_NAME=em-regex-search

cd ~/github/$MARKER_NAME/server
sudo -u www-data -g www-data pipenv run uwsgi \
	--stop /tmp/$MARKER_NAME.pid