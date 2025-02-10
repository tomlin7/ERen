from langchain_core.output_parsers import JsonOutputParser
from pydantic import BaseModel, Field


class ERModel(BaseModel):
    dot_code: str = Field(..., description="DOT format string for the ER diagram")
    sql_code: str = Field(..., description="SQL schema string")


PARSER = JsonOutputParser(pydantic_object=ERModel)
