#!/bin/sh
gunicorn app:app -w 2 --threads 4 -b 0.0.0.0:$DASHBOARD_PORT