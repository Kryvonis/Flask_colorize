#!/bin/bash


curl -H "Content-Type: application/json"\
 -X POST "http://127.0.0.1:5000/" \
 -d '{"src":"/home/kryvonis/PycharmProjects/image_test/images/imgpsh_fullsize.png",
 "color":"102,51,0","method":"overlay"}'