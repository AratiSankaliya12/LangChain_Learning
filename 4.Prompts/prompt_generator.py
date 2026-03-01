from langchain_core.prompts import PromptTemplate

template = PromptTemplate(
    input_variables=["paper", "style", "length"],
    template=(
        "Explain the research paper '{paper}' in a {style} manner. "
        "The explanation should be {length}."
    ),
    validate_template=True,
)

template.save("template.json")
