import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image


# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Dashboard", page_icon=":zap:", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")
# https://assets9.lottiefiles.com/packages/lf20_d6ZJ8R.json (Competitor Analysis)
# ---- LOAD ASSETS ----
lottie_keyword = load_lottieurl(
    "https://assets1.lottiefiles.com/packages/lf20_x17ybolp.json")

lottie_competitor = load_lottieurl(
    "https://assets3.lottiefiles.com/packages/lf20_55vegd04.json"
)

lottie_leaderboard = load_lottieurl(
    "https://assets9.lottiefiles.com/packages/lf20_d6ZJ8R.json"
)

lottie_sentimental = load_lottieurl(
    "https://assets6.lottiefiles.com/private_files/lf30_4bkst7vs.json"
)



# ---- HEADER SECTION ----
with st.container():
    st.subheader("Hi, Welcome to TubeStack :wave:")
    st.title("We Provide Best Tools For YouTube Content Creators !")
    st.write(
        "TubeStack is a web extension for the YouTube content creators to help grow their channel and help them finding high-performing, searchable video topics. "
        "It creates an engagement leaderboard for everyone who comments and do likes on any channel, the creator can view their channel's top contributors. You can know whether a video is loved or hated also get the top loved and hated comments and give an overall emotion ratio of the video."
    )
    st.write("[Learn More >](https://pythonandvba.com)")
    st.title("Modules")
    # st.write("##")

# ---- WHAT I DO ----
with st.container():
    # st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header('1) Keyword Explorer and Research Tool')
        st.write(
            """
            - This tool provides all the features related to keyword research and selection for your upcoming video content to rank it on the YouTube search.
            - Users can find the real-time trending keywords of currents hot topics of a particular region for their upcoming videos.
            - Users can find the top searched keywords with high search volume and low competitiveness.
            - It includes a related keyword section that helps the creators to think and choose the variety of the top-rated keywords to optimize their video in search results.
            """
        )
    with right_column:
        st.write("\n")
        st.write("\n")
        st_lottie(lottie_keyword, height=300, key="keyword")

# st.write("##")
st.write("\n")
st.write("\n")

with st.container():
    # st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header('2) Video Competitive Analysis Tool')
        st.write(
            """
            - This tool provides all the features and strategies which help to identify your competitors and their strategies. So, you can determine your strengths and weaknesses in optimizing your video content.
            - Users can view the video impact and influence score of any competitor’s video based on the ratio of views, likes, and dislikes of the video and further calculating the comments replies, and likes
            - Users can view the SEO Score of any video based on how the metadata relevant information such as tag characters, tags in title and description, title words in the description, etc. is used in the video
            - Users can get the video summary including the number of views, likes, dislikes, comments, etc. of the opened video.
            - Users can get the Channel info of the opened video including channel views, subscribers, and the number of videos.
            """
        )

    with right_column:
        st.write("\n")
        st.write("\n")
        st_lottie(lottie_competitor, height=300, key="competitor")
        
        
st.write("\n")
st.write("\n")

# st.write("##")

with st.container():
    # st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header('3) Engagement Leader board Tool')
        st.write(
            """
            - This tool analyzes the viewer's contribution to your channel like their involvement in the comment section.
            - It includes a scoring system that calculates the engagement points through an algorithm by gathers comments that were well-liked and replied also created value for the community.
            - It shows the results of Top contributors on the leaderboard with different filtering options such as based on engagement points, no. of comments, and no. of likes.
            - Users can view the leaderboard ranking of their top contributors based on their last week and month data.
            """
        )
        # st.write("[YouTube Channel >](https://youtube.com/c/CodingIsFun)")
    with right_column:
        st.write("\n")
        st.write("\n")
        st_lottie(lottie_leaderboard, height=300, key="leaderboard")


# st.write("##")
st.write("\n")
st.write("\n")

with st.container():
    # st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header('4) Comments Sentimental Analysis Tool')
        st.write(
            """
            - This module will analyze the comments of any YouTube video and determines the sentiment ratio on that video.
            - It gathers all comments on the video and applies the machine learning NLP techniques to analyze the polarity and subjectivity of the comments.
            - Users can view the sentiment response score of the video and see comment details.
            - Users can view top positive and negative comments on their videos based on their polarity and subjectivity. 
            """
        )
        # st.write("[YouTube Channel >](https://youtube.com/c/CodingIsFun)")
    with right_column:
        st.write("\n")
        st.write("\n")
        st_lottie(lottie_sentimental, height=300, key="sentimental")