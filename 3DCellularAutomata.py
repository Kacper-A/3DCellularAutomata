import threading
import random
import pyray as pr


pr.init_window(1280, 720, "3D Cellular Automata")




rozmiar = 10
restart = False
RozmiarPlus = False
RozmiarMinus = False

camera = pr.Camera3D([rozmiar *2, rozmiar *2, rozmiar *2], [0.0, 1.8, 0.0], [0.0, 1.0, 0.0], 60.0, 0)
pr.set_camera_mode(camera, pr.CAMERA_ORBITAL)
pr.set_target_fps(60)

AktualnaTablica = [[[0 for k in range(rozmiar)] for j in range(rozmiar)] for i in range(rozmiar)]
KolejnaTablica = [[[0 for k in range(rozmiar)] for j in range(rozmiar)] for i in range(rozmiar)]
CzasPomiedzyTurami = 1.0
CzyGra = False
Kolor = True
Grayscale = 255
EditMode = False
EditX = 0
EditY = 0
EditZ = 0
EditXplus = False
EditXminus = False
EditYplus = False
EditYminus = False
EditZplus = False
EditZminus = False
zapelnienie = 10

def LosoweUstawianie():
    for x in range(0,rozmiar):
        for y in range(0,rozmiar):
            for z in range(0,rozmiar):
                AktualnaTablica[x][y][z] = (random.randint(1,100)%zapelnienie)

def IleZywychKomorekWokol(x,y,z):
    licznik = 0
    #26 przypadkow
    if(x<(rozmiar-1)):
        if(AktualnaTablica[x+1][y][z]==1):
            licznik +=1
    if(x<(rozmiar-1) and z<(rozmiar-1)):
        if(AktualnaTablica[x+1][y][z+1]==1):
            licznik +=1
    if(x<(rozmiar-1) and z>0):
        if(AktualnaTablica[x+1][y][z-1]==1):
            licznik +=1
    if(x<(rozmiar-1) and y<(rozmiar-1)):
        if(AktualnaTablica[x+1][y+1][z]==1):
            licznik +=1
    if(x<(rozmiar-1) and y<(rozmiar-1) and z<(rozmiar-1)):
        if(AktualnaTablica[x+1][y+1][z+1]==1):
            licznik +=1
    if(x<(rozmiar-1) and y<(rozmiar-1) and z>0):
        if(AktualnaTablica[x+1][y+1][z-1]==1):
            licznik +=1
    if(x<(rozmiar-1) and y>0):
        if(AktualnaTablica[x+1][y-1][z]==1):
            licznik +=1
    if(x<(rozmiar-1) and y>0 and z<(rozmiar-1)):
        if(AktualnaTablica[x+1][y-1][z+1]==1):
            licznik +=1
    if(x<(rozmiar-1) and y>0 and z>0):
        if(AktualnaTablica[x+1][y-1][z-1]==1):
            licznik +=1
    #wszystkie dla x+1 sa powyzej
    if(z<(rozmiar-1)):
        if(AktualnaTablica[x][y][z+1]==1):
            licznik +=1
    if(z>0):
        if(AktualnaTablica[x][y][z-1]==1):
            licznik +=1
    if(y<(rozmiar-1)):
        if(AktualnaTablica[x][y+1][z]==1):
            licznik +=1
    if(y<(rozmiar-1) and z<(rozmiar-1)):
        if(AktualnaTablica[x][y+1][z+1]==1):
            licznik +=1
    if(y<(rozmiar-1) and z>0):
        if(AktualnaTablica[x][y+1][z-1]==1):
            licznik +=1
    if(y>0):
        if(AktualnaTablica[x][y-1][z]==1):
            licznik +=1
    if(y>0 and z<(rozmiar-1)):
        if(AktualnaTablica[x][y-1][z+1]==1):
            licznik +=1
    if(y>0 and z>0):
        if(AktualnaTablica[x][y-1][z-1]==1):
            licznik +=1
    #wszystkie dla x+0 sa powyzej
    if(x>0):
        if(AktualnaTablica[x-1][y][z]==1):
            licznik +=1
    if(x>0 and z<(rozmiar-1)):
        if(AktualnaTablica[x-1][y][z+1]==1):
            licznik +=1
    if(x>0 and z>0):
        if(AktualnaTablica[x-1][y][z-1]==1):
            licznik +=1
    if(x>0 and y<(rozmiar-1)):
        if(AktualnaTablica[x-1][y+1][z]==1):
            licznik +=1
    if(x>0 and y<(rozmiar-1) and z<(rozmiar-1)):
        if(AktualnaTablica[x-1][y+1][z+1]==1):
            licznik +=1
    if(x>0 and y<(rozmiar-1) and z>0):
        if(AktualnaTablica[x-1][y+1][z-1]==1):
            licznik +=1
    if(x>0 and y>0):
        if(AktualnaTablica[x-1][y-1][z]==1):
            licznik +=1
    if(x>0 and y>0 and z<(rozmiar-1)):
        if(AktualnaTablica[x-1][y-1][z+1]==1):
            licznik +=1
    if(x>0 and y>0 and z>0):
        if(AktualnaTablica[x-1][y-1][z-1]==1):
            licznik +=1
    return licznik

