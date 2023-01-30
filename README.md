# OIDC Endpoint Test

## Key Generation

Source: https://www.scottbrady91.com/openssl/creating-rsa-keys-using-openssl

``` bash
openssl genrsa -out test.key 3072
openssl rsa -in test.key -pubout -out test.pub
```
