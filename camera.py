import cv2
import streamlit as st
from PIL import Image
import numpy as np
import os
from deepface import DeepFace
import tempfile


# Directory for saving images
SAVE_DIR = "D:\\registered_images"
if not os.path.exists(SAVE_DIR):
    os.makedirs(SAVE_DIR)

def main():
    st.title("Face Recognition Web App")
    st.write("This is a face recognition web app")

    if "registered_face" not in st.session_state:
        st.session_state.registered_face = None

    action = st.selectbox("Choose option", ["Register", "Authenticate"])

    if action == "Register":
        st.write("Register your face in our database")

        enable = st.checkbox("Enable camera")
        picture = st.camera_input("Take a picture", disabled=enable)
        if picture:
            img_pil = Image.open(picture)
            st.image(img_pil, caption="Registered Image", use_column_width=True)

            # Save the captured image
            img_path = os.path.join(SAVE_DIR, "registered.jpg")
            img_pil.save(img_path)
            st.session_state.registered_face = img_path
            st.success(f"Image saved to {img_path}")

    elif action == "Authenticate":
        st.write("Face verification")

        if st.session_state.registered_face is None:
            st.warning("Please register your face first")
        else:
            enable = st.checkbox("Enable camera")
            picture = st.camera_input("Takes a picture", disabled=enable)
            if picture:
                img_pil = Image.open(picture)
                st.image(img_pil, caption="Verification Photo", use_column_width=True)
                print(img_pil)
                print(st.session_state.registered_face)
                # Perform face verification
                try:
                    # Save the verification image temporarily
                    with tempfile.NamedTemporaryFile(suffix=".jpg", delete=False) as tmp_file:
                        img_pil.save(tmp_file.name)
                        tmp_img_path = tmp_file.name  # Store the temporary path

                    verification_result = DeepFace.verify(
                        img1_path=st.session_state.registered_face,
                        img2_path=tmp_img_path,
                        model_name="VGG-Face"
                    )
                    if verification_result["verified"]:
                        st.success("Verification successful")
                    else:
                        st.error("Verification failed")

                except Exception as e:
                    st.error("Error: " + str(e))
                finally:
                    # Remove the temporary file after verification
                    if os.path.exists(tmp_img_path):
                        os.remove(tmp_img_path)

if __name__ == "__main__":
    main()
