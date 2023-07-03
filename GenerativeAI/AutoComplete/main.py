import streamlit as st
from langchain.llms import HuggingFacePipeline

hf = HuggingFacePipeline.from_model_id(
    model_id="gpt2",
    task="text-generation",
    pipeline_kwargs={"max_new_tokens": 10},
)

def generate_text(prompt):
    generated_text = hf(prompt)
    return generated_text

def main():
    st.title("Autocomplete Demo")
    prompt = st.text_input("Enter your text:")
    generated_text = generate_text(prompt)

    # Display generated text in bold font
    st.markdown(f"{generated_text}")

if __name__ == "__main__":
    main()
