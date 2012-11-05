import os
import unittest
from __main__ import vtk, qt, ctk, slicer

#
# SlicerRtDemo_RSNA2012_SelfTest
#

class SlicerRtDemo_RSNA2012_SelfTest:
  def __init__(self, parent):
    parent.title = "SlicerRT Demo RSNA2012 Self Test"
    parent.categories = ["Testing.TestCases"]
    parent.dependencies = ["DicomRtImport", "DoseAccumulation", "DoseVolumeHistogram", "Contours"]
    parent.contributors = ["Csaba Pinter (Queen's)"]
    parent.helpText = """
    This is a self test that automatically runs the demo/tutorial prepared for RSNA 2012.
    """
    parent.acknowledgementText = """This file was originally developed by Csaba Pinter, PerkLab, Queen's University and was supported through the Applied Cancer Research Unit program of Cancer Care Ontario with funds provided by the Ontario Ministry of Health and Long-Term Care""" # replace with organization, grant and thanks.
    self.parent = parent

    # Add this test to the SelfTest module's list for discovery when the module
    # is created.  Since this module may be discovered before SelfTests itself,
    # create the list if it doesn't already exist.
    try:
      slicer.selfTests
    except AttributeError:
      slicer.selfTests = {}
    slicer.selfTests['SlicerRtDemo_RSNA2012_SelfTest'] = self.runTest

  def runTest(self):
    tester = SlicerRtDemo_RSNA2012_SelfTest_Test()
    tester.runTest()

#
# qSlicerRtDemo_RSNA2012_SelfTest_Widget
#

class SlicerRtDemo_RSNA2012_SelfTestWidget:
  def __init__(self, parent = None):
    if not parent:
      self.parent = slicer.qMRMLWidget()
      self.parent.setLayout(qt.QVBoxLayout())
      self.parent.setMRMLScene(slicer.mrmlScene)
    else:
      self.parent = parent
    self.layout = self.parent.layout()
    if not parent:
      self.setup()
      self.parent.show()

  def setup(self):
    # Instantiate and connect widgets ...

    # reload button
    # (use this during development, but remove it when delivering
    #  your module to users)
    self.reloadButton = qt.QPushButton("Reload")
    self.reloadButton.toolTip = "Reload this module."
    self.reloadButton.name = "SlicerRtDemo_RSNA2012_SelfTest Reload"
    self.layout.addWidget(self.reloadButton)
    self.reloadButton.connect('clicked()', self.onReload)

    # reload and test button
    # (use this during development, but remove it when delivering
    #  your module to users)
    self.reloadAndTestButton = qt.QPushButton("Reload and Test")
    self.reloadAndTestButton.toolTip = "Reload this module and then run the self tests."
    self.layout.addWidget(self.reloadAndTestButton)
    self.reloadAndTestButton.connect('clicked()', self.onReloadAndTest)

    # Add vertical spacer
    self.layout.addStretch(1)

  def onReload(self,moduleName="SlicerRtDemo_RSNA2012_SelfTest"):
    """Generic reload method for any scripted module.
    ModuleWizard will subsitute correct default moduleName.
    """
    import imp, sys, os, slicer

    widgetName = moduleName + "Widget"

    # reload the source code
    # - set source file path
    # - load the module to the global space
    filePath = eval('slicer.modules.%s.path' % moduleName.lower())
    p = os.path.dirname(filePath)
    if not sys.path.__contains__(p):
      sys.path.insert(0,p)
    fp = open(filePath, "r")
    globals()[moduleName] = imp.load_module(
        moduleName, fp, filePath, ('.py', 'r', imp.PY_SOURCE))
    fp.close()

    # rebuild the widget
    # - find and hide the existing widget
    # - create a new widget in the existing parent
    parent = slicer.util.findChildren(name='%s Reload' % moduleName)[0].parent()
    for child in parent.children():
      try:
        child.hide()
      except AttributeError:
        pass
    # Remove spacer items
    item = parent.layout().itemAt(0)
    while item:
      parent.layout().removeItem(item)
      item = parent.layout().itemAt(0)
    # create new widget inside existing parent
    globals()[widgetName.lower()] = eval(
        'globals()["%s"].%s(parent)' % (moduleName, widgetName))
    globals()[widgetName.lower()].setup()

  def onReloadAndTest(self,moduleName="SlicerRtDemo_RSNA2012_SelfTest"):
    self.onReload()
    evalString = 'globals()["%s"].%sTest()' % (moduleName, moduleName)
    tester = eval(evalString)
    tester.runTest()

