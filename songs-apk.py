from datetime import datetime
import re
import urllib
import os,urllib2
from bs4 import BeautifulSoup
import sys
import requests

####Optional####
def apk(name):
        

        name=name.split()
        name="+".join(name)

        urls="https://apkpure.com/search?q="+str(name)
        print urls
        url=urllib2.urlopen(urls)
        soup=BeautifulSoup(url,'html.parser')

        for apk in soup.find_all('div',{'id':'search-res'}):
            apks=apk.find('a').get('href')

            download_apk= "https://apkpure.com"+str(apks)+"/download?from=details"
            url_download=urllib2.urlopen(download_apk)
            print download_apk

            soup_download=BeautifulSoup(url_download)
            for let_me_download in soup_download.find_all('a',{'id':'download_link'},href=True):
                 link = let_me_download['href']
            download=requests.get(link).content
            f=open('%s.apk'%name,'wb')
            f.write(download)
            f.close()

        return link

##NOW the real part for songs##
version = sys.version_info[0]


if version == 2:  
    user_input = raw_input
    import urllib2
    urlopen = urllib2.urlopen  
    encode = urllib.urlencode  
    
    
else:  
    user_input = input
    import urllib.request
    import urllib.parse
    




def title(url):##If you want you can delete this function##
    try:
        page = urlopen(url).read()
        title = str(page).split('<title>')[1].split('</title>')[0]
    except:
        title = 'Youtube Song'
    
    return title

def my_name():##I Have no Idea why the fuck i wrote this function!!
    print("kashyap")







def song_download():
       

        song = user_input('Enter the name of song: ')  
        
        try:
            query_string = encode({"search_query" : song})
            content = urlopen("http://www.youtube.com/results?" + query_string)
            
            if version == 3:
                ##I hate RE

                search_results = re.findall(r'href=\"\/watch\?v=(.{11})', content.read().decode())
                
            else:
                ##ok!! if its not going work! I'm gonna kill you!!!
                search_results = re.findall(r'href=\"\/watch\?v=(.{11})', content.read())
                ##finally(Thanks to git)
                
        except:
            print('Something happened!!')
            exit(1)

        # youtube2mp3 API
        downloadLinkOnly = 'http://www.youtubeinmp3.com/fetch/?video=' + 'http://www.youtube.com/watch?v=' + search_results[0]
        try:
            print('Downloading %s' % song)
            urllib.urlretrieve(downloadLinkOnly, filename='%s.mp3' % song)
            urllib.urlcleanup()  
        except:
            print('Error  %s' % song)
            exit(1)






def exit(bye):
    print('\nThank you!!Fuck off now!!.')
    sys.exit(bye)


def main():
    try:
        my_name()
       # apk('gtu')


        try:
            
                song_download()
            
        except NameError:
            exit(1)
    except KeyboardInterrupt:
        exit(1)



if __name__ == '__main__':
    main()  
    exit(0)  
