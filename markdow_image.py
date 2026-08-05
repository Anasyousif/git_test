def create_markdown_image(alt_text):
    markdown_part1 = f"![{alt_text}]"
    def inner_func(url):
        url = url.replace("(", "%28")
        url = url.replace(")", "%29")
        markdown_part2 = f"{markdown_part1}({ url})"
        def innermost(title=None):
            if title is None:
                return markdown_part2
            return f'{markdown_part2[:-1]} "{title}")'
                
        return innermost

    return inner_func    
