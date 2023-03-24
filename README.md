#### To-Do List Application ####
This is a simple to-do list application built in Python using the tkinter library. The application allows you to add, complete, and delete tasks. Each task is represented as a dictionary in the tasks list, which has two properties: task (the task description) and completed (a boolean value indicating whether the task has been completed or not).

#### Usage ####
Clone the repository or download the app.py file.
Open a terminal window and navigate to the directory containing the app.py file.
Run the following command to start the application:
 'python app.py'
--The application window will open. 
--Enter a task in the 'Add a task: field' and click the Add button to add it to the list.
--To mark a task as completed, select it in the list and click the Complete button.
--To delete a task, select it in the list and click the Delete button.
--To view the list of tasks, click the Show Tasks button.

### Using Docker ###

Build the Docker image by running the following command:

'docker build -t todoapp .'

Once the image is built, you can run a container using the following command:

'docker run --rm -p 8000:8000 todoapp'

This will start a container from the "todoapp" image and map port 8000 in the container to port 8000 on the host machine. The --rm flag specifies that the container should be removed when it stops.

You can now access the application by navigating to http://localhost:8000 in your web browser.


#### Acknowlegement ####
This project was created by Eric Skariah Alexander as part of an Interview for Newsreels.app