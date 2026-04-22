# Doug's Blog 🚀

This site serves to document my thoughts and journeys through AI, development, and technology. 

## 🛠 Local Development

To run the blog locally and see changes in real-time:

1. Ensure Hugo is installed
2. Navigate to the root directory
   ```bash
    cd flickdm.github.io
   ```
3. Start the development server:
   ```bash
   hugo server
   ```
4. View the site:
    - Open http://localhost:1313/ in your browser.

## 📝 Content Creation

Blog posts live in content/posts/. 

Use this command to scaffold a new post:
```bash
hugo new posts/<post-name>/index.md
```
### Post Structure Requirements:

After creating the file, ensure your frontmatter includes:

- title: The name of your post.
- author: Your name.
- cover: Path to an image in static/img/.
- description: A short summary for SEO and previews.
- tags: An array of strings (e.g., ['AI', 'Coding']).

## 📖 Adding to Reading List

The "Reading List" is a curated collection of articles I've read, including my personal takeaways.

Use this command:
```bash
hugo new reading/article-slug.md
```

## 🚀 Deployment

 🔗 https://flickdm.github.io/