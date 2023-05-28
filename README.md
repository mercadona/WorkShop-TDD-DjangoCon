# TDD applied to Django API development

## Setup the environment

### Repl.it

Just click on the following button and login/signup:

[![Run on Repl.it](https://replit.com/badge/github/mercadona/workshop-tdd-django)](https://replit.com/new/github/mercadona/workshop-tdd-django)

In case of missing `pytest` command just open a `Shell` tab and follow the "Local setup" steps.

### Local setup

```bash
python3 -m venv venv
. venv/bin/activate 
pip install -r requirements.txt
```

For some macOS if _pip_ install fails run this command and then repeat the setup:

```bash
export C_INCLUDE_PATH=/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.8/Headers
```

## Run tests

```bash
pytest
```

## Work files

- [carts/tests.py](carts/tests.py): Tests
- [carts/views.py](carts/views.py): Implementation
- [carts/urls.py](carts/urls.py): List of API urls

## Exercises

Remember:
- Write a test
- Run all tests and see it fail
- Write the minimum code to pass the test
- Run all tests and see it pass
- Refactor the code
- Repeat

### Exercise 0.0: Retrieve the products in the cart when is empty

- [ ] Write a new test case for the `GET /cart/` endpoint
- [ ] Expect the response to be a `200` status code
- [ ] Expect the response.json() to be 
```json
{
  "lines": []
}
```
- [ ] Run the tests and see it fail with `AssertionError: assert 404 == 200`
- [ ] Implement the `GET /cart/` endpoint with a hardcoded response
- [ ] Add the following code to `carts/views.py`:
```python
def cart_detail(request):
    return JsonResponse(data={"lines": []})
```
- [ ] Run the tests and see it pass
- [ ] Refactor the code
- [ ] Run the tests and see it pass
- [ ] Repeat

### Exercise 0.1: Retrieve the products in the cart when has products

- [ ] Write a new test case for the `GET /cart/` endpoint
- [ ] Add a product to the cart `CartLine.objects.create(reference="50776", quantity=5)`
- [ ] Expect the response to be a `200` status code
- [ ] Expect the response.json() to be 
```json
{
  "lines": [
    {
      "reference": "50776",
      "quantity": 5
    }
  ]
}
```
- [ ] Run the tests and see it fail with `AssertionError: assert {'lines': []} == {'lines': [{'reference': '50776', 'quantity': 5}]}`
- [ ] Fix the implementation to retrieve the products in the cart
- [ ] Run the tests and see it pass
- [ ] Refactor the code
- [ ] Run the tests and see it pass
- [ ] Repeat

### Exercise 1: Add products to a cart

- [ ] Write a new test case for the `POST /cart/products/add/` endpoint
- [ ] Use the following data to add a product to the cart
```json
{
  "reference": "33333",
  "quantity": 2
}
```
- [ ] Expect the response to be a `200` status code
- [ ] Expect the response.json() to be 
```json
{
  "lines": [
    {
      "reference": "33333",
      "quantity": 2
    }
  ]
}
```
- [ ] Run the tests and see it fail
- [ ] Write the minimum code to pass the test
- [ ] Run the tests and see it pass
- [ ] Refactor the code
- [ ] Run the tests and see it pass
- [ ] Repeat

### Exercise 2: Substract products from a cart

* Given a cart with 2 products, one with reference `33333` and quantity `4` and another with reference `11111` and quantity `2`.
* When I substract a product with reference `33333` and quantity `2`.
* Then the cart should have 2 products, one with reference `33333` and quantity `2` and another with reference `11111` and quantity `2`.

- [ ] Write a new test case for the `POST /cart/products/substract/` endpoint
- [ ] Use the following data to substract a product from the cart
```json
{
  "reference": "11111",
  "quantity": 2
}
```
- [ ] Expect the response.json() to be 
```json
{
  "lines": [
    {
      "reference": "33333",
      "quantity": 1
    },
    {
      "reference": "11111",
      "quantity": 2
    }
  ]
}
```

- [ ] Run the tests and see it fail
- [ ] Write the minimum code to pass the test
- [ ] Run the tests and see it pass
- [ ] Refactor the code
- [ ] Run the tests and see it pass
- [ ] Repeat

### Exercise 4: Add the total quantity of products in the cart

* Given a cart with 2 products, one with reference `33333` and quantity `4` and another with reference `11111` and quantity `1`.
* When I retrieve the cart
* Then the cart should have a total quantity of `5`.
* And the response should be
```json
{
  "lines": [
    {
      "reference": "33333",
      "quantity": 4
    },
    {
      "reference": "11111",
      "quantity": 1
    }
  ],
  "total_quantity": 5
}
```

- [ ] Run the tests and see it fail
- [ ] Write the minimum code to pass the test
- [ ] Run the tests and see it pass
- [ ] Refactor the code
- [ ] Run the tests and see it pass
- [ ] Repeat
 