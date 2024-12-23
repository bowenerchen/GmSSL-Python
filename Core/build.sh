#! /bin/bash



rm -rf build_gmssm/*
rm -rf gmssl_libs/*

cd build_gmssl && cmake -DCMAKE_INSTALL_PREFIX=../gmssl_libs ../GmSSL-3.1.1 && make -j2 && make install
