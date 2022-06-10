import streamlit as st
from PIL import Image

from tf_od.helper import perform_od, to_tensor

st.title('Object Detection')
st.header('Upload an image and get reconized objects')

result = st.file_uploader(label='Please upload 1 image')

if result:
    pil_image = Image.open(result)
    st.image(result, caption='Your image')

    converted = to_tensor(pil_image)
    clss = perform_od(converted)
    st.write(clss)
    st.success('Done!')
