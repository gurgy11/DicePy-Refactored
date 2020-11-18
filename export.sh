#!/bin/bash

echo "Exporting and setting Flask app and setting environment as development..."

# Export Flask app and environment
export FLASK_APP=dicepy
export FLASK_ENV=development

# Set Flask app as this app
FLASK_APP=dicepy