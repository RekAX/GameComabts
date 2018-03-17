# -*- coding: utf-8 -*-
import os
import time
from tqdm import tqdm
import threading
import shutil
from shutil import copyfile
from removepic import del_pic


con = input('Cashin nomre: ')
daxil = int(input("Odenish edilen gun: "))
ay = input("odenish edilen ay: ")
il = input("odenish edilen il: ")
a= 1

pic_dir = 'C:/logs/image'
for file in os.listdir(pic_dir):
    if file.endswith('.png'):
        os.remove(file)


cedvel = []


if daxil < 9:
    gun ='0{}'.format(daxil + a)
else:
    gun = daxil + a


def copy ():
    '''With threads copy currently file. if code give any error day + 1 we can as see'''
    try:
        print(threading.current_thread().getName(), 'is Starting')
        copy = copyfile('//cash' + con + '/CashIn/log/CashInTerminalWpf_debug_{}-{}-{}_00000.txt'.format(gun, ay, il),
                        'C:/logs/terminal.txt')

        print(threading.current_thread().getName(), 'is Exiting')

    except FileNotFoundError:

        print(threading.current_thread().getName(), 'is Starting')

        copy = copyfile('//cash' + con + '/CashIn/log/CashInTerminalWpf_debug.txt',
                        'C:/logs/terminal.txt')
        print(threading.current_thread().getName(), 'is Exiting')



def bar():
    #print(threading.current_thread().getName(), 'is Starting')
    for i in tqdm(range(100)):

        time.sleep(0.05)
    time.sleep(0.01)
    emeliyyat()
    #print(threading.current_thread().getName(), 'is Exiting')



tre1 = threading.Thread(target=bar,name='bar')
tre2 = threading.Thread(target=copy,name='copy')


tre1.start()
tre2.start()




def pic(con,il,ay,gun,saat,deq,san):
    global daxil


    #os.remove('C:/logs/image/*.jpg')
    #print(con)
    if daxil < 9:
        gun = '0{}'.format(daxil)
    else:
        gun = daxil

    #print('def - san',san)

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



    #print('san = ',san,'deq',deq,'saat= ',saat)
    line = [int(san) - 1, int(san), int(san) + 1]

    #print('line',line)

    for a in line:
        if a < 10:
            a = '0{}'.format(a)
            print('oldu = ',a)

        if a == 60:
            a = '00'
            deq = deq + 1
            if deq == 60:
                saat = saat + 1
        mydir = '//cash' + con + '/images/{}{}{}/'.format(il, ay, gun)
        #print('line a:',a)
        #print('deq = ',deq)


        for file in os.listdir(mydir) :

            if file.startswith('{}{}{}_'.format(saat,deq,a)) and file.endswith('_{}_bottom.jpg'.format(con)):
                print('copyfile{}{}{}'.format(saat, deq, a))
                time.sleep(0.001)
            #print(mydir+file)
                copydir = mydir+file
                shutil.copy2(copydir, 'C:/logs/image/terminalloadpic{}{}{}.jpg'.format(saat, deq, a))
          #      print(copydir, 'C:/logs/image/terminalloadpic{}{}{}.jpg'.format(saat, deq, a))



def emeliyyat():
    del_pic()
    global cedvel
    cek = 'CashInTerminalWpf.PagePaySuccess.PrintDocumentOnPrintPage -'
    sonmek = 'CashInTerminalWpf.MainWindow.DoClose - LogFilesCheckerThread'
    ilishme = 'CashInTerminalWpf.PageMoneyInput.CcnetDeviceOnReadCommand - State: JamInAcceptor'
    transID = 'CashInTerminalWpf.PageMoneyInput.InitLocalDbAndInsertPaymentValues - Starting transId:'
    Input_Text = 'CashInTerminalWpf.PageMoneyInput.CcnetDeviceOnBillStacked - Stacked'
   # hesab = 'Hesab nömrəsi: '+ input("search :")
    pasport = "Pasport №:"
    Code = input("Search personal code ==> :")
    hesab = 'Hesab nömrəsi: ' + Code
    abonent = 'Abonent code: ' + Code
    accoount = 'AccountNo: ' + Code
    pul_kocurme = ',Qəbul edən şəxsin mobil nömrəsi: ' + Code
    counter =1



    with open("C:/logs/terminal.txt",encoding='utf-8') as file:

        lines = file.readlines()
        for h in lines:
            #if hesab in h or abonent in h or accoount in h:
            if hesab in h or abonent in h or accoount in h or pul_kocurme in h:

                print(h)
                for w in lines[counter:]:
                    if transID in w:
                        print(w[:14],w[96:127])
                    if Input_Text in w:
                        cedvel.append(w[6:14])
                        print(w[:14],w[85:].replace('\n', ''))
                    if cek in w:
                        print(w[85:].replace('\n', ''))
                    if sonmek in w :
                        print('Texniki nasazlıq - Terminal Sönüb')
                        exit()
                    if ilishme in w:
                        print(w[:14].replace('\n', ''),'- Caşında  ilişmə olub!!!')
                    if pasport in w:
                        break



            counter=counter+1
    #global daxil
    for a in cedvel:

        saat = a[:2]
        deq = a[3:5]
        san = a[6:8]


        #print(san)
        tre4 = threading.Thread(target=pic(con,il,ay,gun,saat,deq,san), name="progress")
        tre5 = threading.Thread(target=bar_pic(), name='bar')
        tre4.start()
        tre5.start()

def bar_pic():
    # print(threading.current_thread().getName(), 'is Starting')
    for i in tqdm(range(100)):
        time.sleep(0.01)
    time.sleep(0.01)
    # print(threading.current_thread().getName(), 'is Exiting')



