# NOTICE: mvnrepository.com does not allow scraping. Therefore, we cannot provide this functionality.
# Although it might be possible to get around this restriction by using headless browsers, doing so would be unethical. The script will just return the URL, which you may manually check to obtain the license details.

from bs4 import BeautifulSoup
import requests

def create_mvn_url(dependency):
    # Construct and return the NPM package URL
    # https://mvnrepository.com/artifact/org.apache.httpcomponents/httpclient
    return f"https://mvnrepository.com/artifact/{dependency}"

# Example usage
if __name__ == "__main__":
    # Load your HTML content (e.g., from a file or a web request)
    url = create_mvn_url("org.apache.httpcomponents/httpclient")
    print(f"Manually check License at : {url}")
