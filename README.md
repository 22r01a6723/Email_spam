P3-Spam-Mail-Classification-by-NLP-and-ML
About the Project:
This project focuses on Email Spam Classification using Machine Learning and a user-friendly Streamlit interface. The application classifies emails as either Spam or Ham (Not Spam) by leveraging a Multinomial Naive Bayes model trained on a dataset of email messages. The entire workflow, from data preprocessing to model deployment, is structured for simplicity and functionality.

Execution Steps:

1).Install Anaconda Software:
    Anaconda was installed to manage the Python environment and dependencies. The base directory was used for project execution.

2).Download Dataset:
    The spam.csv dataset was downloaded from Kaggle and stored in the current working directory. This dataset contains labeled email messages categorized as spam or ham.

3).Create and Train the Model (spamDetector.ipynb):

    A Jupyter Notebook file was written and executed to preprocess the data, train the machine learning model, and save the model for later use.
Steps in the Notebook:
    1.Loaded the dataset and removed irrelevant columns.
 
    2.Preprocessed the data by encoding spam as 1 and ham as 0.
 
    3.Used CountVectorizer to convert email text into numerical features.
 
    4.Split the data into training and testing sets using train_test_split.
 
    5.Trained a Multinomial Naive Bayes model and evaluated its accuracy.
 
    6.Saved the trained model and vectorizer using pickle for reuse.
 

4).Build a Streamlit Interface (spamDetector.py):

  A Streamlit script was created to provide a web-based interface for spam detection.
  Features in Streamlit App:

  1.Users can input email text directly in a text area.
  
  2.A Classify Email button triggers the classification process.
  
  3.Displays results with intuitive messages:
   i).Not A Spam Email (Ham) in green.
   ii). Spam Email in red.
   
   4.Styled using Streamlit's markdown for a clean, user-friendly interface.
 
5).Run the Application:

  1.The integrated terminal was opened in the base Conda directory.
  
  2.The following command was executed to start the Streamlit app:
      "streamlit run spamDetector.py"
      
  3.The app runs locally in the browser, where users can input email text to classify.

Outcome:
The project successfully classifies emails into spam or ham categories. The interface is intuitive and allows users to test the classifier in real time. This solution can be extended with advanced models or larger datasets for improved performance.
