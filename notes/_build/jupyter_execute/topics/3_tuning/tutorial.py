#!/usr/bin/env python
# coding: utf-8

# # 3.5 Tutorial
# 
# In this tutorial we will put into practice the concepts we have learned in the previous sections.
# 
# The task is as follows:
# 1. Fork the [Git tutorial repository](https://github.com/comp0190/git_tutorial)
# 2. Clone the repository to your local machine
# 3. Create a new branch
# 4. Edit the Python script to implement hyperparameter tuning and logging
# 5. Push your changes to your remote repository
# 6. **Bonus!** - Create a pull request to merge your changes into the original [Git tutorial repository](https://github.com/comp0190/git_tutorial)
# 
# Hints and tips are provided below. Feel free to also refer to the previous sections for more information.
# 
# ## Forking the repository and cloning to your local machine
# 
# Firstly, install Git on your local machine. You can find instructions for doing this [here](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).
# 
# To fork the repository, click the **Fork** button in the top right corner of the repository page.
# 
# To clone the repository to your local machine, open a terminal and navigate to the directory where you want to clone the repository. Then run the following command:
# 
# ```bash
# git clone <forked_repository_url>
# ```
# 
# Alternatively, you can use the **Code** button and clone the repository using [GitHub Desktop](https://desktop.github.com/).
# 
# For an example of how to create a new branch, refer to [3.2 Git](/topics/3_tuning/git).
# 
# ## Implementing hyperparameter tuning
# 
# Open the Python file in your favourite text editor. We want to add grid search to find the best hyperparameters for our model. Check out the hyperparameter tuning slides and the [grid search](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html) documentation for more information on how to do this.
# 
# ## Logging the results of your experiments
# 
# We want to log the results of our experiments so that we can compare them later. You can also log the hyperparameters used for each experiment so that you can easily see which hyperparameters were used for each experiment.
# 
# You can refer to [3.4 Logging](/topics/3_tuning/logging) for more information on how to do this.
# 
# ## Committing your changes and pushing to your remote repository
# 
# You should try and make regular commits to your local repository rather than combining different changes in one go. This will help you keep track of your changes and make it easier to revert to a previous version if you make a mistake.
# 
# For an example of how to commit, refer to [3.2 Git](/topics/3_tuning/git)
# 
# To push your changes to your remote repository, run the following command:
# 
# ```bash
# git push origin <branch_name>
# ```
# 
# ## Bonus! - Creating a pull request
# 
# If you want to share your changes with the rest of the class, you can create a pull request to merge your changes into the main repository.
# 
# The GitHub documentation has a [guide](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request) on how to do this.
