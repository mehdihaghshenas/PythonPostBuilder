from PIL import Image, ImageDraw, ImageFont

# Define the text for each slide
slides_text = [
    {
        "title": "Exploring .NET 8 and Python: \n A Developer's Perspective",
        "content": "Hey LinkedIn community! 👋\n\nAs someone who has had the pleasure of working \n extensively with both .NET and Python, I wanted \nto share my thoughts on the recent advancements \n in .NET 8 and how it stacks up against Python."
    },
    {
        "title": ".NET 8 Highlights",
        "content": "• Performance Improvements\n• Native AOT (Ahead-of-Time) Compilation\n• Enhanced Cross-Platform Capabilities"
    },
    {
        "title": "Python's Strengths",
        "content": "• Simplicity and Readability\n• Extensive Libraries and Community Support\n• Versatility"
    },
    {
        "title": "Flashback to Insightful Video",
        "content": "I recently watched an insightful video that dives deep into the evolution and capabilities of .NET. Check it out here: [The Evolution of .NET](https://www.youtube.com/watch?v=ukwFiwKZnpU&t=224s)."
    },
    {
        "title": "My Take & What Do You Think?",
        "content": "While .NET 8 is pushing the envelope with performance and cross-platform support, Python continues to shine with its simplicity and broad application spectrum.\n\nI'm curious to hear your thoughts! Have you worked with .NET 8 or Python recently? What are your experiences and preferences? Let's discuss in the comments!\n\n#DotNet8 #Python #SoftwareDevelopment #Programming #TechDiscussion"
    }
]

# Define the size of each slide
width, height = 1080, 1080

# Create a list to store the images
slides_images = []

# Define fonts (using default PIL fonts as placeholders)
title_font = ImageFont.truetype("./DejaVuSans/DejaVuSans-Bold.ttf", 60)
content_font = ImageFont.truetype("./DejaVuSans/DejaVuSans.ttf", 40)

for slide in slides_text:
    # Create a blank image with white background
    img = Image.new('RGB', (width, height), color=(255, 255, 255))
    d = ImageDraw.Draw(img)

    # Add title
    d.text((50, 50), slide["title"], font=title_font, fill=(0, 0, 0))

    # Add content
    d.text((50, 150 + (len(slide["title"].split('\n'))-1)*40),
           slide["content"], font=content_font, fill=(0, 0, 0),)

    # Append the image to the list
    slides_images.append(img)

slides_images[0].show()
slides_images[1].show()
slides_images[2].show()
slides_images[3].show()
slides_images[4].show()

# Save images to files
slide_filenames = []
for i, img in enumerate(slides_images):
    filename = f"./images/slide_{i+1}.png"
    img.save(filename)
    slide_filenames.append(filename)

print(slide_filenames)
