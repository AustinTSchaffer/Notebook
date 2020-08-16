# Dockerfile that only contains ENV declarations.

FROM alpine:latest

# No value ENV variable

ENV MYVAR=

# Quotes are optional, but required if there are spaces

ENV QUOTES_OPTIONAL_1=Some_Value_Without_Spaces
ENV QUOTES_OPTIONAL_2="Some Value With Spaces"

# Multiline

ENV \
	TEST_MULTILINE_VAR_1=test1 \
	TEST_MULTILINE_VAR_2= \
	TEST_MULTILINE_VAR_3=test3 \
	TEST_MULTILINE_VAR_4="test4 test4" \
	TEST_MULTILINE_VAR_5=test5 \
	TEST_MULTILINE_VAR_6=test6
	