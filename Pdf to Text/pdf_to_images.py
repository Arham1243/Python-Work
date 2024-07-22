import PyPDF2

def extract_images_from_pdf(pdf_file_path, output_dir):
    with open(pdf_file_path, 'rb') as f:
        pdf_reader = PyPDF2.PdfReader(f)
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            resources = page['/Resources']
            if '/XObject' in resources:
                xObject = resources['/XObject'].get_object()
                for obj in xObject:
                    if xObject[obj]['/Subtype'] == '/Image':
                        size = (xObject[obj]['/Width'], xObject[obj]['/Height'])
                        data = xObject[obj].get_data()
                        with open(f'{output_dir}/image{page_num+1}_{obj[1:]}.jpg', 'wb') as img_file:
                            img_file.write(data)

# Usage
extract_images_from_pdf('files\S2 Page 120 to 245 (1).pdf', 'S2 Page 120 to 245 (1)')
