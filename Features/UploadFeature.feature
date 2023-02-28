Feature: Upload file
  Scenario: Check Upload File Page Elements
    Given Open chrome browser
    And Navigate to page "https://demo.guru99.com/test/upload"
    Then File Upload Demo Page presented

  Scenario: Upload file without accept terms of service
    Given Open chrome browser
    And Navigate to page "https://demo.guru99.com/test/upload"
    When I upload "validFile.png"
    And I click Submit
    Then File upload message should be "No file is uploaded"

 Scenario Outline: Upload file
    Given Open chrome browser
    And Navigate to page "https://demo.guru99.com/test/upload"
    When I upload "<file_name>"
    And I accept terms of service
    And I click Submit
    Then File upload message should be "<upload_message>"
   Examples:
     |file_name      |upload_message|
     |validFile.png  |1 file has been successfully uploaded.|
     |maxFile.txt    |1 file has been successfully uploaded.|
     |emptyFile.txt  |File is empty|
     |overSize.txt   |File should be less than 195.46MB|