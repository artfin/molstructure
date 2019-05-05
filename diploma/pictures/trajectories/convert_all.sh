find . -name "*.eps" -exec epstopdf {} \;
find . -name "*.pdf" -exec pdfcrop {} \;
