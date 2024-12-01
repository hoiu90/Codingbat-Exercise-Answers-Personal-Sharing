def make_tags(tag_name, tag_content):
    return f"<{tag_name}>{tag_content}</{tag_name}>"

print(make_tags("h1", "Hello, World!"))
print(make_tags("p", "This is a paragraph."))
print(make_tags("a", "Visit my website: www.example.com"))