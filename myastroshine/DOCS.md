# MyAstroShine

Astrophoto enhancement and stacking in your browser: one-click Auto Astro,
step-by-step editing, stacking with calibration frames, depth-shift 3D effect,
and a round trip with MyAstroBoard's Astrodex.

Full documentation: <https://github.com/myastroboard/myastroshine/tree/main/docs>

## First start

1. Click **Start**, then give it a moment: Home Assistant can take several
   seconds to show the app as started. Don't click **Start** again - that
   restarts it.
2. Click **Open web UI**, or turn on **Show in sidebar** on the app page to get
   a **MyAstroShine** entry in the Home Assistant sidebar.
3. Drop a photo (or several shots of the same target) and start editing. Using
   the app needs no account.
4. Open **Settings** right away and **create the admin password**: settings,
   logs, tokens and engines are reserved for the administrator, and the first
   person to open Settings chooses that password.

## Configuration

There are no app options: all settings live in **Settings** in the web UI and
are stored in the app's data folder.

## Access

- **Sidebar panel (ingress)**: works wherever Home Assistant works - on your
  network, through Home Assistant Cloud (Nabu Casa) or your own remote URL, and
  in the companion app - with Home Assistant's login in front of it. This is the
  recommended way.
- **Direct URL**: `http://<your-home-assistant>:8002`. **Off by default**: turn
  it on in the app's **Network** section only if you need it (see *Using
  MyAstroShine from MyAstroBoard*). Anyone on your network can then use the app
  without a Home Assistant login; Settings still need the admin password.

Each Home Assistant user is counted on their own for the upload rate limit and
the number of jobs running at once.

**Large uploads behind a proxy.** A proxy in front of Home Assistant can cap
the size of an upload: Cloudflare (a tunnel or a proxied domain) refuses
anything over 100 MB on its Free and Pro plans. Photos usually fit; the ML
engine packages (200-300 MB) do not. Install engines from your local address
(e.g. `http://homeassistant.local:8123`) - it is needed only once.

## Using MyAstroShine from MyAstroBoard

MyAstroBoard's Astrodex can open a photo in MyAstroShine and receive the result
back. MyAstroBoard opens MyAstroShine in a new browser tab, which the sidebar
panel cannot be, so this needs the direct port:

1. Enable port 8002 in this app's **Network** section.
2. In MyAstroShine, **Settings -> Astrodex**: create a token, and add the
   address MyAstroBoard sends results from to the **Astrodex origin
   allowlist** - for MyAstroBoard as a Home Assistant app, its direct URL,
   e.g. `http://192.168.1.10:5000`.
3. In MyAstroBoard, fill in the MyAstroShine connector: base URL
   `http://<home-assistant-ip>:8002` (an IP address, not a `.local` name),
   the token and its signing secret. See the
   [MyAstroBoard guide](https://github.com/myastroboard/myastroboard/blob/main/docs/MYASTROSHINE.md).

## ML engines (StarNet2, DeepSNR)

Optional, and **amd64 only** (the engine packages are x86-64 programs; on a
Raspberry Pi or other aarch64 host the classical algorithms are used). Download
the Linux package yourself from its publisher, then install it from **Settings
-> ML engines**: the app checks it, shows its licence, and installs it once you
accept it.

Engine packages are 200-300 MB and are **not included in Home Assistant
backups**: after restoring a backup, upload them again.

## Backups

Home Assistant backups keep your settings, presets, tokens and the admin
password. The app is stopped for a moment while a backup runs (its database must
not be copied while it changes). Editing sessions and stacks are working copies
that expire on their own and are not backed up; download your finished images.

## Lost admin password

Create an empty file named `reset-admin` in this app's folder under
`addon_configs` (with the Samba share or the File editor app; the folder name
ends with `_myastroshine`), then restart the app. The password is cleared and
the file deleted; open **Settings** to choose a new one.

## Logs

The app's **Log** tab shows the console output. For more detail, open
**Settings -> Logs** in the web UI: set the levels, reproduce the issue, then
export the log. Changes apply without restarting the app.

## Support

Report issues at <https://github.com/myastroboard/myastroshine/issues>.
