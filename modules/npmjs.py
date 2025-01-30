# Copyright 2025 Alessio Marziali
from bs4 import BeautifulSoup
import requests
import logging

# Enable logging across the module
logenabled = False
# Set up logging configuration
logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)  # Create a logger instance

# Download HTML content from the URL
def download_page(dependency):

    if '@' in dependency:
        dependency = '@'.join(dependency.split('@')[:-1])
        dependency = f"https://www.npmjs.com/package/{dependency}"
    else:
        dependency = f"https://www.npmjs.com/package/{dependency}"

    try:
        # Send GET request to the URL
        response = requests.get(dependency)
        
        # Check for HTTP errors
        if response.status_code != 200:
            return f"HTTP {response.status_code}"
        
        # Return the HTML content for successful requests
        return response.text
        
    except requests.RequestException as e:
        return f"Error: {str(e)}"

# Extract license from the HTML content using BeautifulSoup
def extract_license(html_content):
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Locate the section containing license information
    license_section = soup.find('h3', string="License")
    
    if license_section:
        # The sibling <p> tag contains the license text
        license_info = license_section.find_next_sibling('p')
        if license_info:
            return license_info.text.strip()  # Return the extracted text
    
    return None  # Return None if the license information is not found

# Get the license for a given dependency
def get_license(dependency):
    html_content = download_page(dependency)
    return extract_license(html_content)
