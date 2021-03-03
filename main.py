import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

st.markdown(
    """
    <style>
        .css-1v3fvcr {
            color: #142952;
            background: #99b3e6;
        }
    </style>
    """,
    unsafe_allow_html=True
)    
    

@st.cache
def load_data():
    df = pd.read_csv('data/nhl-goals.csv')
    return df

df = load_data()    

def main():
    st.sidebar.header('NHL Records')
    page = st.sidebar.selectbox(
        'Select a Page',
        [
            'Homepage', 'Goals', 'Assists'
        ]
    )
    st.sidebar.markdown("""
        ### Legends:
        ** * ** Active Players

        **PPG** Power Play Goals

        ** GP ** Games Played

        For more info visit the [official web site](https://records.nhl.com/) of the National Hockey League. NHL, the NHL Shield, the word mark and image are registered trademarks.

        All stats are updated until February 2021.

    """)
    if page == 'Homepage':
        st.image('img/nhl-logo.png')
        st.title('Welcome To My NHL Records App!')
        st.image('img/banner.jpg')
        st.subheader(' <<-- Please choose an option in the Sidebar...')

    if page == 'Goals':
        st.image('img/nhl-freez.png')
        st.title('All-Time Goals Leaders')
        st.header('The 700 Club')
        st.table(df.head(8))

        fig = plt.figure()  
        bar_data = df.sort_values(by='Goals', ascending=False)
        bar_data = bar_data.head(8)
        plt.style.use('ggplot')
        plt.barh(bar_data['Player'], bar_data['Goals'])
        plt.gca().invert_yaxis()
        plt.xlabel('Goals')     
        st.pyplot(fig)

        st.header('Top 25 All-Time Goals Leaders')
        st.write(df)


        fig = plt.figure(figsize=(7,10))  
        bar_data = df.sort_values(by='Goals', ascending=False)
        plt.style.use('ggplot')
        plt.barh(bar_data['Player'], bar_data['Goals'])
        plt.gca().invert_yaxis()
        plt.xlabel('Goals')     
        st.pyplot(fig)

    df2 = pd.read_csv('data/nhl-assists.csv')
    if page == 'Assists':
        st.image('img/nhl-freez.png')
        st.title('All-Time Assists Leaders')
        st.header('The 1000 Club')
        st.table(df2.head(13))

        st.header('Top 25 All-Time Assists Leaders')
        
        st.write(df2)

        fig = plt.figure(figsize=(7,10))  
        bar_data = df2.sort_values(by='Assists', ascending=False)
        plt.style.use('ggplot')
        plt.barh(bar_data['Player'], bar_data['Assists'])
        plt.gca().invert_yaxis()
        plt.xlabel('Assists')     
        st.pyplot(fig)


if __name__ == '__main__':
    main()