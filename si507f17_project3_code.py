from bs4 import BeautifulSoup
import unittest
import requests

#########
## Instr note: the outline comments will stay as suggestions, otherwise it's too difficult.
## Of course, it could be structured in an easier/neater way, and if a student decides to commit to that, that is OK.

## NOTE OF ADVICE:
## When you go to make your GitHub milestones, think pretty seriously about all the different parts and their requirements, and what you need to understand. Make sure you've asked your questions about Part 2 as much as you need to before Fall Break!


######### PART 0 #########

# Write your code for Part 0 here.
try:
  newman_data = open("newmandata.html",'r').read()
except:
  newman_data = requests.get("http://newmantaylor.com/gallery.html").text
  fx = open("newmandata.html",'w')
  fx.write(newman_data)
  fx.close()

soup = BeautifulSoup(newman_data, 'html.parser')

#print statements for problem 0 - dont forget to reactivate
# for image in soup.find_all("img"):
# 	if image.get("alt"):
# 		print(image.get("alt"))
# 	else:
# 		print("No alternative text provided!")



######### PART 1 #########

# Get the main page data...

# Try to get and cache main page data if not yet cached
# Result of a following try/except block should be that
# there exists a file nps_gov_data.html,
# and the html text saved in it is stored in a variable 
# that the rest of the program can access.

# We've provided comments to guide you through the complex try/except, but if you prefer to build up the code to do this scraping and caching yourself, that is OK.


try:
  nps_data = open("nps_gov_data.html",'r').read()
except:
  nps_data = requests.get("https://www.nps.gov/index.htm").text
  f = open("nps_gov_data.html",'w')
  f.write(nps_data)
  f.close()



# Get individual states' data...

# Result of a following try/except block should be that
# there exist 3 files -- arkansas_data.html, california_data.html, michigan_data.html
# and the HTML-formatted text stored in each one is available
# in a variable or data structure 
# that the rest of the program can access.

# TRY: 
# To open and read all 3 of the files

# But if you can't, EXCEPT:

# Create a BeautifulSoup instance of main page data 
# Access the unordered list with the states' dropdown


# Get a list of all the li (list elements) from the unordered list, using the BeautifulSoup find_all method

# Use a list comprehension or accumulation to get all of the 'href' attributes of the 'a' tag objects in each li, instead of the full li objects

# Filter the list of relative URLs you just got to include only the 3 you want: AR's, CA's, MI's, using the accumulator pattern & conditional statements


# Create 3 URLs to access data from by appending those 3 href values to the main part of the NPS url. Save each URL in a variable.


## To figure out what URLs you want to get data from (as if you weren't told initially)...
# As seen if you debug on the actual site. e.g. Maine parks URL is "http://www.nps.gov/state/me/index.htm", Michigan's is "http://www.nps.gov/state/mi/index.htm" -- so if you compare that to the values in those href attributes you just got... how can you build the full URLs?


# Finally, get the HTML data from each of these URLs, and save it in the variables you used in the try clause
# (Make sure they're the same variables you used in the try clause! Otherwise, all this code will run every time you run the program!)


# And then, write each set of data to a file so this won't have to run again.
soup = BeautifulSoup(nps_data, 'html.parser')
try:
	nps_ar_data = open("arkansas_data.html",'r').read()
	nps_ca_data = open("california_data.html",'r').read()
	nps_mi_data = open("michigan_data.html",'r').read()
except:
	ul_class = soup.find("ul",{"class":"dropdown-menu"})
	ul_search = ul_class.find_all("li")
	basenprurl = "https://www.nps.gov"
	ul_search_final = []
	
	for item in ul_search:
		hrefdata = item.find("a")['href']
		finalurl = basenprurl+hrefdata
		if "ca" in finalurl or "ar" in finalurl or "mi" in finalurl:
			# print (finalurl)
			ul_search_final.append(finalurl)
	for i in range(len(ul_search_final)):
		stateurlvar1 = ul_search_final[0]
		stateurlvar2 = ul_search_final[1]
		stateurlvar3 = ul_search_final[2]

	nps_ar_data = requests.get(stateurlvar1).text
	f = open("arkansas_data.html",'w')
	f.write(nps_ar_data)
	f.close()

	nps_ca_data = requests.get(stateurlvar2).text
	f1 = open("california_data.html",'w')
	f1.write(nps_ca_data)
	f1.close()

	nps_mi_data = requests.get(stateurlvar3).text
	f2 = open("michigan_data.html",'w')
	f2.write(nps_mi_data)
	f2.close()


######### PART 2 #########

## Before truly embarking on Part 2, we recommend you do a few things:

