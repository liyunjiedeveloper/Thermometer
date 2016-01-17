from ReadTempThread import ReadTempThread

if __name__ == "__main__":
    thrad = ReadTempThread(0, 10)
    thrad.start()