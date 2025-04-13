import streamlit as st

st.title("🎈Hello World")
st.snow()
st.title('title string `<h1>`')
st.header('大見出し `<h2>`')
st.subheader(body='中見出し `<h3>`',
            anchor='title',
            help='`<h3>`あるいは`###`に相当するstreamlitのコマンド',
            divider=True)


with st.echo(code_location='below'):
            st.write(':red[風船アニメーション]')
            st.balloons()
            
