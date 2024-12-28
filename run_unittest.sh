#! /bin/bash

python3 -m unittest easy_gmssl/easy_random_data_test.py
python3 -m unittest easy_gmssl/easy_sm2_key.py
python3 -m unittest easy_gmssl/easy_sm2_sign_test.py
python3 -m unittest easy_gmssl/easy_sm3_key_test.py
python3 -m unittest easy_gmssl/easy_sm4_test.py
