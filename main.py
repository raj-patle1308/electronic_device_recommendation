import streamlit as st
import streamlit.components.v1 as components
import streamlit as st
import pickle
import pandas as pd
import random
from src.remove_ import remove

# Load app.py content
def load_app():
    df = pickle.load(file=open(file=r'src/model/dataframe.pkl', mode='rb'))
    similarity = pickle.load(file=open(file=r'src/model/similarity.pkl', mode='rb'))


    remove()

    def recommend_different_variety(mobile):
        mobile_index = df[df['name'] == mobile].index[0]
        similarity_array = similarity[mobile_index]
        different_variety = random.sample(list(enumerate(similarity_array)),k=10)

        recommended_mobiles_variety = []
        recommended_mobiles_IMG_variety = []
        recommended_mobiles_ratings_variety = []
        recommended_mobiles_price_variety = []
        for i in different_variety:
            recommended_mobiles_variety.append(df['name'].iloc[i[0]])
            recommended_mobiles_IMG_variety.append(fetch_IMG(i[0]))
            recommended_mobiles_ratings_variety.append(df['ratings'].iloc[i[0]])
            recommended_mobiles_price_variety.append(df['price'].iloc[i[0]])

        return recommended_mobiles_variety, recommended_mobiles_IMG_variety, recommended_mobiles_ratings_variety, recommended_mobiles_price_variety


    def recommend(mobile):
        mobile_index = df[df['name'] == mobile].index[0]
        similarity_array = similarity[mobile_index]
        similar_10_mobiles = sorted(list(enumerate(similarity_array)), reverse=True, key=lambda x: x[1])[1:11]

        recommended_mobiles = []
        recommended_mobiles_IMG = []
        recommended_mobiles_ratings = []
        recommended_mobiles_price = []
        for i in similar_10_mobiles:
            recommended_mobiles.append(df['name'].iloc[i[0]])
            recommended_mobiles_IMG.append(fetch_IMG(i[0]))
            recommended_mobiles_ratings.append(df['ratings'].iloc[i[0]])
            recommended_mobiles_price.append(df['price'].iloc[i[0]])

        return recommended_mobiles, recommended_mobiles_IMG, recommended_mobiles_ratings, recommended_mobiles_price

    def fetch_IMG(mobile_index):
        # response = requests.get(url=df['imgURL'].iloc[mobile_index])
        return df['imgURL'].iloc[mobile_index]


    st.title('Mobile Recommender System📲')
    st.markdown('')
    st.markdown('')
    st.markdown(' ')
    mobiles = df['name'].values
    selected_mobile = st.selectbox(label='Select Mobile Name', options=mobiles)

    if st.button('Recommend'):
        mobile_name, mobile_IMG, mobiles_ratings, mobiles_price = recommend(selected_mobile)

        col1, col2, col3, col4, col5 = st.columns(5)

        with col1:
            st.markdown(f"<p style='text-align: center;'>{mobile_name[0]}\n"
                        f"Ratings: {mobiles_ratings[0]}  \n"
                        f"Price: {mobiles_price[0]}", unsafe_allow_html=True)
            st.image(mobile_IMG[0])

        with col2:
            st.markdown(f"<p style='text-align: center;'>{mobile_name[1]}\n"
                        f"Ratings: {mobiles_ratings[1]}  \n"
                        f"Price: {mobiles_price[1]}", unsafe_allow_html=True)
            st.image(mobile_IMG[1])

        with col3:
            st.markdown(f"<p style='text-align: center;'>{mobile_name[2]}\n"
                        f"Ratings: {mobiles_ratings[2]}  \n"
                        f"Price: {mobiles_price[2]}", unsafe_allow_html=True)
            st.image(mobile_IMG[2])

        with col4:
            st.markdown(f"<p style='text-align: center;'>{mobile_name[3]}\n"
                        f"Ratings: {mobiles_ratings[3]}  \n"
                        f"Price: {mobiles_price[3]}", unsafe_allow_html=True)
            st.image(mobile_IMG[3])

        with col5:
            st.markdown(f"<p style='text-align: center;'>{mobile_name[4]}\n"
                        f"Ratings: {mobiles_ratings[4]}  \n"
                        f"Price: {mobiles_price[4]}", unsafe_allow_html=True)
            st.image(mobile_IMG[4])

        st.markdown('---')

        col6, col7, col8, col9, col10 = st.columns(5)

        with col6:
            st.markdown(f"<p style='text-align: center;'>{mobile_name[5]}\n"
                        f"Ratings: {mobiles_ratings[5]}  \n"
                        f"Price: {mobiles_price[5]}", unsafe_allow_html=True)
            st.image(mobile_IMG[5])

        with col7:
            st.markdown(f"<p style='text-align: center;'>{mobile_name[6]}\n"
                        f"Ratings: {mobiles_ratings[6]}  \n"
                        f"Price: {mobiles_price[6]}", unsafe_allow_html=True)
            st.image(mobile_IMG[6])

        with col8:
            st.markdown(f"<p style='text-align: center;'>{mobile_name[7]}\n"
                        f"Ratings: {mobiles_ratings[7]}  \n"
                        f"Price: {mobiles_price[7]}", unsafe_allow_html=True)
            st.image(mobile_IMG[7])

        with col9:
            st.markdown(f"<p style='text-align: center;'>{mobile_name[8]}\n"
                        f"Ratings: {mobiles_ratings[8]}  \n"
                        f"Price: {mobiles_price[8]}", unsafe_allow_html=True)
            st.image(mobile_IMG[8])

        with col10:
            st.markdown(f"<p style='text-align: center;'>{mobile_name[9]}\n"
                        f"Ratings: {mobiles_ratings[9]}  \n"
                        f"Price: {mobiles_price[9]}", unsafe_allow_html=True)
            st.image(mobile_IMG[9])

        mobile_name_variety , mobile_IMG_variety , mobiles_ratings_variety , mobiles_price_variety = recommend_different_variety(selected_mobile)

        st.markdown('---')
        st.markdown('## Other Variety of mobiles')
        st.markdown('---')

        col11, col12, col13, col14, col15 = st.columns(5)

        with col11:
            st.markdown(f"<p style='text-align: center;'>{mobile_name_variety[0]}\n"
                        f"Ratings: {mobiles_ratings_variety[0]}  \n"
                        f"Price: {mobiles_price_variety[0]}", unsafe_allow_html=True)
            st.image(mobile_IMG_variety[0])

        with col12:
            st.markdown(f"<p style='text-align: center;'>{mobile_name_variety[1]}\n"
                        f"Ratings: {mobiles_ratings_variety[1]}  \n"
                        f"Price: {mobiles_price_variety[1]}", unsafe_allow_html=True)
            st.image(mobile_IMG_variety[1])

        with col13:
            st.markdown(f"<p style='text-align: center;'>{mobile_name_variety[2]}\n"
                        f"Ratings: {mobiles_ratings_variety[2]}  \n"
                        f"Price: {mobiles_price_variety[2]}", unsafe_allow_html=True)
            st.image(mobile_IMG_variety[2])

        with col14:
            st.markdown(f"<p style='text-align: center;'>{mobile_name_variety[3]}\n"
                        f"Ratings: {mobiles_ratings_variety[3]}  \n"
                        f"Price: {mobiles_price_variety[3]}", unsafe_allow_html=True)
            st.image(mobile_IMG_variety[3])

        with col15:
            st.markdown(f"<p style='text-align: center;'>{mobile_name_variety[4]}\n"
                        f"Ratings: {mobiles_ratings_variety[4]}  \n"
                        f"Price: {mobiles_price_variety[4]}", unsafe_allow_html=True)
            st.image(mobile_IMG_variety[4])

        col16, col17, col18, col19, col20 = st.columns(5)

        with col16:
            st.markdown(f"<p style='text-align: center;'>{mobile_name_variety[5]}\n"
                        f"Ratings: {mobiles_ratings_variety[5]}  \n"
                        f"Price: {mobiles_price_variety[5]}", unsafe_allow_html=True)
            st.image(mobile_IMG_variety[5])

        with col17:
            st.markdown(f"<p style='text-align: center;'>{mobile_name_variety[6]}\n"
                        f"Ratings: {mobiles_ratings_variety[6]}  \n"
                        f"Price: {mobiles_price_variety[6]}", unsafe_allow_html=True)
            st.image(mobile_IMG_variety[6])

        with col18:
            st.markdown(f"<p style='text-align: center;'>{mobile_name_variety[7]}\n"
                        f"Ratings: {mobiles_ratings_variety[7]}  \n"
                        f"Price: {mobiles_price_variety[7]}", unsafe_allow_html=True)
            st.image(mobile_IMG_variety[7])

        with col19:
            st.markdown(f"<p style='text-align: center;'>{mobile_name_variety[8]}\n"
                        f"Ratings: {mobiles_ratings_variety[8]}  \n"
                        f"Price: {mobiles_price_variety[8]}", unsafe_allow_html=True)
            st.image(mobile_IMG_variety[8])

        with col20:
            st.markdown(f"<p style='text-align: center;'>{mobile_name_variety[9]}\n"
                        f"Ratings: {mobiles_ratings_variety[9]}  \n"
                        f"Price: {mobiles_price_variety[9]}", unsafe_allow_html=True)
            st.image(mobile_IMG_variety[9])

    st.markdown('---')
    st.markdown('Thank You for visiting🙂 \n Made by👨🏻‍💻 XYZ')

