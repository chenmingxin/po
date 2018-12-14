import os


class ReadTxt():
    def __init__(self,filename):
        # self.filename = os.getcwd()+os.sep+"data"+os.sep+filename
        self.filename = filename

    def readtxt(self):
        with open(self.filename,"r",encoding="utf-8") as f:
            a = list()
            for i in f:
                a.append(tuple(i.split()))
            # return a
            print(a)


if __name__ == '__main__':
    ReadTxt("../data/data_login.txt").readtxt()