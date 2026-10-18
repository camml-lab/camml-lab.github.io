# CAMML@SIMaP website

Source for <https://camml-lab.github.io/>, built with [Hugo](https://gohugo.io/) and the [Blowfish](https://blowfish.page/) theme.
Every push to `main` rebuilds and publishes the site automatically (see `.github/workflows/hugo.yml`).

You can make all of the edits below directly in the GitHub web interface.

## Add yourself to the People page

1. Copy an existing folder in `content/members/` (e.g. `content/members/mattia-ragni/`) and rename it to `firstname-lastname`.
2. Edit `index.md` in the new folder: name, role, links and a short bio. The fields are explained in `archetypes/members/index.md`.
3. Add a photo named `photo.jpg` (or `.png`) to the same folder, ideally square and under 1 MB. It's cropped to a circle; if your head gets cut off, set `photo_anchor: "Top"`. Without a photo, your initials are shown.

When someone leaves, set `status: "alumni"`, fill in `end:` (year) and optionally `now:` (where they went). They move to the Alumni list automatically.

## Add a code

1. Copy `content/codes/tensorial/` to a new folder named after the code, e.g. `content/codes/mycode/`.
2. Edit `index.md`: name, one-sentence `summary` (shown on the Codes page), `tags`, `install` command, licence and links, then a longer description below the `---`. The fields are explained in `archetypes/codes/index.md`.
3. Optionally add a square logo named `logo.svg` (or `.png`). Without one, the first letter of the name is shown.

## Add a publication

Add an entry to `data/publications.yaml` (the format is described at the top of that file). Papers are grouped by year, and names that match a member page are shown in bold.

## Edit other pages

- Home page: `content/_index.md`
- Research: `content/research/_index.md`
- Menu: `config/_default/menus.en.toml`
- Colours and custom styles: `assets/css/custom.css`
- Logo: `assets/img/camml-logo.svg` (web version). The editable Inkscape original is in `design/`. If you change it, re-export with
  `inkscape design/camml-logo.inkscape.svg --export-plain-svg --export-text-to-path --export-filename=assets/img/camml-logo.svg`
  after deleting the hidden tracing image layer. Favicons in `static/` are made from `design/camml-icon.svg`.

## Preview locally

```sh
git clone --recurse-submodules https://github.com/camml-lab/camml-lab.github.io.git
cd camml-lab.github.io
hugo server        # then open http://localhost:1313
```

Needs Hugo **extended** between 0.164 and 0.167 (the range supported by Blowfish v3.9; the site is built with 0.167.0).
Ubuntu's packaged Hugo is usually too old: install the `.deb` from the [Hugo releases page](https://github.com/gohugoio/hugo/releases/tag/v0.167.0) instead.
With a local Hugo you can also run `hugo new members/jane-doe` to create a new member folder from the template.

## Checks

Every push and pull request runs `.github/workflows/checks.yml`, which checks member pages, code pages and `data/publications.yaml`
for common mistakes (wrong `status`, malformed DOIs, oversized photos...) and builds the site with warnings treated as errors.
To run the same checks on your machine before each commit:

```sh
pipx install pre-commit    # or: uv tool install pre-commit
pre-commit install         # once per clone
pre-commit run --all-files # run everything by hand
```

## Updating Hugo and Blowfish

Upgrade them together: Blowfish declares which Hugo versions it supports in `themes/blowfish/config.toml` (`[module.hugoVersion]`).

```sh
cd themes/blowfish && git fetch --tags && git checkout vX.Y.Z && cd ../..
```

Then set `HUGO_VERSION` in both `.github/workflows/hugo.yml` and `checks.yml`, and run `pre-commit run --all-files`.
GitHub Actions versions are kept up to date by Dependabot.
