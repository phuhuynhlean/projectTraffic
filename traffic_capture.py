import requests
import time
from PIL import Image

def main():
    #URL and Metadata
    path_quoclo1    = ["loc01","quoclo1-buithanhkhiet","http://giaothong.hochiminhcity.gov.vn/render/ImageHandler.ashx?id=58afea5dbd82540010390c4d&t=1667011700842"]
    path_vovankiet  = ["loc02","vovankiet-caovanlau","http://giaothong.hochiminhcity.gov.vn:80/render/ImageHandler.ashx?id=56de42f611f398ec0c481296&t=1666752019191"]
    path_cauphumi   = ["loc03","vochicong-cauphumi","http://giaothong.hochiminhcity.gov.vn/render/ImageHandler.ashx?id=5aab1f852d266a0017e5afd4&t=1667013794895"]
    path_binhtrieu  = ["loc04","quoclo13-phamvandong","http://giaothong.hochiminhcity.gov.vn/render/ImageHandler.ashx?id=58affc6017139d0010f35cc8"]
    path_caotocLTDG = ["loc05","caotocLTDG-doxuanhop","http://giaothong.hochiminhcity.gov.vn/render/ImageHandler.ashx?id=5d9de43b766c880017188cb6&t=1667014633438"]
    path_quoclo22   = ["loc06","quoclo22-giaphai","http://giaothong.hochiminhcity.gov.vn/render/ImageHandler.ashx?id=589b4379b3bf7600110283c9"]
    path_binhphuoc  = ["loc07","quoclo13-quoclo1","http://giaothong.hochiminhcity.gov.vn/render/ImageHandler.ashx?id=5874656eb807da0011e33cde&t=1667015665586"]
    path_linhxuan   = ["loc08","khavancan-quoclo1","http://giaothong.hochiminhcity.gov.vn/render/ImageHandler.ashx?id=58746314b807da0011e33cce&t=1667015860315"]
    path_vothisau   = ["loc09","vothisau-dinhtienhoang","http://giaothong.hochiminhcity.gov.vn/render/ImageHandler.ashx?id=5a823e425058170011f6eaa4"]
    #Capture image
    capture(path_quoclo1)
    capture(path_vovankiet)
    capture(path_cauphumi)
    capture(path_binhtrieu)
    capture(path_caotocLTDG)
    capture(path_quoclo22)
    capture(path_binhphuoc)
    capture(path_linhxuan)
    capture(path_vothisau)


def capture(path):
    url = path[2]
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36"}
    #Save image
    print("Traffic captured at", time.ctime())
    k = 'data/images/02-11/' + f'{path[0]}-{time.strftime("%Y_%m_%d_%H_%M_%S")}.jpg'
    print(k)
    with open(k, 'wb') as f:
        f.write(requests.get(url, headers=headers).content)
    #Resizing image
    im = Image.open(k)
    imB = im.resize((1024,576))
    imB.save(k)

loop = 1
while True:
    print("Loop: ",loop)
    main()
    #Looping every 20 seconds
    time.sleep(20)
    loop+=1

