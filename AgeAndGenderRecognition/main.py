# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import tensorflow as tf
import os

def prepareFolds():
    for i in range(5):
        files_labels = []
        file = open('data/folds/fold_'+str(i)+'.txt', 'w')
        for l in tf.gfile.FastGFile(
            'data/orginal_folds/fold_'+str(i)+'_data.txt', 'r').readlines()[1:]:
            if len(l.strip().split('\t')[3].replace(" ", ""))>4:
                file.write(l.strip().split('\t')[0]+"/"+l.strip().split('\t')[1].split(".")[0] + " " + l.strip().split('\t')[3].replace(" ", "")+"\n")

        file.close()

def prepareDataNames(mypath):
    dirs = [f for f in os.listdir(mypath) if os.path.isdir(os.path.join(mypath, f))]
    print(dirs)
    for dir in dirs:
        onlyfiles = [mypath+"/"+dir+"/"+f for f in os.listdir(mypath+"/"+dir) if os.path.isfile(os.path.join(mypath+"/"+dir, f))]
        onlyfilesNew = [f.replace("landmark_aligned_face", "").split(".")[0]+f.replace("landmark_aligned_face", "").split(".")[2] for f in onlyfiles]

        for i in range(len(onlyfiles)):
            os.rename(onlyfiles[i], onlyfilesNew[i])



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #prepareDataNames("data/images/aligned")
    #print(os.path.isfile("/home/adrian/Dokumenty/Pracownia/Projekt/data/images/aligned/113830953@N04/11855531166_90b5b3670d_o"))
    prepareFolds()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
