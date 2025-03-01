import requests
import pyautogui
import time
import random
from datetime import datetime
listOfPlayer = ['d', 'f', 'g', 'h', 'j', 'k', 'l']
characters = ['0', 't', 'l', '8', '9','k']
move_user = ['7', '6', '5', '4']
open_ruong = ['0', '3', '8', '6', '5', 'q'] 
day = int(datetime.now().strftime('%d'))
month = int(datetime.now().strftime('%m'))
year = int(datetime.now().strftime('%Y'))


valid = False
skipGame = 1
def checkonline():
    global valid
    last_click_time = time.time() - 60 
    online_image = 'image/online.png'
    avata_image = 'images/avata.png'
    talavua_image = 'images/talavua.png'
    talavuafull_image = 'images/talavuafull.png'
    thulai_image = 'images/thulai.png'
    location_online = find_image_on_screen(online_image)
    location_talavua = find_image_on_screen(talavua_image)
    location_thulai = find_image_on_screen(thulai_image)
    location_avata = find_image_on_screen(avata_image)
    location_talavuafull = find_image_on_screen(talavuafull_image)
    current_time = time.time()
    if location_online is not None or location_talavuafull is not None or location_avata:
        print("online_image found at:", location_online )
        print(" talavua_image found at:", location_talavua)
        print(" thulai_image found at:", location_thulai)
        print(" avata_image found at:", location_avata)
        if current_time - last_click_time >= 60:
            pyautogui.click(location_thulai)
            pyautogui.click(location_talavua)
            pyautogui.click(location_online)
            pyautogui.click(location_avata)
            last_click_time = current_time
        valid = True
def find_image_on_screen(image):
    try:
        location = pyautogui.locateOnScreen(image, confidence=0.8)
        return location
    except pyautogui.ImageNotFoundException:
        return None
def timtran(count):
    switch_key = ''
    global valid9778
    global skipGame
    # start skip
    
    if (count % 27 == 9 or count % 27 == 18) and skipGame == 1:
        print("dang skip")
        pyautogui.press('0')
        time.sleep(2)
        pyautogui.press('a')
        time.sleep(2)
        pyautogui.press('o')
        time.sleep(2)
        pyautogui.press('1')
        time.sleep(2)
    elif count % 27 == 0 and skipGame == 1:
        pyautogui.press('0')
        time.sleep(2)
        pyautogui.press('a')
        time.sleep(2)
        pyautogui.press('o')
        time.sleep(2)
        pyautogui.press('1')
        time.sleep(2)
    
    #end skip
    while True:
        print("valid", valid)
        checkonline()
        if valid == True:
            return
        home_image = 'images/home.png'
        location_timtran = find_image_on_screen(home_image)
        if location_timtran is not None:
            print("home_image found at:", location_timtran)
            pyautogui.press('1')
            time.sleep(1)
            pyautogui.press('2')
            # if count % 27 == 9 or count % 27 == 18:
            #     switch_key = 'i'
            # elif count % 27 == 0:
            #     switch_key = 'u'
            if count % 9 == 0:
                switch_key = 'u'
            elif count % 6 == 3 or count % 6 == 0:
                switch_key = 'i'
            time.sleep(1)
            if switch_key == 'i':
                pyautogui.press(switch_key)
            elif switch_key == 'u':
                pyautogui.press(switch_key)
                time.sleep(1)
                pyautogui.press(switch_key)
            pyautogui.press('3')
            break
        else:
            print("home_image not found on the screen.")
            time.sleep(3)
            pyautogui.press('2')
            time.sleep(1)
            pyautogui.press('3')
def checklistuser(): 
    global valid       
    while True:
        print("valid", valid)
        checkonline()
        if valid == True:
            return
        danhsach_image = 'images/danhsach3.png'
        danhsach_image4 = 'images/danhsach4.png'
        location_danhsach = find_image_on_screen(danhsach_image)
        locals_danhsach4 = find_image_on_screen(danhsach_image4)
        if location_danhsach is not None or locals_danhsach4 is not None:
            print("danhsach_image found at:", location_danhsach)
            break  
        else:
            print("home_image not found on the screen.")
            time.sleep(2)
            pyautogui.press('2')
            time.sleep(1)
            pyautogui.press('3')
