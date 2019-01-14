import clr
clr.AddReference('System.Drawing')
clr.AddReference('System.Windows.Forms')
clr.AddReference('Microsoft.Scripting') # Added
clr.AddReferenceToFileAndPath('resources/IronPython.dll') # Added

from System.Drawing import *
from System.Windows.Forms import *
from Microsoft.Scripting import * # Added
from IronPython.Hosting import * # Added
from System import Console # Added
from System.IO import * # Added

class MyForm(Form):
    def __init__(self):
        # Create child controls and initialize form
        #-----------------------------------------------
        # Window
        #-----------------------------------------------
        cropping = 600
        error_width = 16
        error_height = 39        
        self.Location = Point(cropping/2,cropping/2)
        self.Width = Screen.PrimaryScreen.WorkingArea.Width - cropping
        self.Height = Screen.PrimaryScreen.WorkingArea.Height - cropping
        self.CenterToScreen()
        self.Resize += self.window_OnResize
        #-----------------------------------------------
        # Emulated toolbar (Labels)
        #-----------------------------------------------
        etl_width = 50
        etl_height = 50
        #-----------------------------------------------
        # Emulated toolbar - Label to go back
        #-----------------------------------------------
        lblRewind = Label()
        lblRewind.Name = "lblRewind"
        lblRewind.Size = Size(etl_width,etl_height)
        lblRewind.Location = Point(etl_width*0,0)
        lblRewind.Image = Image.FromFile("resources/40_rewind.png")
        lblRewind.MouseEnter += self.lblRewind_OnMouseEnter
        lblRewind.MouseLeave += self.lblRewind_OnMouseLeave
        self.Controls.Add(lblRewind)
        #-----------------------------------------------
        # Emulated toolbar - Label to go forward
        #-----------------------------------------------
        lblForward = Label()
        lblForward.Name = "lblForward"
        lblForward.Size = Size(etl_width,etl_height)
        lblForward.Location = Point(etl_width*1,0)
        lblForward.Image = Image.FromFile("resources/40_forward.png")
        lblForward.MouseEnter += self.lblForward_OnMouseEnter
        lblForward.MouseLeave += self.lblForward_OnMouseLeave
        self.Controls.Add(lblForward)
        #-----------------------------------------------
        # Emulated toolbar - Label to go home
        #-----------------------------------------------
        lblHome = Label()
        lblHome.Name = "lblHome"
        lblHome.Size = Size(etl_width,etl_height)
        lblHome.Location = Point(etl_width*2,0)
        lblHome.Image = Image.FromFile("resources/40_home.png")
        lblHome.MouseEnter += self.lblHome_OnMouseEnter
        lblHome.MouseLeave += self.lblHome_OnMouseLeave
        self.Controls.Add(lblHome)
        #-----------------------------------------------
        # Emulated toolbar - Label to download
        #-----------------------------------------------
        lblDownload = Label()
        lblDownload.Name = "lblDownload"
        lblDownload.Size = Size(etl_width,etl_height)
        lblDownload.Location = Point(self.Width - error_width - etl_width*2,0)
        lblDownload.Image = Image.FromFile("resources/40_download.png")
        lblDownload.MouseEnter += self.lblDownload_OnMouseEnter
        lblDownload.MouseLeave += self.lblDownload_OnMouseLeave
        self.Controls.Add(lblDownload)
        #-----------------------------------------------
        # Emulated toolbar - Label to upload
        #-----------------------------------------------
        lblUpload = Label()
        lblUpload.Name = "lblUpload"
        lblUpload.Size = Size(etl_width,etl_height)
        lblUpload.Location = Point(self.Width - error_width - etl_width*1,0)
        lblUpload.Image = Image.FromFile("resources/40_upload.png")
        lblUpload.MouseEnter += self.lblUpload_OnMouseEnter
        lblUpload.MouseLeave += self.lblUpload_OnMouseLeave
        self.Controls.Add(lblUpload)
        #-----------------------------------------------
        # Drawing area (Panel)
        #-----------------------------------------------
        panWorld = Panel()
        panWorld.Name = "panWorld"
        panWorld.Size = Size(self.Width - error_width, self.Height - error_height - etl_height)
        panWorld.Location = Point(0,etl_height)
        panWorld.Paint += self.panWorld_OnPaint
        panWorld.Refresh()
        self.Controls.Add(panWorld)        

    def executeScript(self, path, grafx, view):
        engine = Python.CreateEngine()
        scope = engine.CreateScope()
        engine.ExecuteFile(path, scope)
        testFunction = scope.GetVariable("execute")
        testFunction(grafx, view, Font, Brushes, Pens, PointF)

    def panWorld_OnPaint(self, sender, args):
        view = Rectangle(0,0,sender.Width,sender.Height)
        args.Graphics.FillRectangle(SolidBrush(Color.Azure), view)
        self.executeScript("resources/sample.py", args.Graphics, view)

    # =============================================================================
    # EVENTS for Window
    # -----------------------------------------------------------------------------
    def window_OnResize(self, sender, args):
        error_width = 16
        error_height = 39
        etl_width = 50
        etl_height = 50
        self.Controls["lblDownload"].Location = Point(self.Width - error_width - etl_width*2,0)
        self.Controls["lblUpload"].Location = Point(self.Width - error_width - etl_width*1,0)
        self.Controls["panWorld"].Size = Size(self.Width - error_width, self.Height - error_height - etl_height)

    # =============================================================================
    # EVENTS for lblRewind
    # -----------------------------------------------------------------------------
    def lblRewind_OnMouseEnter(self, sender, args):
        sender.Image = Image.FromFile("resources/50_rewind.png")

    def lblRewind_OnMouseLeave(self, sender, args):
        sender.Image = Image.FromFile("resources/40_rewind.png")

    # =============================================================================
    # EVENTS for lblForward
    # -----------------------------------------------------------------------------
    def lblForward_OnMouseEnter(self, sender, args):
        sender.Image = Image.FromFile("resources/50_forward.png")

    def lblForward_OnMouseLeave(self, sender, args):
        sender.Image = Image.FromFile("resources/40_forward.png")

    # =============================================================================
    # EVENTS for lblHome
    # -----------------------------------------------------------------------------
    def lblHome_OnMouseEnter(self, sender, args):
        sender.Image = Image.FromFile("resources/50_home.png")

    def lblHome_OnMouseLeave(self, sender, args):
        sender.Image = Image.FromFile("resources/40_home.png")

    # =============================================================================
    # EVENTS for lblDownload
    # -----------------------------------------------------------------------------
    def lblDownload_OnMouseEnter(self, sender, args):
        sender.Image = Image.FromFile("resources/50_download.png")

    def lblDownload_OnMouseLeave(self, sender, args):
        sender.Image = Image.FromFile("resources/40_download.png")

    # =============================================================================
    # EVENTS for lblUpload
    # -----------------------------------------------------------------------------
    def lblUpload_OnMouseEnter(self, sender, args):
        sender.Image = Image.FromFile("resources/50_upload.png")

    def lblUpload_OnMouseLeave(self, sender, args):
        sender.Image = Image.FromFile("resources/40_upload.png")


Application.EnableVisualStyles()
Application.SetCompatibleTextRenderingDefault(False)

form = MyForm()
Application.Run(form)