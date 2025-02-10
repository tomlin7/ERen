from langchain.prompts import PromptTemplate

PROMPT = PromptTemplate(
    template="""Generate an ER diagram using the standard Entity Relationship model notation in valid DOT format
    and the corresponding SQL schema (Oracle) based on the following description: "{context}".
    The ER diagram should include:
    - Entities as rectangles (strong entities) or double-bordered rectangles (weak entities)
    - Attributes as ovals (single-valued attributes) or double-bordered ovals (multi-valued attributes), dashed ovals for derived attributes
    - Underline text in attributes that are part of the primary key
    - Relationships as diamonds
    - Mark cardinality constraints on connecting lines (e.g., 1, M, N)
    - Double lines for total participation, single lines for partial (don't use arrows)

    Example dot_code output (demonstrating each feature):
    digraph ER {{
        // Graph settings
        node [shape=box, style=filled, fillcolor=lightblue];  // lightblue for entities
        edge [dir=none];
        
        // Entities
        Employee [label="Employee"];
        Project [label="Project"];
        
        // Relationship
        Works_On [shape=diamond, label="Works_On"];
        
        // here's an example of each attribute type
        Emp_ID [shape=ellipse, label=<<u>Emp_ID</u>>];      // Primary key
        Phone [shape=ellipse, peripheries=2];               // Multi-valued
        Age [shape=ellipse, style="dashed"];                // Derived
        Hours [shape=ellipse];                              // Regular attribute
        
        // Relationship connections
        Employee -> Works_On [label="N"];
        Works_On -> Project [label="M"];
        
        // Attribute connections
        Employee -> Emp_ID;
        Employee -> Phone;
        Employee -> Age;
        Works_On -> Hours;
        
        label = "\n\nSimple relevant title here";
        fontsize=20;
    }}
    
    Rule: Don't create entities instead of relationships, and don't create relationships instead of entities, make sure.
    Rule: Entities must be connected with relationships, and attributes must be connected to entities or relationships.
    Rule: Underlined attributes use html tags (they are not a string).
            
    Return the output strictly as a JSON object with the following structure:
    {{
        "dot_code": "<DOT format string>",
        "sql_code": "<SQL schema string>"
    }}""",
    input_variables=["context"],
)
