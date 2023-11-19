import sys
import time
import smbus


SLAVE_ADDR = 0x5c

FUNCTION_READ = 0x03


def main ():
    i2c = smbus.SMBus(1)
    read_register = 0x00  # 読み取るレジスタアドレス
    data_num = 0x04  # データ数
    try:
        while True:
            # スリープの解除
            try:
                i2c.write_i2c_block_data(SLAVE_ADDR, 0x00, [])
            except:
                pass

            # 読み取り命令 (800μsec以上，3msec以下で要求を送信)
            time.sleep(0.002)
            i2c.write_i2c_block_data(SLAVE_ADDR, FUNCTION_READ, [read_register, data_num])

            # データ取得
            time.sleep(0.015)
            block = i2c.read_i2c_block_data(SLAVE_ADDR, read_register, data_num+4)
            humidity = float(block[2] << 8 | block[3])/10
            temperature = float(block[4] << 8 | block[5])/10

            print('温度={}℃  湿度={}%'.format(temperature, humidity))
            time.sleep(1)

    except KeyboardInterrupt:
            sys.exit(0)

 
if __name__ == '__main__':
    main()
