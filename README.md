# Django Postgrest

This repo, is created to demonstrate a solution to slow and heavily pulled endpoints for a production django project

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)
[![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

License: MIT

## Settings

Moved to [settings](http://cookiecutter-django.readthedocs.io/en/latest/settings.html).

## Basic Commands

### Setting Up Your Users

- To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

- To create a **superuser account**, use this command:

      $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

### Type checks

Running type checks with mypy:

    $ mypy django_postgrest

### Test coverage

To run the tests, check your test coverage, and generate an HTML coverage report:

    $ coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html

#### Running tests with pytest

    $ pytest

### Live reloading and Sass CSS compilation

Moved to [Live reloading and SASS compilation](https://cookiecutter-django.readthedocs.io/en/latest/developing-locally.html#sass-compilation-live-reloading).

## Deployment

The following details how to deploy this application.


## Setup locally
#### Postgresql
you need a postgresql-15 locally.
you can simple create a postgresql connection with by docker compose

```docker compose up```

#### Initial Data

To generate initial data, run the `create_initial_data` as below:

```python manage.py runscript create_initial_data```


#### Create ShopProducts View in Postgresql

Run the below command:
```
-- View: public.shop_products

-- DROP VIEW public.shop_products;

CREATE OR REPLACE VIEW public.shop_products
 AS
 SELECT product.name,
    product.description,
    product.price,
    product.discount,
    product.inventory,
    product.shop_id
   FROM shop_product product
  WHERE (product.shop_id IN ( SELECT shop_shop.id
           FROM shop_shop
          WHERE shop_shop.manager_id = (( SELECT authtoken_token.user_id
                   FROM authtoken_token
                  WHERE authtoken_token.key::text = regexp_replace(current_setting('request.headers'::text)::json ->> 'authorization'::text, 'Token '::text, ''::text))))) AND NOT product.is_archived;

ALTER TABLE public.shop_products
    OWNER TO benchmark;

GRANT ALL ON TABLE public.shop_products TO benchmark;
GRANT SELECT ON TABLE public.shop_products TO postgrest;
```

#### Test the app

Now you can run some tests. so run the `gunicorn` with 4 worker:

```
gunicorn config.wsgi:application --workers 4 --bind 0.0.0.0:8000 --log-level critical
```

And `Postgrest`:
```postgrest ./postgrest.conf```

### Load Test
The load testing is done with apache benchmark `ab`, with 100 concurrency and totally 10000 requests.
To run the test on gunicorn run the below command:
```ab ```

##### Gunicorn results:
```
Server Software:        gunicorn
Server Hostname:        localhost
Server Port:            8000

Document Path:          /shop/2001/products/
Document Length:        107146 bytes

Concurrency Level:      100
Time taken for tests:   37.131 seconds
Complete requests:      10000
Failed requests:        0
Total transferred:      1075100000 bytes
HTML transferred:       1071460000 bytes
Requests per second:    269.32 [#/sec] (mean)
Time per request:       371.307 [ms] (mean)
Time per request:       3.713 [ms] (mean, across all concurrent requests)
Transfer rate:          28275.88 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.2      0       3
Processing:    18  369  30.7    364     498
Waiting:       16  369  30.7    364     498
Total:         21  369  30.6    364     498

Percentage of the requests served within a certain time (ms)
  50%    364
  66%    372
  75%    380
  80%    386
  90%    406
  95%    428
  98%    445
  99%    451
 100%    498 (longest request)
```

##### Postgrest results:
```
Server Software:        postgrest/11.1.0
Server Hostname:        localhost
Server Port:            3000

Document Path:          /shop_products?select=name,description,price,discount,inventory&shop_id=eq.2001
Document Length:        107743 bytes

Concurrency Level:      100
Time taken for tests:   10.050 seconds
Complete requests:      10000
Failed requests:        0
Total transferred:      1080030000 bytes
HTML transferred:       1077430000 bytes
Requests per second:    995.02 [#/sec] (mean)
Time per request:       100.500 [ms] (mean)
Time per request:       1.005 [ms] (mean, across all concurrent requests)
Transfer rate:          104946.91 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.4      0      16
Processing:     4  100  82.6     77     881
Waiting:        2   98  82.5     75     880
Total:          5  100  82.6     77     881

Percentage of the requests served within a certain time (ms)
  50%     77
  66%    105
  75%    130
  80%    149
  90%    205
  95%    264
  98%    340
  99%    412
 100%    881 (longest request)
```
