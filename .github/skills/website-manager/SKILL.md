---
name: website-manager
user-invocable: true
description: "**WORKFLOW SKILL** — Assist a website manager maintaining a GitHub-hosted website. Use for content updates, repo maintenance, GitHub Pages deployment, site health checks, and workflow coordination."
---

# Website Manager Workflow

## Purpose
This skill guides the website manager through the full GitHub-backed website maintenance workflow: identifying required content or structural changes, validating the repository state, updating files, and ensuring successful deployment.

## When to use
- Maintaining a static website hosted on GitHub or GitHub Pages
- Updating HTML content, assets, navigation, or site configuration
- Reviewing or fixing broken links, metadata, or publishing settings
- Preparing commits, pull requests, and deployment verification

## Step-by-step process
1. Identify the website source and deployment method
   - Confirm the repository branch used for site content
   - Check for GitHub Pages configuration and relevant files like `_config.yml`
   - Determine whether the site is a raw HTML collection or uses a static site generator
2. Inspect the requested change
   - Locate the target page, asset, or config file
   - Determine if the change affects navigation, links, or page metadata
   - Identify whether this is a content edit, structural update, or deployment fix
3. Make the update safely
   - Preserve existing structure, links, and page formatting
   - Keep metadata consistent across similar pages
   - Use relative paths correctly for assets and links
4. Validate locally before committing
   - Preview changed pages where possible
   - Check for broken links, missing images, or incorrect paths
   - Verify site build or GitHub Pages settings if applicable
5. Commit and document the change
   - Use a clear, descriptive Git commit message
   - Recommend opening a pull request if the change is reviewable
   - Note any deployment branch or publishing details
6. Confirm final state
   - Ensure the change is ready for GitHub merge/deploy
   - If applicable, verify the published site URL and page rendering

## Decision points
- If the repository includes `_config.yml`, treat it as a GitHub Pages/static site generator repo
- If the request is only content editing, focus on page files and links
- If the request mentions deployment or site availability, inspect GitHub Pages settings and branch configuration
- If the change spans multiple files or pages, recommend a PR workflow rather than a direct commit

## Quality checks
- Content updates are applied to the correct file and section
- Relative URLs remain valid after edits
- Navigation or config changes do not break the site
- The repository still matches expected GitHub Pages structure
- Commit message clearly describes the update and intent

## Example prompts
- "Update the About page text and make sure links still work."
- "Fix broken relative links in `2018winter/Cassidy_Reller.html`."
- "Add a new HTML page and connect it to the site navigation."
- "Review this repo for missing GitHub Pages config and suggest fixes."
- "Prepare this website update for GitHub by checking the deployment branch and site settings."
