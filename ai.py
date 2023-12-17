import streamlit as st
import pandas as pd
import openai

# Set your OpenAI API key
openai.api_key = "your_api_key_here"  # Replace with your actual API key

# Sample datasets (replace with your actual datasets)
male_dataset = pd.DataFrame({
    'Name': ['John', 'Bob', 'Charlie'],
    'Email': ['john@example.com', 'bob@example.com', 'charlie@example.com'],
    'Phone': ['123-456-7890', '987-654-3210', '555-123-4567'],
    'Company': ['ABC Corp', 'XYZ Inc', '123 Industries']
})

female_dataset = pd.DataFrame({
    'Name': ['Alice', 'Eve', 'Grace'],
    'Email': ['alice@example.com', 'eve@example.com', 'grace@example.com'],
    'Phone': ['111-222-3333', '444-555-6666', '777-888-9999'],
    'Company': ['Tech Solutions', 'Data Innovations', 'Software Co']
})

def generate_email_content(name, email, phone, company, gender):
    prompt = f"Generate an email for {name}, a {gender} at {company}. Contact them at {email} or {phone}."
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    return response["choices"][0]["text"]

def main():
    st.title("Email Generator App")

    # Choose dataset
    dataset_choice = st.radio("Select dataset:", ["Male Dataset", "Female Dataset"])
    selected_dataset = male_dataset if dataset_choice == "Male Dataset" else female_dataset

    # Display selected dataset
    st.subheader("Selected Dataset:")
    st.write(selected_dataset)

    # Select a user
    selected_user_index = st.selectbox("Select a user:", selected_dataset.index)

    # Extract user information
    user_info = selected_dataset.loc[selected_user_index]
    name, email, phone, company = user_info['Name'], user_info['Email'], user_info['Phone'], user_info['Company']
    gender = "male" if dataset_choice == "Male Dataset" else "female"

    # Generate email content
    email_content = generate_email_content(name, email, phone, company, gender)

    # Display generated email content
    st.subheader("Generated Email Content:")
    st.write(email_content)

    # Add functionality to send the email (implementation depends on your email service)

if __name__ == "__main__":
    main()
