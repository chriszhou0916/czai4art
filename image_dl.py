from google_images_download import google_images_download

response = google_images_download.googleimagesdownload()
arguments = {"keywords":"modern abstract art",
"limit":500,
'format': 'jpg',
"output_directory":"./data",
'size': '>400*300',
'specific_site': 'fineartamerica.com',
'chromedriver': './chromedriver'}
paths = response.download(arguments)

response = google_images_download.googleimagesdownload()
arguments = {"keywords":"flowers",
"limit":500,
'format': 'jpg',
"output_directory":"./data",
'size': '>400*300',
'chromedriver': './chromedriver'}
paths = response.download(arguments)
