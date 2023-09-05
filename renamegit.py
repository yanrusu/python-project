import os


# os.chdir('') 切換位工作置，需至位於 os.listdir() 目標資料夾上層，若 .py 建檔於目標資料夾上層，則無須切換
name = os.listdir('指定資料夾') # os.listdir(type=str)

for item in name:
    if item[-4:] == '.原副檔名':  #將主檔名與副檔名切割 item[-4:]為取最後4個字 視副檔名大小切割 
        newname = item[:-4]+'.新副檔名'
        os.rename(item,newname)
        #os.rename(舊名,新名)

        
print('Finish')