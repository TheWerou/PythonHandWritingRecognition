from HandWritingRecognition.toolfornetwork.CSV_to_IMG import csv_2_img

print("Proces może potrawć do 30 min kontynułować ? Y/n ")
a = input()
if a != "N" or a != "n":
    csvFilePath = "C:/Users/wojte/OneDrive/Pulpit/Programowanie/Python/ZSI/Data/CSV_do_uczenia/A_Z Handwritten Data.csv"
    pathToImgFolder = "C:/Users/wojte/OneDrive/Pulpit/Programowanie/Python/ZSI/Data/Obrazki_do_uczenia"

    csv_2_img(csvFilePath, pathToImgFolder)

