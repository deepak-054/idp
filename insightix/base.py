import hashlib
import sqlite3
import time
from io import StringIO

import altair as alt
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.figure_factory as ff
import seaborn as sns
import streamlit as st
from pycaret.classification import compare_models, setup


def train_model(df,i):
    st.write("Model Name")
    st.write(i)
    model = setup(data = df, target = df.columns[-1])
    # train decision tree
    dt = create_model(i)

    # access the scoring grid
    dt_results = pull()
    st.dataframe(pd.DataFrame(dt_results))
    
    
    st.write('predicted result')
        # predict on new data
    new_data = df.copy()
    new_data.drop('out', axis = 1, inplace = True)
    x = predict_model(dt, data = new_data.loc[:5])
    st.dataframe(x)
    
    
@st.cache_resource
def load_bar():
    
        progress_text = "Operation in progress. Please wait."
        my_bar = st.progress(0, text=progress_text)

        for percent_complete in range(100):
            time.sleep(0.08)
            my_bar.progress(percent_complete + 1, text=progress_text)
        time.sleep(1)
        my_bar.empty()


# Set page configuration
st.set_page_config(
            page_title="insightix",
            page_icon="📊",
            layout="wide",
            initial_sidebar_state="expanded",
        )



s="_"
def make_hashes(password):
	return hashlib.sha256(str.encode(password)).hexdigest()

def check_hashes(password,hashed_text):
	if make_hashes(password) == hashed_text:
		return hashed_text
	return False
# DB Management

conn = sqlite3.connect('data.db')
c = conn.cursor()
# DB  Functions
def create_usertable():
	c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT,password TEXT)')


def add_userdata(username,password):
	c.execute('INSERT INTO userstable(username,password) VALUES (?,?)',(username,password))
	conn.commit()

def login_user(username,password):
	c.execute('SELECT * FROM userstable WHERE username =? AND password = ?',(username,password))
	data = c.fetchall()
	return data

st.header("insightix")
st.markdown("welcome to get insights from your data📊 ")

signup,login,home = st.tabs(["SignUp","Login","Home"])




with signup:
    # st.header("SignUp")
    st.caption("create a account with valid Google mail.")
    st.subheader("Create New Account")
    new_user = st.text_input("Username")
    new_password = st.text_input("Password",type='password')

    if st.button("Signup"):
        create_usertable()
        add_userdata(new_user,make_hashes(new_password))
        # st.success("You have successfully created a valid Account")
        st.info("Account is created and Go to Login Menu to login")
    
    
    
with login:
    st.subheader("Login Section")

    username = st.text_input("User Name")
    password = st.text_input("Password")
    
            
    if st.button("Login"):
        # if password == '12345':
        create_usertable()
        hashed_pswd = make_hashes(password)
        result = login_user(username,check_hashes(password,hashed_pswd))
        print(result)
        if result:
            s+='0'
            st.success("Sucessfully Logged in :)")
                
        else:
            st.warning("wrong credentials try :<")
            st.warning("wrong credentials try")
            st.write(s[0])        
        
    
    if "my_input" not in st.session_state:
        st.session_state["my_input"] = ""

    # my_input = st.text_input("your user name:", st.session_state["my_input"])
    my_input = st.session_state["my_input"]
    
# ''' Exeecution Page '''

