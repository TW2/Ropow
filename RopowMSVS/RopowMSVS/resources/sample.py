def execute(grafx, view, font, brushes, pens, pointf):
	grafx.FillRectangle(brushes.RoyalBlue, view)
	grafx.DrawString("Is it Okay ?", font("Arial", 50), brushes.Black, pointf(50,200))