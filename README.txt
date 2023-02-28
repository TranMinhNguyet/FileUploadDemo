install:
pip install robotframework
pip install robotframework-seleniumlibrary
webdrivermanager chrome –linkpath {Scripts folder}
pip install behave
pip install allure-behave

run test:
behave -f allure_behave.formatter:AllureFormatter -o Reports/ Features/UploadFeature.feature
export report
allure serve Reports/

Notes: for TestData: create maxFile.txt (195.46Mb), overSize.txt (200Mb) 