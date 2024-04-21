import wikipedia as wiki
import pickle
import os


def remove_illegal_characters(original_title):
    illegal_characters = "/\\:*?\"<>|"
    title = original_title
    for char in illegal_characters:
        title = title.replace(char, "")
    return title

def save_and_load_wiki_pages(topics, results_per_subject=1):
    path = os.path.join(".", "wiki")
    for topic in topics:
        for article_dict in load_wiki_pages(topic, number_of_results=results_per_subject):
            # path = os.path.dirname(os.path.abspath(__file__))
            title = remove_illegal_characters(article_dict["title"])
            file = open(file=os.path.join(path, title),mode='wb')
            pickle.dump(article_dict, file)
            file.close()


def load_wiki_pages(topic, number_of_results=500):
    titles = wiki.search(query=topic, results=number_of_results)
    for title in titles:
        try:
            page = wiki.page(title)
            yield {
                'title': page.title,
                'content': page.content,
                'url': page.url,
            }
        except wiki.exceptions.WikipediaException:
            continue
        except Exception as e:
            print(f'Exception encountered :\n{str(e)}')


KEYWORDS = ["South America","Europe", "Asia", "Africa","North America"]

save_and_load_wiki_pages(KEYWORDS, results_per_subject=300)
