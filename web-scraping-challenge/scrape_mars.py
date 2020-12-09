from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# Setup splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

# Open Mars browser
url = 'https://mars.nasa.gov/news/'
browser.visit(url)
time.sleep(1)

#Parse Results
html = browser.html
soup = BeautifulSoup(html, "html.parser")

soup.body

result=soup.find('ul', class_='item_list')
news_title=result.find('div', class_='content_title').text
news_p=result.find('div', class_='article_teaser_body').text
print(news_title)
print(news_p)

#Use splinter to navigate the site and find the image url for the current Featured Mars Image
image_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(image_url)

#Use splinter to navigate the site and find the image url for the current Featured Mars Image
image_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(image_url)

# Click for large image
browser.click_link_by_partial_text('more info')

# Parse results
html = browser.html
soup = BeautifulSoup(html, 'html.parser')

# Search for image source
results = soup.find_all('figure', class_='lede')
relative_image_path = results[0].a['href']
featured_image_url = 'https://www.jpl.nasa.gov' + relative_image_path

print(featured_image_url)

# Open Mars facts browser
facts_url = 'https://space-facts.com/mars/'
browser.visit(facts_url)
time.sleep(1)

html = browser.html
soup = BeautifulSoup(html, 'html.parser')

# Scrape data using Pandas
tables = pd.read_html('https://space-facts.com/mars/')

# Take second table for Mars facts
mars_facts_df = tables[1]

mars_facts_df

# Convert table to html
mars_facts_table = [mars_facts_df.to_html(classes='data table table-borderless', 
                                          index=False, header=False, border=0)]
mars_facts_table

# Open hemispheres browser
hem_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(hem_url)
time.sleep(1)

html = browser.html
soup = BeautifulSoup(html, 'html.parser')

hemisphere_names = []

# Search for the names of all four hemispheres
results = soup.find_all('div', class_="collapsible results")
hemispheres = results[0].find_all('h3')

# Get text and store in list
for name in hemispheres:
    hemisphere_names.append(name.text)

hemisphere_names