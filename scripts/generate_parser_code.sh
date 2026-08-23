#!/usr/bin/env bash

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
GRAMMAR_DIR="${SCRIPT_DIR}../src/drolta"

echo "Changing directory to: ${GRAMMAR_DIR}"
pushd ${GRAMMAR_DIR} > /dev/null

echo Calling ANTLR4
echo.

antlr4 -Dlanguage=Python3 -o parsing -visitor -no-listener DroltaParser.g4 DroltaLexer.g4

echo.
echo "Parser code stored at: ${GRAMMAR_DIR}/parsing"
popd > /dev/null
