#!/usr/bin/env python3
import datetime
import os


def create_post():
    title = input("Post Title: ")
    categories = input("Category: ")

    # Get current date and time
    now = datetime.datetime.now().astimezone()

    # Format for filename: yyyy-mm-dd
    date_filename = now.strftime("%Y-%m-%d")

    # Format for frontmatter: yyyy-mm-d hh:mm:ss +zzzz
    # Using %-d for day without leading zero on macOS/Linux
    date_frontmatter = now.strftime("%Y-%m-%-d %H:%M:%S %z")

    # Format title for filename: lowercase and spaces replaced by dashes
    title_filename = title.lower().replace(" ", "-")
    filename = f"{date_filename}-{title_filename}.markdown"
    filepath = os.path.join("_posts", filename)

    # Prepare frontmatter content
    content = f"""---
layout: post
title:  {title}
date:   {date_frontmatter}
categories: {categories}
---
"""

    # Ensure _posts directory exists
    os.makedirs("_posts", exist_ok=True)

    # Write the file
    with open(filepath, "w") as f:
        f.write(content)

    print(f"Post created successfully: {filepath}")


if __name__ == "__main__":
    create_post()
