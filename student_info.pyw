#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Author: Group II

import sip
sip.setapi('QVariant',2) 

import sys
from main import Ui_MainWindow 
from search import Ui_Dialog
from PyQt4 import QtSql, QtGui, QtCore 


def createConnection():
	db = QtSql.QSqlDatabase.addDatabase('QMYSQL')
	db.setHostName('localhost') 
	db.setDatabaseName('db_student_info') 
	db.setUserName('sysprog_bsit') 
	db.setPassword('bsit3sysprog') 
	db.open()
	print (db.lastError().text())
	return True


class gui(QtGui.QMainWindow):
	recno = 0
	def __init__(self, parent=None):
		super(gui, self).__init__(parent)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)		
		self.model=QtSql.QSqlQueryModel(self)		
		
		self.model.setQuery("select * from tbl_student_info ") 
		self.record=self.model.record(0)
		self.ui.txtId.setText(str(self.record.value("student_id")))
		self.ui.txtFirstName.setText(str(self.record.value("fname")))
		self.ui.txtLastName.setText(str(self.record.value("lname")))
		self.ui.txtCourse.setText(str(self.record.value("course")))
		self.ui.txtYear.setText(str(self.record.value("year")))
		self.ui.txtSection.setText(str(self.record.value("section")))
		
		
		self.model = QtSql.QSqlTableModel(self)
		self.model.setTable("tbl_student_info")	
		self.model.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)
		self.model.select()
		
		QtCore.QObject.connect(self.ui.btnClear, QtCore.SIGNAL('clicked()'),self.clear)
		QtCore.QObject.connect(self.ui.actionSearch, QtCore.SIGNAL('triggered()'),self.MyFormShow)
		QtCore.QObject.connect(self.ui.btnFirst, QtCore.SIGNAL('clicked()'),self.dispFirst)
		QtCore.QObject.connect(self.ui.btnFirst, QtCore.SIGNAL('clicked()'),self.DisableLineEdits)
		QtCore.QObject.connect(self.ui.btnPrev, QtCore.SIGNAL('clicked()'),self.dispPrevious)
		QtCore.QObject.connect(self.ui.btnLast, QtCore.SIGNAL('clicked()' ),self.dispLast)
		QtCore.QObject.connect(self.ui.btnNext, QtCore.SIGNAL('clicked()' ),self.dispNext)
		QtCore.QObject.connect(self.ui.btnNext, QtCore.SIGNAL('clicked()'),self.DisableLineEdits)
		QtCore.QObject.connect(self.ui.btnEdit, QtCore.SIGNAL('clicked()' ),self.EnableLineEdits)
		QtCore.QObject.connect(self.ui.actionExit_2, QtCore.SIGNAL("triggered()"),self.close)
		QtCore.QObject.connect(self.ui.btnExit, QtCore.SIGNAL('clicked()' ),self.close)
		QtCore.QObject.connect(self.ui.btnAdd, QtCore.SIGNAL('clicked()' ),self.AddRecord)
		QtCore.QObject.connect(self.ui.btnAdd, QtCore.SIGNAL('clicked()' ),self.AlertBoxAddRecord)
		QtCore.QObject.connect(self.ui.btnUpdate, QtCore.SIGNAL('clicked()' ),self.UpdateRecord)
		QtCore.QObject.connect(self.ui.btnUpdate, QtCore.SIGNAL('clicked()' ),self.AlertBoxUpdateRecord)
		QtCore.QObject.connect(self.ui.btnEdit, QtCore.SIGNAL('clicked()' ),self.EditRecords)
		QtCore.QObject.connect(self.ui.btnDelete, QtCore.SIGNAL('clicked()' ),self.AlertBoxDeleteRecord)
		QtCore.QObject.connect(self.ui.btnDelete, QtCore.SIGNAL('clicked()' ),self.DeleteRecord)
	
		
	def MyFormShow(self):
		MyFormShowWindow = FormSearch(self)
		MyFormShowWindow.show()
	
	def EnableLineEdits(self):
		self.ui.txtId.setEnabled(True)
		self.ui.txtFirstName.setEnabled(True)
		self.ui.txtLastName.setEnabled(True)
		self.ui.txtCourse.setEnabled(True)
		self.ui.txtSection.setEnabled(True)
		self.ui.txtYear.setEnabled(True)
		
	def DisableLineEdits(self):
		self.ui.txtId.setEnabled(False)
		self.ui.txtFirstName.setEnabled(False)
		self.ui.txtLastName.setEnabled(False)
		self.ui.txtCourse.setEnabled(False)
		self.ui.txtSection.setEnabled(False)
		self.ui.txtYear.setEnabled(False)
		

	def dispFirst(self):
		gui.recno=0
		self.record=self.model.record(gui.recno)
		self.ui.txtId.setText(str(self.record.value("student_id")))
		self.ui.txtFirstName.setText(self.record.value("fname"))
		self.ui.txtLastName.setText(self.record.value("lname"))
		self.ui.txtCourse.setText(self.record.value("course"))
		self.ui.txtYear.setText(self.record.value("year"))
		self.ui.txtSection.setText(self.record.value("section"))
		
							
	def dispPrevious(self):
		gui.recno-=1
		if gui.recno < 0:
			gui.recno=self.model.rowCount()-1
		self.record=self.model.record(gui.recno)
		self.ui.txtId.setText(str(self.record.value("student_id")))
		self.ui.txtFirstName.setText(self.record.value("fname"))
		self.ui.txtLastName.setText(self.record.value("lname"))
		self.ui.txtcourse.setText(self.record.value("course"))
		self.ui.txtYear.setText(self.record.value("year"))
		self.ui.txtSection.setText(self.record.value("section"))
		

	def dispLast(self):
		gui.recno=self.model.rowCount()-1
		self.record=self.model.record(gui.recno)
		self.ui.txtId.setText(str(self.record.value("student_id")))
		self.ui.txtFirstName.setText(self.record.value("fname"))
		self.ui.txtLastName.setText(self.record.value("lname"))
		self.ui.txtCourse.setText(self.record.value("course"))
		self.ui.txtYear.setText(self.record.value("year"))
		self.ui.txtSection.setText(self.record.value("section"))
		
	
	def clear(self):
		self.ui.txtId.setText("")
		self.ui.txtFirstName.setText("")
		self.ui.txtLastName.setText("")
		self.ui.txtYear.setText("")
		self.ui.txtSection.setText("")
                self.ui.txtCourse.setText("")
			
	def dispNext(self):
		gui.recno+=1
		if gui.recno > self.model.rowCount()-1:
			gui.recno=0
		self.record=self.model.record(gui.recno)
		self.ui.txtId.setText(str(self.record.value("student_id")))
		self.ui.txtFirstName.setText(self.record.value("fname"))
		self.ui.txtLastName.setText(self.record.value("lname"))
		self.ui.txtCourse.setText(self.record.value("course"))
		self.ui.txtYear.setText(self.record.value("year"))
		self.ui.txtSection.setText(self.record.value("section"))
		
		
	def AddRecord(self):
		studentId = self.ui.txtIdlineEdit.text()
		studentFName = self.ui.txtFirstNamelineEdit.text()
		studentLName = self.ui.txtLastNamelineEdit.text()
		studentCourse = self.ui.txtCourselineEdit.text()
		studentYear = self.ui.txtYearlineEdit.text()
		studentSection = self.ui.txtSectionlineEdit.text()
			
		self.model.setData(self.model.index(0, 1), studentId)
		self.model.setData(self.model.index(0, 2), studentFName)
		self.model.setData(self.model.index(0, 3), studentLName)
		self.model.setData(self.model.index(0, 4), studentCourse)
		self.model.setData(self.model.index(0, 5), studentYear)
		self.model.setData(self.model.index(0, 6), studentSection)
		
										
	def UpdateRecord(self):
		self.model.submitAll()
		txtId = self.ui.txtId.text()
		txtFirstName = self.ui.txtFirstName.text()
		txtLastName = self.ui.txtLastName.text()
		txtCourse = self.ui.txtCourse.text()
		txtYear = self.ui.txtYear.text()
		txtSection = self.ui.txtSection.text()
			
		self.model.setData(self.model.index(0, 1), txtId)
		self.model.setData(self.model.index(0, 2), txtFirstName)
		self.model.setData(self.model.index(0, 3), txtLastName)
		self.model.setData(self.model.index(0, 4), txtCourse)
		self.model.setData(self.model.index(0, 5), txtYear)
		self.model.setData(self.model.index(0, 6), txtSection)
		self.model.submitAll()
	
	def EditRecords(self):
		self.model.insertRows(0,1)
		self.model.insertRows(0,2)
		self.model.insertRows(0,3)
		self.model.insertRows(0,4)
		self.model.insertRows(0,5)
		self.model.insertRows(0,6)
		self.model.submitAll()
	
	def DeleteRecord(self):
		self.model.removeColumn(1) 
		self.model.removeColumn(2) 
		self.model.removeColumn(3) 
		self.model.removeColumn(4) 
		self.model.removeColumn(5) 
		self.model.removeColumn(6) 
		self.model.submitAll()
				
	def CancelChanges(self):
		self.model.revertAll()
		
	def AlertBoxAddRecord(self):       
		msgBox = QtGui.QWidget(self)
		res = QtGui.QMessageBox.information(msgBox, "Message", "new record successfully added!")
		msgBox.show()

	def AlertBoxUpdateRecord(self):       
		msgBox = QtGui.QWidget(self)
		res = QtGui.QMessageBox.information(msgBox, "Message", "new record saved!")
		msgBox.show()
	
	def AlertBoxDeleteRecord(self):
		msgBox = QtGui.QWidget(self)
		res = QtGui.QMessageBox.question(msgBox, 'Message', "Are you sure you want to continue?", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.QMessageBox.No)
		msgBox.show()
	
