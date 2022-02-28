# Filtering and Classification Module
Reads json file corresponsing to each Instagram profile<br>
Run pattern matching rules on profile biography, full name, category to look for keywords matching to beauty entities<br>
On a match, json file is updated with classified category as "classified_category": "Brand/Retailer/Influencer/Publisher"<br>
On multiple matches, profile will moved to a seprate directory for human intervention to classify it<br>
A profile filtered as Not-A-Beauty-Entity will be discarded

# Tech
Python

# Execution
pthon main.py --work_dir <<work_dir>> --mode 0 <br>
work_dir => location to read json files
