from google_images_download import google_images_download

#class instantiation
response = google_images_download.googleimagesdownload()
arguments = {"keywords":"dslr flowers",
"limit":300,
'format': 'jpg',
"output_directory":"./nebula2",
'size': 'medium',
'chromedriver': './chromedriver'}
paths = response.download(arguments)
