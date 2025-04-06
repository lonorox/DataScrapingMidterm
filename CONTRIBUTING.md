    Elene Baiashvili - File handler setup, Data transformation and data analysis
    Saba Tchumburidze - Data Models setup, parsing every quote, maintaining naming conventions
    Saba Danelia  - Initial project setup, request methods, Author information Parsing 

# Contributors

## @lonorox - Saba Danelia
- Added collectors and a basic parser for books
- Implemented HTTP requests, handlers, and text cleaners
- Developed a web scraper to extract author information
- Applied cleaners to scraped information
- Updated author model class with optional parameters
- Changed cleaner filenames and added next-page scraping in `parser.py`
- Merged contributions from other collaborators

## @saba1122333 - Saba Tchumburidze
- Created data models to match scraped data
- Encapsulated the collector class
- Improved existing project structure
- Enhanced `data_models`, collector, and parser modules
- Implemented `mainParser`
- Finalized code structure with comments and minor improvements

## @EleneBaiashvili
- Fixed collector to follow OOP principles
- Added features to save data in JSON and CSV formats
- Developed a file loader and transformed data into two separate CSV files
- Built a file analyzer to:
  - Identify the most frequent authors and tags
  - Generate CSVs with readable birthdates and calculated author ages
