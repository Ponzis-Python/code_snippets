from urllib import request

file_url = r'http://ipv4.download.thinkbroadband.com/10MB.zip'

def download_file_information(url):
    # open url file
    fileOpen = request.urlopen(url)
    # read the file
    file_info = fileOpen.read()
    #convert to string
    file_info_str = str(file_info)
    # split the lines in to the file
    file_lines = file_info_str.split('\\n')