# Structuring folder
## Overview
This Python script provides functionality to take an input list of data and automatically organize the files, videos, photos, or URLs into a folder structure on the local file system.

## It does the following main things:

* Creates folder structure based on channel name and post title
* Moves relevant files, videos, photos into these folders
* Creates .tmnote files with metadata and .url files for links
* Handles errors and invalid data gracefully

## Main Functions
**create_dirs_all(list_of_data)**
The main function that handles parsing the input data and organizing the content.

## Parameters:

* list_of_data: List containing:
* Author name
* Channel/post title
* Content file path or URL
* Description
* Duration etc.
## Steps:

1. Load environment variables for save locations
2. Clean and validate data
3. Determine content type (file, video, URL)
4. Create folder structure based on channel name and post title
5. Move content file into correct folder
6. Create meta .tmnote file with details
7. Handle errors and skip invalid entries

## Key Considerations:

Validation of input data for illegal characters, empty values
Path construction from variables
Use of shutil for file move operation
Use of try/except for error handling
### Helper Functions
```python
correct_data_title(title): #Cleans post title for use in file paths

correct_file_location(content, date, base_dir): #Determines actual file path on disk

correct_url_name(url): #Gets valid name for .url file
```
## Usage
The script requires a input list with data rows provided in a specific format:

[
  ["Author1", "Post Title 1", "c:\video1.mp4", "Desc", "00:05:23", "2023-01-01"], 
  ["Author2", "Post Title 2", "https://example.com/article", None, None, None]
]

It can then be run simply with:

```python
python main.py create-folders
```
And will automatically organize the content into the folder structure.
