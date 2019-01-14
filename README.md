# Ropow
Respect people !

Ropow is a Visual Studio Community 2017 project working in IronPython and that can run script in Python.

This snippet of IronPython execute a script :
```python
def executeScript(self, path, grafx, view):
    engine = Python.CreateEngine()
    scope = engine.CreateScope()
    engine.ExecuteFile(path, scope)
    testFunction = scope.GetVariable("execute")
    testFunction(grafx, view, Font, Brushes, Pens, PointF)
```

This snippet of IronPython load a script (last line, for the moment, it's hardcoded) :
```python
def panWorld_OnPaint(self, sender, args):
    view = Rectangle(0,0,sender.Width,sender.Height)
    args.Graphics.FillRectangle(SolidBrush(Color.Azure), view)
    self.executeScript("resources/sample.py", args.Graphics, view)
```

This code is the content of 'sample.py' in resources folder :
```python
def execute(grafx, view, font, brushes, pens, pointf):
    grafx.FillRectangle(brushes.RoyalBlue, view)
    grafx.DrawString("Is it Okay ?", font("Arial", 50), brushes.Black, pointf(50,200))
```
