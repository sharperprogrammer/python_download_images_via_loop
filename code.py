# allows us to download images from the web
#    https://stackoverflow.com/questions/3042757/downloading-a-picture-via-urllib-and-python
import urllib.request

# downloads an image from the internet
def downloader(image_url):

    #get the last part of the URL, which is the name of the pokemon + .jpg
    save_url = image_url[40:-1]
    full_file_name = "/Users/sethharper/google drive/development/python_apps/Download_Images_Loop/images/" + save_url
    # image_url = "https://img.pokemondb.net/artwork/large/bulbasaur.jpg"

    # Have to add a header to the request to download the image, otherwise the site 
    #   recognizes us as "weird" traffic, and won't give us the image.
    #     https://medium.com/@speedforcerun/python-crawler-http-error-403-forbidden-1623ae9ba0f
    #     https://stackoverflow.com/questions/45247983/urllib-urlretrieve-with-custom-header
    # opener = urllib.request.build_opener()
    # opener.addheaders = [('User-Agent', 'Chrome/79.0.3945.130')]
    # urllib.request.install_opener(opener)
    
    urllib.request.urlretrieve(image_url,full_file_name)

# downloader("https://img.pokemondb.net/artwork/large/bulbasaur.jpg")

# this function takes the contents of a file, and removes the pieces that don't belong.
#   I did this because when I copied and pasted my output from the Javascript console, I got
#   a bunch of crap I didn't need, and didn't feel like erasing it line by line.
#
# I actually could've done without this function, and done the cleaning up of each line
#   and downloading the files from each url at the same time (without writing to a new file).
#   However, I'm slightly OCD and like looking at a file with a bunch of neat and tidy URLs.
def clean_up_urls():

    oldfile = open("/Users/sethharper/Google Drive/Development/Python_apps/Download_Images_Loop/list_of_urls.txt", "r")
    newfile = open("/Users/sethharper/Google Drive/Development/Python_apps/Download_Images_Loop/clean_urls.txt", "w")

    for line in oldfile:
        # locate the beginning of the actual text on each line that I want
        # create a new string out of the line from there -> to the end of the line minus the last 
        # 3 characters (the , the " and the \n )
        # then restore the "\n" to the end of the line
        line = line[line.find("https://i"):-3] + "\n"
        newfile.write(line)

    oldfile.close()
    newfile.close()

# Loops through the URLs in the file and downloads each image into a folder.
def download_images_from_file():
    file = open("/Users/sethharper/Google Drive/Development/Python_apps/Download_Images_Loop/clean_urls.txt", "r")
    for line in file:
        downloader(line)
    file.close()

clean_up_urls()

# download_images_from_file()