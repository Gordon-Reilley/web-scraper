# Lab 16 - Serverless Functions

## Project Name - Web Scraper

### Author - Gordon P Reilley Jr

### Feature Tasks and Requirements:

- Scrape a Wikipedia page of your choosing and record which passages need citations.
  - E.g. History of Mexico has a few “citations needed”.
- Your web scraper should report the number of citations needed.
- Your web scraper should identify those cases AND include the relevant passage.
  - E.g. Citation needed for “lorem spam and impsum eggs”
  - Consider the “relevant passage” to be the parent element that contains the passage, often a paragraph element.
- Module must be named scraper.py 
- Create function named get_citations_needed_count
  - Takes in a url string and returns an integer.
- Create function named get_citations_needed_report
  - Takes in a url string and returns a report string
  - The string should be formatted with each citation listed in the order found.

### Site I used for Scraping

- https://en.wikipedia.org/wiki/Super_Mario_Bros.