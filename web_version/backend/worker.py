#!/usr/bin/env python3
from celery import Celery
from ritter import ritter_initial_ball

# run with:
# redis-server
# celery -A worker worker --loglevel=debug
app = Celery(__name__, backend='rpc://', broker='redis://localhost:6379/')

circle = app.task(ritter_initial_ball)
@app.task
def get_circle():
    try:
        return ritter_initial_ball()
    except Exception:
        return
