import os                # for handling files and folders
import streamlit as st   # to create a web app easily
from PIL import Image    # to work with images
from rembg import remove # removes background from an image
import io                # for handling binary data (like image bytes)

# Create a Folder (only if it doesn't exist)
os.makedirs("original", exist_ok= True) # create a folder name "original" to store images

st.title("Image Background Remover")

uploaded_file = st.file_uploader("upload a image", type = ["png", "jpg", "jpeg"]) # shows a button to upload images

if uploaded_file is not None: 
    
    file_bytes = uploaded_file.read() # read uploaded data as binary file(0 and 1s)


    original_path = os.path.join("original", uploaded_file.name) # create the full path as original/pic_name.jpg
    with open(original_path, "wb") as f: # put the photo in "original folder"
        f.write(uploaded_file.getbuffer()) # returns the memory view of uploaded files content, allwos us to write the full contetn of file exactly as it is into a new image.


    st.success(f"image saved to {original_path}")


    image = Image.open(uploaded_file) # Opens the image using PIL
    st.image(image, caption="original image", use_column_width=True) # display in the app, using caption


    with st.spinner("Removing background...."): # show loading spinner while removing bg
        output = remove(file_bytes) # this use AI to remove bg
    
    result_image = Image.open(io.BytesIO(output)) # convert o/p back to image, as remove() gave raw image
    st.image(result_image, caption = "Image without background", use_column_width= True) # show

    st.download_button("Download Transparent Image", output, file_name= "no_bg.png") # download button
    # Correct: You use "output" because st.download_button expects binary data (bytes) or a file-like object.