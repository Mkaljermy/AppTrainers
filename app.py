import streamlit as st

# Set the page configuration
st.set_page_config(
    page_title="HR Dashboard",
    page_icon="📊",
    layout="wide",
)

# App title
st.title("HR Dashboard 📊")
st.write("Welcome to the interactive HR Dashboard. Explore key insights and metrics below!")

# Embed Power BI dashboard using an iframe
power_bi_url = "https://app.powerbi.com/reportEmbed?reportId=1a2e14ff-96f9-40e9-80ef-6e177ae8685b&autoAuth=true&ctid=98ee90cf-5011-4a09-98ed-e961946683c4"

st.markdown(
    f"""
    <iframe src="{power_bi_url}" 
    width="100%" height="700" frameborder="0" allowfullscreen="true"></iframe>
    """,
    unsafe_allow_html=True,
)

# Footer section
st.markdown("---")
st.markdown(
    "Made with ❤️ using Streamlit. For questions, reach out to [HR Support](mailto:hr-support@example.com)."
)
