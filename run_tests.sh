#!/bin/bash
coverage run --branch manage.py test
coverage report
coverage html
