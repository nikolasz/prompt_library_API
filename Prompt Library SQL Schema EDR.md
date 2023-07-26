

![[Pasted image 20230725223047.png]]



## # Create a new directed graph
G = nx.DiGraph()

# Add nodes for entities
entities = schema['entities'].keys()
G.add_nodes_from(entities)

# Add edges for relationships
for relationship, rel_type in schema['relationships'].items():
    entity1, entity2 = relationship.split('-')
    if 'via' in rel_type:
        junction_table = rel_type.split(' ')[-1]
        G.add_edge(entity1, junction_table, label="One-to-Many")
        G.add_edge(junction_table, entity2, label="Many-to-One")
    else:
        G.add_edge(entity1, entity2, label=rel_type)

# Draw the graph
pos = nx.spring_layout(G)  # positions for all nodes
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=3000)
edge_labels = nx.get_edge_attributes(G, 'label')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

# Show the plot
plt.show()


# Revised schema with parent-child relationships for prompts

schema = {
  "entities": {
    "Prompt": {
      "Prompt_ID": "Primary Key",
      "Prompt_Text": "Text",
      "Subcategory_ID": "Foreign Key",
      "Source_ID": "Foreign Key",
      "Status": "Text",
      "Parent_ID": "Foreign Key (self-referencing)"
    },
    "Category": {
      "Category_ID": "Primary Key",
      "Category_Name": "Text",
      "Description": "Text"
    },
    "Subcategory": {
      "Subcategory_ID": "Primary Key",
      "Subcategory_Name": "Text",
      "Description": "Text",
      "Category_ID": "Foreign Key"
    },
    "Keyword": {
      "Keyword_ID": "Primary Key",
      "Keyword_Name": "Text"
    },
    "Prompt_Keyword": {
      "Prompt_ID": "Foreign Key",
      "Keyword_ID": "Foreign Key"
    },
    "Usage": {
      "Usage_ID": "Primary Key",
      "Prompt_ID": "Foreign Key",
      "User_ID": "Foreign Key",
      "Access_Date": "DateTime"
    },
    "Source": {
      "Source_ID": "Primary Key",
      "Source_Name": "Text",
      "Source_Type": "Text",
      "Description": "Text"
    }
  },
  "relationships": {
    "Prompt-Subcategory": "Many-to-One",
    "Subcategory-Category": "Many-to-One",
    "Category-Subcategory": "One-to-Many",
    "Prompt-Keyword": "Many-to-Many via Prompt_Keyword",
    "Keyword-Prompt": "Many-to-Many via Prompt_Keyword",
    "Prompt-Source": "Many-to-One",
    "Source-Prompt": "One-to-Many",
    "Prompt-Usage": "One-to-Many",
    "Usage-Prompt": "Many-to-One",
    "Prompt-Prompt": "One-to-Many (self-referencing)"
  }
}

schema
