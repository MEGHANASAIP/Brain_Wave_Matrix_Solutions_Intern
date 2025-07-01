import streamlit as st
import joblib


model = joblib.load('sentimentmodel.pkl')


st.title("Reddit Comment Sentiment Classifier")
st.write("Enter a comment and get the predicted sentiment.")
user_input = st.text_area("Enter your Reddit comment here:")


if st.button("Predict Sentiment"):
    if user_input.strip() == "":
        st.warning("Please enter some text.")
    else:
        # Predict using the loaded pipeline
        prediction = model.predict([user_input])[0]

        # Convert to readable sentiment
        label_map = {
            -1: "Negative 😠",
             0: "Neutral 😐",
             1: "Positive 😊"
        }

        st.subheader("Predicted Sentiment:")
        st.success(label_map[prediction])
