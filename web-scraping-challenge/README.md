# Web-Scraping-Challenge

## Web Scraping Homework - Mission to Mars
### NASA Mars News
Using Jupyter Notebook, I first imported the dependencies and connected to the chromedriver. Using BeautifulSoup, I scraped the NASA website to collect the latest News Title and Paragraph Text, saved as news_title and news_p.

### JPL Mars Space Images - Featured Image
Continuing in the Jupyter Notebook, I scraped the NASA JPL Featured Space Image page. First having to click the "Full Image" button and then "More Info". I used BeautifulSoup to find the relative image path, which I combined with the main URL to get featured_image_url with .jpg.

### Mars Facts
I used Pandas to rscrape the table containing facts about the planet including Diameter, Mass, etc. Then converted it into HTML.

### Mars Hemispheres
I was able to set the browser to open the USGS Astrogeology site. 
