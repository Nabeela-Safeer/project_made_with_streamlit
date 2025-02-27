#  create app of data sweeper
import streamlit as st
import pandas as pd
import os
import numpy as np
from io import BytesIO
import matplotlib.pyplot as plt

# Set up the app
st.set_page_config(page_title='📝 Data Management Tool', page_icon='📊', layout='wide')
st.title('📊 Data Management Tool')
st.write('Upload, view, clean, analyze, and download your data effortlessly!')

# Upload files
uploaded_files = st.file_uploader("📂 Upload Files (CSV, Excel):", type=['csv', 'xlsx'], accept_multiple_files=True)

if uploaded_files:
    for file in uploaded_files:
        file_ext = os.path.splitext(file.name)[-1].lower()
        
        # Read files
        if file_ext == '.csv':
            df = pd.read_csv(file)
        elif file_ext == '.xlsx':
            df = pd.read_excel(file)
        else:
            st.error('❌ Please upload a valid CSV or Excel file.')
            continue
        
        # Display file info
        st.subheader(f'📜 File: {file.name}')
        st.write(f'📌 Size: {file.size} bytes')
        st.write(f'🔍 Extension: {file_ext}')
        
        # Show preview
        st.write('👀 Data Preview:')
        st.dataframe(df.head())

        # Data Summary
        st.subheader("📊 Data Insights")
        if st.checkbox(f"Show Summary for {file.name}"):
            st.write(df.describe())

        # Search & Filter
        st.subheader("🔍 Search & Filter Data")
        search_col = st.selectbox("Select column to search:", df.columns)
        search_value = st.text_input(f"Enter search value for {search_col}:")
        if search_value:
            filtered_df = df[df[search_col].astype(str).str.contains(search_value, case=False, na=False)]
            st.write(f"🔎 Results matching `{search_value}` in `{search_col}`:")
            st.dataframe(filtered_df)

        # Data Cleaning
        st.subheader('🧹 Data Cleaning')
        if st.checkbox(f"Clean data for {file.name}"):
            # Remove Duplicates
            if st.checkbox("🗑 Remove Duplicates"):
                df = df.drop_duplicates()
                st.success("✅ Duplicates removed!")
            
            # Fill Missing Values
            if st.checkbox("📌 Fill Missing Values"):
                fill_option = st.selectbox("Choose a filling method:", ["Fill with 0", "Fill with Mean", "Fill with Median"])
                if fill_option == "Fill with 0":
                    df.fillna(0, inplace=True)
                elif fill_option == "Fill with Mean":
                    df.fillna(df.mean(numeric_only=True), inplace=True)
                elif fill_option == "Fill with Median":
                    df.fillna(df.median(numeric_only=True), inplace=True)
                st.success("✅ Missing values filled!")

        # Column Type Conversion
        st.subheader("🔄 Convert Column Type")
        col_to_convert = st.selectbox("Select column to convert:", df.columns)
        convert_to = st.radio("Convert to:", ["String", "Integer", "Float"])
        if st.button(f"Convert {col_to_convert} to {convert_to}"):
            if convert_to == "String":
                df[col_to_convert] = df[col_to_convert].astype(str)
            elif convert_to == "Integer":
                df[col_to_convert] = pd.to_numeric(df[col_to_convert], errors='coerce').fillna(0).astype(int)
            elif convert_to == "Float":
                df[col_to_convert] = pd.to_numeric(df[col_to_convert], errors='coerce')
            st.success(f"✅ Converted {col_to_convert} to {convert_to}!")

        # Data Visualization
        st.subheader('📊 Data Visualization')
        if st.checkbox(f"Show Visualizations for {file.name}"):
            num_columns = df.select_dtypes(include=[np.number]).columns.tolist()
            if num_columns:
                selected_col = st.selectbox("Select a numeric column:", num_columns)
                
                # Histogram
                fig, ax = plt.subplots()
                df[selected_col].hist(ax=ax, bins=20, color='skyblue', edgecolor='black')
                ax.set_title(f"📊 Histogram of {selected_col}")
                st.pyplot(fig)

                # Boxplot
                fig, ax = plt.subplots()
                df.boxplot(column=selected_col, ax=ax)
                ax.set_title(f"📦 Boxplot of {selected_col}")
                st.pyplot(fig)
            else:
                st.warning("⚠️ No numeric columns found for visualization.")

        # Convert File
        st.subheader('📂 Convert & Download File')
        conversion_type = st.radio(f"Convert {file.name} to:", ('CSV', 'Excel'), key=file.name)
        if st.button(f"Convert & Download {file.name}"):
            buffer = BytesIO()
            new_file_name = file.name.replace(file_ext, f".{conversion_type.lower()}")
            mime_types = "text/csv" if conversion_type == "CSV" else "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"

            if conversion_type == "CSV":
                df.to_csv(buffer, index=False)
            else:
                df.to_excel(buffer, index=False, engine="openpyxl")

            buffer.seek(0)

            # Download Button
            st.download_button(
                label=f"⬇️ Download {new_file_name}",
                data=buffer,
                file_name=new_file_name,
                mime=mime_types
            )

        st.success("✅ All processing completed!")
