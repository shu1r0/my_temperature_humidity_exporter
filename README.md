# ラズパイから温度と湿度を取得するExporter (Flask+uWSGI+ngix)

## SetUp

Install pkg
```
sudo apt install -y python3-pip
sudo apt install -y i2c-tools
sudo apt install -y python3-smbus
```

Get I2C module address.

```
shu1r0@raspi3node1:~/workspace$ i2cdetect -l
i2c-1   i2c             bcm2835 (i2c@7e804000)                  I2C adapter
shu1r0@raspi3node1:~/workspace$ sudo i2cdetect -y 1
     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
00:                         -- -- -- -- -- -- -- -- 
10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
50: -- -- -- -- -- -- -- -- -- -- -- -- 5c -- -- -- 
60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
70: -- -- -- -- -- -- -- --       
```

## Run

```
pip3 install -r requirements.txt
nohup python3 capture_exporter.py &
```

## 参考文献
- https://qiita.com/74th/items/e8dc1ac1295140413dc8


