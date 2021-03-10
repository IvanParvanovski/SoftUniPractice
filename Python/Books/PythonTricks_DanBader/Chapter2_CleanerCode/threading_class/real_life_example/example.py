import time
import requests
import concurrent.futures


img_urls = [
    'https://images.unsplash.com/photo-1516117172878-fd2c41f4a759',
    'https://images.unsplash.com/photo-1532009324734-20a7a5813719',
    'https://images.unsplash.com/photo-15244229656589-6633a470097c',
    'https://images.unsplash.com/photo-1530224264768-7ff8c1789d79',
    'https://images.unsplash.com/photo-1564135624576-c5c88640f235',
    'https://images.unsplash.com/photo-1522364723953-452d3431c267',
]


def download_image(image_url):
    img_bytes = requests.get(image_url).content
    img_name = image_url.split('/')[3]
    img_name_with_format = f'{img_name}.jpg'
    with open(img_name_with_format, 'wb') as img_file:
        img_file.write(img_bytes)
        print(f'{img_name} was downloaded...')


start = time.perf_counter()

# with concurrent.futures.ThreadPoolExecutor() as executor:
#     downloaded_images = list()
#     for img_url in img_urls:
#         downloaded_images.append(executor.submit(requests.get, img_url))
#
#     for downloaded_img in concurrent.futures.as_completed(downloaded_images):
#         img_name = downloaded_img.split()

with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(download_image, img_urls)


finish = time.perf_counter()
print(f'Finished in {finish - start} seconds')
