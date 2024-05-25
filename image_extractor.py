import streamlit as st
import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin, urlparse

# Streamlit UI
st.title("Webpage Image Extractor")
url = st.text_input("Enter the URL of the webpage")
output_folder = "extracted_images"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

if url:
    # Validate the URL
    parsed_url = urlparse(url)
    if not parsed_url.scheme:
        st.error("Please enter a valid URL.")
    else:
        try:
            response = requests.get(url)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, "html.parser")
            img_tags = soup.find_all("img")

            total_images = len(img_tags)
            progress_bar = st.progress(0)
            st.write(f"Found {total_images} images")

            for i, img in enumerate(img_tags):
                img_url = img.get("src")
                if not img_url:
                    continue

                # Handle relative URLs
                img_url = urljoin(url, img_url)

                try:
                    img_response = requests.get(img_url)
                    img_response.raise_for_status()

                    img_data = img_response.content
                    img_name = os.path.join(output_folder, f"image_{i+1}.jpg")

                    with open(img_name, "wb") as img_file:
                        img_file.write(img_data)
                    
                    progress_bar.progress((i + 1) / total_images)
                except Exception as e:
                    st.write(f"Failed to download image {img_url}: {e}")

            st.write("Image extraction completed!")
            st.balloons()

            # Display downloaded images
            for img_file in os.listdir(output_folder):
                img_path = os.path.join(output_folder, img_file)
                st.image(img_path, caption=img_file)

        except requests.exceptions.RequestException as e:
            st.error(f"Error fetching the URL: {e}")
