#!/usr/bin/env bash

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

antlr4-parse \
    ${SCRIPT_DIR}/../src/drolta/DroltaParser.g4 \
    ${SCRIPT_DIR}/../src/drolta/DroltaLexer.g4 \
    prog \
    ${SCRIPT_DIR}/../samples/sample_script.drolta \
    -gui
