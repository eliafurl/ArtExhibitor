#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Define the test directory
TEST_DIR="tests"
SRC_DIR="src"

# Check if the virtual environment is active
if [ -z "$VIRTUAL_ENV" ]; then
    echo "Virtual environment is not active. Activating art_exhibitor..."
    source ./art_exhibitor/bin/activate
fi

# Run the unit tests with coverage
pytest --cov=$SRC_DIR --cov-report=term-missing

# Check if tests passed
if [ $? -eq 0 ]; then
    echo "All tests passed successfully!"
else
    echo "Some tests failed. Please check the output above."
fi