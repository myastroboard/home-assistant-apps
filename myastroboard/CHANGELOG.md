# Changelog

## 1.6.8

### Fixes

- Home Assistant sidebar panel (ingress): requests from the Supervisor were refused (404 on every page)
  because gunicorn reports its IPv4 address in IPv6 form (`::ffff:172.30.32.2`).

Release notes: <https://github.com/myastroboard/myastroboard/releases/tag/v1.6.8>

## 1.6.7

### Features

- Sub-path support: MyAstroBoard runs under a path prefix (Home Assistant sidebar panel via ingress,
  or `X-Forwarded-Prefix` behind a reverse proxy), with a new *External base URL* setting.

### Fixes

- Parameters: the log retention setting moved from *Privacy & search engines* to *Log export*, next to
  the log levels.

Release notes: <https://github.com/myastroboard/myastroboard/releases/tag/v1.6.7>

## 1.6.6

### Features

- Logs: the log file and console levels are set in Parameters -> Log export and apply without a
  restart (e.g. in the Home Assistant app); `LOG_LEVEL` / `CONSOLE_LOG_LEVEL` still override them.

### Fixes

- Setup wizard: on a fresh install it no longer closes by itself a moment after opening, when the
  start page loads.
- Docker: stopping the container is now a clean shutdown (exit code 0, within the 10 s stop timeout)
  instead of a kill, so the Home Assistant app no longer shows "Error" after being stopped.
- Fresh install: no more "Could not attribute location ... circular import" warning at first start.
- Docker: the app now listens on IPv6 as well as IPv4, so it is reachable through names that
  resolve to IPv6, such as `homeassistant.local` in the Home Assistant app's "Open web UI" link.

Release notes: <https://github.com/myastroboard/myastroboard/releases/tag/v1.6.6>

## 1.6.5

### Fixes

- Docker: the image now declares its own `HEALTHCHECK` (on `/health`), no longer only in
  `docker-compose.yml`.
- Docker (amd64): the app no longer crashes at startup on VMs with a generic CPU model (e.g.
  Proxmox `kvm64`, the Home Assistant OS VM default); NumPy is rebuilt for older CPUs.

Release notes: <https://github.com/myastroboard/myastroboard/releases/tag/v1.6.5>

## 1.6.4

### Features

- Privacy: new [Privacy & GDPR](https://github.com/myastroboard/myastroboard/blob/v1.6.4/docs/PRIVACY.md) guide for instance operators, with a data inventory
  and a privacy notice template.
- Privacy: users can download all their data as a ZIP (My Settings -> Security); admins can do it
  for any user.
- Privacy: log lines are kept 90 days by default, configurable in Parameters -> Advanced.
- Security: password sign-in is throttled after repeated failures (`429` with `Retry-After`).
- Privacy: the Astrodex photo map is private by default on new installs; existing installs keep their setting.

### Fixes

- Deleting a user now removes all their files (equipment, observation sessions and attachments,
  plans, wishlist), not only the Astrodex.
- Uploaded pictures (Astrodex, session attachments, MyAstroShine returns) are stripped of EXIF/GPS
  metadata, losslessly; image uploads that are not real images are rejected.
- CI: the CHANGELOG check no longer fails when the base branch moves while the job runs.
- Docker: the entrypoint now follows `DATA_DIR` instead of assuming `/app/data` (needed by the
  Home Assistant app).

Release notes: <https://github.com/myastroboard/myastroboard/releases/tag/v1.6.4>

## 1.6.3

First version packaged as a Home Assistant app. Full history:
<https://github.com/myastroboard/myastroboard/blob/main/CHANGELOG.md>
