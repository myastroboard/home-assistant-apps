# Changelog

## 0.6.0

### Features

- An iPhone ProRAW (`.dng`) opens in the linear editor, and a Milky Way shot with a landscape uses
  the phone's sky mask, single or stacked: no halos round trees, a dark night sky. See
  docs/ALGORITHMS.md "Nightscapes".
- Wide-angle shots (35 mm-equivalent focal up to 50 mm) have their lens vignetting and sky colour
  shading corrected automatically, and a clean stack no longer crushes darker sky to black.
  Phone ProRAW keeps the phone's white balance and stacks with equal weights.
- Stacking follows wide-angle lens distortion: stars stay sharp across the whole stack instead of
  turning into short streaks toward the corners.
- New optional "Style" step before Export: Vivid, Soft glow or Cinematic finishing looks from a
  gallery of your own image, one strength slider, nothing invented. See docs/ALGORITHMS.md "Looks".
  The Astrodex copy carries the style, and its parameters gain a `look` key (myastroboard).
- Night landscapes get two more styles that treat the sky and the ground apart: Galactic core and
  Blue hour, with no halo round the trees. See docs/ALGORITHMS.md "Looks".
- Deep-sky styles, picked with chips above the gallery: Luminous and Structure for nebulae, Deep
  field and Warm core for galaxies, Sparkle and Night velvet for star clusters - stars keep their size.
- Moon and planet styles (Crisp and Moonlight, Crisp and Rich colour), sized to the disc, with no ring
  on the limb; after a built-in preset the Style gallery opens on the matching kind of picture.

### Fixes

- Uploading stack frames now shows real progress and a frame counter instead of sitting at 0 % until
  the end; requests stay under the per-file size limit from Settings (so a reverse proxy accepts them).
- The editor no longer crashes on a phone ProRAW whose capture info has no gain or sensor
  temperature (the info panel now skips fields the API sends as null).
- Stacking now removes an aircraft or satellite trail from a short stack (3 to 10 frames), and the
  default winsorized rejection no longer leaves a faint line where a trail was rejected.
- An upload a proxy refuses as too large (Cloudflare caps requests at 100 MB) now says so and
  suggests the local address, instead of showing the proxy's raw HTML error page.
- Full-resolution renders are about 10% faster (vibrance, denoise and sharpen), with identical
  output. The weekly performance benchmark's full-res budget is now 12 s; see CONTRIBUTING.md.
- Lib update
- Auto Astro now showcases the picture instead of crushing its sky to black: a darker but never
  clipped sky, a lifted object, a neutral background, noise and colour dosed per kind of picture,
  and your Stack settings kept. See docs/ALGORITHMS.md "Auto Astro".
- Stacked composites no longer render with a green sky, and Denoise now also removes the coarser
  grain and colour mottle of real stacks while sparing faint stars. See docs/ALGORITHMS.md.
- Phone Milky Way shots (wide-angle ProRAW) no longer come out covered in green and magenta blotches,
  and a light-polluted sky no longer gets a dark arch and lavender sides. See docs/ALGORITHMS.md
  "Render hints".

Release notes: <https://github.com/myastroboard/myastroshine/releases/tag/v0.6.0>

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
