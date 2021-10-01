import os

# ask the user for the folder name
ProjectName = input("Name the new project/n")

# navigate to projects folder
ProjectsFolder = ("D:\Documents\Python\PythonCodeProjects")
os.chdir(ProjectsFolder)
d = os.getcwd()
print(d)

# create a folder with the project name
