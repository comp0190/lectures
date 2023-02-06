#!/usr/bin/env python
# coding: utf-8

# # 3.4 Logging
# 
# Why can't we just `print()` all of our outputs? Although this is a simple solution, it can be difficult to keep track of all of the information we need. This is especially the case when we want to run lots of experiments.
# 
# To make it easier to keep track of experiments, the hyperparameters we used, and the results of those experiments, we can use a logger. This will allow us to keep track of the information we need in a structured way.
# 
# ## What should we log?
# 
# You should try to log information that will help you to reproduce your experiments, as well as any information that will help you to understand the results of your experiments. This could include:
# 
# * Model architecture
# * Hyperparameters
# * Training and validation losses
# * Metrics
# 
# ## Logging with `logging`
# 
# There are lots of different loggers available in Python. The `logging` module is a built-in Python library that you can use. 
# 
# `logging` has the option to record messages under different levels of severity, which means you can adjust it to only record the messages you want. The five levels of severity are:

# ```{list-table}
# :header-rows: 1
# 
# * - Level
#   - When it's used
# * - DEBUG
#   - Detailed information, typically of interest only when diagnosing problems.
# * - INFO
#   - Confirmation that things are working as expected.
# * - WARNING
#   - An indication that something unexpected happened, or indicative of some problem in the near future (e.g. 'disk space low'). The software is still working as expected.
# * - ERROR
#   - Due to a more serious problem, the software has not been able to perform some function.
# * - CRITICAL
#   - A serious error, indicating that the program itself may be unable to continue running.
# ```

# The default level is `WARNING`, so if you want to log messages at the `INFO` level, you need to set the level to `INFO` or lower.
# 
# For  example:

# In[1]:


import logging

# This  will print a message to the console
logging.warning('This is a warning message')
# This will not print anything because the default level is warning
logging.info('This is an info message')


# We can configure the logger to record messages at a lower level of severity. For example, we can record messages at `debug` level or higher:

# In[2]:


import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')


# To log messages to a file, we can use the `FileHandler`. We can then look at the contents later on to analyse the results of our experiments.
# 
# However, if we are checking for outputs on the console, this will not display the messages. To display the messages on the console, we can use the `StreamHandler`.
# 
# In the following example, we will log the warning messages to a file. Note as we are using a Jupyter notebook, there is no need to use the `StreamHandler` as it will duplicate the messages.

# In[3]:


import logging

# Create logger
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


# Create a file handler and set level to warning
fh = logging.FileHandler('test.log')
fh.setLevel(logging.WARNING)

# Add handlers to logger
logger.addHandler(fh)

# Log code
logger.debug('This is a debug message')
logger.warning('This is a warning message')


# ## Example
# 
# Let's train a decision tree on the [breast cancer](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_breast_cancer.html) dataset. We'll log the time, tree depth, accuracy, precision and ROC AUC to a file.

# In[4]:


import logging

from sklearn.datasets import load_breast_cancer
from sklearn.metrics import precision_score, recall_score, roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier


# Set up the logger:

# In[5]:


logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# Create a file handler
handler = logging.FileHandler('my_output.log')

logger.addHandler(handler)
handler.setFormatter(logging.Formatter("%(asctime)s:%(name)s:%(levelname)s:%(message)s"))


# Load the data

# In[6]:


data = load_breast_cancer()
X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, random_state=0)


# Set the hyperparameters. In this case, we're only going to configure the tree depth.

# In[7]:


# Set the hyperparameters
MAX_DEPTH = 5
# Record max depth
logger.info(f"Max depth: {MAX_DEPTH}")


# Train the model!

# In[8]:


# Train the model
clf = DecisionTreeClassifier(max_depth=MAX_DEPTH)
clf = clf.fit(X_train, y_train)


# ...and evaluate - we can then check the outputs in `my_output.log`.

# In[9]:


# Evaluate the model

accuracy = clf.score(X_test, y_test)
logger.info(f"Accuracy: {accuracy:.2f}")

# Get predictions for other metrics
predictions = clf.predict(X_test)

precision = precision_score(y_test, predictions)
logger.info(f"Precision: {precision:.2f}")
recall = recall_score(y_test, predictions)
logger.info(f"Recall: {recall:.2f}")
auc = roc_auc_score(y_test, predictions)
logger.info(f"AUC: {auc:.2f}")


# ## More information on logging
# * [Python logging documentation](https://docs.python.org/3/library/logging.html)
# * [Logging Cookbook](https://docs.python.org/3/howto/logging-cookbook.html)
# * [Machine learning mastery guide to logging](https://machinelearningmastery.com/how-to-log-machine-learning-results-for-reproducible-research/)
# 
# ## Alternatives to logger
# There are many alternatives to the `logging` module. Here are some of the most popular ones:
# * [Tensorboard](https://www.tensorflow.org/tensorboard)
# * [Weights and Biases](https://wandb.ai/site)
# * [dvc](https://dvc.org/)
