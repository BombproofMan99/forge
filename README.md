# forge

**AI-powered toolkit for open-source maintainers**

Automate the boring (and time-consuming) parts of maintaining open-source projects.

`forge` helps you with:
- Intelligent PR reviews with constructive feedback
- Smart issue triage + label suggestions + first response drafts
- High-quality changelog / release notes generation
- Security audits on dependencies and code
- Code refactoring suggestions
- Contributor onboarding & welcome messages
- And more — with multi-step agent workflows

Works with **Claude**, Ollama, OpenAI, Grok, and other LLMs. Deep GitHub integration via official API.

Built for real maintainers who want to ship faster and burn out less.

## Quick Start

```bash
pip install forge
forge --help
```
Then try:

```bash
# Review a pull request
forge review-pr --repo yourusername/yourproject --pr 123

# Triage an issue
forge triage-issue --repo yourusername/yourproject --issue 456

# Generate changelog since last release
forge generate-changelog --since v1.2.0
```
**Key Features**
-Clean YAML prompt templates (easy to customize or contribute new ones)
-Works with Claude, Ollama (local models), OpenAI, Grok, and others
-Deep GitHub integration — automatically pulls diffs, issue bodies, and context
-Rich, interactive terminal experience
-Configurable via a simple YAML file in ~/.config/forge/
-Agent mode for more complex, back-and-forth tasks
-Ready for CI/CD and professional packaging

**Why I built forge**
I wanted a tool that actually understands the day-to-day reality of OSS maintenance — not just generic code generation. `forge` is designed to reduce burnout while keeping you in control. You decide what to accept, edit, or ignore.
If you're applying for Claude for OSS or just tired of spending evenings on maintenance work, this is for you.
Star ⭐ the repo if it saves you time — every star helps the project grow and reach more maintainers.

**Installation**
```bash
pip install forge
forge config init
```
You'll be guided to add your preferred LLM settings and GitHub personal access token (with `repo` scope).

*Contributing*
Contributions are very welcome! Whether it's a new prompt template, bug fix, or feature idea — check out CONTRIBUTING.md to get started.
