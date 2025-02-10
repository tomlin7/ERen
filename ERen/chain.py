from parser import PARSER

from llm import LLM
from prompt import PROMPT

CHAIN = PROMPT | LLM | PARSER
