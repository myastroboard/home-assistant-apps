# Changelog

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
