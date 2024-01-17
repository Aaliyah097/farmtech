#!/bin/bash

exit_code=0

function lint() {
  echo -e """\n======= run \"$1\" ======="""
  eval "$1"
  retval=$?
  if [ $retval -ne 0 ]; then
    exit_code=$retval
    echo Check failed
  else
    echo Check passed
  fi
  echo -e """======= end \"$1\" ======="""
}

lint "flake8"
lint "black src"
lint "isort src"

exit $exit_code
