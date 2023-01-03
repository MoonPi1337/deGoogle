import codecs, os, fnmatch

bannedUrlsHttps = {'https://fallback.google.com/gen_204', 
'https://www.googleapis.cn/generate_204', 
'https://connectivitycheck.gstatic.com/generate_204', 
'https://play.googleapis.com/generate_204', 
'https://check.googlezip.net/connect', 
'https://www.google.com/gen_204', 
'https://clients3.google.com/generate_204', 
'https://www.google.com/generate_204', 
'https://www.gstatic.com/generate_204',
'https://clients4.google.com/generate_204'}

bannedUrlsHttp = {'http://www.google.com/gen_204', 
'http://www.google.com/generate_204', 
'http://check.googlezip.net/connect', 
'http://www.gstatic.com/generate_204', 
'http://clients3.google.com/generate_204', 
'http://fallback.google.com/gen_204', 
'http://play.googleapis.com/generate_204', 
'http://www.googleapis.cn/generate_204', 
'http://connectivitycheck.gstatic.com/generate_204',
'http://clients4.google.com/generate_204'}

ProjDir = input("Project folder: ")

def findReplace(directory, filePattern):
    for path, dirs, files in os.walk(os.path.abspath(directory)):
        for filename in fnmatch.filter(files, filePattern):
            filepath = os.path.join(path, filename)
            try:
                with codecs.open(filepath,'r','UTF-8') as f:
                    s = f.read()
                for i in bannedUrlsHttp:
                    while i in s:
                        s = s.replace(i,"http://f-droid.org")
                for i in bannedUrlsHttps:
                    while i in s:
                        s = s.replace(i,"https://f-droid.org")
                with codecs.open(filepath,'w','UTF-8') as f:
                    f.write(s)
            except:
                print("Failed to fix {}".format(filepath))

findReplace(ProjDir,"*.jar")
findReplace(ProjDir,"*.h")
findReplace(ProjDir,"*.hpp")
findReplace(ProjDir,"*.xml")
findReplace(ProjDir,"*.mk")
findReplace(ProjDir,"*.sh")
findReplace(ProjDir,"*.kt")
findReplace(ProjDir,"*.kts")

