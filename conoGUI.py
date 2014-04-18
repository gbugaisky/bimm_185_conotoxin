#!/usr/bin/env python

import os
import wx
import wx.lib.sized_controls as sc
import wx.wizard as wiz

from submodules import SeqValidation, callpBLAST

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

class MainFrame(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        #sizers for the controls
        mainSizer = wx.BoxSizer(wx.VERTICAL)
        grid = wx.GridBagSizer(hgap=5, vgap=5)
        hSizer = wx.BoxSizer(wx.HORIZONTAL)

        self.instructions = wx.StaticText(self, label="Enter A Sequence:")
        grid.Add(self.instructions, pos=(0, 0))

        # Sequence sentry box
        self.sequenceBox = wx.TextCtrl(self, size=(400, -1))
        grid.Add(self.sequenceBox, pos=(1, 0))

        # DNA/Protein selector
        sequenceTypeList = ['Nucleotide', "Protein"]
        self.sequenceType = wx.RadioBox(self, label="What type of sequence?", 
            choices=sequenceTypeList, style=wx.RA_SPECIFY_COLS)
        grid.Add(self.sequenceType, pos=(1, 1))
        self.Bind(wx.EVT_RADIOBOX, self.EvtRadioType, self.sequenceType)

        # GO button
        self.submitButton = wx.Button(self, label="BLAST Sequence")
        grid.Add(self.submitButton, pos=(2, 1))
        self.Bind(wx.EVT_BUTTON, self.OnSubmit, self.submitButton)

        mainSizer.Add(grid, 0, wx.ALL, 5)
        self.SetSizerAndFit(mainSizer)

    def EvtRadioType(self, event):
        print ("EvtRadioType: %d\n" % event.GetInt())

    def OnSubmit(self, event):
        sequence = self.sequenceBox.GetValue()
        if not sequence:
            dlg = wx.MessageDialog(self, "Must Enter DNA Sequence!", "Error",
                wx.OK | wx.ICON_INFORMATION)
            dlg.ShowModal()
            dlg.Destroy()

        elif not SeqValidation.validate_dna_string(sequence):
            print "Here"
            dlg = wx.MessageDialog(self, "Sequences must only contain the characters ACGT!",
                "Syntax Error", wx.OK | wx.ICON_INFORMATION)
            dlg.ShowModal()
            dlg.Destroy()

        else:
            print callpBLAST.callpBLAST(sequence)
            dlg = wx.MessageDialog(self, "Your Sequence Is: " + sequence, "INFO",
                wx.OK | wx.ICON_INFORMATION)
            dlg.ShowModal()
            dlg.Destroy()

app = wx.App(redirect = 1, filename = "consolelog.txt")
frame = MainWindow(None, "BLAST Test")
panel = MainFrame(frame)
app.MainLoop()
