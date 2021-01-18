# import sys
from sys import argv,exit
from time import sleep
import pyautogui as pag
import keyboard as kbd
from PyQt5.QtWidgets import QApplication, QMainWindow#, QLineEdit
from PyQt5 import QtCore
# from PyQt5.QtCore import QDir

from automouse_ui import *
# from multiprocessing import Process,Queue, current_process
S_signal = 1
STOP_signal = 1

class MyWindow(QMainWindow, Ui_MainWindow):
	def __init__(self, parent=None):
		super(MyWindow, self).__init__(parent)
		self.setupUi(self)
		self.lineEdit.setText('10') # Default set the time interval as 10 sec
		self.timeIntv = 10
		self.statusbar.showMessage('Click the START button to operate AutoMouse.')

		self.pushButton.clicked.connect(self.Btn_START)
		self.pushButton_2.clicked.connect(self.Btn_STOP)
		self.lineEdit.textChanged.connect(self.setTimeIntv)

		self.mousePos_t = mousePosThread()
		self.mousePos_t.Deamon = True		
		self.mousePos_t.curr_signal.connect(self.updateCurrPos)
		self.mousePos_t.start()
		self.statusbar.showMessage('>>> mousePos thread has started...')


	def updateCurrPos(self,curr):
		self.label_17.setText(str(curr[0]))
		self.label_19.setText(str(curr[1]))

	def updateLeft(self,leftPos):
		# self.leftX, self.LeftY = pag.position()
		self.label_20.setText('X: '+str(leftPos[0]))
		self.label_21.setText('Y: '+str(leftPos[1]))
		self.statusbar.showMessage('Left mouse pos | X: '+str(leftPos[0])+', '+\
			'Y: '+str(leftPos[1]))
		
	def updateRight(self,rightPos):
		# self.rightX, self.rightY = pag.position()
		self.label_13.setText('X: '+str(rightPos[0]))
		self.label_14.setText('Y: '+str(rightPos[1]))
		self.statusbar.showMessage('Right mouse pos | X: '+str(rightPos[0])+', '+\
			'Y: '+str(rightPos[1]))

	def updateStatus(self,statusMsg):
		self.statusbar.showMessage(statusMsg)

	def Btn_START(self):
		global STOP_signal
		self.label.setText('[W]')
		self.label_3.setText('S')
		STOP_signal = 0
		self.label_11.setText('<--X-->')
		self.label_12.setText('<--Y-->')
		self.keyControl_t = keyControlThread(self.timeIntv)
		self.keyControl_t.Deamon = True		
		self.keyControl_t.left_signal.connect(self.updateLeft)
		self.keyControl_t.right_signal.connect(self.updateRight)
		self.keyControl_t.status_signal.connect(self.updateStatus)

		self.stop_t = stopThread()
		self.stop_t.Deamon = True
		self.stop_t.status_signal.connect(self.updateStatus)

		self.keyControl_t.start()
		self.stop_t.start()
		self.statusbar.showMessage('>>> keyControl thread has started...')
		
	def Btn_STOP(self):
		global STOP_signal
		self.label.setText('W')
		self.label_3.setText('[S]')
		STOP_signal = 1
		try:
			self.keyControl_t.left_signal.disconnect(self.updateLeft)
			self.keyControl_t.right_signal.disconnect(self.updateRight)
			self.keyControl_t.status_signal.disconnect(self.updateStatus)
			self.keyControl_t.quit()
			self.label_11.setText('|  X  |')
			self.label_12.setText('|  Y  |')
			self.stop_t.status_signal.disconnect(self.updateStatus)
			self.stop_t.quit()
			self.statusbar.showMessage('>>> keyControl thread has quitted...')
		except Exception:
			self.statusbar.showMessage('[Warning] keyControl thread fails to quit...')

	def setTimeIntv(self):
		try:
			self.timeIntv = float(self.lineEdit.text())
			self.statusbar.showMessage('>>> Time interval set to '+str(self.timeIntv)+' sec.')
		except:
			self.statusbar.showMessage('#000# Invalid time interval!')

	def closeEvent(self,event):
		global STOP_signal
		STOP_signal = 1
		print('You chose to exit the program!')
		try:
			self.mousePos_t.curr_signal.disconnect(self.updateCurrPos)
			self.mousePos_t.quit()
			self.label_17.setText('--')
			self.label_19.setText('--')
			self.statusbar.showMessage('>>> mousePos thread has quitted...')
		except Exception:
			self.statusbar.showMessage('[Warning] mousePos thread fails to quit...')

		self.close()

