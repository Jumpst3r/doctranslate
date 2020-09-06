## Dockerized document translation (odt,doc,docx)

### Description

Translate documents (odt,doc,docx) while retaining formatting and layout

### Usage

To use the docker image, first pull the image using

`docker pull jumpst3r/doctranslate`

And then execute 
```
docker run -it --rm -v /FULL_PATH_TO/example.docx:/input/example.docx -v /FULL_PATH_TO_OUTPUT_FOLDER/:/output/ jumpst3r/doctranslate sh /input/script.sh /input/example.png LANG_CODE /output/
```

where `/FULL_PATH_TO/example.docx` corresponds to the local path of the document you'd like to translate. LANG_CODE should be replaced with the code corresponding to the target language. An exhaustive list of language codes can be found in the `install.json` file.

The output consists of:

- The translated document (same filetype as the input document)

The docker image is also compatible with [DIVAServices](https://github.com/lunactic/DIVAServices) a web-based framework providing streamlined access to DOI methods.

### Sources / Comments

Uses public (unofficial) google-translate API and as such might be limited in terms of numbers of numbers of words to be translated. For details on this issue, refer to [this link](https://github.com/ssut/py-googletrans)
