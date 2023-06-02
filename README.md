# Notion Scripts
Some python scripts I created to automate some tedious notion tasks

Update NOTION_API_KEY at env/keys.py to enable authorization

### Current Scripts
- update_db_select_opts.py
  - Takes a database, a select property and a set of comma separated options and updates the select options, or will create the property with the given options if it does not exist.
  - Current functionality adds options to existing
  - TO-DO: add an overwrite option