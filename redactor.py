from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QListWidget, QHBoxLayout, QVBoxLayout, QFileDialog 
import os
from PIL import Image, ImageFilter
from PyQt5.QtGui import QPixmap
class ImageProcessor:
    def __init__(self):
        self.image = None
        self.dir = None
        self.fileame = None
        self.image_path = None
        self.save_dir = 'Modified/'
    def loadImage(self, dir, filename):
        self.dir = dir
        self.filename = filename
        self.image_path = os.path.join(dir, filename)
        self.image = Image.open(self.image_path)
    def showImage(self, path):
        img_lbl.hide()
        piximage = QPixmap(path)
        w, h = img_lbl.width(), img_lbl.height()
        piximage = piximage.scaled(w, h)
        img_lbl.setPixmap(piximage)
        img_lbl.show()
    def saveImage(self):
        path = os.path.join(self.dir, self.save_dir)
        if not(os.path.exists(path) or os.path.isdir(path)):
            os.mkdir(path)
        image_path = os.path.join(path, self.filename)
        self.image.save(image_path)
    def do_bw(self):
        self.image = self.image.convert('L')
        self.saveImage()
        image_path = os.path.join(self.dir, self.save_dir,self.filename)
        self.showImage(image_path)
    def miroww (self):
        self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)
        self.saveImage()
        image_path = os.path.join(self.dir, self.save_dir,self.filename)
        self.showImage(image_path)
    def left(self):
        self.image = self.image.transpose(Image.ROTATE_90)
        self.saveImage()
        image_path = os.path.join(self.dir, self.save_dir,self.filename)
        self.showImage(image_path)
    def rigt(self):
            self.image = self.image.transpose(Image.ROTATE_270)
            self.saveImage()
            image_path = os.path.join(self.dir, self.save_dir,self.filename)
            self.showImage(image_path)
    def blur(self):
        self.image = self.image.filter(ImageFilter.BLUR)
        self.saveImage()
        image_path = os.path.join(self.dir, self.save_dir,self.filename)
        self.showImage(image_path)
    def cotur(self):    
        self.image = self.image.filter(ImageFilter.CONTOUR)
        self.saveImage()
        image_path = os.path.join(self.dir, self.save_dir,self.filename)
        self.showImage(image_path)





#  Создание  приложения
app2 = QApplication([])
win2 = QWidget()
win2.resize(700, 500)
win2.setWindowTitle('Easy Editor')
# -------------------------------------
# Создание виджетов
# Кнопки
dir_btn = QPushButton('Папка')
left_btn = QPushButton('Лево')
rigt_btn = QPushButton('Право')
mirror_btn = QPushButton('Зерколо')
blur_btn = QPushButton('Блюриь')
bw_btn = QPushButton('Ч/Б')
cotur_btn = QPushButton('Контур')
#--------------------------------------
img_lbl = QLabel('Картинка')
imgs_list = QListWidget()
#-----------------------------------------
# Созданте линий
main_line = QHBoxLayout()
btns_line = QHBoxLayout()
v_line1 = QVBoxLayout()
v_line2 = QVBoxLayout()
#-------------------------------------------
#  Подключение к линиям
btns_line.addWidget(left_btn)
btns_line.addWidget(rigt_btn)
btns_line.addWidget(mirror_btn)
btns_line.addWidget(blur_btn)
btns_line.addWidget(bw_btn)
btns_line.addWidget(cotur_btn)
v_line1.addWidget(dir_btn)
v_line1.addWidget(imgs_list)
v_line2.addWidget(img_lbl)
v_line2.addLayout(btns_line)

main_line.addLayout(v_line1)
main_line.addLayout(v_line2)

win2.setLayout(main_line)
#----------------------------------------------------

# Логика
workdir = ''
workImage = ImageProcessor()
def filter(files, extensions):
    result = []
    for filename in files:
        for ext in extensions:
            if filename.endswith(ext):
                    result.append(filename)
    return result



def openFolder():
    global workdir
    extensions = ['.jpg', '.png', '.bmp', '.gif']
    workdir = QFileDialog.getExistingDirectory()
    file_list = os.listdir(workdir)
    filenames = filter(file_list, extensions)
    imgs_list.clear()
    imgs_list.addItems(filenames)

def openImage():
    filename = imgs_list.currentItem().text()
    workImage.loadImage(workdir, filename)
    workImage.showImage(workImage.image_path)


# Коннект
dir_btn.clicked.connect(openFolder)
imgs_list.itemClicked.connect(openImage)
bw_btn.clicked.connect(workImage.do_bw)
mirror_btn.clicked.connect(workImage.miroww)
left_btn.clicked.connect(workImage.left)
rigt_btn.clicked.connect(workImage.rigt)
blur_btn.clicked.connect(workImage.blur)
cotur_btn.clicked.connect(workImage.cotur)











