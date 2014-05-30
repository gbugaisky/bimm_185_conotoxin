#!/usr/bin/env python

import os
import wx
from submodules import SeqValidation, callpBLAST, calculateMass, calculatepI, predict
from submodules.averageCysteineDistance import averageCysteineDistance

#Manual addition of module for cs_freeze, since setup script is not adding them
def hidden_dependencies_for_exe():
    from scipy.sparse.csgraph import _validation
    import scipy.special._ufuncs_cxx
    import scipy.integrate.vode
    import scipy.integrate.lsoda
    import sklearn.utils.sparsetools._graph_validation
    import sklearn.utils.lgamma

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
        self.submitButton = wx.Button(self, label="Classify Sequence")
        grid.Add(self.submitButton, pos=(2, 1))
        self.Bind(wx.EVT_BUTTON, self.OnSubmit, self.submitButton)

        mainSizer.Add(grid, 0, wx.ALL, 5)
        self.SetSizerAndFit(mainSizer)

    def EvtRadioType(self, event):
        print ("EvtRadioType: %d\n" % event.GetInt())

    def OnSubmit(self, event):
        sequence = self.sequenceBox.GetValue()
        radio_choice = self.sequenceType.GetValue()
        if not sequence:

            dlg = wx.MessageDialog(self, "Must Enter DNA Sequence!", "Error",
                wx.OK | wx.ICON_INFORMATION)
            dlg.ShowModal()
            dlg.Destroy()

        elif not SeqValidation.validate_nuc_string(sequence):
            print "Here"
            dlg = wx.MessageDialog(self, "Sequences must only contain the characters ACGT!",
                "Syntax Error", wx.OK | wx.ICON_INFORMATION)
            dlg.ShowModal()
            dlg.Destroy()

        else:
            #print callpBLAST.callpBLAST(sequence)
            mass = calculateMass.calculateMass(sequence, True)
            pI = calculatepI.calculateIsoelectricPoint(sequence)
            cysAvg = averageCysteineDistance(sequence)
            label = predict.predictLabel(mass, pI, cysAvg)
            dlg = wx.MessageDialog(self, "Your Sequence Is: " + sequence + " with a mass of " + str(mass)
                + " and a Isoelectric point of " + str(pI) + ".  The predicted pharmacalogical family is " 
                + str(label) + ".", "INFO",
                wx.OK | wx.ICON_INFORMATION)
            dlg.ShowModal()
            dlg.Destroy()

app = wx.App(redirect = 1, filename = "errorlog.txt")
frame = MainWindow(None, "ConoDiscover")
panel = MainFrame(frame)
app.MainLoop()
