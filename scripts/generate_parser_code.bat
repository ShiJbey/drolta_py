@ECHO OFF

ECHO Changing directory to: %~dp0..\src\drolta
PUSHD %~dp0..\src\drolta

ECHO Calling ANTLR4
ECHO.

antlr4 -Dlanguage=Python3 -o parsing -visitor -no-listener DroltaParser.g4 DroltaLexer.g4

ECHO.
ECHO Parser code stored at: %~dp0..\src\drolta\parsing
POPD
