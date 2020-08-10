import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px


st.title("Sentiment Analysis of Tweets about US Airlines")
st.sidebar.title("Sentiment Analysis of Tweets about US Airlines")
st.markdown("This dashboard present visual analysis of tweets about US Airlines")
st.sidebar.markdown("This dashboard present visual analysis of tweets about US Airlines")


#data_path = r"C:\Users\shrid\anaconda3\envs\textviz\Tweets.csv"
data_path = r"Tweets.csv"

@st.cache(persist = True)

def load_data():
        data = pd.read_csv(data_path)
        data['tweet_created'] = pd.to_datetime(data['tweet_created'])
        return data

data = load_data()

st.sidebar.subheader("Show random tweets as per sentiment")
random_tweet = st.sidebar.radio('Sentiment', ('positive', 'negative', 'neutral'))
st.sidebar.markdown(data.query("airline_sentiment== @random_tweet")[["text"]].sample(n=1).iat[0,0])

st.sidebar.markdown("### Number of tweets by sentiment")
st.sidebar.markdown("#### Uncheck Hide checkbox to view chart")
select = st.sidebar.selectbox("Visualization type", ['Histogram', 'Piechart'], key = '1')

sentiment_count = data['airline_sentiment'].value_counts()
sentiment_count = pd.DataFrame({'Sentiment': sentiment_count.index, 'Tweets':sentiment_count.values})

if not st.sidebar.checkbox("Hide", True):
        st.markdown("### Number of tweets by sentiment")
        if select == "Histogram":
                fig = px.bar(sentiment_count, x= 'Sentiment', y ='Tweets', color = 'Tweets')
                st.plotly_chart(fig)
        else:
                fig = px.pie(sentiment_count , values = 'Tweets', names = 'Sentiment')
                st.plotly_chart(fig)
