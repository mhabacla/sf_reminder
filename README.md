# About the project
This is a little reminder for the 'Registro de jornada' located inside the Success Factors page.

# Getting Started
## Prerequisites
You need at least Python 3.6.

## Installation
1. Clone the repo `git clone https://github.com/mhabacla/sf_reminder.git`
2. `cd` to the repo
3. If you don't already have virtualenv installed do `pip install virtualenv`.
4. `virtualenv venv` to create your new environment (called 'venv' here).
5. `source venv/bin/activate` to enter in the virtual environment.
6. `pip install -r requirements.txt` to install the requirements in the current environment.

## Configuration
1. Write the Success Factors URL inside the conf/config.yaml file (on the empty URL space).
2. Go to the Windows 'Task Scheduler'.
3. Go to Actions > Create Task.
4. Give it a name.
5. Go to Actions > New
6. Browse the Python path used (this should inside the virtual environment you created). In my case the path it was `C:\projects\python\sf_reminder\venv\Scripts\python.exe`.
7. On this same window add the name of the script (success_factors_reminder.py) to the 'Add arguments (optional)' input.
8. Add the directory path to the 'Start in (optional)' input. Go to the folder where your Python script is located (where you cloned the repo) and copy the path.
9. **Without** closing the window go to Triggers > New
10. Choose the repetition that you want.
11. Click OK.

You can also use a .batch file with the Windows 'Task Scheduler'.
