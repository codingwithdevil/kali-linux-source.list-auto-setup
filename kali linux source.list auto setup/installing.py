import time
import sys
from bs4 import BeautifulSoup

nu = '\033[0m'
re = '\033[1;31m'
gr = '\033[1;32m'
cy = '\033[1;36m'
mg = '\033[1;35m'
def write(in_text):
	for char in in_text:
		time.sleep(0.1)
		sys.stdout.write(char)
		sys.stdout.flush()
		
write(f"{gr}[+]{mg}Coded by Codingwithdevil{nu}....")
print(f"{cy}\n------------------------")
time.sleep(1)
write(f"{gr}[+]{re} Visit youtube channel{nu}...")
print(f"\n-----------------------------")
time.sleep(1)
write(f"\n{gr}[+]{mg}channel: https://www.youtube.com/channel/UCnKlznTEohj_PCw9cuxy8Zg  {nu} ")
print(f"\n")
time.sleep(1)
write(f"{gr}[+]{re}Instagram Profile https://instagram.com/codingwithdevil?utm_medium=copy_link{nu} ")
print(f"\n")
time.sleep(1)
write(f"{gr}[+]{re}Message on Instagram for help & support {nu}...")
print(f"\n")
time.sleep(1)
write(f"{gr}[+]{re}Sourcelist Setup finished  {nu}...")
print(f"\n")