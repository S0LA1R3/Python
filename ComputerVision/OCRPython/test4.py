import pytesseract
import cv2

img = cv2.imread(r'C:\Users\PESSOAL\Documents\GitHub\Python\ComputerVision\OCRPython\Imagens\saida.jpg')
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cv2.imshow('imagem', rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()
tessdataDir = r'C:\Users\PESSOAL\Documents\GitHub\Python\ComputerVision\OCRPython\tessdata'
configTesseract = f'--tessdata-dir "{tessdataDir}" --psm 7'
texto = pytesseract.image_to_string(rgb, lang='por', config=configTesseract)
print(texto)
