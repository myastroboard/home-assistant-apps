# MyAstroBoard apps for Home Assistant

Run MyAstroBoard and MyAstroShine as Home Assistant apps (formerly add-ons) - no
Docker knowledge needed.

[![Add repository to Home Assistant][repo-badge]][repo-link]

| App | What it does |
|-----|--------------|
| [MyAstroBoard](myastroboard/DOCS.md) | Astronomy dashboard: observation planning, sky conditions, astrophotography |
| [MyAstroShine](myastroshine/DOCS.md) | Astrophoto enhancement and stacking, in your browser |

## Installation

1. Click the button above, or in Home Assistant go to **Settings -> Apps -> App store**,
   open the menu (top right) -> **Repositories** and add
   `https://github.com/myastroboard/home-assistant-apps`.
2. Pick the app in the store, click **Install**, then **Start**.
3. Click **Open web UI**.

Requires Home Assistant OS or a Supervised installation, on a 64-bit system
(amd64 or aarch64 - e.g. Raspberry Pi 4/5, Home Assistant Green/Yellow, any x86 PC).

## How this repository works

Each app only wraps its image already published on Docker Hub
(`myastroboard/myastroboard`, `myastroboard/myastroshine`); nothing is built here.

The [update workflow](.github/workflows/update-apps.yml) checks the upstream
GitHub releases every hour. When a newer release exists and its multi-arch image
is on Docker Hub, it bumps `version:` in the app's `config.yaml` and prepends the
release's changelog to the app's `CHANGELOG.md`. Home Assistant then offers the
update to users. It can also be run by hand from the Actions tab.

To add an app: create a folder with `config.yaml`, `README.md`, `DOCS.md`,
`CHANGELOG.md`, `icon.png` and `logo.png`, with `url:` pointing at the upstream
GitHub repository and `image:` at its Docker Hub image. The update workflow picks
it up automatically.

[repo-badge]: https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg
[repo-link]: https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2Fmyastroboard%2Fhome-assistant-apps
