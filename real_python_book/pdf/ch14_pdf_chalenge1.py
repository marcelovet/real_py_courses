from pathlib import Path

from pypdf import PdfReader, PdfWriter

# def page_adder(writer, pages):
#     for page in pages:
#         writer.add_page(page)


class PdfFileSplitter:
    """Pdf reader and writer that can split a pdf file in two
    """

    def __init__(self, path):
        """
            path (str): a str path relative to the cwd
        """
        self.path = path

    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, path):
        pdf_path = Path().cwd() / path

        if pdf_path.suffix != '.pdf':
            raise ValueError('You must define a pdf file')
        if not pdf_path.exists():
            raise FileNotFoundError(f'No pdf found at {pdf_path}')

        self._path = pdf_path
        self._reader = PdfReader(self._path)

    @staticmethod
    def __page_adder(writer, pages):
        for page in pages:
            writer.add_page(page)

    @staticmethod
    def __page_writer(path, writer):
        with path.open(mode='wb') as file:
            writer.write(file)
        return f'A Pdf with {len(writer.pages)} pages was wrote in {path}'

    def split(self, breakpoint):
        part_1 = self._reader.pages[:breakpoint]
        part_2 = self._reader.pages[breakpoint:]
        self.writer1 = PdfWriter()
        self.writer2 = PdfWriter()
        self.__page_adder(self.writer1, part_1)
        self.__page_adder(self.writer2, part_2)

    def write(self, filename):
        file_dir = self.path.parent
        files = [
            file_dir / f'{filename}_1.pdf',
            file_dir / f'{filename}_2.pdf'
        ]
        res_1 = self.__page_writer(files[0], self.writer1)
        res_2 = self.__page_writer(files[1], self.writer2)
        return f'{res_1}\n{res_2}'
