# Data Scraping
1. Fetch instagram profile data and persist the same in json files on disk.

# Tech/Framework
  Node js

# Execution Details
1. At the root of module /src/, execute command: "npm install" to install all dependencies specified in package.json.
2. To run the module, at root level /src/, execute the command: "node src/index.js"
3. Module expects an input file: initial_userids.txt having handful of user ids for beauty entities seperated by newline to start with.<br>
To fetch user-id for beauty brand - maccosmetics, check link: https://www.instagram.com/maccosmetics/?__a=1<br>
Json on this page has a field - "id":"319897212"
To fetch user-id for beauty retailer - sephora, check link: https://www.instagram.com/sephora/?__a=1
4. For every user-id specified in input file, it will fetch 80 suggested usernames at level 1 and then 80 further at level 2 
for each suggested name at level 1, giving a total of 6400 suggested usernames for each user-id. The level can be specified in code if 
needed to be increased further.
5. All the suggested usernames derived at step 3 are written to a file: suggested_accounts.txt
6. Module takes the suggested_accounts.txt as input and fetch profile data for every suggested username. Sucesfully processed usernames 
will be written to file: processed.txt and the ones ending up in error will be written to error.txt.