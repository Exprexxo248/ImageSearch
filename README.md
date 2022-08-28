# ImageSearch
Simple Image Search Machine using EfficientNet with PCA
This is the demo Search Machine for Shoe.

# Crawl Image
Mini Image Crawl program from website: [Bits's Website](https://bitis.com.vn/). With this module, I recommend you to use selenium tool to crawl information from dynamic web pages.

I came up with a way to do this crawl, I use ChromeDriverManager as Seleium Driver. For each div containing objects, I get the link of each product, then reach each product's page and get information from the tags. But this approach soon be blocked by anti-DDOS mechanism. 
Therefore I have redirected to only get information from the aggregate product page. But it also have a problem when request the website, it's need time to load the images when scroll, so I have a solution to prevent that problems by using `driver.implicitly_wait()` after each scroll and information saving action.
The `Shoeobject` have the structure:
Object Format:
```apib
{
  _id : "1209380129204",
  name: "Hunter X1"
  image_url: "https://..."
}

mapping_format:
{
  image_url : _id
}
```

```apib
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


# Search Engine 
I re-use the template app from our past development with the nearly similar with that structure.
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
│  ├── offline_extractor.py
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
Note: In Python, the `__init__.py` file will make the folder become a module, that will help you a lot in import file and module.
The changed that I have made to reuse the template.
## Database
In the NFT case, we use the Rarible API, But in this demo, we use the demo database
## Core/Config file 
