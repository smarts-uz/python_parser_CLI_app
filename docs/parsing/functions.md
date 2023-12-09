# Telegram History Parser - Utilities
This module contains helper functions used by main parser.

## Functions
**get_html(file_path)**
Opens .html file
Parses content using BeautifulSoup
Returns Soup object
Initial parse of Telegram exporter file.

**save_json(data)**
Accepts parsed data lists
Saves as separate JSON files
For interim storage and analysis
prepare_group_info(data)
Restructures group message data
Adds fields like type, text
Returns list of lists
Prepares data for database loading.

**get_text(dict, id)**
Looks up text for a reply ID
Gets original message text
Returns text or None
correct_time_data(text)
Converts Telegram datetime strings
Handles timezone conversion
Returns Python datetime object
Standardizes timestamps.

**define_type(content)**
Detects if message contains file, video etc
Returns cleaned type string
Classifies content type.

**get_htmls(path)**
Scans folder structure with year/month
Finds .html files
Returns list of full paths
Gets export file list.

**logger_path()**
Generates folder path for logs
Creates directories if needed
Returns path
Log file helper.

So various utility functions to support parsing, data cleaning and organization.
