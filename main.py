from googletrans import Translator
import argparse, googletrans
import docx

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--output_language', type=str, default='fr')
    parser.add_argument('--inputfilepath', type=str)
    parser.add_argument('--outputfolder', type=str)
    args = parser.parse_args()
    if args.output_language not in googletrans.LANGCODES and args.output_language not in googletrans.LANGUAGES:
        print("invalid destination language code, must be part of")
        print(googletrans.LANGUAGES)
        exit(1)
    lang = args.output_language
    input_f = args.inputfilepath
    ouput_f = args.outputfolder + 'output.docx'
    translator = Translator()
    doc = docx.Document(input_f)
    for i in range(len(doc.paragraphs)):
        p = doc.paragraphs[i].text
        res = translator.translate(p, dest=args.output_language).text
        doc.paragraphs[i].text = res
    doc.save(ouput_f)
        