def selectuser():
    global valid
    while True:
        print("valid", valid)
        checkonline()
        if valid == True:
            return
        tancong_image = 'images/tancong2.png'
        danhsach_image = 'images/danhsach3.png'
        danhsach_image4 = 'images/danhsach4.png'
        tancongloi  = 'images/tancongloi.png'
        location_danhsach = find_image_on_screen(danhsach_image)
        location_danhsach4 = find_image_on_screen(danhsach_image4)
        location_tancongloi = find_image_on_screen(tancongloi)
        if location_danhsach is not None or location_danhsach4 is not None:
            random_index = random.randint(0, len(listOfPlayer) - 1)
            random_key = listOfPlayer[random_index]
            pyautogui.press(random_key)
            time.sleep(0.1) 
            print("Đã tìm thấy danh sách người đánh")  
        if location_tancongloi is not None:
            print("tancongloi found at:", location_tancongloi)
            pyautogui.press('t')
            break
        location_tancong = find_image_on_screen(tancong_image) 
        if location_tancong is not None:
            print("player selected")
            pyautogui.press('t')
            pyautogui.click(location_tancong)
            print("tancong_image found at", location_tancong)
            break
        # pyautogui.press('t')         
def PlayerOnline():
    # global valid
    # print("valid", valid)
    # checkonline()
    # if valid == True:
    #     return
    pyautogui.press('m')
    time.sleep(0.5)
    pyautogui.press('n')
    selectuser()
def VaoTran():
    global valid
    trongtran_image = 'images/trongtran.png'
    boqua_image = 'images/boqua.png'
    victory_image = 'images/victory.png'
    while True:
        print("valid", valid)
        checkonline()
        if valid == True:
            return
        location_trongtran = find_image_on_screen(trongtran_image)
        location_boqua = find_image_on_screen(boqua_image)
        if location_trongtran is not None:
            print("dang trong tran", location_trongtran)
            for _ in range(4):
                pyautogui.press('b')
            for _ in range(5):  # Vì bạn có 5 ký tự
                random_char = random.choice(characters)
                ramdom_move = random.choice(move_user)
                pyautogui.press(random_char)
                pyautogui.press(ramdom_move)
                pyautogui.press(ramdom_move)
            continue
        if location_boqua is not None:
            print("da tim thay nut bo qua", location_boqua)
            pyautogui.click(location_boqua)
            print("da cham vao nut bo qua")           
            time.sleep(1)
            location_victory = find_image_on_screen(victory_image)
            if location_victory is not None:
                print("da tim thay nut tiep tuc", location_victory)
                time.sleep(1)
                pyautogui.press("t")
                pyautogui.click(location_victory)
                print("da cham vao tiep tuc")           
                break  
        print("Đang đợi để vào trận")               
def MoRuong():
    global valid
    home_image = 'images/home.png'
    thunhaptxt_image = 'images/thunhaptxt.png'
    image_files = [ 'images/khobau3.png','images/bocuoc.png','images/nung.png', 'images/chamdetieptuc.png','images/ban.png']
    while True:
        # print("valid", valid)
        # checkonline()
        # if valid == True:
        #     return
        for image_file in image_files:
            location = find_image_on_screen(image_file)
            if location is not None:
                print(f"{image_file} found at:", location)
                random_openr = random.choice(open_ruong)
                location_nung = find_image_on_screen('images/nung.png')
                if location_nung is not None:
                    pyautogui.click(location_nung)
                pyautogui.press(random_openr)
                pyautogui.click(location)
                time.sleep(1)
        location_home = find_image_on_screen(home_image)
        location_thunhaptxt = find_image_on_screen(thunhaptxt_image)
        if location_thunhaptxt is not None:
            thunhapphieu()
        if location_home is not None:
            print("home_image found at:", location_home)
            break    
def tancong():
    global valid
    chonguoichoi_image ='images/chonguoichoi.png'
    return_image ='images/hayduatoitrolai.png'
    userkhonghd_image = 'images/nguoichoikhonghoatdong.png'
    ngchoikhonghoatdong_image = 'images/ngchoikhonghoatdong.png'
    enterbattle_image ='images/vaotran.png'
    tancong_image = 'images/tancong2.png'
    moc = True
    while moc:
        print("valid", valid)
        checkonline()
        if valid == True:
            return
        location_chodoi = find_image_on_screen(chonguoichoi_image)
        location_tancong = find_image_on_screen(tancong_image)
        time.sleep(1)
        if location_tancong is not None:
            print("dang tan cong", location_tancong)
            pyautogui.click(location_tancong)
            time.sleep(0.5)
        while True:
            print("valid", valid)
            checkonline()
            if valid == True:
                return
            location_vaotran = find_image_on_screen(enterbattle_image)
            if location_tancong is not None:
                print("dang tan cong", location_tancong)
                pyautogui.press('t')
                pyautogui.click(location_tancong)     
            time.sleep(0.5)
            if location_vaotran is not None:
                print("bat dau vao tran", location_vaotran)
                moc = False
                break
            location_return = find_image_on_screen(return_image)
            if location_return is not None:
                print("tim thay : hay dua toi tro lai", location_return)
                PlayerOnline()
            location_userkhonghd = find_image_on_screen(userkhonghd_image)
            if location_userkhonghd is not None:
                print("tim thay : nguoi choi khong hoat dong", location_userkhonghd)
                userkhonghd()
            location_ngchoikhonghoatdong = find_image_on_screen(ngchoikhonghoatdong_image)
            if location_ngchoikhonghoatdong is not None:
                print("tim thay : ng choi khong hoat dong", location_ngchoikhonghoatdong)
                ngchoikhonghoatdong()
            if location_chodoi is None:
                time.sleep(1)
                pyautogui.press("t")
                pyautogui.click(location_tancong)
            print("dang cho doi nut tan cong") 
    while True:
        print("valid", valid)
        checkonline()
        if valid == True:
            return
        location_enterbattle = find_image_on_screen(enterbattle_image)
        if location_enterbattle is not None:
            print("bat dau vao tran", location_enterbattle)
            VaoTran()
            MoRuong()
            break  
        else:
            time.sleep(2)
