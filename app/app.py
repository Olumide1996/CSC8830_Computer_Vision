import streamlit as st
from pathlib import Path


st.set_page_config(
    page_title="CSc 8830 Computer Vision",
    page_icon="CV",
    layout="centered",
)


PROJECT_ROOT = Path(__file__).resolve().parents[1]
KEYNOTE3_DIR = PROJECT_ROOT / "resources" / "keynote3"

KEYNOTE3_PDF = KEYNOTE3_DIR / "CVPR2025_Keynote3_VideoLLM_OlumideAdebisi.pdf"
KEYNOTE3_PPTX = KEYNOTE3_DIR / "CVPR2025_Keynote3_VideoLLM_OlumideAdebisi.pptx"


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
        "link_label": "Open Module 2",
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
        "link_label": "Open Module 3",
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
        "link_label": "Open Module 4",
    },
    {
        "module": "Keynote 3",
        "title": "Video-LLM Feasibility Prototype",
        "description": (
            "A quick Video-LLM prototype inspired by Afshin Dehghan's "
            "CVPR 2025 Video-LLM keynote. The prototype uses "
            "LLaVA-OneVision to analyze sampled video frames and "
            "generate a semantic and safety-oriented response."
        ),
        "url": "https://github.com/Olumide1996/CSC8830_VideoLLM_Prototype",
        "icon": "VLM",
        "status": "Prototype",
        "link_label": "Open Video-LLM Repository",
    },
]


st.title("CSc 8830 Computer Vision")
st.subheader("Assignment Portal")

st.write(
    "This page provides one public starting point for my CSc 8830 "
    "computer vision assignments and project work. Each assignment "
    "or prototype links to its corresponding resources."
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
            label=assignment["link_label"],
        )

        # ----------------------------------------------------------
        # Keynote 3 presentation downloads
        # ----------------------------------------------------------

        if assignment["module"] == "Keynote 3":

            st.markdown("**Presentation files**")

            col1, col2 = st.columns(2)

            with col1:

                if KEYNOTE3_PPTX.exists():

                    with open(KEYNOTE3_PPTX, "rb") as file:

                        st.download_button(
                            label="Download PowerPoint",
                            data=file.read(),
                            file_name=KEYNOTE3_PPTX.name,
                            mime=(
                                "application/vnd.openxmlformats-"
                                "officedocument.presentationml.presentation"
                            ),
                            use_container_width=True,
                        )

                else:

                    st.warning(
                        "PowerPoint presentation file is not available."
                    )

            with col2:

                if KEYNOTE3_PDF.exists():

                    with open(KEYNOTE3_PDF, "rb") as file:

                        st.download_button(
                            label="Download PDF",
                            data=file.read(),
                            file_name=KEYNOTE3_PDF.name,
                            mime="application/pdf",
                            use_container_width=True,
                        )

                else:

                    st.warning(
                        "PDF presentation file is not available."
                    )


st.divider()

st.sidebar.title("Navigation")
st.sidebar.write("CSc 8830 Computer Vision")
st.sidebar.caption("Public assignment portal")

st.sidebar.markdown("### Assignments")

for assignment in ASSIGNMENTS:

    st.sidebar.page_link(
        assignment["url"],
        label=f"{assignment['module']} — {assignment['title']}",
    )


st.info(
    "The assignment applications and project repositories are hosted "
    "separately so that each project can keep its own code and resources, "
    "while this portal provides one public starting point."
)