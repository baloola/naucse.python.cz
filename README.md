# Sudan Club training materials

## Development

you can spin up a local instance for development using the `docker-compose` file:

```bash
docker compose up
```
then simply navigate in your browser to `http://127.0.0.1:8003`

Changes in the code (`markdown files`) should be synchronized.

To enforce changes in some dependencies (e.g updating a photo in [naucse] )

You can build first disabling cache

```bash
docker compose build --no-cache
```

## License


The code is licensed under the terms of the MIT license, see [LICENSE.MIT] file
for full text. By contributing code to this repository, you agree to have it
licensed under the same license.

Content has its own license specified in the appropriate metadata.
Only [free content licenses] are used. By contributing to an already licensed
document, you agree to have it licensed under the same license.
(And feel free to add yourself to the authors list in its metadata.)
When contributing new document(s) a license must be specified in the metadata.

[LICENSE.MIT]: https://github.com/pyvec/naucse.python.cz/blob/master/LICENSE.MIT
[free content licenses]: https://en.wikipedia.org/wiki/List_of_free_content_licenses
[naucse]: https://github.com/baloola/naucse.git