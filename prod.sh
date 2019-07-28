export FLASK_APP=server.py
export FLASK_ENV=production
nohup flask run --host=0.0.0.0 --port=8080 &
