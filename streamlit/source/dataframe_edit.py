def run():

    import streamlit as st
    from PIL import Image
    import matplotlib.pyplot as plt
    import pandas as pd
    import numpy as np

    st.subheader("DataFrame ex")
    df = pd.DataFrame(
        [
            {'명령어': 'st.selectbox', '평점': 4, 'is_widget': True},
            {'명령어': 'st.ballons', '평점': 5, 'is_widget': False},
            {'명령어': 'st.time_input', '평점': 3, 'is_widget': False},
        ]
    )

    st.data_editor(df, height=200, num_rows='fixed')

    st.balloons()