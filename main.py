import sys
import os
import shutil
import subprocess
import logging

def create_project(project_name, framework):
    # Get the current working directory
    cwd = os.getcwd()

    # Get the path to the framework folder
    framework_folder = os.path.join(os.path.dirname(__file__), framework)

    # Create the new project directory
    project_dir = os.path.join(cwd, project_name)
    os.mkdir(project_dir)

    # Copy the contents of the framework folder to the new project directory
    for item in os.listdir(framework_folder):
        item_path = os.path.join(framework_folder, item)
        if os.path.isfile(item_path):
            shutil.copy(item_path, project_dir)
        elif os.path.isdir(item_path):
            shutil.copytree(item_path, os.path.join(project_dir, item))
    
    # Create a Git repository in the project folder
    os.chdir(project_dir)
    do_git = input("Do you want to initialize a Git repository? (y/n): ")
    if do_git.lower() == "y":
        init_git()

    print(f"Project '{project_name}' created successfully!")

def init_git():
    # Check for Git Name
    try:
        name = subprocess.check_output(["git", "config", "--get", "user.name"]).decode("utf-8").strip()
        email = subprocess.check_output(["git", "config", "--get", "user.email"]).decode("utf-8").strip()
    except subprocess.CalledProcessError:
        logging.warning("Git Credentials not found. Please enter your name and email address.")
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        subprocess.run(["git", "config", "--global", "user.name", name])
        subprocess.run(["git", "config", "--global", "user.email", email])
        
    subprocess.run(["git", "init"])
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", "Initial commit"])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: createproject <project_name>")
        sys.exit(1)

    project_name = sys.argv[1]

    print("Select a framework:")
    print("1. Django")
    print("2. Flask")

    choice = input("Enter your choice (1/2): ")

    if choice == "1":
        framework = "django"
    elif choice == "2":
        framework = "flask"
    else:
        print("Invalid choice. Please try again.")
        sys.exit(1)

    create_project(project_name, framework)