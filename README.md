### Hi there, welcome to our project 👋: 
## Collect and Graph Traffic flow through public CCTV in Ho Chi Minh City. 📸📹

The idea of this project is to collect data from [public CCTV provided by the Department of Transportation in HCMC][CCTV] and analyze the statistics collected. We achieved this through a multiple processes, mainly involve utilizing *Yolov5 AI* vision and Python *tkinter* interface. Detailed report about our project is linked [here][report]. 📖📖📖

---

## How to use

To check out our project, install the  [Github][github] of this project and run the ***main.py***. It will open a window as shown here:<br />
![Traffic App](/traffic/app.png "Traffic App")<br /> When the *Graph* button is clicked, the app will draw a chart of the traffic at the selected location and date with a mini analysis of the data beside.<br/>📅

If you wish to see the realtime data, you need to collect it first. To do it, run the ***trafficCapture.py*** file in the folder *module* (remember to change your saved location). After collected the data you want, you need to detect it using ***detect.py*** with the following command in the terminal (assumming you store the at data/images/folder):
```
python detect.py --source data/images/folder
```
The final step is to copy that detected file (*.txt* format, stored in runs/detect/exp...) into the *traffic* folder. Hurray, now you can see the result in **Traffic App**. Opening the app by simply running ***main.py***.
</details>

[CCTV]: http://giaothong.hochiminhcity.gov.vn/Map.aspx
[report]: https://www.overleaf.com/read/rhrsbdsrhjfy
[github]: https://github.com/phuhuynhlean/projectTraffic/

---

## Requirements

In order to run the project properly, you should download and set up some following stuffs: <br />
- Python 3.8.5 or higher;<br />
- Python library: Tkinter, Matplotlib, pandas, numpy, Pillow
<br />

Some tool for you to try reconstructing this project. See our report for more details.
- [Our Report about the project][0] <br />
- [Download Yolov5 from Github][1]<br />
- [Labelling Supporting Tool][2]<br />
- [Dataset with 81 different classes][3]<br />
- [Dataset with transportation which our group uses][4]<br />
- [Link to HCM CCTV which we use to capture][5]<br />
---
</details>

[0]: https://www.overleaf.com/read/rhrsbdsrhjfy
[1]: https://github.com/ultralytics/yolov5
[2]: https://github.com/heartexlabs/labelImg
[3]: https://www.kaggle.com/datasets/ultralytics/coco128
[4]: https://drive.google.com/drive/folders/1EuSmR0u8qjlEPFqwz8gy0GN65eyVT99m
[5]: http://giaothong.hochiminhcity.gov.vn/

<br />

### 📺 Contact us
- [Dinh Thai Duy][duydinh]
- [Huynh Le An Phu][anphu]
- [Le Thanh Hai][thanhhai]
- [Phan Tam Nhu][tamnhu]
- [Nguyen Minh Thuan][minhthuan]
- [Trinh The Hao][jsontrinh]
- [Vo Vuong Bao Huy][baohuy]

---

</details>

[thanhhai]: https://www.facebook.com/hailu03/
[duydinh]: https://www.facebook.com/haudity
[anphu]: https://www.facebook.com/anphuhlap
[tamnhu]: https://www.facebook.com/profile.php?id=100041127529583
[minhthuan]: https://www.facebook.com/lowkeynenemkhongthethay
[jsontrinh]: https://www.facebook.com/profile.php?id=100008612346891
[baohuy]: https://www.facebook.com/profile.php?id=100078422291956

