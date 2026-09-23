# CSc 8830 Computer Vision Assignment Portal

This Streamlit app provides one public starting point for the CSc 8830 computer vision assignments.

## Current live assignments

- Module 2 — Camera Calibration & 2D Measurement
- Module 3 — Image Blurring & Fourier Filtering

## Adding a future assignment

Open `app/app.py` and add another dictionary to the `ASSIGNMENTS` list with:
- module
- title
- description
- public Streamlit URL
- icon
- status

Commit and push the change to GitHub. Streamlit Community Cloud will update the portal from the repository.

## Run locally

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
streamlit run app\app.py
```
