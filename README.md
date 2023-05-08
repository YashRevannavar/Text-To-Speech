# Text-To-Speech

Text-To-Speech is a Python project that performs text-to-speech and PDF processing operations.

## Prerequisites

- Python 3.6 or higher
- pyttsx3
- PyPDF2

## Installation

1. Clone the repository or download the ZIP file.
2. Install the required dependencies by running the following command:

```bash
    pip3 install -r requirements.txt
```

3. Run the project by running the following command:

```bash
    python3 textToSpeech.py
```

## Usage

Text-To-Speech consists of several functions that can be used in different ways. Below are some examples:

speak_init(): Initializes a text-to-speech engine and sets the speaking rate to 205.
read_pdf(location): Reads the content of a PDF file.
text_of_page(reader, page_no): Extracts the text content of a specific page of a PDF file.
speak(text): Speaks out the given text using a text-to-speech engine.

## Contributing

If you want to contribute to this project, feel free to submit a pull request or open an issue. We welcome any contributions that can make this project better.

## License

This project is licensed under the [MIT license](LICENSE.md).
