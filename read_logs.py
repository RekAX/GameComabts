# -*- coding: utf-8 -*-
__author__ = 'Ilkin Zeynalov   contacs :ilkin.zeynalovich@gmail.com'

'''This project create for read cashin logs and see pictures.
our company terminal write logs day ahead for that I write this code one day ahead'''



import os
import time
from tqdm import tqdm
import threading
import shutil
from shutil import copyfile
from removepic import del_pic

'''Number terminal ,date and Account number!'''
con = input('Cashin nomre: ')
daxil_gun = int(input("Odenish edilen gun: "))
ay = input("odenish edilen ay: ")
il = input("odenish edilen il: ")
a= 1

'''Delete all pictures in locale directories'''
pic_dir = 'C:/logs/image'
for file in os.listdir(pic_dir):
    if file.endswith('.png'):
        os.remove(file)

'''Create local list'''
cedvel = []


if daxil_gun < 9:  # if day is tiny 9
    gun ='0{}'.format(daxil_gun + a)
else:
    gun = daxil_gun + a


def copy ():
    '''With threads copy currently file. if code give any error day ahead we can as see'''
    try:
        copy = copyfile('//cash' + con + '/CashIn/log/CashInTerminalWpf_debug_{}-{}-{}_00000.txt'.format(gun, ay, il),
                        'C:/logs/terminal.txt')
        print(threading.current_thread().getName(), 'is Exiting')  #For notification exiting copy


    except FileNotFoundError:


        copy = copyfile('//cash' + con + '/CashIn/log/CashInTerminalWpf_debug.txt',
                        'C:/logs/terminal.txt')
        print(threading.current_thread().getName(), 'is Exiting') #For notification exiting copy

def bar():
    for i in tqdm(range(100)):   # progress bar

        time.sleep(0.05)
    time.sleep(0.01)
    emeliyyat()


"""Start treading bar and copy"""
tre1 = threading.Thread(target=bar,name='bar')
tre2 = threading.Thread(target=copy,name='copy')


tre1.start()
tre2.start()



'''Copy All picture when payment is stacked'''
def pic(con,il,ay,gun,saat,deq,san):

    if daxil_gun < 9:
        gun = '0{}'.format(daxil_gun)
    else:
        gun = daxil_gun


    if int(san) < 4:
        deq = int(deq) - 1
        san = int(san) + 60 - 4
        if int(deq) < 9:
            deq = '0{}'.format(deq)
    else:
        san = int(san) - 4 # or int(san) - 3

    if san == 60:
        san = '00'
        deq = deq+1
        if deq == 60:
            saat = saat + 1



    line = [int(san) - 1, int(san), int(san) + 1] #add list second when stacked and +1 second -1 second


    for a in line:
        if a < 10:    # if second tiny 10 write 0 before second
            a = '0{}'.format(a)
            print('oldu = ',a)

        if a == 60:   # if second is 60 append 1 minute and second equal 00
            a = '00'
            deq = deq + 1
            if deq == 60:
                saat = saat + 1
        mydir = '//cash' + con + '/images/{}{}{}/'.format(il, ay, gun)   # add temrinal directory when we can copy pictures



        for file in os.listdir(mydir) : # append to cycle all files in directory

            if file.startswith('{}{}{}_'.format(saat,deq,a)) and file.endswith('_{}_bottom.jpg'.format(con)): #all files when startend stacked date and ended .jpg
                print('copyfile{}{}{}'.format(saat, deq, a))
                time.sleep(0.001)
            #print(mydir+file)
                copydir = mydir+file
                shutil.copy2(copydir, 'C:/logs/image/terminalloadpic{}{}{}.jpg'.format(saat, deq, a)) #copy all pictures local directory
          #      print(copydir, 'C:/logs/image/terminalloadpic{}{}{}.jpg'.format(saat, deq, a))


'''All process '''
def emeliyyat():
    del_pic() # delete all old pictures
    cek = 'CashInTerminalWpf.PagePaySuccess.PrintDocumentOnPrintPage -'
    sonmek = 'CashInTerminalWpf.MainWindow.DoClose - LogFilesCheckerThread'
    ilishme = 'CashInTerminalWpf.PageMoneyInput.CcnetDeviceOnReadCommand - State: JamInAcceptor'
    transID = 'CashInTerminalWpf.PageMoneyInput.InitLocalDbAndInsertPaymentValues - Starting transId:'
    Input_Text = 'CashInTerminalWpf.PageMoneyInput.CcnetDeviceOnBillStacked - Stacked'
    pasport = "Pasport №:"
    Code = input("Search personal code ==> :")
    hesab = 'Hesab nömrəsi: ' + Code
    abonent = 'Abonent code: ' + Code
    accoount = 'AccountNo: ' + Code
    pul_kocurme = ',Qəbul edən şəxsin mobil nömrəsi: ' + Code
    counter =1



    with open("C:/logs/terminal.txt",encoding='utf-8') as file: #open log file and reading

        lines = file.readlines() # append reading file to list
        for h in lines:  # search in list key sentences
            #if hesab in h or abonent in h or accoount in h:
            if hesab in h or abonent in h or accoount in h or pul_kocurme in h:

                print(h)
                for w in lines[counter:]:
                    if transID in w:                                    #find tranjaction id
                        print(w[:14],w[96:127])                         #show datatime and tansaction id
                    if Input_Text in w:                                 # find all stacked pay
                        cedvel.append(w[6:14])                          #apend list all stacked pay
                        print(w[:14],w[85:].replace('\n', ''))          #show datatime and delete backspace
                    if cek in w:                                        #print chek
                        print(w[85:].replace('\n', ''))                 #show datatime and delete backspace
                    if sonmek in w :                                    # find shuthdown error code
                        print('Texniki nasazlıq - Terminal Sönüb')      #show error type
                        exit()                                          #if terminal is shutdown exit code
                    if ilishme in w:                                    #find when pay is jammed
                        print(w[:14].replace('\n', ''),'- Caşında  ilişmə olub!!!') #show datatime and delete backspace
                    if pasport in w:                                    # end person session when created new pasport number
                        break                                           # find shuthdown error code



            counter=counter+1                   # plus 1 to cycle 
    for a in cedvel:                

        saat = a[:2]                            #stack hour
        deq = a[3:5]                            #stack minute
        san = a[6:8]                            #stacl second


        '''Run copy pictures with progres bar'''
        tre4 = threading.Thread(target=pic(con,il,ay,gun,saat,deq,san), name="progress")
        tre5 = threading.Thread(target=bar_pic(), name='bar')
        tre4.start()
        tre5.start()

def bar_pic():
    for i in tqdm(range(100)):
        time.sleep(0.01)
    time.sleep(0.01)
