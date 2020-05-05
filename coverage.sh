#!/bin/zsh
set -eu

coverage run -m unittest
coverage report
coverage html
open htmlcov/index.html