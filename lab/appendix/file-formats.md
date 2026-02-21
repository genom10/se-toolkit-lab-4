# File formats

<h2>Table of contents</h2>

- [What is a file format?](#what-is-a-file-format)
- [Common file formats](#common-file-formats)
  - [`Markdown`](#markdown)
  - [`JSON`](#json)
  - [`TOML`](#toml)
  - [`YAML`](#yaml)
  - [`.env`](#env)
  - [`Python`](#python)

## What is a file format?

A file format defines how data is structured and stored in a [file](./file-system.md#file).

The [file extension](./file-system.md#extension) (e.g., [`.json`](#json), [`.toml`](#toml), [`.py`](#python)) indicates the format and tells editors and tools how to read the file.

## Common file formats

### `Markdown`

`Markdown` is a [markup language](https://en.wikipedia.org/wiki/Markup_language).

`Markdown` gets translated into [`HTML`](https://en.wikipedia.org/wiki/HTML).

You see the rendered `HTML` when you [open the `Markdown` preview](./vs-code.md#open-the-markdown-preview) in `VS Code` or view a `Markdown` file on `GitHub`.

Docs:

- [Learn Markdown in Y minutes](https://learnxinyminutes.com/docs/markdown/)

### `JSON`

`JSON` (JavaScript Object Notation) is a human-readable text format for structured data.

Docs:

- [JSON.org](https://www.json.org/)
- [Learn JSON in Y minutes](https://learnxinyminutes.com/docs/json/)

Example:

```json
{
  "id": 1,
  "title": "Introduction to Python",
  "published": true
}
```

In this project, `JSON` is used for:

- [`.vscode/settings.json`](../../.vscode/settings.json) — `VS Code` editor settings.
- [`HTTP`](./http.md) request and response bodies when calling the `API`.

### `TOML`

`TOML` (Tom's Obvious, Minimal Language) is a configuration file format designed to be minimal and easy to read.

Docs:

- [TOML documentation](https://toml.io/)
- [Learn TOML in Y minutes](https://learnxinyminutes.com/docs/toml/)

Example:

```toml
[project]
name = "my-app"
version = "1.0.0"

[server]
host = "localhost"
port = 8080
```

In this project, `TOML` is used for [`pyproject.toml`](../../pyproject.toml) — the [`Python`](./python.md) project configuration file.

### `YAML`

`YAML` (YAML Ain't Markup Language) is a human-readable data serialization format commonly used for configuration files.

Docs:

- [YAML specification](https://yaml.org/)
- [Learn YAML in Y minutes](https://learnxinyminutes.com/docs/yaml/)

Example:

```yaml
name: my-app
version: "1.0.0"

server:
  host: localhost
  port: 8080
```

In this project, `YAML` is used for:

- [`.github/workflows/`](../../.github/workflows/) — `GitHub Actions` workflow files.
- [`docker-compose.yml`](../../docker-compose.yml) — [`Docker Compose`](./docker-compose.md) service definitions.

### `.env`

`.env` files store [environment variables](./environments.md) as key-value pairs, one per line.

Docs:

- [Dotenv File Format](https://hexdocs.pm/dotenvy/dotenv-file-format.html)

Example:

```shell
DEBUG=false
PORT=8080
SECRET_KEY=changeme
```

In this project, `.env` files are used for local and `Docker` environment configuration.

### `Python`

`.py` files contain [`Python`](./python.md) source code.

Docs:

- [Learn Python in Y minutes](https://learnxinyminutes.com/docs/python/)

Example:

```python
def greet(name: str) -> str:
    return f"Hello, {name}!"
```

In this project, `.py` files are used for the application code and tests.
