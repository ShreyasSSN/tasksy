import os
import requests
from bs4 import BeautifulSoup
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from urllib.parse import urlparse
from django.utils.text import slugify

def get_logo_and_save(app_link, app_name):
    try:
        if not app_link.startswith(('http://', 'https://')):
            app_link = 'http://' + app_link

            
        print(f"Fetching: {app_link}") 
        # Send a request to the URL
        response = requests.get(app_link)
        response.raise_for_status()  # Raise an error for bad responses

        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Try to find the favicon link
        icon_link = soup.find("link", rel="icon")
        logo_url = icon_link['href'] if icon_link and 'href' in icon_link.attrs else None

        # If favicon link not found, check for other logos
        if not logo_url:
            logo_url = soup.find("link", rel="apple-touch-icon")['href'] if soup.find("link", rel="apple-touch-icon") else None

        # Ensure the logo URL is absolute
        if logo_url:
            parsed_url = urlparse(app_link)
            if not logo_url.startswith(('http://', 'https://')):
                if logo_url.startswith('/'):
                    logo_url = f"{parsed_url.scheme}://{parsed_url.netloc}{logo_url}"
                else:
                    logo_url = f"{parsed_url.scheme}://{parsed_url.netloc}/{logo_url}"
            print(f"Logo URL: {logo_url}")

            # Download the logo image
            logo_response = requests.get(logo_url)
            logo_response.raise_for_status()  # Raise an error for bad responses

            # Create a unique filename based on the app name and save it to the media directory
            logo_name = f"{slugify(app_name)}.png"  # You can adjust the extension based on the actual image type
            path = default_storage.save(f'app_logos/{logo_name}', ContentFile(logo_response.content))

            return path  # Return the file path of the saved logo
    except Exception as e:
        print(f"Error fetching or saving logo for {app_link}: {e}")
    return None
