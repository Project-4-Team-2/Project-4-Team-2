# Project_04 - Alzheimer Risks
Repository for Project 4 of Data visualization bootcamp (U of T SCS)
Project 4: Team 2 

## Project Overview and Purpose 

Dataset: Alzheimer's Disease Dataset

Dataset Source: (https://www.kaggle.com/datasets/rabieelkharoua/alzheimers-disease-dataset/data)

	Libraries used: Pandas, Numpy, MatPlotLib, JSON, Sqlite, SQLAlchemy, Plotly, D3, Tableau, SkLearn, PCA
 	
  	Languages used: Python, SQL
	
 	GitHub Link: https://github.com/Project-4-Team-2/Project-4-Team-2
	
 	Contributors of the projects: Anna, Ria, Yi, Yumai

**HIGH LEVEL PROBLEM STATEMENT** 
	
What are modifiable and nonmodifiable metrics that most accurately predict onset of Alzheimer’s Disease?

**HYPOTHESIS** 

There is no individual metric that can predict Alzheimer’s disease. 

**Sub-questions covering 3 topics and a tableau dashboard:**

1. Can demographic features help predict the Alzheimer’s diagnosis through correlation and statistical analysis? 
2. Did lifestyle choices impact your likelihood of developing Alzheimer’s? 
3. Can Medical History factors aid in prediction of your likelihood of Alzheimer's? 

### Purpose ###

This project aims to develop a tool to identify the key factors that contribute to the onset and progression of Alzheimer's Disease. 

We used Python to clean and transform data and stored it on SQL database. Data was accessed through sqlite or the downloaded csv files. Simple data visualizations were done using plotly, seaborn and Tableau. Final images were created and displayed in our Tableau dashboard. 

## Workflow ## 

![FlowChart](https://github.com/user-attachments/assets/9ee4b29d-e659-42bf-862b-d4943cff7db6)

## Interactive Dashboard and Machine Learning ##

Please follow these steps to interact with our data visualizations, dashboard and Machine Learning Models:

Our data analysis can be separated into five main components: 

1. Unsupervised Learning Model
   > i. Please navigate to "Alzheimer_UnsupervisedTraining _All" to view unsupervised training completed for all features in this dataset.
   > 
   > ii. Please navigate to "Alzheimer_UnsupervisedTraining _Lifestyle" to view unsupervised training completed for lifestyle features in this dataset.
   >
   > iii. Unsupervised machine learning for demographic features can be found in "Alzheimer_Demographic_MLU.ipynb".
   > 
2. Supervised Learning Model
   > i. Navigate to "Alzheimer_SupervisedTraining" to view all the attempted supervised learning models for all features in this dataset. Our Random Tree Classification and Decision Tree models produce recall and accuracy scores >90%. We attempted RandomOverSampler from imbalanced-learn in order to randomly select samples from minority classes and adding them to the training dataset, to improve resolution and signal-to-noise ratio.
   >
   > ii. Navigate to "Alzheimer_Demographic_MLS.ipynb" to view our Machine Learning Model for Demographics data combined with the Top 5 Features. Random Tree Classifier was able to yield recall of 98% and 90%, with accuracy at 95%.
   > 
3. Neural Network Machine Learning Model
   > i. Navigate to "Alzheimer_NeuralNetwork_TopFeatures" to view our Neural Network Machine Learning Model for the Top Features in our dataset (Functional Assessment, ADL, Memory Complaints, MMSE, Behavioral Problems). These top features were determined by analyzing >0.2 Spearman's Correlation Coefficients. Also in this file is the Random Tree Classifier that identifies a recall of 98% and 90% with an accuracy of 93%. This is higher, and more reliable than our Neural Network Model, which yields an accuracy of 81% and a loss of 0.47, whilst for the validation set has an accuracy of 85% with a loss of 0.38. Although the Neural Network is reliable (with generalization and low likelihood of over-fitting), we can see higher accuracy and recall with the Random Tree Classifier.
   > 
   > ii. Navigate to "Alzheimer_NeuralNetwork_All" to view a Neural Network model produced for all features in this dataset. Unfortunately, Accuracy was low and Loss high for these models, and validation also yielded unreliability if all features were used.
   >
   > iii. Neural Network model for demographic features can be found in "Alzheimer_Demographic_DL.ipynb"

4. Please view our Presentation Powerpoint at "Project 04 _ Team 2 Powerpoint"
   
6. Preprocessing and Data Visualization (Category based)
   > i. Navigate to "alzheimer_analysis_pre" to view data cleaning and preliminary visualizations for BMI, Physical Activity, Diet Quality, Sleep Quality and Alcohol Consumption using Seaborn and Plotly. This is the base file we used to produce the "alzheimer_clean.csv" file for later analysis.
   > 
   > ii. Navigate to "Alzheimer_Demographic_Visual.ipynb" to view visualizations produced using Plotly, dash and Seaborn. This file utilized SQlite to store the data on a SQL database.
   > 
   > iii. Please navigate to branch "Ria" to view visualizations for Medical History related features.
   > 
   > iv. Please navigate to branch "annabranch" to view visualizations and exploratory supervised learning models for features under the "Lifestyle Choices" category.
   >
   > v. Data visualization including Tableau processing, unsupervised machine learning, supervised machine learning and neural network for "Demographic" category can be found in the branch "Yi".

### Please view our Tableau Dashboard as linked below ###

![EduLevel](https://github.com/user-attachments/assets/8c26bb4d-f55a-4c32-8304-d95a4f54190e)

LINK: https://public.tableau.com/app/profile/yi.wen7753/viz/ADFactors/FactorsImpactonAD?publish=yes

LINK: https://public.tableau.com/app/profile/yi.wen7753/viz/Corr_visual/Corr_diagnosis_features?publish=yes

## Ethical Considerations ##

1. Copy right - The dataset was obtained from kaggle website with CC BY 4.0 license which allows users to share and adapt the dataset for any purpose with no issue of copywrite.

2. Privacy and Data Protection - Personal information of patients and doctors are protected in this dataset
   
3. Distribution of Benefits - The dataset used in this project is for education purposes. The dataset was analyzed and presented publicly and transparently which can bring pulics' attention to diagnosis of Alzheimer's disease.

## Data Source References ##

@misc{rabie_el_kharoua_2024,
title={Alzheimer's Disease Dataset},
url={https://www.kaggle.com/dsv/8668279},
DOI={10.34740/KAGGLE/DSV/8668279},
publisher={Kaggle},
author={Rabie El Kharoua},
year={2024}
}

## Code References ##

https://imbalanced-learn.org/stable/references/generated/imblearn.over_sampling.RandomOverSampler.html

https://seaborn.pydata.org/
