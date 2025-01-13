import streamlit as st
import base64

# Set the page configuration
st.set_page_config(
    page_title="HR Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Function to set a background image
def set_background(image_file):
    with open(image_file, "rb") as img_file:
        base64_img = base64.b64encode(img_file.read()).decode()
    st.markdown(
        f"""
        <style>
        body {{
            background-image: url("data:image/jpg;base64,{base64_img}");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
            background-position: center;
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )

# Custom CSS for styling
st.markdown(
    """
    <style>
    .header-title {
        font-size: 36px;
        font-weight: bold;
        color: #2b5797; /* White text for contrast */
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.6); /* Subtle shadow for better visibility */
        text-align: center;
        margin-top: 20px;
        margin-bottom: 10px;
    }
    .sub-title {
        font-size: 18px;
        color: #f0f0f0; /* Subtle light gray text */
        text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.5);
        text-align: center;
        margin-bottom: 20px;
    }
    .dashboard-container {
        display: flex;
        justify-content: center; /* Center the iframe horizontally */
        align-items: center;
        margin-top: 10px;
        margin-bottom: 10px;
    }
    iframe {
        width: 70%; /* Reduced width for narrower display */
        height: 600px; /* Maintain height */
        border: none;
        border-radius: 8px;
        box-shadow: 0px 4px 16px rgba(0, 0, 0, 0.3); /* Shadow for better contrast */
    }
    footer {
        text-align: center;
        color: #ffffff; /* White text for footer */
        margin-top: 1px;
        font-size: 14px;
        text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.6);
    }
    footer a {
        color: #d1ecf1; /* Light blue for links */
        text-decoration: none;
    }
    footer a:hover {
        text-decoration: underline;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# App header
st.markdown("<div class='header-title'>HR Dashboard 📊</div>", unsafe_allow_html=True)
st.markdown(
    "<div class='sub-title'>Explore key HR insights and make data-driven decisions effortlessly.</div>",
    unsafe_allow_html=True,
)

# Embed Power BI dashboard with a centered and narrower frame
power_bi_url = (
    "https://app.powerbi.com/reportEmbed?reportId=1a2e14ff-96f9-40e9-80ef-6e177ae8685b"
    "&autoAuth=true&ctid=98ee90cf-5011-4a09-98ed-e961946683c4"
    "&filterPaneEnabled=false&navContentPaneEnabled=false"
)

st.markdown(
    f"""
    <div class="dashboard-container">
        <iframe src="{power_bi_url}" class="dashboard-frame"></iframe>
    </div>
    """,
    unsafe_allow_html=True,
)

# Footer section
st.markdown("---")
st.markdown(
    """
    <footer>
        Made with ❤️ using Streamlit. For questions, reach out to 
        <a href="https://www.linkedin.com/in/mohammad-aljermy/" target="_blank">Mohammad A-jermy</a>.
    </footer>
    """,
    unsafe_allow_html=True,
)
