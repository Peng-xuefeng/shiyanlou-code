#下载一个给定网页的某个文件，到指定的路径下
#如果有同名文件，检查内容是否一致，如果一致不下载了，不一致将本次下载的内容文件名后面加上(1)
import requests
import os

def whetherExistSameNameFile(path,filename,fileText):
    names = os.listdir(path)
    if filename in names:
        fobj = open('E:/movie'+'/'+filename)
        s = fobj.read()
        fobj.close()
        if s == fileText:
            print('Already download')
        else:
            fobj = open('E:/movie'+'/'+'new.txt','w')
            fobj.write(fileText)
            fobj.close()
            print('Download finish')
    else:
        fobj = open('E:/movie'+'/'+filename,'w')
        fobj.write(fileText)
        fobj.close()
        print('Download finish')
        
    
def download(url):
    """
    下载一个文件，到指定目录下
    """
    try:
        req = requests.get(url)
    except:
        print('Invalid URL "{}"'.format(url))
    if req.status_code == 200:
        filename = url.split('/')[-1]
        fileText = req.text
        whetherExistSameNameFile('E:/movie',filename,fileText)

if __name__ =='__main__':
    URL = input("Please input a URL:")
    download(URL)
