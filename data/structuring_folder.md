## Structuring folder
# Overview
This Python script provides functionality to take an input list of data and automatically organize the files, videos, photos, or URLs into a folder structure on the local file system.

# It does the following main things:

* Creates folder structure based on channel name and post title
* Moves relevant files, videos, photos into these folders
*Creates .tmnote files with metadata and .url files for links
*Handles errors and invalid data gracefully
Main Functions
create_dirs_all(list_of_data)
The main function that handles parsing the input data and organizing the content.

Parameters:

list_of_data: List containing:
Author name
Channel/post title
Content file path or URL
Description
Duration etc.
Steps:

Load environment variables for save locations
Clean and validate data
Determine content type (file, video, URL)
Create folder structure based on channel name and post title
Move content file into correct folder
Create meta .tmnote file with details
Handle errors and skip invalid entries
Key Considerations:

Validation of input data for illegal characters, empty values
Path construction from variables
Use of shutil for file move operation
Use of try/except for error handling
Helper Functions
correct_data_title(title): Cleans post title for use in file paths

correct_file_location(content, date, base_dir): Determines actual file path on disk

correct_url_name(url): Gets valid name for .url file

Usage
The script requires a input list with data rows provided in a specific format:

Copy code

[
  ["Author1", "Post Title 1", "c:\video1.mp4", "Desc", "00:05:23", "2023-01-01"], 
  ["Author2", "Post Title 2", "https://example.com/article", None, None, None]
]
It can then be run simply with:

Copy code

python organizer.py
And will automatically organize the content into the folder structure.
