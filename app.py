import streamlit as st
from analyzer import analyze_code

st.title("🧠 Smart Code Analyzer")

code = st.text_area(
    "Paste your Python code here:",
    height=300
)

if st.button("Analyze Code"):
    if code.strip():
        result = analyze_code(code)

        if result["success"]:
            st.success(result["message"])

            st.subheader("Analysis Results")

            for issue in result["issues"]:
                st.write("•", issue)
        else:
            st.error(result["message"])
    else:
        st.warning("Please enter some Python code.")