with home:
    st.header("Enter your data file")
            
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        # report the best model
        load_bar()

        # Can be used wherever a "file-like" object is accepted:
        data_file,columns = st.columns([7,5])
        
        with data_file:
            dataframe = pd.read_csv(uploaded_file)
            st.dataframe(dataframe)

        
        with columns:
            col = dataframe.columns
            st.write("columns",col)
        # df = pd.DataFrame(uploaded_file)
        
        load_bar()    
        st.title("Statistical Analysis")
        st.subheader("Data description: ")
        st.write(dataframe.describe())
        
        st.subheader("Performing Null Count analysis and removing null values")
        
        
        null_count,nonnull_count = st.columns([5,5])
        
        with null_count:
            st.subheader("row,column shape: ")
            st.write(dataframe.shape)
            null_count = dataframe.isna().sum()
            st.write(null_count)
            
        dataframe = dataframe.dropna()
        
            
        with nonnull_count:
            st.write("After Removing Null Values")   
            st.subheader("row,column shape: ")
            st.write(dataframe.shape)
            nonnull_count = dataframe.isna().sum()
            st.write(dataframe.isna().sum())
            
        
        st.title("Data Visualization")
        
        x = st.selectbox("X-axis: ",[i for i in col])
        
        y = st.selectbox("Y-axis: ",[i for i in col])
        
        
        if x and y: st.bar_chart(dataframe,x=x,y=y)
            
            
        st.subheader("select the input data to train")
        
        _train = st.multiselect("Input Data: ",[i for i in col])
        
        
        st.subheader("select the output data")
        st.warning("output variable must be single")
        _out = st.selectbox("Output Data: ",([i for i in col]))
        
        df = pd.DataFrame(dataframe[list(_train)])
        df['out'] = dataframe[_out]
            
        if st.button("Selection completed..!"):
            st.success("Finalized data for Training Model")
            st.dataframe(df)
        
        st.dataframe(df)
        st.header("Select The Model You want to Train:")
        
        option = st.selectbox(
            'Model Type',
            ('','Regression', 'Classification'))
        st.caption("Regression: Predicts a value")
        st.caption("Classification: Classify a value")

        if st.button("submit"):
            st.write('You selected:', option)
        
            if option == 'Regression':
                
                st.info('''Regression in machine learning is a type of supervised learning that is used for predicting a 
                        continuous numerical value based on input data. It is often employed to model and analyze relationships
                        between variables, making it a fundamental technique in statistics and data analysis. Regression models 
                        help you understand how the input features influence the target variable and make predictions based on 
                        this understanding.''')
                            
                from pycaret.regression import *
                from pycaret.regression import compare_models
                
                
                with st.spinner('Comparative Analysis Takesplace...'):
                    grid = setup(data=df, target=df.columns[-1], html=True,verbose=True)
                    best = compare_models()
                    time.sleep(100)
                st.success('Done!')
                
                x = get_metrics()
                results = pull()
                st.title("Models with Score Values")
                st.dataframe(results)
                
                models = [i for i in results[:3]]
                st.title("Models with Good Performance Scores")
                
                for i in models:
                    st.write(i)
                    
                st.info("Training Data with best models")
                
                print(models[0][0])
                st.write(models[0][0])
                model_sr = list(results.index)
                model_ch = []
                model_acc = results['Accuracy']
                
                for i in range(len(results['Model'])):
                    if int(model_acc[i])==1 or int(model_acc[i]==0):
                        pass
                    else:
                        st.write(results['Model'][i])
                        model_ch.append(i)
                    
                    
                st.info("Training Data with best models")
                print(model_sr)
                print(model_ch)
                st.write(df.loc[1].values)
                for i in range(len(model_ch)):
                    if i:
                        print(model_ch[i-1])
                        # print(model_sr[i])
                        train_model(df,model_sr[model_ch[i-1]])
                
                
                
            
            else:
                
                from pycaret.classification import *
                from pycaret.classification import compare_models
                st.write("You Selected",option)
                st.info('''classification is a fundamental concept in machine learning and is widely used in a variety of domains. 
                        The choice of the classification algorithm and the quality of the data play a crucial role in the success 
                        of a classification task.''')
                st.info("Take a break it takes 5 to 10 minutes to complete....")
                
                with st.spinner('Comparative Analysis Takesplace...'):
                    grid = setup(data=df, target=df.columns[-1], html=True,verbose=True)
                    best = compare_models()
                    time.sleep(100)
                st.success('Done!')
                
                x = get_metrics()
                results = pull()
                st.title("Models with Score Values")
                st.dataframe(results)
                
                models_name = results[results.columns[0]]
                model_sr = results.index
                st.title("Models with Good Performance Scores")
                
                model_sr = list(results.index)
                model_ch = []
                model_acc = results['Accuracy']
                
                for i in range(len(results['Model'])):
                    if int(model_acc[i])==1 or int(model_acc[i]==0):
                        pass
                    else:
                        st.write(results['Model'][i])
                        model_ch.append(i)
                    
                    
                st.info("Training Data with best models")
                print(model_sr)
                print(model_ch)
                st.write(df.loc[1].values)
                for i in range(len(model_ch)):
                    if i:
                        print(model_ch[i-1])
                        # print(model_sr[i])
                        train_model(df,model_sr[model_ch[i-1]])
                
                
                

        
        
                        
    
        