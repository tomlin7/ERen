# ERen - ER diagrams from natural language queries

ERen is a tool to generate Entity Relationship Diagrams (ERDs) from natural language queries. It is designed to be used by software developers and students to quickly create ERDs from textual simple/detailed descriptions of the entities and relationships in a system.

ERen's frontend is a streamlit app that takes a natural language query as input from users and presents the ERD and SQL generated. It utilizes the [Graphviz](https://graphviz.org/) library for visualizing the ERD and saving it in PNG format.

## Features

- Simple natural language query as input
- Generates ERDs and SQL queries
- Fine tuned for generating accurate ERDs

## Usage

1. Run the Streamlit app: `streamlit run app.py`
2. Input your text description of entities and relationships
3. View ERD of the query, copy the generated SQL queries

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
