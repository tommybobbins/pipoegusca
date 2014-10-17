#!/bin/bash

/usr/bin/curl -o /tmp/request.html -s http://433host:80/switchsocket/energenie/1/2/${1}/ --user foo:bar >/tmp/request_output.txt 2>&1
