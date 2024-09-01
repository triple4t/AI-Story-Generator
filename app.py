from openai import OpenAI
import urllib.request  
from PIL import Image
import streamlit as st
 
import os
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

client = OpenAI()

def generate_image(image_description):
    response = client.images.generate(
        model="dall-e-3",
        prompt=image_description,
        n=1,
        size="1024x1024"  
    )

   
    image_url = response.data[0].url

   
    urllib.request.urlretrieve(image_url, 'img.png')

    img = Image.open("img.png")
    return img

st.title('Storybook')

story = """
---
Once upon a time in a forest, there was a speedy rabbit named Hare who always boasted about how fast he could run. His friend, Tortoise, was slow and steady.

---
One day, Hare challenged Tortoise to a race. Confident in his speed, Hare was sure he would win easily.

---
The race began, and Hare quickly ran far ahead of Tortoise. Seeing how slow Tortoise was, Hare decided to take a nap under a tree.

---
Meanwhile, Tortoise kept moving steadily and consistently. He passed the sleeping Hare without stopping.

---
When Hare woke up, he saw Tortoise near the finish line. Hare ran as fast as he could, but it was too late. Tortoise crossed the finish line and won the race. The forest animals cheered for Tortoise, celebrating his victory through perseverance and determination.
"""

images = []

if st.button('Generate Storybook'):
    pages = story.split('---')

    descriptions = [
        "A speedy rabbit named Hare boasting about his speed to a slow and steady tortoise named Tortoise in a forest.",
        "Hare confidently challenging Tortoise to a race, with Hare looking sure of his win and Tortoise accepting the challenge.",
        "The race begins, Hare quickly running far ahead of Tortoise and deciding to take a nap under a tree.",
        "Tortoise moving steadily and consistently, passing the sleeping Hare without stopping.",
        "Hare waking up and seeing Tortoise near the finish line, running fast but too late as Tortoise crosses the finish line with the forest animals cheering."
    ]

    for i, (page, description) in enumerate(zip(pages, descriptions)):
        st.subheader(f'Page {i+1}')
        st.write(page.strip())
        img_description = description
        
        if img_description:
            img = generate_image(img_description)
            images.append(img)
            st.image(img)

    if images:
        st.title('Generated Storybook')
        for i, img in enumerate(images):
            st.subheader(f'Page {i+1}')
            st.image(img)
