# Changelog

## 1.9.2

### Features

- Moon: supermoons, micromoons, Blue Moons and the traditional Full Moon names ("Beaver Supermoon") are
  computed and shown in the Moon report, the phase calendar and the upcoming events
  ([ASTROPHOTOGRAPHY.md](https://github.com/myastroboard/myastroboard/blob/v1.9.2/docs/ASTROPHOTOGRAPHY.md#full-moons-astroweatherfull_moonspy)).
- Equipment presets: Vaonis Atlas Twin, Unistellar Odyssey, Odyssey Pro, eVscope 2 and eQuinox 2, DWARFLAB Draco
  and Celestron Origin Mark II smart telescopes, each with its built-in camera and mount ([EQUIPMENT.md](https://github.com/myastroboard/myastroboard/blob/v1.9.2/docs/EQUIPMENT.md#bundles-smart-telescopes)).
- Equipment presets: ZWO Seestar TC20 tripod and TH10 tripod head accessories.
- Equipment presets: 43 more common items - Celestron C6 / C9.25 / C11 and EdgeHD 9.25 / 11, William Optics
  and Sky-Watcher refractors and Newtonians, ZWO and Player One cameras, Canon, Nikon and Sony camera bodies,
  ZWO, Sky-Watcher and Celestron mounts.
- Equipment presets are now edited as one small file per gear type and manufacturer under
  `presets/equipment/`, with JSON Schemas and a checking script run in CI
  ([EQUIPMENT.md](https://github.com/myastroboard/myastroboard/blob/v1.9.2/docs/EQUIPMENT.md#adding-or-editing-a-preset)).

### Fixes

- ISS / CSS trackers: a Celestrak overload (HTTP 5xx) no longer needs an admin to clear it; Celestrak is
  asked again on its own after 6 h, 12 h, then 24 h ([SPACEFLIGHT.md](https://github.com/myastroboard/myastroboard/blob/v1.9.2/docs/SPACEFLIGHT.md#tle-data)).
- Equipment presets: a Vespera II created from its preset no longer shows a payload warning for its own
  built-in mount ([EQUIPMENT.md](https://github.com/myastroboard/myastroboard/blob/v1.9.2/docs/EQUIPMENT.md#preset-field-reference)).

Release notes: <https://github.com/myastroboard/myastroboard/releases/tag/v1.9.2>

## 1.9.1

### Features

- Lighter and faster server: one process with request threads on small hosts (about 200 MB less memory),
  two from 2 CPUs and 4 GB, and pages stay quick during SkyTonight calculations
  ([docs/1.INSTALLATION.md](https://github.com/myastroboard/myastroboard/blob/v1.9.1/docs/1.INSTALLATION.md#workers-and-threads)).
- New smart telescope presets: Seestar S50 Pro and S30 Plus, Vaonis Vespera 3, Vespera Pro 2 and Atlas
  ([docs/EQUIPMENT.md](https://github.com/myastroboard/myastroboard/blob/v1.9.1/docs/EQUIPMENT.md#bundles-smart-telescopes)).
- Framing simulator: galaxies are outlined by their catalogue ellipse and orientation, and zoom buttons
  sharpen the sky image around small fields ([docs/SKYTONIGHT.md](https://github.com/myastroboard/myastroboard/blob/v1.9.1/docs/SKYTONIGHT.md#framing-simulator)).

### Fixes

- Smart telescopes added from the Equipment tab now get their built-in camera and a combination, so the
  framing simulator can show their field; Seestar frames are drawn in portrait, as the device records
  ([docs/EQUIPMENT.md](https://github.com/myastroboard/myastroboard/blob/v1.9.1/docs/EQUIPMENT.md#bundles-smart-telescopes)).
- The framing simulator lists the combinations it cannot show with what each one lacks, and a link to
  edit them ([docs/SKYTONIGHT.md](https://github.com/myastroboard/myastroboard/blob/v1.9.1/docs/SKYTONIGHT.md#framing-simulator)).
- Aurora forecast on phones: each time slot's header wraps instead of overflowing, and the Kp value fits
  in narrow columns.
- Astro weather no longer falls back to its reduced forecast for some locations: it stopped requesting
  unused upper-air variables, one of which made Open-Meteo answer with an error.
- The weather forecast decodes again on humid nights: a fractional fog percentage made the fast decoder
  fail and fall back to the slower JSON request, which drops several variables.
- SkyTonight no longer stops calculating until the next restart after a worker was killed for lack of
  memory (every run then failed with "Working outside of application context").
- Signing in at a local `http://` address works again with the HTTPS-only session cookie on: the page
  no longer reloads forever ([docs/6.REVERSE_PROXY.md](https://github.com/myastroboard/myastroboard/blob/v1.9.1/docs/6.REVERSE_PROXY.md)).
- Demo mode: `/login?signin` shows the sign-in form again in a browser already browsing the demo
  ([docs/DEMO_MODE.md](https://github.com/myastroboard/myastroboard/blob/v1.9.1/docs/DEMO_MODE.md)).
- My astro year: format, theme and signature are chosen once for the whole slideshow and apply to the
  preview, "This screen" and "All screens" alike ([docs/MY_PROGRESS.md](https://github.com/myastroboard/myastroboard/blob/v1.9.1/docs/MY_PROGRESS.md)).
- Community, Astrodex, Catalogue Collection, Observation Log and montages: pictures load as small
  previews instead of full-size astrophotos, so these pages open quickly and scroll smoothly
  ([docs/COMMUNITY.md](https://github.com/myastroboard/myastroboard/blob/v1.9.1/docs/COMMUNITY.md)).

Release notes: <https://github.com/myastroboard/myastroboard/releases/tag/v1.9.1>

## 1.9.0

### Features

- My Progress: a "My astro year" review of any year, screen by screen and each one shareable, highlighted
  from 1 December to 15 January; badges earned from your log, seasonal challenges and a Messier marathon
  planner for your latitude in Astrodex -> Progress ([docs/MY_PROGRESS.md](https://github.com/myastroboard/myastroboard/blob/v1.9.0/docs/MY_PROGRESS.md)).
- Phones: each row of sub-tabs becomes one menu button showing the current sub-tab, instead of pills that
  wrapped over half the screen ([docs/MOBILE.md](https://github.com/myastroboard/myastroboard/blob/v1.9.0/docs/MOBILE.md)).
- Profiles and Community: a display name and picture shown wherever others see you, and a Community tab
  (opt-in) with a member directory, profiles, an activity feed and shared "together" totals, never a
  ranking; also a step of the first-run wizard ([docs/COMMUNITY.md](https://github.com/myastroboard/myastroboard/blob/v1.9.0/docs/COMMUNITY.md)).
- Privacy: optionally publish your own privacy notice (an address, or a text served at `/privacy`), linked from
  the login page, the footer and My settings -> Security; and clean the location data still in pictures uploaded
  before 1.6.4, in App settings -> Configuration ([docs/PRIVACY.md](https://github.com/myastroboard/myastroboard/blob/v1.9.0/docs/PRIVACY.md#publishing-your-privacy-notice)).
- A cleaner footer (logo, version, links, compact language and theme pickers, readable in every theme),
  and a language picker on the login page ([docs/USER_SETTINGS.md](https://github.com/myastroboard/myastroboard/blob/v1.9.0/docs/USER_SETTINGS.md)).
- Documentation: the guides are now a searchable website, [docs.myastroboard.org](https://docs.myastroboard.org/),
  starting with a visual tour of the application.

### Fixes

- Interface texts that still sent you to "Parameters -> Advanced" now name the current screens (App settings ->
  Configuration or Connectors), and the My settings -> Notifications messages, the meteor shower / comet lead time
  ("2 days") and the footer theme picker are translated in every language.

Release notes: <https://github.com/myastroboard/myastroboard/releases/tag/v1.9.0>

## 1.8.3

### Features

- Share card: a short note under the MyAstroBoard signature option explains that keeping it helps others discover the project.

### Fixes

- Object images: the cache of DSS2 thumbnails (Astrodex Collection, object details) is now capped at 200 MiB, oldest first ([docs/ASTRODEX.md](https://github.com/myastroboard/myastroboard/blob/v1.8.3/docs/ASTRODEX.md)).
- Demo mode: logged nights older than 60 days are removed with the Astrodex items they added, so the demo no longer grows on disk ([docs/DEMO_MODE.md](https://github.com/myastroboard/myastroboard/blob/v1.8.3/docs/DEMO_MODE.md)).
- Sky images: the fallback used when CDS hips2fits is down now renders in bands, using about 110 MB instead of 1.3 GB for a large picture, so small servers no longer kill the worker mid-download.
- Observation Log: an entry's object type and constellation are now translated.
- Parameters -> Logs: the Delete logs button now asks for confirmation, and its messages are translated.
- Demo mode: Astrodex pictures that could not be downloaded are retried on later checks, and constellations are stored as full names so they are translated (Astrodex, Plan My Night, Observation Log).
- Parameters -> Users: creating an account on a slow server no longer reports a failure when the account was in fact created, and the password is hashed before the database write lock is taken.
- Low memory: the startup log records the host's CPUs, memory and container limits, and Parameters -> Metrics warns below 1 GB (and says so when the metrics cannot be collected, instead of freezing); minimum requirements are documented ([docs/1.INSTALLATION.md](https://github.com/myastroboard/myastroboard/blob/v1.8.3/docs/1.INSTALLATION.md#system-requirements)).

Release notes: <https://github.com/myastroboard/myastroboard/releases/tag/v1.8.3>

## 1.8.2

### Features

- Demo mode (`DEMO_MODE=true`): a public, read-only instance that fills itself with demo data and plans
  every night from SkyTonight. Installation guide in [docs/DEMO_MODE.md](https://github.com/myastroboard/myastroboard/blob/v1.8.2/docs/DEMO_MODE.md).
- Docker image now runs Python 3.15 (up from 3.14).

### Fixes

- Maps no longer fail with HTTP 502 on every tile not already cached: the map tile proxy could not read
  OpenStreetMap's responses since niquests replaced urllib3.
- A browser still signed in to a deleted (or restored-over) account is signed out at its next request instead
  of reading install data. See [docs/AUTHENTICATION.md](https://github.com/myastroboard/myastroboard/blob/v1.8.2/docs/AUTHENTICATION.md#sessions).
- Only admins can clear the Celestrak block of the ISS / CSS trackers, as documented; the button is hidden
  from other accounts.
- The setup wizard closes as soon as Skip, Skip all, Finish or "Go to SkyTonight" is clicked, instead of
  staying on screen until its choice was saved (a second click then skipped a step or saved twice).
- The HTTPS-only session cookie can no longer be turned on from a plain-HTTP page, where the browser would
  drop it and lock the admin out. Recovery steps in [docs/6.REVERSE_PROXY.md](https://github.com/myastroboard/myastroboard/blob/v1.8.2/docs/6.REVERSE_PROXY.md).

Release notes: <https://github.com/myastroboard/myastroboard/releases/tag/v1.8.2>

## 1.8.1

### Fixes

- DSS2 sky images (object thumbnails, framing backgrounds) fall back to mirrors of the survey (ESA, MAST, CSIRO,
  China-VO) when CDS hips2fits is down; cards show a placeholder when no server answers. See
  [docs/SKYTONIGHT.md](https://github.com/myastroboard/myastroboard/blob/v1.8.1/docs/SKYTONIGHT.md#sky-image).
- Object information falls back to the SIMBAD mirrors (CfA Harvard, IDIA) when CDS SIMBAD is down, and its sources
  line now says when the data comes from the local catalogue instead of SIMBAD.

Release notes: <https://github.com/myastroboard/myastroboard/releases/tag/v1.8.1>

## 1.8.0

### Features

- Framing simulator: see what your sensor frames on a deep-sky target, over a real image of the sky, with rotation,
  comparison of up to three equipment combinations and PNG export - from SkyTonight, the Wishlist, Plan My Night and
  Astrodex. See [docs/SKYTONIGHT.md](https://github.com/myastroboard/myastroboard/blob/v1.8.0/docs/SKYTONIGHT.md#framing-simulator).
- Share cards: turn an Astrodex picture (with its acquisition details), a logged session, tonight's sky or an upcoming
  event into a ready-to-post image in the social-network formats (4:5, 1:1, 16:9, 9:16), made in the browser and
  never showing your location. See [docs/SHARE_CARDS.md](https://github.com/myastroboard/myastroboard/blob/v1.8.0/docs/SHARE_CARDS.md).

### Fixes

- Map tiles: a failure while reading a tile from OpenStreetMap no longer returns a server error; the
  cached tile is served instead, as for any other upstream failure.

Release notes: <https://github.com/myastroboard/myastroboard/releases/tag/v1.8.0>

## 1.7.4

### Fixes

- Security: Pillow updated to 13.0.0, which fixes several image-decoding vulnerabilities (JPEG, TIFF, PDF, GIF, BMP);
  astropy, pandas, SQLAlchemy and alembic also updated to their latest releases.

Release notes: <https://github.com/myastroboard/myastroboard/releases/tag/v1.7.4>

## 1.7.3

### Features

- Maps: OpenStreetMap vector maps drawn in the browser, with light, dark and night vision red styles, loaded and
  cached by the server instead of Esri tiles - see [docs/CACHE_SYSTEM.md](https://github.com/myastroboard/myastroboard/blob/v1.7.3/docs/CACHE_SYSTEM.md#map-tile-cache).

### Fixes

- Astrodex photo map: the mouse wheel scrolls the page again; it zooms the map only after a click on it.
- *What's new* window: the release just published is listed again instead of "could not be loaded" (its changelog
  entries are read from the release tag's Unreleased section, archived only after tagging).
- Screen-reader labels (close buttons, menu toggle, language and theme pickers, sky widget, photo slideshow arrows,
  location order buttons) are now translated instead of always English.
- SkyTonight deep-sky and comet lists load in well under a second again instead of timing out with "Failed to
  load SkyTonight results" on slow disks (Docker Desktop on Windows).
- SkyTonight sky map: opens about three times faster, and its filters respond at once, with a thousand or more
  targets plotted.

Release notes: <https://github.com/myastroboard/myastroboard/releases/tag/v1.7.3>

## 1.7.2

### Features

- Parameters: MQTT brokers are now shared connections, managed in Configuration and picked by the MQTT / Home Assistant
  connector; an existing broker setup is migrated automatically - see [docs/HOME_ASSISTANT.md](https://github.com/myastroboard/myastroboard/blob/v1.7.2/docs/HOME_ASSISTANT.md#mqtt-connections).
- Parameters: sub-tabs reordered (Locations, Configuration, Connectors, Logs, Users, Metrics, Backup / Restore); Log export
  now sits under Logs.
- Connectors: the "Display name" field only shows on connectors with an Observatory panel (AllSky), the only place it
  is used.
- Observatory: AllSky sensor data now arrives over MQTT from AllSky's Publish Data module (v2024.12 and v2026), on a shared
  MQTT connection; v2026's shared environment sensor is shown first - see [docs/CONNECTORS.md](https://github.com/myastroboard/myastroboard/blob/v1.7.2/docs/CONNECTORS.md#sensor-data-module).

### Fixes

- Saving the Parameters -> Configuration settings no longer resets the connector settings (AllSky URL, MQTT broker).
- Observatory: AllSky sensor card shows a dome temperature (Dew Heater ambient, else the fan's control temperature) with the fan threshold on the fan row; the camera sensor `TEMPERATURE_C` `0` placeholder is hidden - see [docs/CONNECTORS.md](https://github.com/myastroboard/myastroboard/blob/v1.7.2/docs/CONNECTORS.md).

### Breaking changes

- AllSky connector: sensor data no longer reads the Export module file (`export_json_path` is gone). Pick an MQTT
  connection in the *Sensor data* module and set up AllSky's Publish Data module as the card shows.

Release notes: <https://github.com/myastroboard/myastroboard/releases/tag/v1.7.2>

## 1.7.1

### Features

- Observatory: AllSky sensor card shows the Fans module (state, PWM duty %, temperature and threshold, up to two fans).

### Fixes

- AllSky connector supports AllSky v2026.10 as well as v2024.12 (auto-detected); the card explains the Export
  module setup - see [docs/CONNECTORS.md](https://github.com/myastroboard/myastroboard/blob/v1.7.1/docs/CONNECTORS.md#allsky-versions).
- AllSky sensor data no longer stays empty forever when the first read failed (e.g. Export file not written yet):
  the cached reading now expires after 5 minutes, or 1 minute when empty.
- Connector cards: *Configure* buttons line up across a row, and an open settings panel starts right
  under its button instead of below a gap when a neighbouring card is taller.

Release notes: <https://github.com/myastroboard/myastroboard/releases/tag/v1.7.1>

## 1.7.0

### Features

- Footer update notice opens a *What's new* window listing the changelog entries since the installed version,
  with breaking changes gathered on top, instead of linking straight to GitHub.
- Storage moves from JSON files to a SQLite database (`data/myastroboard.db`) with versioned schema
  migrations; existing data is imported, verified and archived automatically on first start - see
  [docs/DATABASE.md](https://github.com/myastroboard/myastroboard/blob/v1.7.0/docs/DATABASE.md).
- `backend/db/manage.py` command line for recovery (reset a password, disable 2FA) without editing files.
- Parameters -> Metrics gets a Database block: schema version, size, journal mode, integrity check.
- Parameters -> Backup / Restore shows the 1.7 upgrade archive (`data/backups/`) and deletes it once no longer needed.

### Breaking changes

- One-way data migration: once 1.7 has started, going back to 1.6 means restoring
  `data/backups/pre-1.7-*.zip`. Hand-editing `users.json`/`config.json` is replaced by the
  `manage.py` command line and the Admin backup/restore.

Release notes: <https://github.com/myastroboard/myastroboard/releases/tag/v1.7.0>

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
