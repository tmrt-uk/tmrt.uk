# trmt.uk

This is a very basic Jekyll site for trmt.uk, styled using Bootstrap. 

## Project Structure

- **_layouts/**: Contains layout files for the site.
  - **default.html**: The default layout for all pages.
  - **post.html**: The layout for individual blog posts.
  
- **_posts/**: Contains blog posts in markdown format.
  - **2024-01-01-welcome-to-jekyll.md**: The first blog post.

- **_includes/**: Contains reusable HTML snippets.
  - **header.html**: The header section of the site.
  - **footer.html**: The footer section of the site.
  - **navigation.html**: The navigation menu.

- **assets/**: Contains static assets like CSS and JavaScript.
  - **css/**: Custom CSS styles.
    - **style.css**: Styles for the site.
  - **js/**: JavaScript files.
    - **main.js**: JavaScript for interactive features.

- **_config.yml**: Configuration file for Jekyll.

- **index.html**: The main landing page of the site.

- **about.md**: Information about the site or the author.

- **Gemfile**: Specifies the Ruby gems required for the Jekyll site.

## Setup Instructions

1. **Install Jekyll**: Make sure you have Ruby and Bundler installed. Then, install Jekyll by running:
   ```
   gem install jekyll bundler
   ```

2. **Install Dependencies**: Navigate to the project directory and run:
   ```
   bundle install
   ```

3. **Run the Site**: Start the Jekyll server with:
   ```
   bundle exec jekyll serve
   ```
   Your site will be available at `http://localhost:4000`.

4. **Customize**: Modify the content in the `_posts/`, `_includes/`, and other files to personalize your site.