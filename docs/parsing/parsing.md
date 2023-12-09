# Telegram History Parser
## Overview
This module parses Telegram chat history exported as .html files and extracts relevant message data into structured format.

## Key functions:

**get_info()** - Main parser, extracts message data from HTML

**final_result_info()** - Orchestrator, handles file processing

**get_html(), save_json()** - Helper functions

## Main Functions
**get_info(html)**
Parses HTML content and returns extracted data as lists of dictionaries containing:

* Learning channel messages
* Group content replies
* All messages combined
## Steps:

* Find all .message divs
* Get key parts like ID, timestamp, text
* Handle standalone and joined messages
* Process media types (files, video, URLs)
* Populate dictionaries
* Returns [channel, replies, all]

**final_result_info(path)**
Top-level function to handle a directory of .html files.

## For each file:

* Get HTML content
* Extract data with get_info()
* Save interim JSON
* Post-process data
* Storestructured output
Returns channel and group data ready for database.

## Helper Functions

**get_html(filepath)**: Loads .html file from disk

**save_json(data)**: Saves interim parser output as JSON

**prepare_group_info()**: Restructures group data

**get_from_name_*()**: Handles message owners

**correct_*()**: Clean up text and timestamps

## Usage
```python
chats, groups = final_result_info(history_dir)
save_to_db(chats)
save_to_db(groups)
```
So it takes a directory of Telegram history files and extracts out clean structured chat data ready for loading into a database or other applications.