class FormSearch(QtGui.QDialog):
	def __init__(self, parent=None):
		super(FormSearch, self).__init__(parent)
		QtGui.QWidget.__init__(self, parent)
		self.ui = Ui_Dialog()
		self.ui.setupUi(self)	
		self.model = QtSql.QSqlTableModel(self)		
		self.model.setTable("tbl_student_info")		
		self.model.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)
		self.model.removeColumn(0) 
		self.model.select()
		
		self.model.setHeaderData(0, QtCore.Qt.Horizontal, "ID NUMBER")
		self.model.setHeaderData(1, QtCore.Qt.Horizontal, "FIRST NAME")
		self.model.setHeaderData(2, QtCore.Qt.Horizontal, "LAST NAME")
		self.model.setHeaderData(3, QtCore.Qt.Horizontal, "COURSE")
		self.model.setHeaderData(4, QtCore.Qt.Horizontal, "YEAR")
		self.model.setHeaderData(5, QtCore.Qt.Horizontal, "SECTION")
		
		
		self.ui.tableView.setModel(self.model)		
		QtCore.QObject.connect(self.ui.btnSearch, QtCore.SIGNAL('clicked()' ),self.AlertSearchRecord)
		QtCore.QObject.connect(self.ui.btnSearch, QtCore.SIGNAL('clicked()' ),self.SearchRecord)
	

	def SearchRecord(self):
		self.model.setFilter("student_id like '"+self.ui.txtSearch.text()+"%'")
		self.model.setFilter("fname like '"+self.ui.txtSearch.text()+"%'")
		self.model.setFilter("lname like '"+self.ui.txtSearch.text()+"%'")
		self.model.setFilter("year '"+self.ui.txtSearch.text()+"%'")
		self.model.setFilter("section like '"+self.ui.txtSearch.text()+"%'")
		self.model.setFilter("course like '"+self.ui.txtSearch.text()+"%'")
	

	def CancelChanges(self):
		self.model.revertAll()
		msgBox = QtGui.QWidget(self)
		res = QMessageBox.information(msgBox, "Message", "NO")
		msgBox.show()

if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)

if not createConnection():
	sys.exit(1)

myapp = gui()
myapp.show()
sys.exit(app.exec_())


