from pypdf import PdfReader

reader = PdfReader(r"C:\Users\kalan\Downloads\9d84d7144fdda9c9b303a4ed972b9722.pdf")
number_of_pages = len(reader.pages)


text = ""
for i in range(1,number_of_pages):

    # temp = reader.pages[i]
    text = text +" \n\n "+  (reader.pages[i]).extract_text()

print(text)