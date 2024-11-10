import unittest
import asyncio
from llmsherpa.readers.file_reader import LayoutPDFReader
from llmsherpa.readers import Document


class TestFileReader(unittest.TestCase):

    def setUp(self):
        """
        Set up a LayoutPDFReader instance with an actual parser API URL.
        """
        self.parser_api_url = "http://localhost:5001/api/parseDocument"  # Replace with the actual endpoint
        self.reader = LayoutPDFReader(self.parser_api_url)

    def test_read_pdf_with_url(self):
        """
        Test reading a PDF from a URL by calling the actual service.
        Ensures that read_pdf successfully returns a Document object when given a valid URL.
        """
        # Replace with a real URL to a PDF file that the API can parse
        pdf_url = "https://getsamplefiles.com/download/pdf/sample-1.pdf"  # Replace with an accessible PDF URL, or mock
        
        # Call read_pdf with a URL
        document = self.reader.read_pdf(pdf_url)
        
        # Check if a Document object is returned
        self.assertIsInstance(document, Document)
        self.assertGreater(len(document.chunks()), 0, "Document should contain chunks")

    def test_read_pdf_with_url_async(self):
        """
        Test reading a PDF from a URL by calling the actual service.
        Ensures that read_pdf successfully returns a Document object when given a valid URL.
        """
        # Replace with a real URL to a PDF file that the API can parse
        pdf_url = "https://getsamplefiles.com/download/pdf/sample-1.pdf"  # Replace with an accessible PDF URL, or mock
        
        # Call read_pdf with a URL
        document = asyncio.run(self.reader.read_pdf_async(pdf_url))
        
        # Check if a Document object is returned
        self.assertIsInstance(document, Document)
        self.assertGreater(len(document.chunks()), 0, "Document should contain chunks")

if __name__ == '__main__':
    unittest.main()
