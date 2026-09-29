import streamlit as st

st.set_page_config(
    page_title="CSc 8830 Computer Vision",
    page_icon="CV",
    layout="centered",
)

ASSIGNMENTS = [
    {
        "module": "Module 2",
        "title": "Camera Calibration & 2D Measurement",
        "description": (
            "Camera calibration and real-world 2D measurement "
            "using a smartphone image."
        ),
        "url": "https://csc8830-module2-olumide.streamlit.app",
        "icon": "M2",
        "status": "Live",
    },
    {
        "module": "Module 3",
        "title": "Image Blurring in Spatial and Fourier Domains",
        "description": (
            "Comparison of Gaussian image blurring using spatial "
            "convolution and Fourier-domain multiplication."
        ),
        "url": "https://csc8830-module3-olumide.streamlit.app",
        "icon": "M3",
        "status": "Live",
    },
    {
        "module": "Module 4",
        "title": "Human Boundary Segmentation",
        "description": (
            "Classical OpenCV segmentation for RGB and thermal images, "
            "with a SAM2 comparison and Fourier-domain analysis."
        ),
        "url": "https://csc8830-module4-olumide.streamlit.app",
        "icon": "M4",
        "status": "Live",
    },
]


st.title("CSc 8830 Computer Vision")
st.subheader("Assignment Portal")

st.write(
    "This page provides one public starting point for my CSc 8830 "
    "computer vision assignments. Each assignment opens its own "
    "live web application."
)

st.divider()

st.header("Assignments")

for assignment in ASSIGNMENTS:
    with st.container(border=True):
        st.markdown(
            f"### {assignment['icon']} — {assignment['module']}: "
            f"{assignment['title']}"
        )

        st.write(assignment["description"])
        st.caption(f"Status: {assignment['status']}")

        st.page_link(
            assignment["url"],
            label=f"Open {assignment['module']}",
        )

st.divider()

st.sidebar.title("Navigation")
st.sidebar.write("CSc 8830 Computer Vision")
st.sidebar.caption("Public assignment portal")

st.sidebar.markdown("### Live assignments")

for assignment in ASSIGNMENTS:
    st.sidebar.page_link(
        assignment["url"],
        label=f"{assignment['module']} — {assignment['title']}",
    )


st.info(
    "The assignment applications are hosted separately so that each "
    "assignment can keep its own GitHub repository, while this portal "
    "provides one public starting point."
)