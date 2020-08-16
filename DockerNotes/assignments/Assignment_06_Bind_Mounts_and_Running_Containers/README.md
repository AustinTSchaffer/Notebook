# Assignment 6 - Jekyll Static Site Generator

- Use Jekyll "Static Site Generator" to start a local web server
- Bridge gap between local file access and apps running in containers
- Use `bindmount-sample-1` for source code
- Edit files with editor on our host using native tools
- Container detects changes with host files
- Use Bret Fisher's Jekyll Server
- Change the file in `_posts/` and refresh browser

```bash
docker run -p 80:4000 -v "$(pwd):/site" bretfisher/jekyll-serve
```

