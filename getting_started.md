# Getting started with your local python environment:

Here's a step-by-step guide on how to use virtualenv:

1) Install virtualenv if you haven't already. You can do this with pip:

```
pip install virtualenv
```

2) Navigate to your project directory and create a new virtual environment. Replace env with the name you want to give to your environment:

```
cd my_project
virtualenv env
```

3) Activate the virtual environment:

```
source env/bin/activate   #mac
.\env\Scripts\activate    #windows
```

4) Now you can install packages using pip and they will be installed in the virtual environment, not globally:

```
pip install <package-name>
```

5) When you're done working, you can deactivate the virtual environment:

```
deactivate
```

To keep your project in a GitHub repository, you can initialize a new Git repository in your project directory and push it to GitHub:

1) Initialize a new Git repository:

```
git init
```

2) Add all files to the repository and commit:

```
git add .
git commit -m "Initial commit"
```

3) Go to GitHub and create a new repository. Then, link the local repository to the GitHub repository and push:

```
git remote add origin https://github.com/username/repository.git
git push -u origin master
```


