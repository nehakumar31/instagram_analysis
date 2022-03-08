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
2. Python Neo4j Graph database, Neo4j Graph Data Science library
3. Cypher query language for analysis
4. Reference to Cypher manual: https://neo4j.com/developer/cypher/
5. Reference to Neo4j gds library: https://neo4j.com/docs/graph-data-science/current/

# Execution Details
1. Module has a file NetworkAnalysis.pdf containing few queries and their output for analysis done on Network graph
2. Environment requirements are specified in env_requirements.txt file
3. python main.py --nodes_file ./data/AllNodes --relations_file ./data/Relationship* --username **** --password ****