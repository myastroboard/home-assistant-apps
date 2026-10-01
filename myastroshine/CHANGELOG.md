# Changelog

## 0.5.1

### Fixed

- **Clean stop exit code.** Stopping the container now exits with code 0
  instead of 143. uvicorn re-raised the SIGTERM after its graceful shutdown, so
  Home Assistant reported the app as "did not handle SIGTERM" and showed an
  error on the app card.

Release notes: <https://github.com/myastroboard/myastroshine/releases/tag/v0.5.1>

## 0.5.0

First release as a Home Assistant app: a single container (no Redis or worker),
sidebar panel (ingress) with Home Assistant's login in front, admin password for
Settings, ML engine upload from Settings, and support for older x86-64 CPUs.

Release notes: <https://github.com/myastroboard/myastroshine/releases/tag/v0.5.0>
