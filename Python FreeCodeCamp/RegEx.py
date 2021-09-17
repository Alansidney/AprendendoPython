#Find the hostname in a email
import re
email = "asj2@cin.ufpe.br "

hostName = re.findall('.*@([^ ])*', email)

print (hostName)