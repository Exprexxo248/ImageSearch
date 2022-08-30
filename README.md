# ImageSearch
Simple Image Search Machine using EfficientNet with PCA
This is the demo Search Machine for Shoe.

# Step to create a simple search engine using your template app
## Crawl Image

Mini Image Crawl program from website: [Bitis's Website](https://bitis.com.vn/). With this module, I recommend using the Selenium tool to crawl information from dynamic web pages.

I came up with a way to do this crawl, I use ChromeDriverManager as Selenium Driver. For each div containing objects, I get the link of each product, then reach each product's page and get information from the tags. But this approach soon is blocked by anti-DDOS mechanism. 
Therefore I have redirected only to get information from the aggregate product page. But it also has a problem when requesting the website, it need time to load the images when scrolling, so I have a solution to prevent that problem by using `driver.implicitly_wait()` after each scroll and information saving action. 
Note: In this demo, I just take the links of the images and then process them sequentially, no need to download all the images, just the links of the images.
The `ShoeObject` has the structure:
Object Format:
```json
{
  _id : "1209380129204",
  name: "Hunter X1"
  image_url: "https://..."
}

mapping format:
{
  "http://....1" : 1,
  "http://....2" : 2,
  ...
}
```

```
./
...
├── crawler
│  ├── crawler.py
│  ├── extractor.py
│  ├── features.pkl
│  ├── keys.pkl
│  ├── mapping.json
│  └── objects.json
...
```
## Extractor
After crawling the necessary information, the next step is to extract the features of the images using the appropriate model. The model used is EfficientnetB4, which has 1792 features, stored as a 1792-dimensional array. These vectors are then saved in **`vectors.pkl`** and names are stored in: **`feature.pkl`**. 

Tips: You can replace the feature extraction model by changing **`self.model`** present in class **`MyEfficientModel`** and **`FeatureExtractor`** and keep in mind that these two models must be the same.

***
# Search Engine 
I re-use the template app from our past development with a nearly similar to that structure.
```
.
├── app
│  ├── core
│  │  └── config.py
│  ├── database
│  │  └── db.py
│  ├── main.py
│  ├── models
│  │  └── item.py
│  ├── routers
│  │  └── item.py
│  ├── service
│  │  ├── crawler
│  │  ├── feature_extractor.py
│  │  ├── file_handle.py
│  │  └── model_results_processing.py
│  ├── static
│  │  └── Data
│  │     ├── objects.json
│  │     ├── vector_features.pkl
│  │     └── vector_tokens.pkl
│  ├── temp
│  │  └── Crawler
│  │     └── Data
│  │        └── tmp
│  └── test_main.http
├── auto_scrawl.sh
├── crawler
│  ├── crawler.py
│  ├── extractor.py
│  ├── features.pkl
│  ├── keys.pkl
│  ├── mapping.json
│  └── objects.json
├── docker-compose.yml
├── Dockerfile
├── README.md
└── requirements.txt
```
Note: In Python, the `__init__.py` file will make the folder become a module, which will help you a lot in importing files and modules.
The changes that I have made are to reuse the template.
## Database
In the NFT case, we use the Rarible API to retrieve the information of each NFT item. But in this demo, we use the demo database loaded from file: `./static/Data/objects.json`.



## Core/Config file 
