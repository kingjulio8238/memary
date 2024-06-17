from icrawler.builtin import GoogleImageCrawler
import os

google_crawler = GoogleImageCrawler(storage={'root_dir': 'images'})

def get_logo(model_name):
    search_query = f"{model_name} logo"
    google_crawler.crawl(keyword=search_query, max_num=1)

llm_models = ["gpt-3.5-turbo"]
vision_models = ["gpt-4-vision-preview"]

logos = []
logo_idx = 0
for model in llm_models:
    logo_idx += 1
    get_logo(model)
    logos.append(f"images/{logo_idx:06}.png")

# os.removedirs("images")