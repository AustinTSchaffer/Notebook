FROM alpine
RUN apk add --update alpine-sdk
COPY hello.c /
RUN make hello
CMD /hello