def thunhapphieu():
    global valid
    while True:
        print("valid", valid)
        checkonline()
        if valid == True:
            return
        thunhapphieu_image = 'images/thunhapphieu.png'
        thoatthunhapphieu_image = 'images/thoatthunhapphieu.png'
        location_thunhapphieu = find_image_on_screen(thunhapphieu_image)
        location_thoatthunhapphieu = find_image_on_screen(thoatthunhapphieu_image)
        # if checkonline() == True:
        #     break
        if location_thunhapphieu is not None:
            print("thunhapphieu_image found at:", location_thunhapphieu)
            pyautogui.press('p')
            time.sleep(5)
            print("da tim thay nut thu nhan phieu")
        if location_thoatthunhapphieu is not None:
            print("thoatthunhapphieu_image found at:", location_thoatthunhapphieu)
            pyautogui.click(location_thoatthunhapphieu)
            print("da tim thay nut thoat thu nhan phieu")
            break
        time.sleep(1)        
def userkhonghd():
    global valid
    while True:
        print("valid", valid)
        checkonline()
        if valid == True:
            return
        userkhonghd_image = 'images/nguoichoikhonghoatdong.png'
        location_userkhonghd = find_image_on_screen(userkhonghd_image)
        if location_userkhonghd is not None:
            print("userkhonghd_image found at:", location_userkhonghd)
            time.sleep(0.5)
            pyautogui.press('n')
            selectuser()
            break
def ngchoikhonghoatdong():
    global valid
    while True:
        print("valid", valid)
        checkonline()
        if valid == True:
            return
        ngchoikhonghoatdong_image = 'images/ngchoikhonghoatdong.png'
        location_userkhonghd = find_image_on_screen(ngchoikhonghoatdong_image)
        if location_userkhonghd is not None:
            print("userkhonghd_image found at:", location_userkhonghd)
            time.sleep(0.5)
            pyautogui.press('n')
            selectuser()
            break
input_value = input('Nhập 1 là skip  2 là không skip (Nhấn Enter để mặc định là skip): ')
if input_value == '':
    skipGame = 1
else:
    skipGame = int(input_value)
    # nhap key
# check = input('Nhập key: ')
# key_info = requests.get('https://pastebin.com/raw/ndUWNUVf').text.split('\n')
# for key in key_info:
#     keyip = key.split('|')
#     fulltime = keyip[1].split('/')
#     if check == keyip[0]:
#         if day == int(fulltime[0]) and month == int(fulltime[1]) and year == int(fulltime[2]):
#             print('Key hết hạn')
#             exit()    
#         else:
count =  1
while True:
    while True:
        checkonline()
        print("valid", valid)
        if valid == True:
            valid = False
            break
        else:
            print(f"Đang chạy lần thứ {count}")
            tainguyen_image = 'images/tainguyen.png'
            thunhapphieu_image = 'images/thunhapphieu.png'
            thoat_lsbitancong = 'images/thoatthunhapphieu.png'
            location_thunhapphieu = find_image_on_screen(thunhapphieu_image)
            location_lsbitancong = find_image_on_screen(thoat_lsbitancong)
            if location_lsbitancong is not None:
                print("lsbitancong_image found at:", location_lsbitancong)
                pyautogui.click(location_lsbitancong)
            if location_thunhapphieu is not None:
                thunhapphieu()
            location_tainguyen = find_image_on_screen(tainguyen_image)
            print(location_tainguyen)   
            if location_tainguyen is not None:
                pyautogui.click(location_tainguyen)
                print("da tim thay nut tai nguyen")
                time.sleep(1)
                timtran(count)
                checklistuser()
                selectuser()
                tancong()
                count += 1
                valid = False
                break