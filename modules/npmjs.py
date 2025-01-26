from bs4 import BeautifulSoup
import requests
import sys  # Add this import at the top of the file

def create_npm_url(dependency):
    # Construct and return the NPM package URL
    return f"https://www.npmjs.com/package/{dependency}"

def download_page(url):
    try:
        # Send GET request to the URL
        response = requests.get(url)
        
        # Check for HTTP errors
        if response.status_code != 200:
            return f"HTTP {response.status_code}"
        
        # Return the HTML content for successful requests
        return response.text
        
    except requests.RequestException as e:
        return f"Error: {str(e)}"


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

# Example usage
if __name__ == "__main__":
    # Replace the hardcoded value with command line argument
    if len(sys.argv) > 1:
        dependency = sys.argv[1]  # Get the dependency from command line arguments
        url = create_npm_url(dependency)
    else:
        print("Please provide a dependency as a command line argument.")
        sys.exit(1)  # Exit if no argument is provided

    html_content = download_page(url)
    
    # Check if the response indicates an error
    if html_content.startswith(('HTTP', 'Error')):
        print(f"Failed to fetch package information: {html_content}")
        sys.exit(1)
    
    # Extract and print the license
    license_type = extract_license(html_content)
    print(f"License: {license_type}")
