## for cookies

# import requests
#
#
# url = "http://www.???.com"
#
# r = requests.get(url)
#
# print("cookies ：", r.cookies)
#
# print("cookies：", r.cookies['BDORZ'])
#




# # for contents
#
import requests


url = "http://www.bing.com"


url_img = "https://bing.com/sa/simg/hpc27.png"
r = requests.get(url_img)


print(r.content)

with open("./bing.png", "wb") as f:
    f.write(r.content)

