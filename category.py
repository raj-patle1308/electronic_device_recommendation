import streamlit as st

st.title('Tv Recommender System📺')
# Define the options for the dropdown
tv_options = ["Samsung TV", "Sony TV"]

# Create the dropdown menu
selected_tv = st.selectbox("Select a TV brand:", tv_options)

# Samsung TV data
samsung_tvs = [
    {
        "name": "Samsung QLED Q60T",
        "image": "image/1.jpg",
        "description": "The Samsung QLED Q60T offers stunning picture quality with vibrant colors and deep blacks."
    },
    {
        "name": "Samsung Crystal UHD TU8000",
        "image": "image/2.jpg",
        "description": "Experience crystal clear colors that are fine-tuned to deliver a naturally crisp and vivid picture."
    },
    {
        "name": "Samsung Frame TV",
        "image": "image/3.jpg",
        "description": "The Frame TV seamlessly blends into any living space with customizable bezel options."
    }
]

# Sony TV data
sony_tvs = [
    {
        "name": "Sony Bravia X800H",
        "image": "image/4.jpg",
        "description": "Sony Bravia X800H delivers a powerful picture with a wide range of colors and enhanced clarity."
    },
    {
        "name": "Sony OLED A8H",
        "image": "image/5.jpg",
        "description": "The Sony OLED A8H features perfect blacks, incredible contrast, and stunning color depth."
    },
    {
        "name": "Sony X900H",
        "image": "image/6.jpg",
        "description": "The X900H combines stunning picture quality with an immersive audio experience."
    }
]

# Function to display TV details in a row
def display_tv_details(tvs):
    cols = st.columns(3)
    for col, tv in zip(cols, tvs):
        col.image(tv["image"], caption=tv["name"], use_column_width=True)
        col.write(tv["description"])

# Display the selected TV brand details
if selected_tv == "Samsung TV":
    display_tv_details(samsung_tvs)
elif selected_tv == "Sony TV":
    display_tv_details(sony_tvs)
