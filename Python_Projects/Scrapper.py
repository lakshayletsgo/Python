import pandas as pd
import requests
from bs4 import BeautifulSoup

# Read the data from the Excel file
df = pd.read_excel("Web scraping assignment no address.xlsx")


def extract_address(url):
    # Make a request to the website
    response = requests.get(url)

    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, "html.parser")

    # Find the address
    address = soup.find("address")

    # Return the address text
    if address:
        return address.text
    else:
        return " "

df["Address"] = ""
df = df.astype({"Address": str})
# Loop through each row of the DataFrame
for i, row in df.iterrows():
    url = row["Website"]
    address = extract_address(url)
    df.at[i, "Address"] = address

# Write the data back to the Excel file
if (address):
    (df.to_excel("Web scraping assignment no address.xlsx", index=False))
else:
        df.to_excel("Web scraping assignment no address.xlsv", index= False)


