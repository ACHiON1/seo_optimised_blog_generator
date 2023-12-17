import streamlit as st
import openai

# Set your OpenAI API key
openai.api_key = "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"  # Replace with your actual API key

def generate_content(prompt):
    linkedin_text = openai.Completion.create(
        engine="davinci",
        prompt=f"Create a LinkedIn post about a book:\n{prompt}",
        max_tokens=100
    ).choices[0].text.strip()

    facebook_text = openai.Completion.create(
        engine="davinci",
        prompt=f"Create a Facebook post about a book:\n{prompt}",
        max_tokens=100
    ).choices[0].text.strip()

    instagram_text = openai.Completion.create(
        engine="davinci",
        prompt=f"Create an Instagram post about a book:\n{prompt}",
        max_tokens=100
    ).choices[0].text.strip()

    tweet_text = openai.Completion.create(
        engine="davinci",
        prompt=f"Create a tweet about a book:\n{prompt}",
        max_tokens=100
    ).choices[0].text.strip()

    linkedin_image = generate_image(prompt)
    facebook_image = generate_image(prompt)
    instagram_image = generate_image(prompt)

    return {
        "LinkedIn": {"text": linkedin_text, "image": linkedin_image},
        "Facebook": {"text": facebook_text, "image": facebook_image},
        "Instagram": {"text": instagram_text, "image": instagram_image},
        "Twitter": {"text": tweet_text}
    }

def generate_image(prompt):
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="256x256",
    )
    image_url = response["data"][0]["url"]
    return image_url

def main():
    st.title("Social Media Content Generator")

    # Get user input
    prompt = st.text_area("Enter a prompt for the book:")

    # Generate content
    if st.button("Generate Content"):
        with st.spinner("Generating content..."):
            content = generate_content(prompt)

            # Display content
            st.subheader("LinkedIn Post:")
            st.write(content["LinkedIn"]["text"])
            st.image(content["LinkedIn"]["image"], caption="LinkedIn Image", use_column_width=True)

            st.subheader("Facebook Post:")
            st.write(content["Facebook"]["text"])
            st.image(content["Facebook"]["image"], caption="Facebook Image", use_column_width=True)

            st.subheader("Instagram Post:")
            st.write(content["Instagram"]["text"])
            st.image(content["Instagram"]["image"], caption="Instagram Image", use_column_width=True)

            st.subheader("Twitter Tweet:")
            st.write(content["Twitter"]["text"])

if __name__ == "__main__":
    main()
