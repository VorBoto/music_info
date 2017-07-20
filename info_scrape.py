
from bs4 import BeautifulSoup
from urllib import request
from urllib import error
import csv
from selenium import webdriver

base_url = "http://www.musicrow.com/directory"
url = "http://www.musicrow.com/directory/index327a8.php?id=3260&cat=14"

def get_site_selenium(url):
    """
       Get url and return the page source
       Returns page_source
    """
    driver = webdriver.PhantomJS()
    driver.get(url)
    return driver.page_source


def grab_information(html):
    """
    grab needed informatino from the sites

    name = first-name,last-name,buisness Name-optional
    email
    phone number
    address 1
    address 2
    city
    state
    zip code
    """
    # Initiate some variables
    name = "--NONE--"
    email = "--NONE--"
    phone_number = "--NONE--"
    remaining = "--NONE--"

    # Create soup from page source
    soup = BeautifulSoup(html,'html.parser')

    # Location placeholders
    col3 = soup.find_all("div", id="col3")[0]
    rows = col3.find_all("div", class_="row")
    row0 = rows.pop(0)
    name = row0.h1.text
    remaining = row0.text.strip()
    for row in rows:
        if "Email:" in row.find_all("span")[0]:
            email = row.find_all("span")[1].text
        if "Office Phone:" in row.find_all("span")[0]:
            phone_number = row.find_all("span")[1].text
    return (name,email,phone_number,remaining)

# url ends to visit
url_ends = ["/index327a8.php?id=4803&amp;cat=14",
            "/index327a8.php?id=5231&amp;cat=14",
            "/index327a8.php?id=5848&amp;cat=14",
            "/index327a8.php?id=4404&amp;cat=14",
            "/index327a8.php?id=3260&amp;cat=14",
            "/index327a8.php?id=2951&amp;cat=14",
            "/index327a8.php?id=2949&amp;cat=14",
            "/index327a8.php?id=4399&amp;cat=14",
            "/index327a8.php?id=2960&amp;cat=14",
            "/index327a8.php?id=2959&amp;cat=14",
            "/index327a8.php?id=5547&amp;cat=14",
            "/index327a8.php?id=5844&amp;cat=14",
            "/index327a8.php?id=5694&amp;cat=14",
            "/index327a8.php?id=4304&amp;cat=14",
            "/index327a8.php?id=5991&amp;cat=14",
            "/index327a8.php?id=3928&amp;cat=14",
            "/index327a8.php?id=5762&amp;cat=14",
            "/index327a8.php?id=5056&amp;cat=14",
            "/index327a8.php?id=5404&amp;cat=14",
            "/index327a8.php?id=3959&amp;cat=14",
            "/index327a8.php?id=4343&amp;cat=14",
            "/index327a8.php?id=2957&amp;cat=14",
            "/index327a8.php?id=2950&amp;cat=14",
            "/index327a8.php?id=4230&amp;cat=14",
            "/index327a8.php?id=6031&amp;cat=14",
            "/index327a8.php?id=5818&amp;cat=14",
            "/index327a8.php?id=5712&amp;cat=14",
            "/index327a8.php?id=5811&amp;cat=14",
            "/index327a8.php?id=2954&amp;cat=14",
            "/index327a8.php?id=5695&amp;cat=14",
            "/index327a8.php?id=3899&amp;cat=14",
            "/index327a8.php?id=5355&amp;cat=14",
            "/index327a8.php?id=3361&amp;cat=14",
            "/index327a8.php?id=4148&amp;cat=14",
            "/index327a8.php?id=4413&amp;cat=14",
            "/index327a8.php?id=4432&amp;cat=14",
            "/index327a8.php?id=4369&amp;cat=14",
            "/index327a8.php?id=5724&amp;cat=14",
            "/index327a8.php?id=5988&amp;cat=14",
            "/index327a8.php?id=4884&amp;cat=14",
            "/index327a8.php?id=5832&amp;cat=14",
            "/index327a8.php?id=5109&amp;cat=14",
            "/index327a8.php?id=4921&amp;cat=14",
            "/index327a8.php?id=5455&amp;cat=14",
            "/index327a8.php?id=5230&amp;cat=14",
            "/index327a8.php?id=4821&amp;cat=14",
            "/index327a8.php?id=5435&amp;cat=14",
            "/index327a8.php?id=4933&amp;cat=14",
            "/index327a8.php?id=2955&amp;cat=14",
            "/index327a8.php?id=5827&amp;cat=14",
            "/index327a8.php?id=3005&amp;cat=14",
            "/index327a8.php?id=4910&amp;cat=14",
            "/index327a8.php?id=4410&amp;cat=14",
            "/index327a8.php?id=2952&amp;cat=14",
            "/index327a8.php?id=3366&amp;cat=14",
            "/index327a8.php?id=2953&amp;cat=14",
            "/index327a8.php?id=5065&amp;cat=14",
            "/index327a8.php?id=3907&amp;cat=14",
            "/index327a8.php?id=2958&amp;cat=14",
            "/index327a8.php?id=5125&amp;cat=14",
            "/index327a8.php?id=4902&amp;cat=14",
            "/index327a8.php?id=4080&amp;cat=14",
            "/index327a8.php?id=3256&amp;cat=14"]

# Create csv file for output
the_file = open("output.txt", "w")

# Create instance of csv writer
csvwriter = csv.writer(the_file,dialect='unix')

# Create and write header information to csv file
header = ("NAME","EMAIL","PHONE_NUMBER","REMAINING")
csvwriter.writerow(header)

# For each url ending get informatino
for end in url_ends:
    # Format url for each 
    url = base_url + end
    # Get each page source
    html = get_site_selenium(url)
    # Extract the needed informaiton
    info = grab_information(html)
    # Write each row of informaiton
    csvwriter.writerow(info)

# Close the csv file
the_file.close()
    
    
    
