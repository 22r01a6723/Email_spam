import streamlit as st
import pickle

# Load the model and vectorizer
model = pickle.load(open('spam.pkl', 'rb'))
cv = pickle.load(open('vec.pkl', 'rb'))

# Main application
def main():
    # Title and header styling
    st.markdown("<h1 style='text-align: center; color: #4CAF50;'>Email Spam Classification</h1>", unsafe_allow_html=True)
    st.markdown("""
        <p style="text-align: center; color: #555555; font-size: 18px;">
        This is a Machine Learning application to classify emails as spam or ham.
        </p>
    """, unsafe_allow_html=True)
    
    # Add some spacing
    st.markdown("<br><br>", unsafe_allow_html=True)

    # Input text area for email
    st.subheader("Enter Email Text Below")
    user_input = st.text_area("Email Content", height=200, placeholder="Type or paste an email here...")

    # Classify button with some styling
    classify_button = st.button("Classify Email", key="classify_btn", help="Click to classify the entered email")

    # Displaying the result
    if classify_button:
        if user_input:
            data = [user_input]
            vec = cv.transform(data).toarray()
            result = model.predict(vec)
            
            if result[0] == 0:
                st.markdown("<h4 style='color: #4CAF50;'>This is Not A Spam Email</h4>", unsafe_allow_html=True)
            else:
                st.markdown("<h4 style='color: #FF5733;'>This is A Spam Email</h4>", unsafe_allow_html=True)
        else:
            st.warning("Please enter some text to classify.")

    # Footer for a nice touch
    st.markdown("""
        <hr>
        <p style="text-align: center; color: #888888; font-size: 12px;">
        Powered by Streamlit & Machine Learning | Developed by You
        </p>
    """, unsafe_allow_html=True)

# Run the app
if __name__ == '__main__':
    main()