def load_app1():
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

def load_app2():
    st.title('Laptop Recommender System💻')
    # Define the options for the dropdown
    laptop_options = ["Dell Laptop", "HP Laptop"]

    # Create the dropdown menu
    selected_laptop = st.selectbox("Select a laptop brand:", laptop_options)

    # Dell laptop data
    dell_laptops = [
        {
            "name": "Dell XPS 13",
            "image": "image/7.jpg",
            "description": "The Dell XPS 13 offers a stunning 4K display, powerful performance, and a sleek design."
        },
        {
            "name": "Dell Inspiron 15",
            "image": "image/8.jpg",
            "description": "Experience seamless multitasking with the Dell Inspiron 15, featuring a powerful Intel processor."
        },
        {
            "name": "Dell G5 15",
            "image": "image/9.jpg",
            "description": "The Dell G5 15 is a gaming laptop with a high-refresh-rate display and excellent graphics performance."
        }
    ]

    # HP laptop data
    hp_laptops = [
        {
            "name": "HP Spectre x360",
            "image": "image/10.jpg",
            "description": "The HP Spectre x360 is a convertible laptop with a vibrant display and long battery life."
        },
        {
            "name": "HP Envy 13",
            "image": "image/11.jpg",
            "description": "The HP Envy 13 offers premium performance in a lightweight and stylish design."
        },
        {
            "name": "HP Pavilion 15",
            "image": "image/12.jpg",
            "description": "The HP Pavilion 15 provides a great balance of performance and affordability."
        }
    ]

    # Function to display laptop details in a row
    def display_laptop_details(laptops):
        cols = st.columns(3)
        for col, laptop in zip(cols, laptops):
            col.image(laptop["image"], caption=laptop["name"], use_column_width=True)
            col.write(laptop["description"])

    # Display the selected laptop brand details
    if selected_laptop == "Dell Laptop":
        display_laptop_details(dell_laptops)
    elif selected_laptop == "HP Laptop":
        display_laptop_details(hp_laptops)