class mousePosThread(QtCore.QThread):
	curr_signal = QtCore.pyqtSignal(list)

	def __init__(self):
		super(mousePosThread, self).__init__()

	def __del__(self):
		self.wait()

	def run(self):
		while True:
			sleep(0.01)
			currX, currY = pag.position()
			self.curr_signal.emit([currX,currY])


class keyControlThread(QtCore.QThread):
	left_signal = QtCore.pyqtSignal(list)
	right_signal = QtCore.pyqtSignal(list)
	status_signal = QtCore.pyqtSignal(str)
	"""docstring for keyControl"""
	def __init__(self,timeIntv):
		super(keyControlThread, self).__init__()
		self.timeIntv = timeIntv
		print('Time interval set to ',self.timeIntv)

	def run(self):
		global S_signal
		while True:
			if STOP_signal==1:
				break
			sleep(0.01)
			# print('Time interval set to ',self.timeIntv)
			if kbd.is_pressed('a'):
				leftX,leftY = pag.position()
				self.left_signal.emit([leftX,leftY])
			elif kbd.is_pressed('d'):
				rightX,rightY = pag.position()
				self.right_signal.emit([rightX,rightY])
			elif kbd.is_pressed('w'):
				S_signal = 0
				self.status_signal.emit('Mouse Automating started!')
				while True:
					if S_signal==1:
						self.status_signal.emit('Mouse Automating stopped!')
						break
					else:
						try:
							self.status_signal.emit('>>>LEFT<<< Move to ['+\
								str(leftX)+','+str(leftY)+'].')
							pag.moveTo(leftX, leftY, duration=0)
							self.status_signal.emit('>>>LEFT ['+\
								str(leftX)+','+str(leftY)+']<<< Set the button ON, wait '+\
								str(self.timeIntv)+' sec.')
							pag.click() 
							sleep(self.timeIntv)
							self.status_signal.emit('>>>LEFT<<< Set the button OFF.')
							pag.click()
							## move to [leftX, leftY]
							## set the left button ON, wait <timeIntv>, then OFF
							if S_signal==1:
								self.status_signal.emit('Mouse Automating stopped!')
								break

							self.status_signal.emit('>>>RIGHT<<< Move to ['+\
								str(rightX)+','+str(rightY)+'].')
							pag.moveTo(rightX, rightY, duration=0)
							self.status_signal.emit('>>>RIGHT ['+\
								str(rightX)+','+str(rightY)+']<<< Set the button ON, wait '+\
								str(self.timeIntv)+' sec.')
							pag.click()
							sleep(self.timeIntv)
							self.status_signal.emit('>>>RIGHT<<< Set the button OFF.')
							pag.click()
							## move to [rightX, rightY]
							## set the right button ON, wait <timeIntv>, then OFF
						except Exception as e:
							self.status_signal.emit('#111# '+str(e))
							break
		print('KeyControl Thread loop stopped!')

class stopThread(QtCore.QThread):
	status_signal = QtCore.pyqtSignal(str)
	"""docstring for stopThread"""
	def __init__(self):
		super(stopThread, self).__init__()
	
	def run(self):
		global S_signal
		while True:
			if STOP_signal==1:
				break
			sleep(0.01)
			if kbd.is_pressed('s'):
				S_signal = 1
				self.status_signal.emit('>>> \"STOP(s)\" key pressed, waiting...')
		print('Stop Thread loop stopped!')
		



		




if __name__ == '__main__':
	app = QApplication(argv)
	amak = MyWindow()
	amak.show()
	exit(app.exec_())