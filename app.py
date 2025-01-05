import streamlit as st
from PIL import Image

# Title of the app
st.title("Display Image with a Button")

# Button to show the image
if st.button("Show Image"):
    # Load the image from the local folder
    image_path = r"myimage.jpg"  # Replace with the path to your image
    try:
        image = Image.open(image_path)
        # Display the image
        st.image(image, caption="Your Image", use_column_width=True)
    except FileNotFoundError:
        st.error("Image not found. Please check the file path.")
else:
    st.write("Click the button to display the image.")
