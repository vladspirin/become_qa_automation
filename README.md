# become_qa_automation

This framework is designed in order to perform tests for GitHub using UI and API approaches
## Framework structure
### Config module
Config module consists of all needed configuration except external libraries
### Application module 
How to add application under test
1. Create a folder inside tests/<your_application_name>
2. Create a folder inside application module src/applications/<your_application_name>
3. Use the same coding standards to create a code
### Helpers module
Some helper scripts
### Tests module
Tests module consists of all related to the test framework Python scripts.
### Virtual environment 
1. Please make sure that .venv (.env) added to .gitignore file
2. Install all needed additional libraries using PIP, example pip install <your_library>
