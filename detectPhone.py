import os
import time
import webbrowser

def openUrls():
	firefox = webbrowser.get("firefox")
	firefox.open_new_tab("www.google.com")
	time.sleep(2)
	firefox.open_new_tab("www.yahoo.com")
	time.sleep(2)
	firefox.open_new_tab("www.youtube.com")

def main():
	os.system("touch detect.txt")
	while(True):
		time.sleep(10)
		os.system("sudo arp-scan -l > detect.txt")
		if "xx:xx:xx:xx:xx:xx" in open("detect.txt").read():
			print("Phone detected!")
			os.system("rm detect.txt")
			openUrls()
			break

if __name__ == '__main__':
	main()