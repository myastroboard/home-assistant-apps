# MyAstroBoard Home Assistant apps - instructions for AI coding agents

The Home Assistant app repository (formerly add-ons) for MyAstroBoard and MyAstroShine. Each app
only wraps its image already published on Docker Hub (`myastroboard/myastroboard`,
`myastroboard/myastroshine`): nothing is built here.

## Organization standards

The rules shared by every MyAstroBoard repository live in the synced file below. They apply here
in full, except where "Relaxed here" says otherwise; this file only adds what is specific to the
apps. Do not edit the synced copy: change it in
[myastroboard/.github](https://github.com/myastroboard/.github/tree/main/standards).

@.github/instructions/org-standards.instructions.md

### Relaxed here

- **Changelog** (standards section 12): this repository has no releases of its own, so no root
  `CHANGELOG.md` and no changelog gate. Each app's `CHANGELOG.md` is what Home Assistant shows
  users, and the update workflow writes it (see below).
- **Logging** (standards section 4): `scripts/update_apps.py` is a standalone, standard-library
  CI script; its `print()` output is the workflow log, by design.
- **Python tooling** (standards section 13): that single script has no ruff configuration; CI
  exercises it with `--dry-run`.

## Layout

| Path | What |
|---|---|
| `<app>/config.yaml` | The app manifest: `version`, `image`, `url` (upstream repo), `arch`, ingress, ports, environment |
| `<app>/CHANGELOG.md` | Release notes shown in Home Assistant - generated |
| `<app>/DOCS.md`, `<app>/README.md` | The app's documentation tab and store description |
| `<app>/apparmor.txt` | The app's AppArmor profile |
| `<app>/icon.png`, `<app>/logo.png` | Store artwork |
| `scripts/update_apps.py` | Bumps each app to its latest upstream release |
| `repository.yaml` | The repository's identity in the Home Assistant app store |

## Hard rules

- **Never hand-edit `version:` or an app's `CHANGELOG.md`.** The hourly
  [update workflow](.github/workflows/update-apps.yml) bumps `version:` only once the release's
  multi-arch image is on Docker Hub for every declared `arch`, and prepends that release's notes,
  read from the upstream `CHANGELOG.md` at the tag. A hand-set version can point users at an image
  they cannot pull.
- **The upstream images and changelogs are a cross-repository contract.** The script accepts both
  upstream heading styles (`## 1.6.3 (date)` and `## [0.4.2] - date`); an upstream change to its
  changelog layout, image name, or a new required environment variable must be checked here.
- **Every `config.yaml` choice carries its reason as a comment** (ingress, kept direct port,
  `timeout`, `backup_exclude`, environment): keep them when editing, and add one for any new key.
- **Ingress and direct access coexist on purpose**: some features (installable app, push
  notifications, Astrodex stream, MyAstroShine photo return) do not work through ingress.

## Adding an app

Create a folder with `config.yaml`, `README.md`, `DOCS.md`, `CHANGELOG.md`, `icon.png` and
`logo.png`, with `url:` pointing at the upstream GitHub repository and `image:` at its Docker Hub
image. The update workflow and the lint matrix pick it up automatically.

## Checks before calling a change done

```bash
python3 scripts/update_apps.py --dry-run   # what the update workflow would bump
```

- CI runs the Home Assistant app linter (`frenck/action-addon-linter`) on every app folder, plus
  the dry run above.
- A `config.yaml` change is verified by installing the app on a real Home Assistant instance.
