# File Handling Utility Functions
## Overview
This module contains helper functions to process file paths, titles, URLs etc. to generate a clean folder structure and file names.

## Functions
**correct_post_title(post_title)**
Cleans and formats post title text into path friendly structure.

* Splits compound titles on '|' and '#'
* Reverses order
* Handles cases with slashes and colons
* Returns list of path components
**correct_video_title(video_path, post_title)**
* Constructs final video file name from parts.
* Gets last path component of video_path
* Prepends post_title for uniqueness
* Returns file name with extensions
**correct_data_title(data_title)**
* Gets year from datetime object for folder name.

**correct_file_location(video_path, data_title, base_dir)**
* Searches base folder structure for actual file location on disk.

* Iterates year and date folders
* Constructs full path using base, year, date etc.
* Returns final absolute path if file exists
**correct_video_duration(duration)**
* Converts duration in HH:MM:SS format to compact name format.

**correct_url_name(url)**
* Extracts readable name from URL for .url file.

* Cleans leading protocol
* Gets last path part or defaults to domain
* Returns truncated name if too long
##Usage
```python
title = correct_post_title(raw_title)
name = correct_video_title(path, title) 
location = correct_file_location(path, date, base)
```
So these functions process raw input names, paths, URLs to generate a clean folder structure and standardized filenames for organization.
