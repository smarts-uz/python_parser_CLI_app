# Telegram Parser - Database Functions
## Overview
Module contains functions to:

* Extract data from DB
* Transform and enrich
* Update records
* Add relations between tables
## Functions

**read_channel_db()**
* Gets channel messages text
* Returns dict with ID: text
* get_info_from_db()
* Extracts required group message columns
* Returns list of tuples
  
**update_group_name(dict)**
* Accepts mappings of ID: name
* Updates the related records
  
**update_group_text()**
* Enriches group text from channel
* Updates matched records
  
**add_parser_channel_id()**
* Joins group and channel records
* Adds channel ID reference to group
  
**update_db()**
Orchestrator function to:
* Get data from DB
* Massage into right structure
* Update names and text
* Add channel relations
**read_group_content()**
* Returns enriched group data
* For final analysis/use
  
So various functions to sync and enhance the parsed Telegram data stored in the database tables.
