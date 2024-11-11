#!/bin/sh

#diff -r --exclude .pyc --exclude venv ../docs/ ../../../gitlab/montty/docs/
diff -r --exclude='*.pyc' \
    --exclude='.git' \
    --exclude='.pytest_cache' \
    --exclude='.coverage' \
    --exclude='venv' \
    ../ ../../../gitlab/montty
