# A Todo App
#### Video Demo: https://youtu.be/45MLGMPPBgI
#### Description:
    For my Final project for CS50x I created a todo app using Flask, SQLite3 and a bit of html. Initially I tried to create it using Javascript but I couldn't save the todos. So here you are a todo web app where you can list all the todos that you need to complete during your time at CS50x and edit them as needed or mark them completed. You can also view different todos that you have completed.

    First you will need to register if you don't have an account here while registering your password must contain special symbols, capital letters in order to register(Be sure not to forget your password!)
    Then you can easily add edit and complete the todos. I have not given a todo delete option cause you can't just not complete a todo you need to complete it inorder to run it xD.

    Initially I tried to create it using Javascript but it was not successful so I used some distribution codes from CS50: Finance and its helpers functions.

    The `template` contains html codes to render any of the html for any situations.
    The `apology.html` contains code to show an apology to the user if any error occurs while running the web application.
    The `done.html` renders the todo's that have been done it is implemented with a jinja for loop looping in done which is passed as the list of todos that have been done in the `app.py` `done` function.

    The `edit.html` renders the form to edit the todo.
    And the `index.html` is just the first empty page that you open into after you login.

    `layout.html` consists of all the file imports desription from nav bars to other things.

    `login` and `register` are login and register forms respectively.

    And the `todo.html` renders the todo form in essence adding the todo.

    `app.py` contains all the running codes from `login` functions, `logout` for logging in the user and logging them out, `register`functions for registering the new user, `index` to render the index page, `todo` to add todos,
    `edit` to edit the todo, `onedit` identifies which edit has been pressed, `done` identifies and removes from todo list and add to list of done todos. `todo_done` renders the list of todos completed by you.

    In `helpers.py`, it includes some distribution code from CS50:Finance, the only addition is the `password_check` which checks whether the entered password for registration satisfies the criteria or not. For this we use regular expressions which make the code easier and shorter just a line of if else. The `pattern` generates a raw string consisting of symbols, uppercase and lowercase letters and digits which is checked or matched with the entered password.

    `final.db` is the database which has two tables mainly: the table for storing users and another for storing their todos.

    `todo-functions.js` is the functional implementation of my todo app using JavaScript without beauty.

    It is a simple program the main problem that occured while creating this was how to enable the edit function. But in the end applied it as deletion and insertion. I just couldn't update the data in the database so I opted to remove the pressed edit and then replace it with the new one.

    Thank you!