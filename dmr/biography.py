import streamlit as st


st.set_page_config(page_title="Diana's Memoir", page_icon=":maple_leaf:", layout="wide")

    
col1, col2 = st.columns([2, 1])  # Make the left column wider

# Add text to the left column
with col1:
    st.subheader("Hi, welcome to the biography of")
    st.title("DIANA MAE RETULLA :feather:")
    st.write("I hope this biography will help you know this person more")

# Add the image to the right column
with col2:
    st.image("meow.jpg", width=300, caption='meow meow meow')


with st.container(): 
     st.write("---") 
     left_column, right_column = st.columns(2) 
     with left_column: 
        st.header("What I do") 
        st.write("##") 
        st.write(
            """
            p0odwijjd:
            - msalsalsa
            - asmmals
            jkkdp
            ddkds
            """
        )