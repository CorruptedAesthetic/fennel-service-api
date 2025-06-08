#!/bin/bash

function all() {
  migrate
  pip3 install -r requirements.txt
  python3 -m safety check -r requirements.txt
  python3 manage.py check
  run_tests
  static
  setup
}

function all_no_tests() {
  migrate
  pip3 install -r requirements.txt
  python3 -m safety check -r requirements.txt
  python3 manage.py check
  static
  setup
}

function run_tests() {
  coverage run manage.py test -v 2
}

function clean() {
  files=$(find . -name "__pycache__")
  files2=$(find . -iregex ".*\.\(pyc\)")
  rm -rf "${files2}"
  rm -rf "${files}"
}

function wait_for_database() {
  echo "🔍 Waiting for database to be ready..."
  local max_attempts=30
  local attempt=1
  
  while [ $attempt -le $max_attempts ]; do
    echo "Database connection attempt $attempt/$max_attempts..."
    
    # Test database connection using Django's built-in check
    if python3 manage.py check --database default >/dev/null 2>&1; then
      echo "✅ Database is ready!"
      return 0
    fi
    
    echo "⏳ Database not ready, waiting 5 seconds..."
    sleep 5
    attempt=$((attempt + 1))
  done
  
  echo "❌ Database failed to become ready after $max_attempts attempts"
  return 1
}

function migrate() {
  echo "🚀 Starting database migration process..."
  
  # Wait for database to be ready first
  if ! wait_for_database; then
    echo "💥 CRITICAL: Database connection failed - cannot run migrations"
    exit 1
  fi
  
  echo "📊 Running Django migrations..."
  local max_attempts=5
  local attempt=1
  
  while [ $attempt -le $max_attempts ]; do
    echo "Migration attempt $attempt/$max_attempts..."
    
    if python3 manage.py migrate; then
      echo "✅ Migrations completed successfully!"
      return 0
    fi
    
    echo "⚠️ Migration attempt $attempt failed, retrying in 10 seconds..."
    sleep 10
    attempt=$((attempt + 1))
  done
  
  echo "❌ CRITICAL: Migrations failed after $max_attempts attempts"
  exit 1
}

function makemigrations() {
  python3 manage.py makemigrations main
  python3 manage.py makemigrations dashboard
  python3 manage.py makemigrations
}

function static() {
  python3 manage.py collectstatic --no-input
}

function run() {
  python3 manage.py runserver 0.0.0.0:8080
}

function shell() {
  python3 manage.py shell
}

function check() {
  # We're going to ignore E1101, since Django exposes members to Model classes
  # that PyLint can't see.
  clear && \
   black . && \
   pylint main --disable=E1101,W0613,R0903,C0301,C0114,C0115,C0116,R0801,E203 && \
   pylint dashboard --disable=E1101,W0613,R0903,C0301,C0114,C0115,C0116,R0801,E203 && \
   flake8 main --count --extend-ignore E1101,W0613,R0903,C0301,C0114,C0115,C0116,R0801,E203 --exclude ./main/migrations,./main/tests --max-complexity=10 --max-line-length=127 --statistics
   flake8 dashboard --count --extend-ignore E1101,W0613,R0903,C0301,C0114,C0115,C0116,R0801,E203 --exclude ./dashboard/migrations,./dashboard/tests --max-complexity=10 --max-line-length=127 --statistics
}

function gunicorn_run() {
  gunicorn --workers=8 --threads=8 --max-requests=8 fennel.wsgi:application --bind 0.0.0.0:1234
}

function setup() {
  python3 manage.py createadmin
}

mkdir -p profile
case "$1" in

check)
  makemigrations
  migrate
  check
  ;;

startapp)
  python3 manage.py startapp "$2"
  ;;

clean)
  clean
  ;;

migrate)
  migrate
  ;;

test)
  run_tests
  ;;

run)
  run
  ;;

init-all-run)
  all
  gunicorn_run
  ;;

init-all-run-prod)
  all_no_tests
  gunicorn_run
  ;;

docker-init-all)
  check
  all
  ;;

all-run)
  check
  all
  run
  ;;

all)
  all
  ;;

makemigrations)
  makemigrations
  ;;

shell)
  shell
  ;;

esac
