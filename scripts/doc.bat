@echo off

rem this script generates the markdown documentation of our proto3 messages
rem and services. in order to run this script you need to have the protoc-gen-doc
rem plugin installed: https://github.com/pseudomuto/protoc-gen-doc
rem this script should be executed from the root folder of this project:
rem \scripts\doc.bat

del /s /q docs\*.md

protoc -I.\proto --doc_out=. --doc_opt=markdown,docs\protocol.md proto\*.proto

pdoc --html --force --config show_source_code=False --output-dir docs olcarpc
py scripts\docpost.py
