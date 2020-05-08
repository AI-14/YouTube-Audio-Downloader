__author__ = 'Amaan Izhar'
"""
    BACK-END:
    This is the logic behind YAD-YouTube Audio Downloader. Here we connect signals-slots and perform necessary operations
    needed to download an audio from YouTube in the best bitrate available.
"""

from PyQt5 import QtWidgets as qtw
from PyQt5.QtWidgets import QFileDialog
from mainUi import Ui_MainWindow
from pytube import YouTube
import sys

class MainWindowFunctionality(qtw.QMainWindow):
    def __init__(self):
        """
            Method to initialize all instance variables and connect signals-slots.
        """
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.dest_path = ''
        self.link = ''
        self.yt = None
        self.videos = []
        self.ui.list_widget.addItem('Video Titles: ')
        self.ui.destination_button.clicked.connect(self.select_destination_folder)
        self.ui.add_list_button.clicked.connect(self.add_link_to_list)
        self.ui.download_button.clicked.connect(self.download_videos)
        self.ui.clear_list_button.clicked.connect(self.clear_list)

    def select_destination_folder(self):
        """
           Method to store the path of the destination folder where all the downloaded audios will be saved.
        """
        try:
            self.dest_path = QFileDialog.getExistingDirectory(self, 'Choose Folder')
            if self.dest_path == '': # A case where no destination folder is selected and an appropriate message to display.
                msg_not_selected = qtw.QMessageBox()
                msg_not_selected.setWindowTitle('Error')
                msg_not_selected.setIcon(qtw.QMessageBox.Critical)
                msg_not_selected.setText('Destination folder not selected.')
                msg_not_selected.setStandardButtons(qtw.QMessageBox.Ok)
                msg_not_selected.exec_()
            else: # Appropriate message for successful selection of the destination folder.
                msg_selected = qtw.QMessageBox()
                msg_selected.setWindowTitle('Information')
                msg_selected.setIcon(qtw.QMessageBox.Information)
                msg_selected.setText('Destination folder successfully selected.')
                msg_selected.setStandardButtons(qtw.QMessageBox.Ok)
                msg_selected.exec_()
        except Exception: # Displaying an appropriate message in case of an exception.
            error_msg = qtw.QMessageBox()
            error_msg.setWindowTitle('Error')
            error_msg.setIcon(qtw.QMessageBox.Critical)
            error_msg.setText('An error occurred. Please try again.')
            error_msg.exec_()

    def add_link_to_list(self):
        """
            Method to add the video titles of the links in the list widget.
        """
        try:
            self.link = self.ui.input_text.text()       # Getting the link from the text box.
            self.yt = YouTube(self.link)                # Fetching the link's attributes.
            video_title = self.yt.title
            while 'YouTube.' in video_title: # Sometimes the title has only 'YouTube' in it. Therefore we keep looping till the actual title is fetched.
                self.yt = YouTube(self.link)
                video_title = self.yt.title

            self.videos.append(self.yt)
            self.ui.list_widget.addItem(video_title)    #Adding the link's title in the list widget.
            self.ui.input_text.clear()
        except Exception: # Displaying an appropriate message in case of an exception.
            error_msg = qtw.QMessageBox()
            error_msg.setWindowTitle('Error')
            error_msg.setIcon(qtw.QMessageBox.Critical)
            error_msg.setText('Invalid link! Try again.')
            error_msg.exec_()
            self.ui.input_text.clear()

    def download_videos(self):
        """
            Method for downloading the video in the best available quality (based on audio bitrate).
        """
        if len(self.videos) == 0 or len(self.dest_path) == 0:
            msg_empty_list = qtw.QMessageBox()
            msg_empty_list.setWindowTitle('Information')
            msg_empty_list.setIcon(qtw.QMessageBox.Information)
            msg_empty_list.setText('List is empty or destination folder is not selected!')
            msg_empty_list.setStandardButtons(qtw.QMessageBox.Ok)
            msg_empty_list.exec_()
        else:
            # Here we are getting the the audio formats based on their [abr] attribute. Normally it ranges from 128kbps-160kbps.
            # Also, the downloaded audio can be a .mp4 or a .webm file because we are specifically getting maximum kbps value.
            try:
                for item in self.videos:
                    vid_formats = item.streams.filter(only_audio=True)
                    kbps_val = []
                    for option in vid_formats:
                        # In the next 3 lines , we are extracting the kbps value.
                        start_index = str(option).index('abr="') + 5
                        end_index = str(option).index('kbps"')
                        audio_quality = str(option)[start_index:end_index]
                        kbps_val.append(int(audio_quality))

                    max_quality = str(max(kbps_val))      # getting the maximum kbps value.
                    value_to_check = 'abr="' + max_quality + 'kbps"'
                    for i, item in enumerate(vid_formats):
                        if value_to_check in str(item):
                            audio_to_download = vid_formats[i]
                            audio_to_download.download(self.dest_path)      # downloading the audio and saving it in the destination folder.

                msg_dwnld_success = qtw.QMessageBox()
                msg_dwnld_success.setWindowTitle('Information')
                msg_dwnld_success.setIcon(qtw.QMessageBox.Information)
                msg_dwnld_success.setText('Successfully downloaded!')
                msg_dwnld_success.setStandardButtons(qtw.QMessageBox.Ok)
                msg_dwnld_success.exec_()

                self.clear_list()

            except Exception: # Displaying an appropriate message in case of an exception.
                error_msg = qtw.QMessageBox()
                error_msg.setWindowTitle('Error')
                error_msg.setIcon(qtw.QMessageBox.Critical)
                error_msg.setText('An error occurred while downloading! Try again.')
                error_msg.exec_()


    def clear_list(self):
        """:
            Method to clear the list widget.
        """
        self.videos.clear()
        self.ui.list_widget.clear()
        self.ui.list_widget.addItem('Video Titles: ')

# STARTING THE APPLICATION
if __name__ == '__main__':
    app = qtw.QApplication([])
    win = MainWindowFunctionality()
    win.show()
    sys.exit(app.exec_())