def load_app3():

    st.title('Watch Recommender System⌚')
    # Define the options for the dropdown
    watch_options = ["Boat Watch", "Noise Watch"]

    # Create the dropdown menu
    selected_watch = st.selectbox("Select a watch brand:", watch_options)

    # Boat watch data
    boat_watches = [
        {
            "name": "Boat Watch Flash",
            "image": "image/13.jpg",
            "description": "The Boat Watch Flash features a round dial design with multiple sports modes and long battery life."
        },
        {
            "name": "Boat Storm",
            "image": "image/14.jpg",
            "description": "The Boat Storm offers real-time health monitoring and personalized fitness plans."
        },
        {
            "name": "Boat Watch Xtend",
            "image": "image/15.jpg",
            "description": "The Boat Watch Xtend comes with a built-in Alexa and customizable watch faces."
        }
    ]

    # Noise watch data
    noise_watches = [
        {
            "name": "Noise ColorFit Pro 3",
            "image": "image/16.jpg",
            "description": "The Noise ColorFit Pro 3 features a large display with a range of fitness tracking options."
        },
        {
            "name": "NoiseFit Endure",
            "image": "image/17.jpg",
            "description": "The NoiseFit Endure offers a rugged design with up to 20 days of battery life."
        },
        {
            "name": "NoiseFit Evolve",
            "image": "image/18.jpg",
            "description": "The NoiseFit Evolve combines a sleek design with AMOLED display and multiple sports modes."
        }
    ]

    # Function to display watch details in a row
    def display_watch_details(watches):
        cols = st.columns(3)
        for col, watch in zip(cols, watches):
            col.image(watch["image"], caption=watch["name"], use_column_width=True)
            col.write(watch["description"])

    # Display the selected watch brand details
    if selected_watch == "Boat Watch":
        display_watch_details(boat_watches)
    elif selected_watch == "Noise Watch":
        display_watch_details(noise_watches)

def main():

    st.sidebar.image("logo.jpg", use_column_width=True, output_format='PNG', width=100)
    st.sidebar.title("Welcome")
    option = st.sidebar.radio("", ["Categories", "About Us"])

    if option == "Categories":
        st.sidebar.write("Select a category:")
        category_option = st.sidebar.radio("Categories", ["Mobile Recommendation", "TV Recommendation","Laptop Recommendation","Watch Recommendation"])

        if category_option == "Mobile Recommendation":
            load_app()
        elif category_option == "TV Recommendation":
            load_app1()
        elif category_option == "Laptop Recommendation":
            load_app2()
        elif category_option == "Watch Recommendation":
            load_app3()
    elif option == "About Us":
        st.markdown("## About Us")
        st.write("""
        Welcome to our electronic devices recommendation platform! 
        We aim to provide you with accurate and personalized recommendations for mobile phones and other gadgets based on your preferences and requirements. 
        Our team of experts constantly reviews and updates our database to ensure that you receive the latest and most relevant recommendations. 
        Whether you're looking for a budget-friendly smartphone or a high-end tablet, we've got you covered. 
        Explore our platform and find the perfect electronic device that suits your needs!
        """)


# Run the main function
if __name__ == "__main__":
    main()
