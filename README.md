# Portfolio site

A static portfolio modeled on lesmana.framer.website. It's plain HTML, CSS, and JS with no build step.

## Pages
| File | Page |
|---|---|
| `index.html` | Home |
| `about.html` | About: hero, origins, design principles, experience timeline, "Beyond The Screens" photos |
| `works.html` | All projects, with category filter tabs |
| `work.html` | One project case study. Copy it once per project and link each card to its copy. |
| `contact.html` | Contact form + FAQ |
| `blog.html` | All articles |
| `post.html` | One article. Copy it once per article. |

## Where to edit
- **Header, mobile menu and footer:** `js/layout.js`, used by every page, so edit once. It also highlights the current page in the nav.
- **Page text:** in each `.html` file. Search for `Your Name`, `Your City`, `hello@yourdomain.com`, and `+000` to replace the placeholders.
- **Contact form email address:** `CONTACT_EMAIL` at the top of `js/pages.js`. The form opens the visitor's email app with the message filled in; no server is needed.
- **Works filter:** each project card on `works.html` has `data-cats="mobile ux"` etc.; the words match the tabs' `data-filter` values.
- `css/style.css` holds the design tokens (colors, fonts, sizes) at the top; `css/pages.css` styles the inner pages.
- `js/main.js` holds the shared animations. The ring images, archive titles and years, and the testimonial timing are listed at the top of the file. `js/pages.js` holds the inner-page behaviour.
- `assets/images/` contains the placeholders. See its README for what each file is.
- `documents/` holds the reference teardown (`DESIGN-NOTES.md`) and the screenshots and video from the original site.

## Run locally
```bash
python -m http.server 5173
```
Then open http://localhost:5173.

## Deploy
Drag the folder onto https://app.netlify.com/drop, or push it to GitHub and enable GitHub Pages. No build settings are needed.
