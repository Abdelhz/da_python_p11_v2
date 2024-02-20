# gudlift-registration

1. Why

    This is a proof of concept (POC) project to show a light-weight version of our competition booking platform. The aim is the keep things as light as possible, and use feedback from the users to iterate.

2. Getting Started

    This project uses the following technologies:

    * Python v3.x+

    * [Flask](https://flask.palletsprojects.com/en/1.1.x/)

        Whereas Django does a lot of things for us out of the box, Flask allows us to add only what we need.

    * [Virtual environment](https://virtualenv.pypa.io/en/stable/installation.html)

        This ensures you'll be able to install the correct packages without interfering with Python on your machine.

        Before you begin, please ensure you have this installed globally.

3. Installation

    * After cloning, change into the directory and type <code>virtualenv .</code>. This will then set up a a virtual python environment within that directory.

    * Next, type <code>source bin/activate</code>. You should see that your command prompt has changed to the name of the folder. This means that you can install packages in here without affecting affecting files outside. To deactivate, type <code>deactivate</code>

    * Rather than hunting around for the packages you need, you can install in one step. Type <code>pip install -r requirements.txt</code>. This will install all the packages listed in the respective file. If you install a package, make sure others know by updating the requirements.txt file. An easy way to do this is <code>pip freeze > requirements.txt</code>

    * Flask requires that you set an environmental variable to the python file. However you do that, you'll want to set the file to be <code>server.py</code>. Check [here](https://flask.palletsprojects.com/en/1.1.x/quickstart/#a-minimal-application) for more details

    **This can be achieved using the following command:**

    1. Navigate to the server.py directory

    ```bash
    cd path_to_server.py_directory
    ```

    2. Add the server.py file to the environment variables

    **On Unix-based systems (Linux, MacOS, including git bash for windows):**

    ```bash
    export FLASK_APP=server.py
    ```

    **On Windows Command Prompt:**

    ```bash
    set FLASK_APP=server.py
    ```

    **On Windows PowerShell:**

    ```bash
    $env:FLASK_APP = "server.py"
    ```

    * You should now be ready to test the application. In the directory, type either <code>flask run</code> or <code>python -m flask run</code>. The app should respond with an address you should be able to go to using your browser.

4. Current Setup

    The app is powered by [JSON files](https://www.tutorialspoint.com/json/json_quick_guide.htm). This is to get around having a DB until we actually need one. The main ones are:

    * competitions.json - list of competitions
    * clubs.json - list of clubs with relevant information. You can look here to see what email addresses the app will accept for login.

5. Testing

    In this pro.

    We also like to show how well we're testing, so there's a module called
    [coverage](https://coverage.readthedocs.io/en/coverage-5.1/) you should add to your project.

## Issues and branches

**We have divided and the repository in many different branches, each one for the identified issues**:

*List of branches and issues they treat :*

* **basic_branch_improvements** : In this branch we implemented basic code improvements, like error handling with "try, except". This branch served as base for all the following branches.

* **FIX_01/ERROR_Entering_unknown_email_crashes_app** : In this branch we treat the issue where the application crashes when entering a non existant email address.

* **FIX_01/2/ERROR_Handling_NotFound_competition_Crashes_app** : This is a sub branch for the 1st issue, in it we treat the same issue but this time for the "book" route.

* **FIX_02/BUG_Using_More_Points-Or-Places_Than_Available** : In this branch we treat the issue where the users tries to purchase more places than the number of points the club possesses. We also added to it the fix for the issue where the user tries to purchase more places than the number of places the competition possesses.

* **FIX_03/increment-to-FIX_02/BUG_booking_more_than_12_places_per_comp** : This branche is an increment to the previous branch (FIX_02), this is done to avoid bugs since we are working on the same route (purchasePlaces).
In this branch we treat the issue where the user tries to purchase more than 12 places (12 is the maximum number of places a club is allowed to purchase).

* **FIX_04/increment-to-FIX_01/2/BUG_booking_in_past_competitions** : This branche is an increment to the previous branch (FIX_01/2), this is done to avoid bugs since we are working on the same route (book).
In this branch we treat the issue where the user tries to purchase places for a past competition ! In this case the user cannot access the "purchasePlaces" page !

* **FIX_05/increment-to-FIX_03/BUG_Points_and_places_updates_are_not_reflected** : This branche is an increment to the previous branch (FIX_03), this is done to avoid bugs since we are working on the same route (purchasePlaces).
In this branch we treat the issue where the persistance of date is not assured for the update of club's points (When  purchasing places the club's points are changed and the updates were not reflected on the file), we added to it the fix for the same issue where the persistance of date is not assured for the update of competition's available places (When  purchasing places the competition's available places are changed and the updates were not reflected on the file).

* **FIX_06/FEATURE_Implement_Points_Display_Board** : In this branch we implemented the feature of displaying the clubs and their current points.

* **Merging_branches_before_Master** : This branch served for the merging of all the previous branches before serving them to the master branch. this is done to prevent putting bugged code into the master branch, since the merging process can cause that.

* **QA** : This is the "asked for" branch by the QA team. In it all the fixes features, tests are implemented and ready for testing.

## Performed tests

### Fixture

The fixture file is named "conftest.py" and it contains all the fixtures necessary for the tests.

### Unit Tests

Those tests are contained in a file named "unit_tests.py" in a folder named "unit" and it contains all the unit tests for each of the issues treated and fixed.

### Integration tests

Those tests are contained in a file named "integration_tests.py" in a folder named "integration" and it contains all the integration tests where we test each route in a general way.

### Performance tests

To perform this test we used the module "locust". The test in contained in a file named "locustfile.py" in a folder named "performance" and it containes all tasks for each of the routes. The result of the test in showed in a png file in the same folder.

### Test's coverage

To perform this test we used the module "coverage". The result of the coverage test in showed in two png files in a folder named "coverage".

