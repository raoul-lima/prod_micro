# prod_micro
micro service produit
acces: localhost/api/product_items/

terminale:
curl -X PATCH http://127.0.0.1:8000/api/product_items/1 -H 'Content-Type: application/json' -d '{"product_price":600}'

 curl -X "DELETE" http://127.0.0.1:8000/api/product_items/1    
 
 curl -X GET http://127.0.0.1:8000/api/product_items/2/   
 
 curl -X POST -H "Content-Type: application/json" http://127.0.0.1:8000/api/product-items/ -d "{\"product_name\":\"test\",\"product_price\":\"1000\"}"
