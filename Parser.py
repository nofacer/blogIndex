import markdown
import os


def parse_article_info_from_name(filename):
    md = markdown.Markdown(extensions=['meta'])
    with open(filename) as f:
        data = f.read()
        md.convert(data)
        return md.Meta, data


def is_md(filename):
    if filename.split('.')[-1] == 'md':
        return True
    else:
        return False


def parse(dest_dir):
    result = []

    articles = list(filter(is_md, os.listdir(dest_dir)))
    for article in articles:
        article_path = os.path.join(dest_dir, article)
        article_info, data = parse_article_info_from_name(article_path)
        result.append((article_info, data))

    return result
