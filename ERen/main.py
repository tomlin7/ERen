import graphviz
import streamlit as st
from chain import CHAIN
from constants import *

st.title("ERen - ER diagrams in seconds!")
st.write(
    "ChatGPT (or similar) fails to generate proper ER diagrams, ERen solves this issue!"
)
st.write("Enter a simple or detailed description of the ER diagram as you need.")

description = st.text_input(
    "Description:",
    placeholder="eg. Employee working on projects",
)

if st.button("Generate Diagram and SQL"):
    if description.strip():
        with st.spinner("Generating..."):
            result = CHAIN.invoke(description)
            dot_code = result.get("dot_code", "")
            sql_code = result.get("sql_code", "")

            if dot_code:
                st.subheader("ER Diagram:")
                # st.graphviz_chart(dot_code, use_container_width=True)

                graph = graphviz.Source(dot_code)
                svg_content = graph.pipe(format="svg").decode("utf-8")
                st.image(
                    svg_content,
                    use_container_width=True,
                    caption="long press to save image",
                )
            else:
                st.error("Failed to generate ER diagram.")

            if sql_code:
                st.subheader("SQL:")
                st.code(sql_code, language="sql")
            else:
                st.error("Failed to generate SQL schema.")

            if dot_code:
                with st.expander("See how the diagram is generated..."):
                    st.info(
                        "To see how the diagram is made, copy the code below to [any DOT viewer](https://edotor.net) (click to open)"
                    )
                    st.code(dot_code, language="dot")
    else:
        st.warning("Please enter a description.")

    st.divider()

    st.image(
        PIC,
        use_container_width=True,
        caption="*Attack on Titan Reference",
    )
