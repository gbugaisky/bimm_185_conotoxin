#!/usr/bin/env python

import os
import wx
import wx.lib.sized_controls as sc

#End of imports

class MainWindow(wx.Frame):
	def __init__(self, parent, title):
		wx.Frame.__init__(self, parent, title=title, size=(800, 600))
		self.CreateStatusBar()

		#Menu Setup
		filemenu = wx.Menu()

		menuAbout = filemenu.Append(wx.ID_ABOUT, "&About", "Information about this application")
		filemenu.AppendSeparator()
		menuExit = filemenu.Append(wx.ID_EXIT, "E&xit", "Quit the application")

		#Create Menu Bar
		menuBar = wx.MenuBar()
		menuBar.Append(filemenu, "&File")
		self.SetMenuBar(menuBar)

		#Bind Menu Events
		self.Bind(wx.EVT_MENU, self.onAbout, menuAbout)
		self.Bind(wx.EVT_MENU, self.onExit, menuExit)

		self.Show(True)

	def onAbout(self, e):
		pass

	def onExit(self, e):
		self.Close(True)


app = wx.App(False)
frame = MainWindow(None, "BLAST Test")
app.MainLoop()