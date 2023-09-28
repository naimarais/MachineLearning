{
  "metadata": {
    "language_info": {
      "codemirror_mode": {
        "name": "python",
        "version": 3
      },
      "file_extension": ".py",
      "mimetype": "text/x-python",
      "name": "python",
      "nbconvert_exporter": "python",
      "pygments_lexer": "ipython3",
      "version": "3.8"
    },
    "kernelspec": {
      "name": "python",
      "display_name": "Python (Pyodide)",
      "language": "python"
    }
  },
  "nbformat_minor": 4,
  "nbformat": 4,
  "cells": [
    {
      "cell_type": "markdown",
      "source": "<p style=\"text-align:center\">\n    <a href=\"https://skills.network/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkML0101ENSkillsNetwork20718538-2022-01-01\" target=\"_blank\">\n    <img src=\"https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/assets/logos/SN_web_lightmode.png\" width=\"200\" alt=\"Skills Network Logo\">\n    </a>\n</p>\n\n<h1 align=\"center\"><font size=\"5\">Final Project: Classification with Python</font></h1>\n",
      "metadata": {}
    },
    {
      "cell_type": "markdown",
      "source": "<h2>Table of Contents</h2>\n<div class=\"alert alert-block alert-info\" style=\"margin-top: 20px\">\n    <ul>\n    <li><a href=\"https://#Section_1\">Instructions</a></li>\n    <li><a href=\"https://#Section_2\">About the Data</a></li>\n    <li><a href=\"https://#Section_3\">Importing Data </a></li>\n    <li><a href=\"https://#Section_4\">Data Preprocessing</a> </li>\n    <li><a href=\"https://#Section_5\">One Hot Encoding </a></li>\n    <li><a href=\"https://#Section_6\">Train and Test Data Split </a></li>\n    <li><a href=\"https://#Section_7\">Train Logistic Regression, KNN, Decision Tree, SVM, and Linear Regression models and return their appropriate accuracy scores</a></li>\n</a></li>\n</div>\n<p>Estimated Time Needed: <strong>180 min</strong></p>\n</div>\n\n<hr>\n",
      "metadata": {}
    },
    {
      "cell_type": "markdown",
      "source": "# Instructions\n",
      "metadata": {}
    },
    {
      "cell_type": "markdown",
      "source": "In this notebook, you will  practice all the classification algorithms that we have learned in this course.\n\n\nBelow, is where we are going to use the classification algorithms to create a model based on our training data and evaluate our testing data using evaluation metrics learned in the course.\n\nWe will use some of the algorithms taught in the course, specifically:\n\n1. Linear Regression\n2. KNN\n3. Decision Trees\n4. Logistic Regression\n5. SVM\n\nWe will evaluate our models using:\n\n1.  Accuracy Score\n2.  Jaccard Index\n3.  F1-Score\n4.  LogLoss\n5.  Mean Absolute Error\n6.  Mean Squared Error\n7.  R2-Score\n\nFinally, you will use your models to generate the report at the end. \n",
      "metadata": {}
    },
    {
      "cell_type": "markdown",
      "source": "# About The Dataset\n",
      "metadata": {}
    },
    {
      "cell_type": "markdown",
      "source": "The original source of the data is Australian Government's Bureau of Meteorology and the latest data can be gathered from [http://www.bom.gov.au/climate/dwo/](http://www.bom.gov.au/climate/dwo/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkML0101ENSkillsNetwork20718538-2022-01-01).\n\nThe dataset to be used has extra columns like 'RainToday' and our target is 'RainTomorrow', which was gathered from the Rattle at [https://bitbucket.org/kayontoga/rattle/src/master/data/weatherAUS.RData](https://bitbucket.org/kayontoga/rattle/src/master/data/weatherAUS.RData?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkML0101ENSkillsNetwork20718538-2022-01-01)\n\n\n",
      "metadata": {}
    },
    {
      "cell_type": "markdown",
      "source": "This dataset contains observations of weather metrics for each day from 2008 to 2017. The **weatherAUS.csv** dataset includes the following fields:\n\n| Field         | Description                                           | Unit            | Type   |\n| ------------- | ----------------------------------------------------- | --------------- | ------ |\n| Date          | Date of the Observation in YYYY-MM-DD                 | Date            | object |\n| Location      | Location of the Observation                           | Location        | object |\n| MinTemp       | Minimum temperature                                   | Celsius         | float  |\n| MaxTemp       | Maximum temperature                                   | Celsius         | float  |\n| Rainfall      | Amount of rainfall                                    | Millimeters     | float  |\n| Evaporation   | Amount of evaporation                                 | Millimeters     | float  |\n| Sunshine      | Amount of bright sunshine                             | hours           | float  |\n| WindGustDir   | Direction of the strongest gust                       | Compass Points  | object |\n| WindGustSpeed | Speed of the strongest gust                           | Kilometers/Hour | object |\n| WindDir9am    | Wind direction averaged of 10 minutes prior to 9am    | Compass Points  | object |\n| WindDir3pm    | Wind direction averaged of 10 minutes prior to 3pm    | Compass Points  | object |\n| WindSpeed9am  | Wind speed averaged of 10 minutes prior to 9am        | Kilometers/Hour | float  |\n| WindSpeed3pm  | Wind speed averaged of 10 minutes prior to 3pm        | Kilometers/Hour | float  |\n| Humidity9am   | Humidity at 9am                                       | Percent         | float  |\n| Humidity3pm   | Humidity at 3pm                                       | Percent         | float  |\n| Pressure9am   | Atmospheric pressure reduced to mean sea level at 9am | Hectopascal     | float  |\n| Pressure3pm   | Atmospheric pressure reduced to mean sea level at 3pm | Hectopascal     | float  |\n| Cloud9am      | Fraction of the sky obscured by cloud at 9am          | Eights          | float  |\n| Cloud3pm      | Fraction of the sky obscured by cloud at 3pm          | Eights          | float  |\n| Temp9am       | Temperature at 9am                                    | Celsius         | float  |\n| Temp3pm       | Temperature at 3pm                                    | Celsius         | float  |\n| RainToday     | If there was rain today                               | Yes/No          | object |\n| RainTomorrow  | If there is rain tomorrow                             | Yes/No          | float  |\n\nColumn definitions were gathered from [http://www.bom.gov.au/climate/dwo/IDCJDW0000.shtml](http://www.bom.gov.au/climate/dwo/IDCJDW0000.shtml?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkML0101ENSkillsNetwork20718538-2022-01-01)\n\n",
      "metadata": {}
    },
    {
      "cell_type": "markdown",
      "source": "## **Import the required libraries**\n",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "# All Libraries required for this lab are listed below. The libraries pre-installed on Skills Network Labs are commented.\n# !mamba install -qy pandas==1.3.4 numpy==1.21.4 seaborn==0.9.0 matplotlib==3.5.0 scikit-learn==0.20.1\n# Note: If your environment doesn't support \"!mamba install\", use \"!pip install\"",
      "metadata": {},
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": "# Surpress warnings:\ndef warn(*args, **kwargs):\n    pass\nimport warnings\nwarnings.warn = warn",
      "metadata": {
        "trusted": true
      },
      "execution_count": 1,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": "#you are running the lab in your  browser, so we will install the libraries using ``piplite``\nimport piplite\nawait piplite.install(['pandas'])\nawait piplite.install(['numpy'])\n",
      "metadata": {
        "trusted": true
      },
      "execution_count": 2,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": "import pandas as pd\nfrom sklearn.linear_model import LogisticRegression\nfrom sklearn.linear_model import LinearRegression\nfrom sklearn import preprocessing\nimport numpy as np\nfrom sklearn.neighbors import KNeighborsClassifier\nfrom sklearn.model_selection import train_test_split\nfrom sklearn.neighbors import KNeighborsClassifier\nfrom sklearn.tree import DecisionTreeClassifier\nfrom sklearn import svm\nfrom sklearn.metrics import jaccard_score\nfrom sklearn.metrics import f1_score\nfrom sklearn.metrics import log_loss\nfrom sklearn.metrics import confusion_matrix, accuracy_score\nimport sklearn.metrics as metrics",
      "metadata": {
        "trusted": true
      },
      "execution_count": 3,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": "### Importing the Dataset\n",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "from pyodide.http import pyfetch\n\nasync def download(url, filename):\n    response = await pyfetch(url)\n    if response.status == 200:\n        with open(filename, \"wb\") as f:\n            f.write(await response.bytes())",
      "metadata": {
        "trusted": true
      },
      "execution_count": 4,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": "path='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-ML0101EN-SkillUp/labs/ML-FinalAssignment/Weather_Data.csv'",
      "metadata": {
        "trusted": true
      },
      "execution_count": 5,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": "await download(path, \"Weather_Data.csv\")\nfilename =\"Weather_Data.csv\"",
      "metadata": {
        "trusted": true
      },
      "execution_count": 6,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": "df = pd.read_csv(\"Weather_Data.csv\")\ndf.head()",
      "metadata": {
        "trusted": true
      },
      "execution_count": 7,
      "outputs": [
        {
          "execution_count": 7,
          "output_type": "execute_result",
          "data": {
            "text/plain": "       Date  MinTemp  MaxTemp  Rainfall  Evaporation  Sunshine WindGustDir  \\\n0  2/1/2008     19.5     22.4      15.6          6.2       0.0           W   \n1  2/2/2008     19.5     25.6       6.0          3.4       2.7           W   \n2  2/3/2008     21.6     24.5       6.6          2.4       0.1           W   \n3  2/4/2008     20.2     22.8      18.8          2.2       0.0           W   \n4  2/5/2008     19.7     25.7      77.4          4.8       0.0           W   \n\n   WindGustSpeed WindDir9am WindDir3pm  ...  Humidity9am  Humidity3pm  \\\n0             41          S        SSW  ...           92           84   \n1             41          W          E  ...           83           73   \n2             41        ESE        ESE  ...           88           86   \n3             41        NNE          E  ...           83           90   \n4             41        NNE          W  ...           88           74   \n\n   Pressure9am  Pressure3pm  Cloud9am  Cloud3pm  Temp9am  Temp3pm  RainToday  \\\n0       1017.6       1017.4         8         8     20.7     20.9        Yes   \n1       1017.9       1016.4         7         7     22.4     24.8        Yes   \n2       1016.7       1015.6         7         8     23.5     23.0        Yes   \n3       1014.2       1011.8         8         8     21.4     20.9        Yes   \n4       1008.3       1004.8         8         8     22.5     25.5        Yes   \n\n   RainTomorrow  \n0           Yes  \n1           Yes  \n2           Yes  \n3           Yes  \n4           Yes  \n\n[5 rows x 22 columns]",
            "text/html": "<div>\n<style scoped>\n    .dataframe tbody tr th:only-of-type {\n        vertical-align: middle;\n    }\n\n    .dataframe tbody tr th {\n        vertical-align: top;\n    }\n\n    .dataframe thead th {\n        text-align: right;\n    }\n</style>\n<table border=\"1\" class=\"dataframe\">\n  <thead>\n    <tr style=\"text-align: right;\">\n      <th></th>\n      <th>Date</th>\n      <th>MinTemp</th>\n      <th>MaxTemp</th>\n      <th>Rainfall</th>\n      <th>Evaporation</th>\n      <th>Sunshine</th>\n      <th>WindGustDir</th>\n      <th>WindGustSpeed</th>\n      <th>WindDir9am</th>\n      <th>WindDir3pm</th>\n      <th>...</th>\n      <th>Humidity9am</th>\n      <th>Humidity3pm</th>\n      <th>Pressure9am</th>\n      <th>Pressure3pm</th>\n      <th>Cloud9am</th>\n      <th>Cloud3pm</th>\n      <th>Temp9am</th>\n      <th>Temp3pm</th>\n      <th>RainToday</th>\n      <th>RainTomorrow</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>0</th>\n      <td>2/1/2008</td>\n      <td>19.5</td>\n      <td>22.4</td>\n      <td>15.6</td>\n      <td>6.2</td>\n      <td>0.0</td>\n      <td>W</td>\n      <td>41</td>\n      <td>S</td>\n      <td>SSW</td>\n      <td>...</td>\n      <td>92</td>\n      <td>84</td>\n      <td>1017.6</td>\n      <td>1017.4</td>\n      <td>8</td>\n      <td>8</td>\n      <td>20.7</td>\n      <td>20.9</td>\n      <td>Yes</td>\n      <td>Yes</td>\n    </tr>\n    <tr>\n      <th>1</th>\n      <td>2/2/2008</td>\n      <td>19.5</td>\n      <td>25.6</td>\n      <td>6.0</td>\n      <td>3.4</td>\n      <td>2.7</td>\n      <td>W</td>\n      <td>41</td>\n      <td>W</td>\n      <td>E</td>\n      <td>...</td>\n      <td>83</td>\n      <td>73</td>\n      <td>1017.9</td>\n      <td>1016.4</td>\n      <td>7</td>\n      <td>7</td>\n      <td>22.4</td>\n      <td>24.8</td>\n      <td>Yes</td>\n      <td>Yes</td>\n    </tr>\n    <tr>\n      <th>2</th>\n      <td>2/3/2008</td>\n      <td>21.6</td>\n      <td>24.5</td>\n      <td>6.6</td>\n      <td>2.4</td>\n      <td>0.1</td>\n      <td>W</td>\n      <td>41</td>\n      <td>ESE</td>\n      <td>ESE</td>\n      <td>...</td>\n      <td>88</td>\n      <td>86</td>\n      <td>1016.7</td>\n      <td>1015.6</td>\n      <td>7</td>\n      <td>8</td>\n      <td>23.5</td>\n      <td>23.0</td>\n      <td>Yes</td>\n      <td>Yes</td>\n    </tr>\n    <tr>\n      <th>3</th>\n      <td>2/4/2008</td>\n      <td>20.2</td>\n      <td>22.8</td>\n      <td>18.8</td>\n      <td>2.2</td>\n      <td>0.0</td>\n      <td>W</td>\n      <td>41</td>\n      <td>NNE</td>\n      <td>E</td>\n      <td>...</td>\n      <td>83</td>\n      <td>90</td>\n      <td>1014.2</td>\n      <td>1011.8</td>\n      <td>8</td>\n      <td>8</td>\n      <td>21.4</td>\n      <td>20.9</td>\n      <td>Yes</td>\n      <td>Yes</td>\n    </tr>\n    <tr>\n      <th>4</th>\n      <td>2/5/2008</td>\n      <td>19.7</td>\n      <td>25.7</td>\n      <td>77.4</td>\n      <td>4.8</td>\n      <td>0.0</td>\n      <td>W</td>\n      <td>41</td>\n      <td>NNE</td>\n      <td>W</td>\n      <td>...</td>\n      <td>88</td>\n      <td>74</td>\n      <td>1008.3</td>\n      <td>1004.8</td>\n      <td>8</td>\n      <td>8</td>\n      <td>22.5</td>\n      <td>25.5</td>\n      <td>Yes</td>\n      <td>Yes</td>\n    </tr>\n  </tbody>\n</table>\n<p>5 rows × 22 columns</p>\n</div>"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": "### Data Preprocessing\n",
      "metadata": {}
    },
    {
      "cell_type": "markdown",
      "source": "#### One Hot Encoding\n",
      "metadata": {}
    },
    {
      "cell_type": "markdown",
      "source": "First, we need to perform one hot encoding to convert categorical variables to binary variables.\n",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "df_sydney_processed = pd.get_dummies(data=df, columns=['RainToday', 'WindGustDir', 'WindDir9am', 'WindDir3pm'])",
      "metadata": {
        "trusted": true
      },
      "execution_count": 8,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": "Next, we replace the values of the 'RainTomorrow' column changing them from a categorical column to a binary column. We do not use the `get_dummies` method because we would end up with two columns for 'RainTomorrow' and we do not want, since 'RainTomorrow' is our target.\n",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "df_sydney_processed.replace(['No', 'Yes'], [0,1], inplace=True)",
      "metadata": {
        "trusted": true
      },
      "execution_count": 9,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": "### Training Data and Test Data\n",
      "metadata": {}
    },
    {
      "cell_type": "markdown",
      "source": "Now, we set our 'features' or x values and our Y or target variable.\n",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "df_sydney_processed.drop('Date',axis=1,inplace=True)",
      "metadata": {
        "trusted": true
      },
      "execution_count": 10,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": "df_sydney_processed = df_sydney_processed.astype(float)",
      "metadata": {
        "trusted": true
      },
      "execution_count": 11,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": "features = df_sydney_processed.drop(columns='RainTomorrow', axis=1)\nY = df_sydney_processed['RainTomorrow']",
      "metadata": {
        "trusted": true
      },
      "execution_count": 12,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": "### Linear Regression\n",
      "metadata": {}
    },
    {
      "cell_type": "markdown",
      "source": "#### Q1) Use the `train_test_split` function to split the `features` and `Y` dataframes with a `test_size` of `0.2` and the `random_state` set to `10`.\n",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "#Enter Your Code, Execute and take the Screenshot",
      "metadata": {},
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": "x_train, x_test, y_train, y_test = train_test_split(features, Y, test_size=0.2, random_state=10)\nprint ('Train set:', x_train.shape, y_train.shape)\nprint ('Test set:', x_test.shape, y_test.shape)",
      "metadata": {
        "trusted": true
      },
      "execution_count": 13,
      "outputs": [
        {
          "name": "stdout",
          "text": "Train set: (2616, 66) (2616,)\nTest set: (655, 66) (655,)\n",
          "output_type": "stream"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": "#### Q2) Create and train a Linear Regression model called LinearReg using the training data (`x_train`, `y_train`).\n",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "#Enter Your Code, Execute and take the Screenshot",
      "metadata": {},
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": "from sklearn import linear_model\nLinearReg = linear_model.LinearRegression()\nLinearReg.fit(x_train, y_train)",
      "metadata": {
        "trusted": true
      },
      "execution_count": 14,
      "outputs": [
        {
          "execution_count": 14,
          "output_type": "execute_result",
          "data": {
            "text/plain": "LinearRegression()",
            "text/html": "<style>#sk-container-id-1 {color: black;background-color: white;}#sk-container-id-1 pre{padding: 0;}#sk-container-id-1 div.sk-toggleable {background-color: white;}#sk-container-id-1 label.sk-toggleable__label {cursor: pointer;display: block;width: 100%;margin-bottom: 0;padding: 0.3em;box-sizing: border-box;text-align: center;}#sk-container-id-1 label.sk-toggleable__label-arrow:before {content: \"▸\";float: left;margin-right: 0.25em;color: #696969;}#sk-container-id-1 label.sk-toggleable__label-arrow:hover:before {color: black;}#sk-container-id-1 div.sk-estimator:hover label.sk-toggleable__label-arrow:before {color: black;}#sk-container-id-1 div.sk-toggleable__content {max-height: 0;max-width: 0;overflow: hidden;text-align: left;background-color: #f0f8ff;}#sk-container-id-1 div.sk-toggleable__content pre {margin: 0.2em;color: black;border-radius: 0.25em;background-color: #f0f8ff;}#sk-container-id-1 input.sk-toggleable__control:checked~div.sk-toggleable__content {max-height: 200px;max-width: 100%;overflow: auto;}#sk-container-id-1 input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {content: \"▾\";}#sk-container-id-1 div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 input.sk-hidden--visually {border: 0;clip: rect(1px 1px 1px 1px);clip: rect(1px, 1px, 1px, 1px);height: 1px;margin: -1px;overflow: hidden;padding: 0;position: absolute;width: 1px;}#sk-container-id-1 div.sk-estimator {font-family: monospace;background-color: #f0f8ff;border: 1px dotted black;border-radius: 0.25em;box-sizing: border-box;margin-bottom: 0.5em;}#sk-container-id-1 div.sk-estimator:hover {background-color: #d4ebff;}#sk-container-id-1 div.sk-parallel-item::after {content: \"\";width: 100%;border-bottom: 1px solid gray;flex-grow: 1;}#sk-container-id-1 div.sk-label:hover label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 div.sk-serial::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: 0;}#sk-container-id-1 div.sk-serial {display: flex;flex-direction: column;align-items: center;background-color: white;padding-right: 0.2em;padding-left: 0.2em;position: relative;}#sk-container-id-1 div.sk-item {position: relative;z-index: 1;}#sk-container-id-1 div.sk-parallel {display: flex;align-items: stretch;justify-content: center;background-color: white;position: relative;}#sk-container-id-1 div.sk-item::before, #sk-container-id-1 div.sk-parallel-item::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: -1;}#sk-container-id-1 div.sk-parallel-item {display: flex;flex-direction: column;z-index: 1;position: relative;background-color: white;}#sk-container-id-1 div.sk-parallel-item:first-child::after {align-self: flex-end;width: 50%;}#sk-container-id-1 div.sk-parallel-item:last-child::after {align-self: flex-start;width: 50%;}#sk-container-id-1 div.sk-parallel-item:only-child::after {width: 0;}#sk-container-id-1 div.sk-dashed-wrapped {border: 1px dashed gray;margin: 0 0.4em 0.5em 0.4em;box-sizing: border-box;padding-bottom: 0.4em;background-color: white;}#sk-container-id-1 div.sk-label label {font-family: monospace;font-weight: bold;display: inline-block;line-height: 1.2em;}#sk-container-id-1 div.sk-label-container {text-align: center;}#sk-container-id-1 div.sk-container {/* jupyter's `normalize.less` sets `[hidden] { display: none; }` but bootstrap.min.css set `[hidden] { display: none !important; }` so we also need the `!important` here to be able to override the default hidden behavior on the sphinx rendered scikit-learn.org. See: https://github.com/scikit-learn/scikit-learn/issues/21755 */display: inline-block !important;position: relative;}#sk-container-id-1 div.sk-text-repr-fallback {display: none;}</style><div id=\"sk-container-id-1\" class=\"sk-top-container\"><div class=\"sk-text-repr-fallback\"><pre>LinearRegression()</pre><b>In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook. <br />On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.</b></div><div class=\"sk-container\" hidden><div class=\"sk-item\"><div class=\"sk-estimator sk-toggleable\"><input class=\"sk-toggleable__control sk-hidden--visually\" id=\"sk-estimator-id-1\" type=\"checkbox\" checked><label for=\"sk-estimator-id-1\" class=\"sk-toggleable__label sk-toggleable__label-arrow\">LinearRegression</label><div class=\"sk-toggleable__content\"><pre>LinearRegression()</pre></div></div></div></div></div>"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": "#### Q3) Now use the `predict` method on the testing data (`x_test`) and save it to the array `predictions`.\n",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "#Enter Your Code, Execute and take the Screenshot",
      "metadata": {},
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": "predictions = LinearReg.predict(x_test)",
      "metadata": {
        "trusted": true
      },
      "execution_count": 15,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": "#### Q4) Using the `predictions` and the `y_test` dataframe calculate the value for each metric using the appropriate function.\n",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "#Enter Your Code, Execute and take the Screenshot",
      "metadata": {},
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": "from sklearn.metrics import r2_score\nLinearRegression_MAE = np.mean(np.absolute(predictions - y_test))\nLinearRegression_MSE = np.mean((predictions - y_test)**2)\nLinearRegression_R2 =  r2_score(y_test , predictions)\n\nprint( 'MAE:', LinearRegression_MAE)\nprint('MSE:', LinearRegression_MSE)\nprint ('R2:',LinearRegression_R2)",
      "metadata": {
        "trusted": true
      },
      "execution_count": 18,
      "outputs": [
        {
          "name": "stdout",
          "text": "MAE: 0.2563193284828244\nMSE: 0.1157212427649327\nR2: 0.4271288403809509\n",
          "output_type": "stream"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": "#### Q5) Show the MAE, MSE, and R2 in a tabular format using data frame for the linear model.\n",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "#Enter Your Code, Execute and take the Screenshot",
      "metadata": {},
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": "Report = {\"Metrics\" :[\"MAE\", \"MSE\", \"R2\"], \"Values\" : [LinearRegression_MAE, LinearRegression_MSE, LinearRegression_R2]}\nLinear_Report= pd.DataFrame(Report)\nLinear_Report\n          ",
      "metadata": {
        "trusted": true
      },
      "execution_count": 19,
      "outputs": [
        {
          "execution_count": 19,
          "output_type": "execute_result",
          "data": {
            "text/plain": "  Metrics    Values\n0     MAE  0.256319\n1     MSE  0.115721\n2      R2  0.427129",
            "text/html": "<div>\n<style scoped>\n    .dataframe tbody tr th:only-of-type {\n        vertical-align: middle;\n    }\n\n    .dataframe tbody tr th {\n        vertical-align: top;\n    }\n\n    .dataframe thead th {\n        text-align: right;\n    }\n</style>\n<table border=\"1\" class=\"dataframe\">\n  <thead>\n    <tr style=\"text-align: right;\">\n      <th></th>\n      <th>Metrics</th>\n      <th>Values</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>0</th>\n      <td>MAE</td>\n      <td>0.256319</td>\n    </tr>\n    <tr>\n      <th>1</th>\n      <td>MSE</td>\n      <td>0.115721</td>\n    </tr>\n    <tr>\n      <th>2</th>\n      <td>R2</td>\n      <td>0.427129</td>\n    </tr>\n  </tbody>\n</table>\n</div>"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": "### KNN\n",
      "metadata": {}
    },
    {
      "cell_type": "markdown",
      "source": "#### Q6) Create and train a KNN model called KNN using the training data (`x_train`, `y_train`) with the `n_neighbors` parameter set to `4`.\n",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "#Enter Your Code Below, Execute, and Save the Screenshot of the Final Output",
      "metadata": {},
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": "KNN = KNeighborsClassifier(n_neighbors = 4).fit(x_train,y_train)",
      "metadata": {
        "trusted": true
      },
      "execution_count": 20,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": "#### Q7) Now use the `predict` method on the testing data (`x_test`) and save it to the array `predictions`.\n",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "#Enter Your Code Below, Execute, and Save the Screenshot of the Final Output",
      "metadata": {},
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": "predictions = KNN.predict(x_test)",
      "metadata": {
        "trusted": true
      },
      "execution_count": 24,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": "#### Q8) Using the `predictions` and the `y_test` dataframe calculate the value for each metric using the appropriate function.\n",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "#Enter Your Code Below, Execute, and Save the Screenshot of the Final Output",
      "metadata": {},
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": "KNN_Accuracy_Score = metrics.accuracy_score(y_test, predictions)\nKNN_JaccardIndex = jaccard_score(y_test, predictions)\nKNN_F1_Score = f1_score(y_test, predictions)\n\nprint(\"KNN_Accuracy_Score:\", KNN_Accuracy_Score )\nprint(\"KNN_JaccardIndex:\", KNN_JaccardIndex)\nprint(\"KNN_F1_Score:\", KNN_F1_Score)",
      "metadata": {
        "trusted": true
      },
      "execution_count": 25,
      "outputs": [
        {
          "name": "stdout",
          "text": "KNN_Accuracy_Score: 0.8183206106870229\nKNN_JaccardIndex: 0.4251207729468599\nKNN_F1_Score: 0.5966101694915255\n",
          "output_type": "stream"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": "### Decision Tree\n",
      "metadata": {}
    },
    {
      "cell_type": "markdown",
      "source": "#### Q9) Create and train a Decision Tree model called Tree using the training data (`x_train`, `y_train`).\n",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "#Enter Your Code, Execute and take the Screenshot",
      "metadata": {},
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": "Tree = DecisionTreeClassifier(criterion=\"entropy\", max_depth = 4)\nTree.fit(x_train, y_train)",
      "metadata": {
        "trusted": true
      },
      "execution_count": 26,
      "outputs": [
        {
          "execution_count": 26,
          "output_type": "execute_result",
          "data": {
            "text/plain": "DecisionTreeClassifier(criterion='entropy', max_depth=4)",
            "text/html": "<style>#sk-container-id-2 {color: black;background-color: white;}#sk-container-id-2 pre{padding: 0;}#sk-container-id-2 div.sk-toggleable {background-color: white;}#sk-container-id-2 label.sk-toggleable__label {cursor: pointer;display: block;width: 100%;margin-bottom: 0;padding: 0.3em;box-sizing: border-box;text-align: center;}#sk-container-id-2 label.sk-toggleable__label-arrow:before {content: \"▸\";float: left;margin-right: 0.25em;color: #696969;}#sk-container-id-2 label.sk-toggleable__label-arrow:hover:before {color: black;}#sk-container-id-2 div.sk-estimator:hover label.sk-toggleable__label-arrow:before {color: black;}#sk-container-id-2 div.sk-toggleable__content {max-height: 0;max-width: 0;overflow: hidden;text-align: left;background-color: #f0f8ff;}#sk-container-id-2 div.sk-toggleable__content pre {margin: 0.2em;color: black;border-radius: 0.25em;background-color: #f0f8ff;}#sk-container-id-2 input.sk-toggleable__control:checked~div.sk-toggleable__content {max-height: 200px;max-width: 100%;overflow: auto;}#sk-container-id-2 input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {content: \"▾\";}#sk-container-id-2 div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-2 div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-2 input.sk-hidden--visually {border: 0;clip: rect(1px 1px 1px 1px);clip: rect(1px, 1px, 1px, 1px);height: 1px;margin: -1px;overflow: hidden;padding: 0;position: absolute;width: 1px;}#sk-container-id-2 div.sk-estimator {font-family: monospace;background-color: #f0f8ff;border: 1px dotted black;border-radius: 0.25em;box-sizing: border-box;margin-bottom: 0.5em;}#sk-container-id-2 div.sk-estimator:hover {background-color: #d4ebff;}#sk-container-id-2 div.sk-parallel-item::after {content: \"\";width: 100%;border-bottom: 1px solid gray;flex-grow: 1;}#sk-container-id-2 div.sk-label:hover label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-2 div.sk-serial::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: 0;}#sk-container-id-2 div.sk-serial {display: flex;flex-direction: column;align-items: center;background-color: white;padding-right: 0.2em;padding-left: 0.2em;position: relative;}#sk-container-id-2 div.sk-item {position: relative;z-index: 1;}#sk-container-id-2 div.sk-parallel {display: flex;align-items: stretch;justify-content: center;background-color: white;position: relative;}#sk-container-id-2 div.sk-item::before, #sk-container-id-2 div.sk-parallel-item::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: -1;}#sk-container-id-2 div.sk-parallel-item {display: flex;flex-direction: column;z-index: 1;position: relative;background-color: white;}#sk-container-id-2 div.sk-parallel-item:first-child::after {align-self: flex-end;width: 50%;}#sk-container-id-2 div.sk-parallel-item:last-child::after {align-self: flex-start;width: 50%;}#sk-container-id-2 div.sk-parallel-item:only-child::after {width: 0;}#sk-container-id-2 div.sk-dashed-wrapped {border: 1px dashed gray;margin: 0 0.4em 0.5em 0.4em;box-sizing: border-box;padding-bottom: 0.4em;background-color: white;}#sk-container-id-2 div.sk-label label {font-family: monospace;font-weight: bold;display: inline-block;line-height: 1.2em;}#sk-container-id-2 div.sk-label-container {text-align: center;}#sk-container-id-2 div.sk-container {/* jupyter's `normalize.less` sets `[hidden] { display: none; }` but bootstrap.min.css set `[hidden] { display: none !important; }` so we also need the `!important` here to be able to override the default hidden behavior on the sphinx rendered scikit-learn.org. See: https://github.com/scikit-learn/scikit-learn/issues/21755 */display: inline-block !important;position: relative;}#sk-container-id-2 div.sk-text-repr-fallback {display: none;}</style><div id=\"sk-container-id-2\" class=\"sk-top-container\"><div class=\"sk-text-repr-fallback\"><pre>DecisionTreeClassifier(criterion=&#x27;entropy&#x27;, max_depth=4)</pre><b>In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook. <br />On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.</b></div><div class=\"sk-container\" hidden><div class=\"sk-item\"><div class=\"sk-estimator sk-toggleable\"><input class=\"sk-toggleable__control sk-hidden--visually\" id=\"sk-estimator-id-2\" type=\"checkbox\" checked><label for=\"sk-estimator-id-2\" class=\"sk-toggleable__label sk-toggleable__label-arrow\">DecisionTreeClassifier</label><div class=\"sk-toggleable__content\"><pre>DecisionTreeClassifier(criterion=&#x27;entropy&#x27;, max_depth=4)</pre></div></div></div></div></div>"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": "#### Q10) Now use the `predict` method on the testing data (`x_test`) and save it to the array `predictions`.\n",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "#Enter Your Code, Execute and take the Screenshot",
      "metadata": {},
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": "predictions = Tree.predict(x_test)",
      "metadata": {
        "trusted": true
      },
      "execution_count": 27,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": "#### Q11) Using the `predictions` and the `y_test` dataframe calculate the value for each metric using the appropriate function.\n",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "#Enter Your Code, Execute and take the Screenshot",
      "metadata": {},
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": "Tree_Accuracy_Score = metrics.accuracy_score(y_test, predictions)\nTree_JaccardIndex = jaccard_score(y_test, predictions)\nTree_F1_Score = f1_score(y_test, predictions)\n\nprint(\"Tree_Accuracy_Score:\", Tree_Accuracy_Score)\nprint(\"Tree_JaccardIndex:\", Tree_JaccardIndex)\nprint(\"Tree_F1_Score:\", Tree_F1_Score)",
      "metadata": {
        "trusted": true
      },
      "execution_count": 28,
      "outputs": [
        {
          "name": "stdout",
          "text": "Tree_Accuracy_Score: 0.8183206106870229\nTree_JaccardIndex: 0.48034934497816595\nTree_F1_Score: 0.6489675516224188\n",
          "output_type": "stream"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": "### Logistic Regression\n",
      "metadata": {}
    },
    {
      "cell_type": "markdown",
      "source": "#### Q12) Use the `train_test_split` function to split the `features` and `Y` dataframes with a `test_size` of `0.2` and the `random_state` set to `1`.\n",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "#Enter Your Code, Execute and take the Screenshot",
      "metadata": {},
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": "x_train, x_test, y_train, y_test = train_test_split( features, Y, test_size=0.2, random_state=1)",
      "metadata": {
        "trusted": true
      },
      "execution_count": 31,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": "#### Q13) Create and train a LogisticRegression model called LR using the training data (`x_train`, `y_train`) with the `solver` parameter set to `liblinear`.\n",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "#Enter Your Code, Execute and take the Screenshot",
      "metadata": {},
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": "LR = LogisticRegression(C=0.01, solver='liblinear').fit(x_train,y_train)\nLR",
      "metadata": {
        "trusted": true
      },
      "execution_count": 32,
      "outputs": [
        {
          "execution_count": 32,
          "output_type": "execute_result",
          "data": {
            "text/plain": "LogisticRegression(C=0.01, solver='liblinear')",
            "text/html": "<style>#sk-container-id-3 {color: black;background-color: white;}#sk-container-id-3 pre{padding: 0;}#sk-container-id-3 div.sk-toggleable {background-color: white;}#sk-container-id-3 label.sk-toggleable__label {cursor: pointer;display: block;width: 100%;margin-bottom: 0;padding: 0.3em;box-sizing: border-box;text-align: center;}#sk-container-id-3 label.sk-toggleable__label-arrow:before {content: \"▸\";float: left;margin-right: 0.25em;color: #696969;}#sk-container-id-3 label.sk-toggleable__label-arrow:hover:before {color: black;}#sk-container-id-3 div.sk-estimator:hover label.sk-toggleable__label-arrow:before {color: black;}#sk-container-id-3 div.sk-toggleable__content {max-height: 0;max-width: 0;overflow: hidden;text-align: left;background-color: #f0f8ff;}#sk-container-id-3 div.sk-toggleable__content pre {margin: 0.2em;color: black;border-radius: 0.25em;background-color: #f0f8ff;}#sk-container-id-3 input.sk-toggleable__control:checked~div.sk-toggleable__content {max-height: 200px;max-width: 100%;overflow: auto;}#sk-container-id-3 input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {content: \"▾\";}#sk-container-id-3 div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-3 div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-3 input.sk-hidden--visually {border: 0;clip: rect(1px 1px 1px 1px);clip: rect(1px, 1px, 1px, 1px);height: 1px;margin: -1px;overflow: hidden;padding: 0;position: absolute;width: 1px;}#sk-container-id-3 div.sk-estimator {font-family: monospace;background-color: #f0f8ff;border: 1px dotted black;border-radius: 0.25em;box-sizing: border-box;margin-bottom: 0.5em;}#sk-container-id-3 div.sk-estimator:hover {background-color: #d4ebff;}#sk-container-id-3 div.sk-parallel-item::after {content: \"\";width: 100%;border-bottom: 1px solid gray;flex-grow: 1;}#sk-container-id-3 div.sk-label:hover label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-3 div.sk-serial::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: 0;}#sk-container-id-3 div.sk-serial {display: flex;flex-direction: column;align-items: center;background-color: white;padding-right: 0.2em;padding-left: 0.2em;position: relative;}#sk-container-id-3 div.sk-item {position: relative;z-index: 1;}#sk-container-id-3 div.sk-parallel {display: flex;align-items: stretch;justify-content: center;background-color: white;position: relative;}#sk-container-id-3 div.sk-item::before, #sk-container-id-3 div.sk-parallel-item::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: -1;}#sk-container-id-3 div.sk-parallel-item {display: flex;flex-direction: column;z-index: 1;position: relative;background-color: white;}#sk-container-id-3 div.sk-parallel-item:first-child::after {align-self: flex-end;width: 50%;}#sk-container-id-3 div.sk-parallel-item:last-child::after {align-self: flex-start;width: 50%;}#sk-container-id-3 div.sk-parallel-item:only-child::after {width: 0;}#sk-container-id-3 div.sk-dashed-wrapped {border: 1px dashed gray;margin: 0 0.4em 0.5em 0.4em;box-sizing: border-box;padding-bottom: 0.4em;background-color: white;}#sk-container-id-3 div.sk-label label {font-family: monospace;font-weight: bold;display: inline-block;line-height: 1.2em;}#sk-container-id-3 div.sk-label-container {text-align: center;}#sk-container-id-3 div.sk-container {/* jupyter's `normalize.less` sets `[hidden] { display: none; }` but bootstrap.min.css set `[hidden] { display: none !important; }` so we also need the `!important` here to be able to override the default hidden behavior on the sphinx rendered scikit-learn.org. See: https://github.com/scikit-learn/scikit-learn/issues/21755 */display: inline-block !important;position: relative;}#sk-container-id-3 div.sk-text-repr-fallback {display: none;}</style><div id=\"sk-container-id-3\" class=\"sk-top-container\"><div class=\"sk-text-repr-fallback\"><pre>LogisticRegression(C=0.01, solver=&#x27;liblinear&#x27;)</pre><b>In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook. <br />On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.</b></div><div class=\"sk-container\" hidden><div class=\"sk-item\"><div class=\"sk-estimator sk-toggleable\"><input class=\"sk-toggleable__control sk-hidden--visually\" id=\"sk-estimator-id-3\" type=\"checkbox\" checked><label for=\"sk-estimator-id-3\" class=\"sk-toggleable__label sk-toggleable__label-arrow\">LogisticRegression</label><div class=\"sk-toggleable__content\"><pre>LogisticRegression(C=0.01, solver=&#x27;liblinear&#x27;)</pre></div></div></div></div></div>"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": "#### Q14) Now, use the `predict` and `predict_proba` methods on the testing data (`x_test`) and save it as 2 arrays `predictions` and `predict_proba`.\n",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "#Enter Your Code, Execute and take the Screenshot",
      "metadata": {},
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": "predictions = LR.predict(x_test)\n",
      "metadata": {
        "trusted": true
      },
      "execution_count": 37,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": "predict_proba = LR.predict_proba(x_test)\npredict_proba",
      "metadata": {
        "trusted": true
      },
      "execution_count": 36,
      "outputs": [
        {
          "execution_count": 36,
          "output_type": "execute_result",
          "data": {
            "text/plain": "array([[0.71865751, 0.28134249],\n       [0.9758825 , 0.0241175 ],\n       [0.49701165, 0.50298835],\n       ...,\n       [0.97264147, 0.02735853],\n       [0.73340911, 0.26659089],\n       [0.38535984, 0.61464016]])"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": "#### Q15) Using the `predictions`, `predict_proba` and the `y_test` dataframe calculate the value for each metric using the appropriate function.\n",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "#Enter Your Code, Execute and take the Screenshot",
      "metadata": {},
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": "LR_Accuracy_Score = metrics.accuracy_score(y_test, predictions)\nLR_JaccardIndex = jaccard_score(y_test, predictions)\nLR_F1_Score = f1_score(y_test, predictions)\nLR_Log_Loss = log_loss(y_test, predict_proba)\n\nprint(\"LR_Accuracy_Score:\", LR_Accuracy_Score)\nprint(\"LR_JaccardIndex:\", LR_JaccardIndex)\nprint(\"LR_F1_Score:\", LR_F1_Score)\nprint(\"LR_Log_Loss:\", LR_Log_Loss)",
      "metadata": {
        "trusted": true
      },
      "execution_count": 40,
      "outputs": [
        {
          "name": "stdout",
          "text": "LR_Accuracy_Score: 0.8274809160305343\nLR_JaccardIndex: 0.4840182648401826\nLR_F1_Score: 0.6523076923076923\nLR_Log_Loss: 0.3800847372796161\n",
          "output_type": "stream"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": "### SVM\n",
      "metadata": {}
    },
    {
      "cell_type": "markdown",
      "source": "#### Q16) Create and train a SVM model called SVM using the training data (`x_train`, `y_train`).\n",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "#Enter Your Code Below, Execute, and Save the Screenshot of the Final Output",
      "metadata": {},
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": "SVM = svm.SVC(kernel= \"rbf\")\nSVM.fit(x_train, y_train)",
      "metadata": {
        "trusted": true
      },
      "execution_count": 41,
      "outputs": [
        {
          "execution_count": 41,
          "output_type": "execute_result",
          "data": {
            "text/plain": "SVC()",
            "text/html": "<style>#sk-container-id-4 {color: black;background-color: white;}#sk-container-id-4 pre{padding: 0;}#sk-container-id-4 div.sk-toggleable {background-color: white;}#sk-container-id-4 label.sk-toggleable__label {cursor: pointer;display: block;width: 100%;margin-bottom: 0;padding: 0.3em;box-sizing: border-box;text-align: center;}#sk-container-id-4 label.sk-toggleable__label-arrow:before {content: \"▸\";float: left;margin-right: 0.25em;color: #696969;}#sk-container-id-4 label.sk-toggleable__label-arrow:hover:before {color: black;}#sk-container-id-4 div.sk-estimator:hover label.sk-toggleable__label-arrow:before {color: black;}#sk-container-id-4 div.sk-toggleable__content {max-height: 0;max-width: 0;overflow: hidden;text-align: left;background-color: #f0f8ff;}#sk-container-id-4 div.sk-toggleable__content pre {margin: 0.2em;color: black;border-radius: 0.25em;background-color: #f0f8ff;}#sk-container-id-4 input.sk-toggleable__control:checked~div.sk-toggleable__content {max-height: 200px;max-width: 100%;overflow: auto;}#sk-container-id-4 input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {content: \"▾\";}#sk-container-id-4 div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-4 div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-4 input.sk-hidden--visually {border: 0;clip: rect(1px 1px 1px 1px);clip: rect(1px, 1px, 1px, 1px);height: 1px;margin: -1px;overflow: hidden;padding: 0;position: absolute;width: 1px;}#sk-container-id-4 div.sk-estimator {font-family: monospace;background-color: #f0f8ff;border: 1px dotted black;border-radius: 0.25em;box-sizing: border-box;margin-bottom: 0.5em;}#sk-container-id-4 div.sk-estimator:hover {background-color: #d4ebff;}#sk-container-id-4 div.sk-parallel-item::after {content: \"\";width: 100%;border-bottom: 1px solid gray;flex-grow: 1;}#sk-container-id-4 div.sk-label:hover label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-4 div.sk-serial::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: 0;}#sk-container-id-4 div.sk-serial {display: flex;flex-direction: column;align-items: center;background-color: white;padding-right: 0.2em;padding-left: 0.2em;position: relative;}#sk-container-id-4 div.sk-item {position: relative;z-index: 1;}#sk-container-id-4 div.sk-parallel {display: flex;align-items: stretch;justify-content: center;background-color: white;position: relative;}#sk-container-id-4 div.sk-item::before, #sk-container-id-4 div.sk-parallel-item::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: -1;}#sk-container-id-4 div.sk-parallel-item {display: flex;flex-direction: column;z-index: 1;position: relative;background-color: white;}#sk-container-id-4 div.sk-parallel-item:first-child::after {align-self: flex-end;width: 50%;}#sk-container-id-4 div.sk-parallel-item:last-child::after {align-self: flex-start;width: 50%;}#sk-container-id-4 div.sk-parallel-item:only-child::after {width: 0;}#sk-container-id-4 div.sk-dashed-wrapped {border: 1px dashed gray;margin: 0 0.4em 0.5em 0.4em;box-sizing: border-box;padding-bottom: 0.4em;background-color: white;}#sk-container-id-4 div.sk-label label {font-family: monospace;font-weight: bold;display: inline-block;line-height: 1.2em;}#sk-container-id-4 div.sk-label-container {text-align: center;}#sk-container-id-4 div.sk-container {/* jupyter's `normalize.less` sets `[hidden] { display: none; }` but bootstrap.min.css set `[hidden] { display: none !important; }` so we also need the `!important` here to be able to override the default hidden behavior on the sphinx rendered scikit-learn.org. See: https://github.com/scikit-learn/scikit-learn/issues/21755 */display: inline-block !important;position: relative;}#sk-container-id-4 div.sk-text-repr-fallback {display: none;}</style><div id=\"sk-container-id-4\" class=\"sk-top-container\"><div class=\"sk-text-repr-fallback\"><pre>SVC()</pre><b>In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook. <br />On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.</b></div><div class=\"sk-container\" hidden><div class=\"sk-item\"><div class=\"sk-estimator sk-toggleable\"><input class=\"sk-toggleable__control sk-hidden--visually\" id=\"sk-estimator-id-4\" type=\"checkbox\" checked><label for=\"sk-estimator-id-4\" class=\"sk-toggleable__label sk-toggleable__label-arrow\">SVC</label><div class=\"sk-toggleable__content\"><pre>SVC()</pre></div></div></div></div></div>"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": "#### Q17) Now use the `predict` method on the testing data (`x_test`) and save it to the array `predictions`.\n",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "#Enter Your Code Below, Execute, and Save the Screenshot of the Final Output",
      "metadata": {},
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": "predictions = SVM.predict(x_test)\n",
      "metadata": {
        "trusted": true
      },
      "execution_count": 43,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": "#### Q18) Using the `predictions` and the `y_test` dataframe calculate the value for each metric using the appropriate function.\n",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "SVM_Accuracy_Score = metrics.accuracy_score(y_test, predictions)\nSVM_JaccardIndex = jaccard_score(y_test, predictions)\nSVM_F1_Score = f1_score(y_test, predictions)\n\nprint(\"SVM_Accuracy_Score:\", SVM_Accuracy_Score)\nprint(\"SVM_JaccardIndex:\", SVM_JaccardIndex)\nprint(\"SVM_F1_Score:\", SVM_F1_Score)",
      "metadata": {
        "trusted": true
      },
      "execution_count": 44,
      "outputs": [
        {
          "name": "stdout",
          "text": "SVM_Accuracy_Score: 0.7221374045801526\nSVM_JaccardIndex: 0.0\nSVM_F1_Score: 0.0\n",
          "output_type": "stream"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": "### Report\n",
      "metadata": {}
    },
    {
      "cell_type": "markdown",
      "source": "#### Q19) Show the Accuracy,Jaccard Index,F1-Score and LogLoss in a tabular format using data frame for all of the above models.\n\n\\*LogLoss is only for Logistic Regression Model\n",
      "metadata": {}
    },
    {
      "cell_type": "code",
      "source": "List_acc=[KNN_Accuracy_Score,Tree_Accuracy_Score,LR_Accuracy_Score,SVM_Accuracy_Score]\nList_jac=[KNN_JaccardIndex,Tree_JaccardIndex,LR_JaccardIndex, SVM_JaccardIndex]\nList_F1= [KNN_F1_Score,Tree_F1_Score,LR_F1_Score,SVM_F1_Score]\nList_Log=['NA','NA', LR_Log_Loss,'NA']\n\n\nReport = pd.DataFrame(List_acc, index=['KNN', 'Decision Tree', 'Logistic regression', 'SVM'])\nReport.columns=['Accuracy_score']\nReport.insert(loc=1, column='Jaccard_Index', value= List_jac)\nReport.insert(loc=2, column='F1_score', value= List_F1)\nReport.insert(loc=3, column='Log_loss', value= List_Log)\n\n\nReport   ",
      "metadata": {
        "trusted": true
      },
      "execution_count": 52,
      "outputs": [
        {
          "execution_count": 52,
          "output_type": "execute_result",
          "data": {
            "text/plain": "                     Accuracy_score  Jaccard_Index  F1_score  Log_loss\nKNN                        0.818321       0.425121  0.596610        NA\nDecision Tree              0.818321       0.480349  0.648968        NA\nLogistic regression        0.827481       0.484018  0.652308  0.380085\nSVM                        0.722137       0.000000  0.000000        NA",
            "text/html": "<div>\n<style scoped>\n    .dataframe tbody tr th:only-of-type {\n        vertical-align: middle;\n    }\n\n    .dataframe tbody tr th {\n        vertical-align: top;\n    }\n\n    .dataframe thead th {\n        text-align: right;\n    }\n</style>\n<table border=\"1\" class=\"dataframe\">\n  <thead>\n    <tr style=\"text-align: right;\">\n      <th></th>\n      <th>Accuracy_score</th>\n      <th>Jaccard_Index</th>\n      <th>F1_score</th>\n      <th>Log_loss</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>KNN</th>\n      <td>0.818321</td>\n      <td>0.425121</td>\n      <td>0.596610</td>\n      <td>NA</td>\n    </tr>\n    <tr>\n      <th>Decision Tree</th>\n      <td>0.818321</td>\n      <td>0.480349</td>\n      <td>0.648968</td>\n      <td>NA</td>\n    </tr>\n    <tr>\n      <th>Logistic regression</th>\n      <td>0.827481</td>\n      <td>0.484018</td>\n      <td>0.652308</td>\n      <td>0.380085</td>\n    </tr>\n    <tr>\n      <th>SVM</th>\n      <td>0.722137</td>\n      <td>0.000000</td>\n      <td>0.000000</td>\n      <td>NA</td>\n    </tr>\n  </tbody>\n</table>\n</div>"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": "<h2 id=\"Section_5\">  How to submit </h2>\n\n<p>Once you complete your notebook you will have to share it. You can download the notebook by navigating to \"File\" and clicking on \"Download\" button.\n\n<p>This will save the (.ipynb) file on your computer. Once saved, you can upload this file in the \"My Submission\" tab, of the \"Peer-graded Assignment\" section.  \n",
      "metadata": {}
    },
    {
      "cell_type": "markdown",
      "source": "<h2>About the Authors:</h2> \n\n<a href=\"https://www.linkedin.com/in/joseph-s-50398b136/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkML0101ENSkillsNetwork20718538-2022-01-01\">Joseph Santarcangelo</a> has a PhD in Electrical Engineering, his research focused on using machine learning, signal processing, and computer vision to determine how videos impact human cognition. Joseph has been working for IBM since he completed his PhD.\n\n### Other Contributors\n\n[Svitlana Kramar](https://www.linkedin.com/in/svitlana-kramar/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMML0232ENSkillsNetwork30654641-2022-01-01)\n",
      "metadata": {}
    },
    {
      "cell_type": "markdown",
      "source": "## Change Log\n\n| Date (YYYY-MM-DD) | Version | Changed By    | Change Description          |\n| ----------------- | ------- | ------------- | --------------------------- |\n| 2022-06-22        | 2.0     | Svitlana K.   | Deleted GridSearch and Mock |\n\n## <h3 align=\"center\"> © IBM Corporation 2020. All rights reserved. <h3/>\n",
      "metadata": {}
    }
  ]
}