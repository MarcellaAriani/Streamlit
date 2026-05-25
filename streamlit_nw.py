import streamlit as st
st.write("Hello, Streamlit!")

st.title("Marcella Ariani")
st.header("Data Scientist")
st.markdown("Marcella is a data scientist with experience in machine learning and data analysis.")
st.subheader("Skills")
st.caption("- Python\n- R\n- SQL\n- Machine Learning\n- Data Visualization")
st.code("x = 2025")
st.latex(r''' ((x^2 + y^2 - 1)^3 = x^2y^3) ''')

# Display another image from a URL

st.subheader("Image from Google:")
image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0f/Grosser_Panda.JPG/250px-Grosser_Panda.JPG"
st.image(image_url)

# Display an audio file from a local file

st.subheader("Audio:")
audio_file = open(r"C:\Users\Marcella\Music\Enau X Ari Lesmana - Sesi Potret _ EMOTIONAL ANIMATION LIRIK VIDEO [9AU10MiOlOk].mp3", "rb")
st.audio(audio_file)

# Display a video from YouTube using an iframe (Streamlit does not natively support YouTubeembeds)

st.subheader("Video from YouTube:")
youtube_url = "https://www.youtube.com/watch?v=MUvH2Vlxwg8"
st.components.v1.html(

    f"""
    <iframe width="560" height="315"
    src="https://www.youtube.com/embed/{youtube_url.split('=')[-1]}"
    frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope;
    picture-in-picture" 
    allowfullscreen></iframe>
    """, 
    height=315
)

st.checkbox('Yes')
st.button('Click Me')
st.radio('Pick your gender', ['Male', 'Female'])
st.selectbox('Pick a fruit', ['Apple', 'Banana', 'Orange'])
st.multiselect('Choose a planet', ['Jupiter', 'Mars', 'Neptune'])
st.select_slider('Pick a mark', ['Bad', 'Good', 'Excellent'])
st.slider('Pick a number', 0, 50)

st.number_input('Pick a number', 0, 10)
st.text_input('Email address')
st.date_input('Traveling date')
st.time_input('School time')
st.text_area('Description')
st.file_uploader('Upload a photo')
st.color_picker('Choose your favorite color')

import time

st.balloons()




st.success("You did it!")
st.error("Error occurred")
st.warning("This is a warning")
st.info("It's easy to build a Streamlit app")
st.exception(RuntimeError("RuntimeError exception"))


st.sidebar.title("This is written inside the sidebar")
st.sidebar.button("Click")
st.sidebar.radio("Pick your gender", ["Male","Female"])


import matplotlib.pyplot as plt
import numpy as np

rand = np.random.normal(1, 2, size=20)
fig, ax = plt.subplots()
ax.hist(rand, bins=15)
st.pyplot(fig)


import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(10, 2), columns=['x', 'y'])
st.line_chart(df)


import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(10, 2), columns=['x', 'y'])
st.bar_chart(df)


import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(10, 2), columns=['x', 'y'])
st.area_chart(df)


import pandas as pd
import numpy as np
import altair as alt

df = pd.DataFrame(np.random.randn(500, 3), columns=['x', 'y', 'z'])
chart = alt.Chart(df).mark_circle().encode(
    x='x', y='y', size='z', color='z', tooltip=['x', 'y', 'z']
)
st.altair_chart(chart, use_container_width=True)



import graphviz

st.graphviz_chart('''
    digraph {
        Big_shark -> Tuna
        Tuna -> Mackerel
        Mackerel -> Small_fishes
        Small_fishes -> Shrimp
    }
''')

import graphviz

st.graphviz_chart('''
    digraph {
        Big_shark -> Tuna
        Tuna -> Salmon          
        Tuna -> Mackerel
        Mackerel -> Small_fishes
        Small_fishes -> Shrimp
    }
''')


import numpy as np
import streamlit as st

df = pd.DataFrame(
    np.random.randn(500, 2) / [50, 50] + [37.76, -122.4], columns=['lat', 'lon']
)
st.map(df)