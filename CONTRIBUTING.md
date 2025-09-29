# Contributing to Agno Documentation

Agno is an open-source project and we welcome contributions to our documentation.

## 👩‍💻 How to contribute

Please follow the [fork and pull request](https://docs.github.com/en/get-started/quickstart/contributing-to-projects) workflow:

- Fork the repository.
- Create a new branch for your feature.
  - Add your documentation improvements or new content.
  - **Ensure your Pull Request follows our guidelines (see below).**
  - Send a pull request.
  - We appreciate your support & input!

## Pull Request Guidelines

To maintain a clear and organized project history, please adhere to the following guidelines when submitting Pull Requests:

1.  **Title Format:** Your PR title must start with a type tag enclosed in square brackets, followed by a space and a concise subject.
    - Example: `[docs] Add authentication guide`
    - Common types for documentation:
      - `[docs]` - Documentation content changes (new pages, updates, improvements)
      - `[fix]` - Fixes to documentation (broken links, typos, incorrect information)
      - `[style]` - Formatting changes (no content changes)
    - Other valid types: `[feat]`, `[test]`, `[refactor]`, `[build]`, `[ci]`, `[chore]`, `[perf]`, `[revert]`.
2.  **Link to Issue:** The PR description should ideally reference the issue it addresses using keywords like `fixes #<issue_number>`, `closes #<issue_number>`, or `resolves #<issue_number>`.
    - Example: `This PR fixes #42 by adding documentation for the new feature.`

## Development setup

1. Clone the repository.
2. Install the [Mintlify CLI](https://www.npmjs.com/package/mintlify):
   ```bash
   npm i -g mintlify
   ```
3. Run the documentation site locally at the root of your documentation (where `docs.json` is):
   ```bash
   mint dev
   ```
4. The docs will be available at `http://localhost:3000`.

## Documentation Structure

The documentation is organized into the following main sections:

- **introduction/** - Getting started guides and overview
- **tutorials/** - Step-by-step tutorials
- **how-to/** - Task-oriented guides
- **concepts/** - Conceptual explanations
- **integrations/** - Integration guides
- **reference/** - Reference documentation
- **reference-api/** - API reference (auto-generated)
- **examples/** - Example code and use cases
- **templates/** - Documentation templates and boilerplates
- **agent-os/** - AgentOS-specific documentation
- **deploy/** - Deployment guides
- **evals/** - Evaluation documentation
- **faq/** - Frequently asked questions
- **videos/** - Video tutorials and resources
- **_snippets/** - Reusable code snippets

## Writing Guidelines

1. **Use clear, concise language** - Write for developers who may be new to the framework.
2. **Include code examples** - Show, don't just tell. Use code snippets to illustrate concepts.
3. **Follow MDX format** - All documentation uses MDX (Markdown with JSX support).
4. **Use consistent formatting** - Follow the existing style in the documentation.
5. **Test your changes** - Always run `mint dev` to preview your changes before submitting.
6. **Link to related content** - Help users navigate by linking to related documentation.

### Code Examples

Use standard markdown code blocks with language tags:

```python
from agno.agent import Agent

agent = Agent(name="MyAgent")
agent.print_response("Hello, world!")
```

For code snippets from files, you can reference them with filename and line numbers:

```python hackernews_agent.py lines
from agno.agent import Agent
from agno.tools.hackernews import HackerNewsTools

agent = Agent(tools=[HackerNewsTools()])
```

For multi-platform code examples, use the `<CodeGroup>` component with separate code blocks for each platform:

- Wrap multiple code blocks in `<CodeGroup>` tags
- Each code block should specify the platform (e.g., `bash Mac`, `bash Windows`)
- Include a blank line between code blocks

Example from the documentation:
```
<CodeGroup>

```bash Mac
pip install agno
```

```bash Windows  
pip install agno
```

</CodeGroup>
```

The `_snippets/` directory contains reusable MDX components (like common setup steps) that can be referenced across multiple documentation pages for consistency.

### Adding New Pages

1. Create a new `.mdx` file in the appropriate directory.
2. Add frontmatter at the top of the file:
   ```mdx
   ---
   title: "Your Page Title"
   description: "Brief description of the page content"
   ---
   ```
3. Update `docs.json` to include the new page in the navigation structure.
4. Test the page appears correctly in local preview.

## Updating API Reference

The API reference in `reference-api/` is auto-generated from the AgentOS OpenAPI schema. To update it:

1. Run an AgentOS cookbook with the latest version of Agno.
2. Download the latest API reference:
   ```bash
   curl -o reference-api/openapi.json http://localhost:7777/openapi.json
   ```
3. Delete all files in the `reference-api/schema/` folder (the auto-generated files).
4. Generate the new API reference:
   ```bash
   npx @mintlify/scraping@latest openapi-file reference-api/openapi.json -o reference-api/schema
   ```
5. Run `mint dev` to preview the changes.

## Types of Contributions

We welcome various types of documentation contributions:

**Content Improvements**
- Fix typos, grammar, or unclear explanations
- Add missing information or clarify existing content
- Improve code examples or add new ones
- Update outdated information

**New Documentation**
- Add tutorials for common use cases
- Document new features or integrations
- Create how-to guides for specific tasks
- Add troubleshooting guides

**Structure and Navigation**
- Improve documentation organization
- Enhance navigation in `docs.json`
- Add cross-references between related pages

**Issue Reports**
- Report broken links or images
- Identify outdated or incorrect information
- Suggest improvements to existing content

## Local Testing

Before submitting a pull request, test your changes locally:

1. Run `mint dev` in the root directory.
2. Navigate through your changes in the browser.
3. Verify all pages load correctly, code examples are properly formatted, links work as expected, and images display correctly.

## Formatting and Validation

Ensure your documentation meets our quality standards:

- Check for broken links and review all internal and external links.
- Validate code examples and make sure all code snippets are syntactically correct.
- Run `mint build` to catch any build errors.
- Preview your changes locally to ensure proper formatting.

Message us on [Discord](https://discord.gg/4MtYHHrgA8) or post on [Discourse](https://community.agno.com/) if you have any questions or need help with your contribution.

## 📚 Resources

- <a href="https://docs.agno.com/introduction" target="_blank" rel="noopener noreferrer">Documentation</a>
- <a href="https://discord.gg/4MtYHHrgA8" target="_blank" rel="noopener noreferrer">Discord</a>
- <a href="https://community.agno.com/" target="_blank" rel="noopener noreferrer">Discourse</a>
