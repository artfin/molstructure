* To make .eps standalone file using Tex: <br /> 
```latex example.tex``` --  generates ```example.dvi``` <br /> 
```dvips -E example.dvi -o example.pdf``` <br />
(but it should be viewed and properly cropped)

* Alternative way to create high-quality image is to clear PDF page of numbering and other stuff, leaving only the picture of interest. Then crop automatically using the following command: <br /> 
```pdfcrop example.pdf```

* Command line option ```trim``` used together with ```convert``` lets you trim borders of the identical color as the corners of an image: <br />
```convert input.png -trim output.png``` 

* Creating scalable python graphic for Tex: <br />
-- saving plot to .eps format <br />
-- using ```epstopdf``` utility convert .eps image to .pdf file <br />:
```epstopdf example.png -o example.pdf``` <br />
-- automatically crop using ```pdfcrop```

* Converting ```.jpg```, ```.tiff``` to ```.eps``` format using ImageMagick's ```convert``` (it is a good practice to use the eps2 format; resulting eps file much smaller because it uses the JPEG compression algorithm): <br />
```convert example.tiff eps2:example.eps```
