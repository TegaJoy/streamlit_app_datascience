import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import altair

# load a file and display in your application
@st.cache_data
def load_data(filename):
    filepath = 'datasets/'+str(filename)+'.csv'
    df = pd.read_csv(filepath)
    return df

data = load_data('ds_salaries')
st.title('Data Science Salaries Analysis')
st.header('Datasets obtained in year 2023')

try:
    data = load_data('ds_salaries')
    st.write(data.head(10))
    st.dataframe(data.head(10))
    
    total_salary = np.sum(data.salary_in_usd)
    min_sal = np.min(data.salary_in_usd)
    max_sal = np.max(data.salary_in_usd)
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Salary", total_salary, "USD")
    col2.metric("Max salary", max_sal, "$")
    col3.metric("Min salary", min_sal, "$")
    
    # add a filter
    job_titles = data.job_title.unique()
    jobs_selection = st.multiselect(
        "job_titles", job_titles, [job_titles[0], 
                                  job_titles[2]]
    )
                                                                                           
    selected_job_titles = data[data['job_title'].isin(jobs_selection)]
                                                     

# table'''## Top 5 rows ''' 
    st.dataframe(selected_job_titles.head()) 
    
    # pie chart 
    # st.write(data.company_location.unique())
    #st.write(data.employment_type.unique())
    location = data.company_location.value_counts().head()
    explode =(0,0.1,0.2,0.1,0.2)
    fig1, ax1 = plt.subplots(figsize=(10,10))
    ax1.pie(location, labels=location.index, autopct='%1.1f%%', explode=explode)
    ax1.axis("equal")
    st.write("records from different countries")
    st.pyplot(fig1)
    
    # bar chart
    st.write(
        ''' ### Mean Salary by countries'''
    )
    df = data.groupby('company_location')['salary_in_usd'].mean().sort_values(
        ascending=True)
    st.bar_chart(df)
        
    df = data.groupby('work_year')['salary_in_usd'].mean().sort_values(
        ascending=True)
    st.bar_chart(df) 
    
    #   Bar chart is categorical. With line chart, it shows the series
    
    df = data.groupby('work_year')['salary_in_usd'].mean().sort_values(ascending=True)
    st.line_chart(df) 
    
except SyntaxError as s:
    st.error(
        ''' Error: '''% s.reason
    )    
        
        


 