# Agno Docs

## Development

Install the [Mintlify CLI](https://www.npmjs.com/package/mintlify) to run documentation site locally:

```
npm i -g mint
```

Run the following command at the root of your documentation (where mint.json is)

```
mint dev
```

## Publishing Changes

Publish changes by pushing to the main branch

```
git add .
git commit -m "update message"
git push
```

## How to generate a new API reference

1. Run an `AgentOS` cookbook with the latest version of Agno
2. Run `curl -o reference-api/openapi.json http://localhost:7777/openapi.json` to download the latest API reference
3. Delete all the other files in the `reference-api` folder. NOT THE `overview` file.
4. Run `npx @mintlify/scraping@latest openapi-file reference_api/openapi.json -o reference-api` to generate the new API reference
5. Run `mint dev` to see the changes

## Troubleshooting

- Mintlify dev isn't running - Run `mint update` it'll update dependencies.
- Page loads as a 404 - Make sure you are running in a folder with `docs.json`
