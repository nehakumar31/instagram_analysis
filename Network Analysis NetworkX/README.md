# Network Analysis
1. Analyse the beauty entities network with input as Nodes and Relationships
  **Nodes** => Node Name and its label

  | Id  | Label |
  | ---------------| ----------- |
  | maccosmetics   | Brand  |
  | sarah   | Influencer   |
  
  **Relationship** => Directed relations from a beauty entity as source to its suggested profile as target
  | Source  | Target |
  | --------| ----------- |
  | maccosmetics   | fentybeauty  |
  | sarah   | kate        |
  | maccosmetics   | sarah  |
  
  
3. Metric to measure entity strength: 
   Betweenness centrality
   Closeness centrality
   In-Degree centrality
   Out-Degree centrality
   Page rank   
   

# Tech/Framework
1. Coding Language - python
2. Python NetworkX

# Execution Details
1. Module has execution results for input files maintained in dir: /data/
2. Environemnt requirements are specified in env_requirements.txt file
3. python main.py --nodes_file /data/AllNodes --relations_file /data/Relationship*