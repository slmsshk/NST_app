import UI
import streamlit as st

from PIL import Image
import cv2
import tensorflow as tf
import numpy as np

import time,os


# ++++++++++++++++++++++++++++++++++++++
# Clean Ram
# ==========================================

reset=st.button('click to reset and start fresh')

if reset:
    # os.remove('style.png')
    try:
        os.remove("st.jpg")
        UI.write('done1 st',tag='p',padding=1,bg='green')
        os.remove("im.jpg")
        UI.write('done2 im',tag='p',padding=1,bg='green')
        os.remove("final.jpg")
        UI.write('done',tag='p',padding=1,bg='green')
    except:
        UI.write(':)',tag='p',padding=1,bg='yellow')
        
refresh=st.button('refresh')

if refresh:
    st.experimental_rerun()


# ++++++++++++++++++++++++++++++++++++++
# Page setup
# ==========================================


UI.add_bg_from_local('Style Background.jpg')

UI.write("NST-Neural Styles Transfer",tag='h1',bg='maroon',fontsize=30)


# ++++++++++++++++++++++++++++++++++++++
# Taking User Upload
# ======================================

col1,col2=st.columns(2)

with col1:
    
    UI.write('Upload your photo',bg='green',fontsize=20,tag='h2')
    image_file = st.file_uploader(" ",type=['jpg'])

    if image_file is not None:

        # col1.write(image_file.name)
        # Open St format to Image format
        img = Image.open(image_file)
        # col1.image(img) #Display the image
        cv2.imwrite(img=cv2.cvtColor(np.array(img),cv2.COLOR_RGB2BGR),filename='im.jpg') #Save the file
        cv2.imwrite(img=cv2.cvtColor(np.array(img),cv2.COLOR_RGB2BGR),filename='i'+image_file.name)
        

with col2:
    
    UI.write('Upload Style photo',bg='green',fontsize=20,tag='h2')
    style_file = st.file_uploader("Close the file after Upload",type=['jpg'],key='style')

    if style_file is not None:

        # col1.write(image_file.name)
        # Open St format to Image format
        sty = Image.open(style_file)
        col2.image(sty) #Display the image
        cv2.imwrite(img=cv2.cvtColor(np.array(sty),cv2.COLOR_RGB2BGR),filename='st.jpg') #Save the file
        cv2.imwrite(img=cv2.cvtColor(np.array(sty),cv2.COLOR_RGB2BGR),filename='s'+style_file.name)

UI.write('Neural Style transfer image',tag='h1',fontsize=35,bg='orange',color='white')

but=st.button('press for Style transfer')

if but:
    try:
        import sty
        st.image('final.jpg')
        

        with open("final.jpg", "rb") as file:
            btn = st.download_button(
                    label="Download image",
                    data=file,
                    file_name="style.png",
                    mime="image/png"
                )
    except:
        st.write(';)')