#
# SlicerRtDemo_RSNA2012_SelfTestLogic
#

class SlicerRtDemo_RSNA2012_SelfTestLogic:
  """This class should implement all the actual 
  computation done by your module.  The interface 
  should be such that other python code can import
  this class and make use of the functionality without
  requiring an instance of the Widget
  """
  def __init__(self):
    pass

  def hasImageData(self,volumeNode):
    """This is a dummy logic method that 
    returns true if the passed in volume
    node has valid image data
    """
    if not volumeNode:
      print('no volume node')
      return False
    if volumeNode.GetImageData() == None:
      print('no image data')
      return False
    return True


class SlicerRtDemo_RSNA2012_SelfTestTest(unittest.TestCase):
  """
  This is the test case for your scripted module.
  """

  def delayDisplay(self,message,msec=1000):
    """This utility method displays a small dialog and waits.
    This does two things: 1) it lets the event loop catch up
    to the state of the test so that rendering and widget updates
    have all taken place before the test continues and 2) it
    shows the user/developer/tester the state of the test
    so that we'll know when it breaks.
    """
    print(message)
    self.info = qt.QDialog()
    self.infoLayout = qt.QVBoxLayout()
    self.info.setLayout(self.infoLayout)
    self.label = qt.QLabel(message,self.info)
    self.infoLayout.addWidget(self.label)
    qt.QTimer.singleShot(msec, self.info.close)
    self.info.exec_()

  def setUp(self):
    """ Do whatever is needed to reset the state - typically a scene clear will be enough.
    """
    slicer.mrmlScene.Clear(0) #TODO:

    self.delayMs = 700

    #TODO: Comment out
    #logFile = open('d:/pyTestLog.txt', 'w')
    #logFile.write(repr(slicer.modules.models) + '\n')
    #logFile.write(repr(slicer.modules.SlicerRtDemo_RSNA2012_SelfTest) + '\n')
    #logFile.write(repr(slicer.modules.dicomrtimport) + '\n')
    #logFile.write(repr(slicer.modules.models) + '\n')
    #logFile.close()

    self.moduleName = "SlicerRtDemo_RSNA2012_SelfTest"

  def clickAndDrag(self,widget,button='Left',start=(10,10),end=(10,40),steps=20,modifiers=[]):
    """Send synthetic mouse events to the specified widget (qMRMLSliceWidget or qMRMLThreeDView)
    button : "Left", "Middle", "Right", or "None"
    start, end : window coordinates for action
    steps : number of steps to move in
    modifiers : list containing zero or more of "Shift" or "Control"
    """
    style = widget.interactorStyle()
    interator = style.GetInteractor()
    if button == 'Left':
      down = style.OnLeftButtonDown
      up = style.OnLeftButtonUp
    elif button == 'Right':
      down = style.OnRightButtonDown
      up = style.OnRightButtonUp
    elif button == 'Middle':
      down = style.OnMiddleButtonDown
      up = style.OnMiddleButtonUp
    elif button == 'None' or not button:
      down = lambda : None
      up = lambda : None
    else:
      raise Exception("Bad button - should be Left or Right, not %s" % button)
    if 'Shift' in modifiers:
      interator.SetShiftKey(1)
    if 'Control' in modifiers:
      interator.SetControlKey(1)
    interator.SetEventPosition(*start)
    down()
    for step in xrange(steps):
      frac = float(step)/steps
      x = int(start[0] + frac*(end[0]-start[0]))
      y = int(start[1] + frac*(end[1]-start[1]))
      interator.SetEventPosition(x,y)
      style.OnMouseMove()
    up()
    interator.SetShiftKey(0)
    interator.SetControlKey(0)

  def runTest(self):
    """Run as few or as many tests as needed here.
    """
    self.setUp()

    self.test_SlicerRtDemo_RSNA2012_SelfTest_FullTest()

  def test_SlicerRtDemo_RSNA2012_SelfTest_FullTest(self):
    # Check for DicomRtImport module
    self.assertTrue( slicer.modules.dicomrtimport )
    self.assertTrue( slicer.modules.brainsresample )
    self.assertTrue( slicer.modules.dosevolumehistogram )
    self.assertTrue( slicer.modules.doseaccumulation )

    self.TestSection_00SetupPaths()
    self.TestSection_01OpenTempDatabase()
    self.TestSection_02DownloadDay1Data()
    self.TestSection_03ImportDay1Study()
    self.TestSection_04SelectLoadablesAndLoad()
    self.TestSection_05LoadDay2Data()
    self.TestSection_06SetDisplayOptions()
    self.TestSection_07RegisterDay2CTToDay1CT()

    #self.TestSection_06ClearDatabase()

  def TestSection_00SetupPaths(self):
    slicerRtDemo_RSNA2012_SelfTestDir = slicer.app.temporaryPath + '/SlicerRtDemo_RSNA2012_SelfTest'
    if not os.access(slicerRtDemo_RSNA2012_SelfTestDir, os.F_OK):
      os.mkdir(slicerRtDemo_RSNA2012_SelfTestDir)

    self.dicomDataDir = slicerRtDemo_RSNA2012_SelfTestDir + '/EclipseEntPhantomRtData'
    if not os.access(self.dicomDataDir, os.F_OK):
      os.mkdir(self.dicomDataDir)

    self.day2DataDir = slicerRtDemo_RSNA2012_SelfTestDir + '/EclipseEntComputedDay2Data'
    if not os.access(self.day2DataDir, os.F_OK):
      os.mkdir(self.day2DataDir)

    self.dicomDatabaseDir = slicerRtDemo_RSNA2012_SelfTestDir + '/CtkDicomDatabase'
    self.dicomZipFilePath = slicerRtDemo_RSNA2012_SelfTestDir + '/EclipseEntDicomRt.zip'
    self.tempDir = slicerRtDemo_RSNA2012_SelfTestDir + '/Temp'

  def TestSection_01OpenTempDatabase(self):
    # Open test database and empty it
    try:
      qt.QDir().mkpath(self.dicomDatabaseDir)

      if slicer.dicomDatabase:
        self.originalDatabaseDirectory = os.path.split(slicer.dicomDatabase.databaseFilename)[0]
      else:
        self.originalDatabaseDirectory = None
        settings = qt.QSettings()
        settings.setValue('DatabaseDirectory', self.dicomDatabaseDir)

      dicomWidget = slicer.modules.dicom.widgetRepresentation().self()
      dicomWidget.onDatabaseDirectoryChanged(self.dicomDatabaseDir)
      self.assertTrue( slicer.dicomDatabase.isOpen )

      initialized = slicer.dicomDatabase.initializeDatabase()

    except Exception, e:
      import traceback
      traceback.print_exc()
      self.delayDisplay('Test caused exception!\n' + str(e),self.delayMs)

  def TestSection_02DownloadDay1Data(self):
    import urllib
    downloads = (
        ('http://slicer.kitware.com/midas3/download?items=10704', self.dicomZipFilePath),
        )

    downloaded = 0
    for url,filePath in downloads:
      if not os.path.exists(filePath) or os.stat(filePath).st_size == 0:
        if downloaded == 0:
          self.delayDisplay('Downloading Day 1 input data...',self.delayMs)
        print('Requesting download from %s...' % (url))
        urllib.urlretrieve(url, filePath)
        downloaded += 1
    if downloaded > 0:
      self.delayDisplay('Downloading Day 1 input data finished',self.delayMs)

    numOfFilesInDicomDataDir = len([name for name in os.listdir(self.dicomDataDir) if os.path.isfile(self.dicomDataDir + '/' + name)])
    if (numOfFilesInDicomDataDir != 141):
      slicer.app.applicationLogic().Unzip(self.dicomZipFilePath, self.dicomDataDir)
      self.delayDisplay("Unzipping done",self.delayMs)

  def TestSection_03ImportDay1Study(self):
    self.delayDisplay("Import Day 1 study",self.delayMs)

    try:
      mainWindow = slicer.util.mainWindow()
      mainWindow.moduleSelector().selectModule('DICOM')

      # Import study to database
      dicomWidget = slicer.modules.dicom.widgetRepresentation().self()
      dicomWidget.dicomApp.suspendModel()
      indexer = ctk.ctkDICOMIndexer()
      self.assertTrue( indexer )

      indexer.addDirectory( slicer.dicomDatabase, self.dicomDataDir )
      indexer.waitForImportFinished()
      dicomWidget.dicomApp.resumeModel()

      self.assertTrue( len(slicer.dicomDatabase.patients()) == 1 )
      self.assertTrue( slicer.dicomDatabase.patients()[0] )

    except Exception, e:
      import traceback
      traceback.print_exc()
      self.delayDisplay('Test caused exception!\n' + str(e),self.delayMs)

  def TestSection_04SelectLoadablesAndLoad(self):
    self.delayDisplay("Select loadables and load data",self.delayMs)

    try:
      # Choose first patient from the patient list
      dicomWidget = slicer.modules.dicom.widgetRepresentation().self()
      index = dicomWidget.tree.indexAt(qt.QPoint(0,0))
      dicomWidget.onTreeClicked(index)

      # Make sure the loadables are good (RT is assigned to 3 out of 4 and they are selected)
      loadablesByPlugin = dicomWidget.detailsPopup.loadablesByPlugin
      rtFound = False
      loadablesForRt = 0
      for plugin in loadablesByPlugin:
        if plugin.loadType == 'RT':
          rtFound = True
        else:
          continue
        for loadable in loadablesByPlugin[plugin]:
          loadablesForRt += 1
          self.assertTrue( loadable.selected )

      self.assertTrue( rtFound )
      self.assertTrue( loadablesForRt == 2 )

      dicomWidget.detailsPopup.loadCheckedLoadables()

    except Exception, e:
      import traceback
      traceback.print_exc()
      self.delayDisplay('Test caused exception!\n' + str(e),self.delayMs)

  def TestSection_05LoadDay2Data(self):
    import urllib
    downloads = (
        ('http://slicer.kitware.com/midas3/download?items=10702', self.day2DataDir + '/2_ENT_IMRT_Day2.nrrd', slicer.util.loadVolume),
        ('http://slicer.kitware.com/midas3/download?items=10703', self.day2DataDir + '/5_RTDOSE_Day2.nrrd', slicer.util.loadVolume),
        )

    downloaded = 0
    for url,filePath,loader in downloads:
      if not os.path.exists(filePath) or os.stat(filePath).st_size == 0:
        if downloaded == 0:
          self.delayDisplay('Downloading Day 2 input data...',self.delayMs)
        print('Requesting download from %s...\n' % (url))
        urllib.urlretrieve(url, filePath)
        downloaded += 1
      if loader:
        print('Loading %s...' % (os.path.split(filePath)[1]))
        loader(filePath)
    if downloaded > 0:
      self.delayDisplay('Downloading Day 2 input data finished',self.delayMs)

  def TestSection_06SetDisplayOptions(self):
    self.delayDisplay('Setting display options for loaded data',self.delayMs)

    layoutManager = slicer.app.layoutManager()
    layoutManager.setLayout(3)

    # Set Day 2 dose color map
    day2Dose = slicer.util.getNode(pattern='5_RTDOSE_Day2')
    day2Dose.GetDisplayNode().SetAndObserveColorNodeID("vtkMRMLColorTableNodeRainbow")

    # Set CT windows
    day1CT = slicer.util.getNode(pattern='2: ENT IMRT')
    day1CT.GetDisplayNode().SetAutoWindowLevel(0)
    day1CT.GetDisplayNode().SetWindowLevel(250,80)

    day2CT = slicer.util.getNode(pattern='2_ENT_IMRT_Day2')
    day2CT.GetDisplayNode().SetAutoWindowLevel(0)
    day2CT.GetDisplayNode().SetWindowLevel(250,80)

    # Set volumes to show
    sliceWidgetNames = ['Red', 'Green', 'Yellow']
    for sliceWidgetName in sliceWidgetNames:
      slice = layoutManager.sliceWidget(sliceWidgetName)
      sliceLogic = slice.sliceLogic()
      compositeNode = sliceLogic.GetSliceCompositeNode()
      compositeNode.SetBackgroundVolumeID(day1CT.GetID())
      compositeNode.SetForegroundVolumeID(day2CT.GetID())
      sliceLogic.SetForegroundOpacity(0.5)

    layoutManager.sliceWidget(sliceWidgetNames[0]).sliceController().setSliceOffsetValue(138)
    layoutManager.sliceWidget(sliceWidgetNames[1]).sliceController().setSliceOffsetValue(-18)
    
    # Set structure visibilities/transparencies
    body = slicer.util.getNode(pattern='BODY_Contour_RibbonModel')
    body.GetDisplayNode().SetOpacity(0.3)
    optBrain = slicer.util.getNode(pattern='optBRAIN_Contour_RibbonModel')
    optBrain.GetDisplayNode().SetVisibility(0)
    optOptic = slicer.util.getNode(pattern='optOptic_Contour_RibbonModel')
    optOptic.GetDisplayNode().SetVisibility(0)
    brain = slicer.util.getNode(pattern='BRAIN_Contour_RibbonModel')
    brain.GetDisplayNode().SetOpacity(0.3)
    ptv = slicer.util.getNode(pattern='PTV1_Contour_RibbonModel')
    ptv.GetDisplayNode().SetOpacity(0.4)
    ctv = slicer.util.getNode(pattern='CTV_Contour_RibbonModel')
    ctv.GetDisplayNode().SetOpacity(0.5)

    threeDView = layoutManager.threeDWidget(0).threeDView()
    self.clickAndDrag(threeDView,button='Middle',start=(10,220),end=(10,10))
    self.clickAndDrag(threeDView,start=(10,70),end=(90,10))

  def TestSection_07RegisterDay2CTToDay1CT(self):
    try:
      mainWindow = slicer.util.mainWindow()
      #mainWindow.moduleSelector().selectModule('BRAINSFit')

    except Exception, e:
      import traceback
      traceback.print_exc()
      self.delayDisplay('Test caused exception!\n' + str(e),self.delayMs)

  def TestSection_06ClearDatabase(self):
    self.delayDisplay("6: Clear database",self.delayMs)

    initialized = slicer.dicomDatabase.initializeDatabase()
    self.assertTrue( initialized )

    slicer.dicomDatabase.closeDatabase()
    self.assertFalse( slicer.dicomDatabase.isOpen )

    self.delayDisplay("Restoring original database directory",self.delayMs)
    if self.originalDatabaseDirectory:
      dicomWidget = slicer.modules.dicom.widgetRepresentation().self()
      dicomWidget.onDatabaseDirectoryChanged(self.originalDatabaseDirectory)