# - Create BeautifulSoup objects out of all the data you have access to in variables from Part 1
# - Do some investigation on those BeautifulSoup objects. What data do you have about each state? How is it organized in HTML?

# HINT: remember the method .prettify() on a BeautifulSoup object -- might be useful for your investigation! So, of course, might be .find or .find_all, etc...

# HINT: Remember that the data you saved is data that includes ALL of the parks/sites/etc in a certain state, but you want the class to represent just ONE park/site/monument/lakeshore.

# We have provided, in sample_html_of_park.html an HTML file that represents the HTML about 1 park. However, your code should rely upon HTML data about Michigan, Arkansas, and Califoria you saved and accessed in Part 1.

# However, to begin your investigation and begin to plan your class definition, you may want to open this file and create a BeautifulSoup instance of it to do investigation on.

# Remember that there are things you'll have to be careful about listed in the instructions -- e.g. if no type of park/site/monument is listed in input, one of your instance variables should have a None value...

ar_soup = BeautifulSoup(nps_ar_data, 'html.parser')
ca_soup = BeautifulSoup(nps_ca_data, 'html.parser')
mi_soup = BeautifulSoup(nps_mi_data, 'html.parser')

ar_soupobjects = ar_soup.find("ul", {"id" : "list_parks"})
single_ar_soupobject = ar_soupobjects.find("li", {"class" : "clearfix"})

ca_soupobjects = ca_soup.find("ul", {"id" : "list_parks"})
single_ca_soupobject = ca_soupobjects.find("li", {"class" : "clearfix"})

mi_soupobjects = mi_soup.find("ul", {"id" : "list_parks"})
single_mi_soupobject = mi_soupobjects.find("li", {"class" : "clearfix"})

## Define your class NationalSite here:


class NationalSite(object):
	def __init__(self, soupobject):
		self.soupobject = soupobject
		self.location = soupobject.h4.text
		self.name = soupobject.h3.a.text
		try: 
			self.type = soupobject.h2.text
		except: 
			self.type = "None"
		self.description = soupobject.p.text
		self.cachename = self.name+"_"+self.location+"_basic_info_cache.html"

	def __str__(self):
		return "{} | {}".format(self.name, self.location)

	def get_mailing_address(self):

		all_links_list = self.soupobject.find_all("a")
		for link in all_links_list:
			if "basicinfo" in link.get("href"):
				basic_info_link = link.get("href")
		try:
			nationalsite_basic_info = open(self.cachename,'r').read()
		except:
			nationalsite_basic_info = requests.get(basic_info_link).text
			f = open(self.cachename,'w')
			f.write(nationalsite_basic_info)
			f.close()

		mailingsoup = BeautifulSoup(nationalsite_basic_info, "html.parser")
		streetaddress = mailingsoup.find("span", {"itemprop":"streetAddress"}).span.text
		localaddress = mailingsoup.find("span", {"itemprop":"addressLocality"}).text
		regionaddress = mailingsoup.find("span", {"itemprop":"addressRegion"}).text
		postaladdress = mailingsoup.find("span", {"itemprop":"postalCode"}).text
		addresslines = " {} / {} / {} / {}".format(streetaddress, localaddress, regionaddress, postaladdress)
		return addresslines

	def __contains__(self, input):
		rvalue = False
		if input in self.name:
			rvalue = True
		return rvalue








# print (test_nationalsite_object)


## Recommendation: to test the class, at various points, uncomment the following code and invoke some of the methods / check out the instance variables of the test instance saved in the variable sample_inst:

# f = open("sample_html_of_park.html",'r')
# soup_park_inst = BeautifulSoup(f.read(), 'html.parser') # an example of 1 BeautifulSoup instance to pass into your class
# sample_inst = NationalSite(soup_park_inst)
# f.close()


######### PART 3 #########

# Create lists of NationalSite objects for each state's parks.

# HINT: Get a Python list of all the HTML BeautifulSoup instances that represent each park, for each state.

arkansas_natl_sites = []
all_ar_objects = ar_soupobjects.find_all("li", {"class" : "clearfix"})
print (all_ar_objects)



##Code to help you test these out:
# for p in california_natl_sites:
# 	print(p)
# for a in arkansas_natl_sites:
# 	print(a)
# for m in michigan_natl_sites:
# 	print(m)



######### PART 4 #########

## Remember the hints / things you learned from Project 2 about writing CSV files from lists of objects!

## Note that running this step for ALL your data make take a minute or few to run -- so it's a good idea to test any methods/functions you write with just a little bit of data, so running the program will take less time!

## Also remember that IF you have None values that may occur, you might run into some problems and have to debug for where you need to put in some None value / error handling!

