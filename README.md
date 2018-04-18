# scrapy-image-download
Basic python code to scrape images using python and scrapy

Hello Guys!
This is the initial code version to scrape images from a website (Here, I scraped espncricinfo, as it is my favourite website)

To make this code working,

1. First create a Scrapy project "scrapy startproject espn-cricinfo-images" 
2. Browsing through the project structure, you could see a lot of python files and a directory "Spider". 

3.For this basic code to work we need to do two things,
	1. Create our own custom spider and name it like "cricinfo_spider.py". For now leave it untouched
	2. Modify the below files inside the project structure,
			"settings.py"
			"items.py"

4.Let’s start with the settings.py  file which only requires to quick updates. The first is to find the ITEMS_PIPELINE  tuple, uncomment it (if it’s commented out), and add in the following setting:
	# Configure item pipelines
	# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
	ITEM_PIPELINES = {
    		'scrapy.contrib.pipeline.images.FilesPipeline': 1,
		}
		
	This setting will activate Scrapy’s default file scraping capability.
	
5.The second update to the settings.py can be appended to the bottom of the file. This value, FILES_STORE , is simply the path to the output directory where the download images will be stored:
	FILES_STORE = "*/your_path/"
	
6.Now we can move on to items.py , which allows us to define a data object model for the webpages our spider crawls:
	import scrapy
	class TutorialItem(scrapy.Item):
    		files  = scrapy.Field()
    		file_urls  = scrapy.Field()
    		pass
		
Note: you can either modify settings.py and items.py yourself or directly copy files attached here
