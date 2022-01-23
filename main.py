import streamlit as st


def hello():
    try:
        import pandas as pd

        from sklearn import linear_model as lm

        st.title('Predict House Price')

        df = pd.read_csv('house_price.csv')

        area = df['area']

        price = df['price']

        reg = lm.LinearRegression()

        reg.fit(df[['area']], df.price)

        user_inpu = int(st.text_input("Enter Area To Predict Price: "))

        res = reg.predict([[user_inpu]])

        st.write(res)


    except ValueError:
        st.write('Please Enter Some Value and use only numbers.')


st.write(hello())
