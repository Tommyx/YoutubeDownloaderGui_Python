'''
Created on 07.08.2019

@author: Thomas
'''
import youtube_dl, os, sys

from PySide              import QtCore 
from PySide.QtCore       import QPoint
from PySide.QtGui        import QFileDialog, QMessageBox
from PySide.QtGui        import QIcon
from PySide.QtGui        import QMainWindow
from PySide.QtGui import QApplication

from UiLoader           import UiLoader
import shutil

class Window(QMainWindow):
    
    
    def __init__(self):
        apply(QMainWindow.__init__, (self,))
        self.ico                = QIcon()
        self.offset             = QPoint()
        self.appdir             = os.path.abspath(os.curdir)        
        loader                  = UiLoader(self)
        self.desktop_path        = os.path.join(os.path.expanduser('~'), 'Desktop')                        
        uifile              = os.path.join(self.appdir,'gui.ui')
        self.ui             = loader.loadUi(uifile, self)
       
        #self.setAttribute(Qt.WA_TranslucentBackground)
        #self.setWindowFlags(Qt.FramelessWindowHint)  
           
        self.connect(self.ui.btn_convert,       QtCore.SIGNAL('clicked()')  ,self.buttonclicked_btn_convert)
        self.connect(self.ui.btn_dest,          QtCore.SIGNAL('clicked()')  ,self.buttonclicked_btn_dest)
        self.connect(self.ui.btn_close,         QtCore.SIGNAL('clicked()')  ,self.buttonclicked_btn_close)
        
        self.ico.addFile(os.path.join(self.appdir,"icon.png")) 
        self.setWindowTitle("Youtube Downloader")
        self.setWindowIcon(self.ico)
        self.show()
        
    def buttonclicked_btn_close(self):
        self.close()
        self.console_gui.close()
        sys.exit()
    
    def buttonclicked_btn_convert(self):
        if (self.ui.textfield_dest.text() != "" and self.ui.textfield_url.text() != "" ) :
            
            qualily = self.ui.cbx_quality.currentText()
            
            if not (self.ui.chk_video.isChecked()):
                ydl_opts = { 'format':qualily+'audio',
                             'outtmpl': self.ui.textfield_dest.text()+".mp3"
                     }
            else :
               
                ydl_opts = { 'format': qualily,
                             'outtmpl': self.ui.textfield_dest.text()+".mp4"
                           }
            ydl = youtube_dl.YoutubeDL(ydl_opts)
            ydl.download([self.ui.textfield_url.text()])
                
            QMessageBox.information(self,"Information","Finished" )
        else : 
            QMessageBox.information(self,"Information","Set a path and url !" )
             
    def buttonclicked_btn_dest(self):
        self.file = QFileDialog.getSaveFileName(self,"Give a Name", self.desktop_path)
        self.ui.textfield_dest.setText(self.file[0])
        
def main(args):
    app                     =   QApplication(args)
    win                     =   Window()
    app.setApplicationName("Youtube Downloader")
    win.setWindowTitle("Youtube Downloader")
    
    win.show()
    app.exec_()

if __name__=="__main__":
    main(sys.argv)
    
    
        
        