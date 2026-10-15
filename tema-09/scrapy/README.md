# [Scrapy](https://scrapy.org/)

Example of how to scrape a page.

## Clean html or visit the [source](http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html)

```html
<html lang="en-us" class="no-js">
   <body id="default" class="default">
       <article class="product_page">
           <div class="row">
               <div class="col-sm-6 product_main">
                   <h1>A Light in the Attic</h1>
                   <p class="price_color">£51.77</p>
                   <p class="instock availability">
                       <i class="icon-ok"></i>
                       In stock (22 available)
                   </p>
               </div>
           </div>
           <p>Description ... ... ... ... ...</p>
       </article>
   </body>
</html>
```

## Docker

### Build the image

```bash
$ docker build -t ugr_sai_scrapy .
```

### Run the image

```bash
$ docker run -it -v ${PWD}:/opt/project ugr_sai_scrapy bash
```

### Start new project

```bash
$ scrapy startproject ugr_sai .
```

### Run the example

```bash
$ clear; scrapy crawl --nolog books
```

## docker-compose

### Build the image

```bash
$ docker-compose build scrapy
```

### Run the image

```bash
$ docker-compose run scrapy bash
```

### Start new project

```bash
$ scrapy startproject ugr_sai .
```

### Run the example

```bash
$ clear; scrapy crawl --nolog books
```