def KolejnaTura():
    threading.Timer(CzasPomiedzyTurami, KolejnaTura).start()
    if(CzyGra):
        for x in range(0,rozmiar):
            for y in range(0,rozmiar):
                for z in range(0,rozmiar):
                    temp = IleZywychKomorekWokol(x,y,z)
                    if (temp < progUmierania):
                        KolejnaTablica[x][y][z] = 0
                    elif(temp >=progOzywania and temp <=progPrzezywania):
                        KolejnaTablica[x][y][z] = 1
                    elif(temp>progPrzezywania):
                        KolejnaTablica[x][y][z] = 0
                    else:
                        KolejnaTablica[x][y][z] = AktualnaTablica[x][y][z]

        for x in range(0,rozmiar):
            for y in range(0,rozmiar):
                for z in range(0,rozmiar):
                    AktualnaTablica[x][y][z] = KolejnaTablica[x][y][z]
    

progUmierania=3 # jezeli bedzie mniej niz tyle komorek wokol komurki, komurka umiera
progPrzezywania=10 # jezeli bedzie mniej niz tyle komurek, komurka zachowa swoj stan, jezeli wiecej umze
progOzywania = 7 # jezeli bedznie mial w granicy od progu Orzywania do proguPrzezywania, komurka staje sie zywa
LosoweUstawianie()
KolejnaTura()
while not pr.window_should_close():
    pr.update_camera(camera)
    pr.begin_drawing()
    pr.clear_background(pr.RAYWHITE)
    pr.begin_mode_3d(camera)
    
    
    for x in range(0,rozmiar):
        for y in range(0,rozmiar):
            for z in range(0,rozmiar):
                if(AktualnaTablica[x][y][z]==1):
                    pr.draw_cube(pr.Vector3((-rozmiar)/2+x,(-rozmiar)/2+y,(-rozmiar)/2+z,),1.0,1.0,1.0,pr.Color(int(255*(x/rozmiar)*Kolor + Grayscale*(not Kolor)),int(255*(y/rozmiar)*Kolor + Grayscale*(not Kolor)),int(255*(z/rozmiar)*Kolor + Grayscale*(not Kolor)),255 - 200*EditMode))
                    pr.draw_cube_wires(pr.Vector3((-rozmiar)/2+x,(-rozmiar)/2+y,(-rozmiar)/2+z,),1.0,1.0,1.0,pr.BLACK)
    
    if(EditMode == True):
        pr.draw_cube_wires(pr.Vector3(-0.5,-0.5,-0.5),rozmiar,rozmiar,rozmiar,pr.RED)
        pr.draw_cube(pr.Vector3((-rozmiar)/2+EditX,(-rozmiar)/2+EditY,(-rozmiar)/2+EditZ,),1.0,1.0,1.0,pr.Color(255,0,0,255))

    

    
    
    
    

    pr.end_mode_3d()
    #rysowanie po ekranie ponizej
    pr.draw_fps(10,10)
    CzasPomiedzyTurami = pr.gui_slider_bar(pr.Rectangle(20,50,120,20),"","CzasPomiedzyTurami",CzasPomiedzyTurami,0,2)
    CzyGra = pr.gui_check_box(pr.Rectangle(20,80,20,20),"CzyGra",CzyGra)
    RozmiarPlus = pr.gui_button(pr.Rectangle(20,110,120,20),"rozmiar +1")
    RozmiarMinus = pr.gui_button(pr.Rectangle(20,135,120,20),"rozmiar -1")
    restart = pr.gui_button(pr.Rectangle(20,160,120,20),"restart")
    Kolor = pr.gui_check_box(pr.Rectangle(20,190,20,20),"Kolor",Kolor)
    Grayscale = pr.gui_slider_bar(pr.Rectangle(20,220,120,20),"","Grayscale",Grayscale,0,255)
    EditMode = pr.gui_check_box(pr.Rectangle(20,250,20,20),"EditMode",EditMode)

    if(pr.gui_button(pr.Rectangle(1150,20,120,20),"5%zapelnieniania")):
        zapelnienie = 20
        LosoweUstawianie()
    if(pr.gui_button(pr.Rectangle(1150,50,120,20),"10%zapelnieniania")):
        zapelnienie = 10
        LosoweUstawianie()
    if(pr.gui_button(pr.Rectangle(1150,80,120,20),"20%zapelnieniania")):
        zapelnienie = 5
        LosoweUstawianie()
    if(pr.gui_button(pr.Rectangle(1150,110,120,20),"50%zapelnieniania")):
        zapelnienie = 2
        LosoweUstawianie()

    if(EditMode == True):
        CzyGra = False
        pr.draw_cube(pr.Vector3((-rozmiar)/2+EditX,(-rozmiar)/2+EditY,(-rozmiar)/2+EditZ,),1.0,1.0,1.0,pr.Color(255,0,0,0))
        EditXplus = pr.gui_button(pr.Rectangle(20,280,60,20),"EditX+1")
        if(EditXplus==True):
            if(EditX<rozmiar-1):
                EditX+=1
            else:
                editX=rozmiar-1
            EditXplus = False
        EditXminus = pr.gui_button(pr.Rectangle(90,280,60,20),"EditX-1")
        if(EditXminus==True):
            if(EditX>0):
                EditX-=1
            EditXminus = False
        EditYplus = pr.gui_button(pr.Rectangle(20,310,60,20),"EditY+1")
        if(EditYplus==True):
            if(EditY<rozmiar-1):
                EditY+=1
            else:
                editY=rozmiar-1
            EditYplus = False
        EditYminus = pr.gui_button(pr.Rectangle(90,310,60,20),"EditY-1")
        if(EditYminus==True):
            if(EditY>0):
                EditY-=1
            EditYminus = False
        EditZplus = pr.gui_button(pr.Rectangle(20,340,60,20),"EditZ+1")
        if(EditZplus==True):
            if(EditZ<rozmiar-1):
                EditZ+=1
            else:
                editZ=rozmiar-1
            EditZplus = False
        EditZminus = pr.gui_button(pr.Rectangle(90,340,60,20),"EditZ-1")
        if(EditZminus==True):
            if(EditZ>0):
                EditZ-=1
            EditZminus = False
        if(pr.gui_button(pr.Rectangle(20,370,60,20),"Ozyw")): 
            if(EditX<rozmiar and EditY<rozmiar and EditZ<rozmiar):
                AktualnaTablica[EditX][EditY][EditZ]=1
        if(pr.gui_button(pr.Rectangle(90,370,60,20),"Zabij")): 
            if(EditX<rozmiar and EditY<rozmiar and EditZ<rozmiar):
                AktualnaTablica[EditX][EditY][EditZ]=0
        if(pr.gui_button(pr.Rectangle(20,400,130,20),"Wyczysc Plansze")):
            for x in range(0,rozmiar):
                for y in range(0,rozmiar):
                    for z in range(0,rozmiar):
                        AktualnaTablica[x][y][z]=0
    if(restart == True):
        restart = False
        LosoweUstawianie()

    if(RozmiarMinus == True):
        if(rozmiar >5):
            rozmiar -=1
            AktualnaTablica = [[[0 for k in range(rozmiar)] for j in range(rozmiar)] for i in range(rozmiar)]
            KolejnaTablica = [[[0 for k in range(rozmiar)] for j in range(rozmiar)] for i in range(rozmiar)]
            camera = pr.Camera3D([rozmiar *2, rozmiar *2, rozmiar *2], [0.0, 1.8, 0.0], [0.0, 1.0, 0.0], 60.0, 0)
            pr.set_camera_mode(camera, pr.CAMERA_ORBITAL)
            LosoweUstawianie()

    if(RozmiarPlus == True):
        rozmiar +=1
        AktualnaTablica = [[[0 for k in range(rozmiar)] for j in range(rozmiar)] for i in range(rozmiar)]
        KolejnaTablica = [[[0 for k in range(rozmiar)] for j in range(rozmiar)] for i in range(rozmiar)]
        camera = pr.Camera3D([rozmiar *2, rozmiar *2, rozmiar *2], [0.0, 1.8, 0.0], [0.0, 1.0, 0.0], 60.0, 0)
        pr.set_camera_mode(camera, pr.CAMERA_ORBITAL)
        LosoweUstawianie()

    
    
    
    pr.end_drawing()
    
pr.close_window()