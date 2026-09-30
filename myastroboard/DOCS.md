# MyAstroBoard

Self-hosted astronomy dashboard: observation planning, sky and weather
conditions, SkyTonight recommendations, Astrodex, equipment and sessions.

Full documentation: <https://github.com/myastroboard/myastroboard/tree/main/docs>

## First start

1. Click **Start**, then give it a moment: Home Assistant can take several
   seconds to show the app as started. Don't click **Start** again - that
   restarts it.
2. Click **Open web UI**, or turn on **Show in sidebar** on the app page to get
   a **MyAstroBoard** entry in the Home Assistant sidebar. See *Access* below
   for the difference with the direct URL (port 5000).
3. Sign in with `admin` / `admin` and **change the password immediately** - a
   banner reminds you until you do.
4. The setup wizard asks for your observing location; everything else is set
   from **Parameters** in the web UI.

The first SkyTonight calculation can take several minutes on a Raspberry Pi.

## Configuration

There are no app options: all settings live in the web UI and are stored in the
app's data folder, which Home Assistant backups include (caches and logs are
excluded and rebuilt automatically).

To use another host port, change it in the app's **Network** section.

## Logs

The app's **Log** tab shows the console output (warnings and errors by default).
To troubleshoot, go to **Parameters -> Log export** in the web UI: set the log
file level (and, if you want more detail in the **Log** tab, the console level)
to `DEBUG`, reproduce the issue, then export the logs. Changes apply without
restarting the app. (Available from MyAstroBoard 1.6.6.)

## Home Assistant integration

MyAstroBoard can publish its data to Home Assistant over MQTT. It is optional:
enable the MQTT connector in **Parameters -> Connectors** and point it at your
broker (for the Mosquitto broker app: host `core-mosquitto`, port 1883, with a
Home Assistant user). The companion Lovelace card is installed separately via
HACS. See the
[Home Assistant guide](https://github.com/myastroboard/myastroboard/blob/main/docs/HOME_ASSISTANT.md).

## Access

MyAstroBoard can be opened in two ways. Both show the same data and use
MyAstroBoard's own sign-in (your Home Assistant account does not sign you in).

- **Sidebar panel (ingress)**: the **MyAstroBoard** entry in the Home Assistant
  sidebar. It works wherever Home Assistant works - on your network, through
  Home Assistant Cloud (Nabu Casa) or your own remote URL, and in the Home
  Assistant companion app - without opening any port.
- **Direct URL**: `http://<your-home-assistant>:5000` (the port set in the
  app's **Network** section). Local network only, unless you put a reverse
  proxy in front of it - see the
  [reverse proxy guide](https://github.com/myastroboard/myastroboard/blob/main/docs/6.REVERSE_PROXY.md).

### What the sidebar panel cannot do

The panel runs inside the Home Assistant page, so the browser features that
need MyAstroBoard to be the page itself are switched off there:

| Feature | Sidebar panel | Direct URL over HTTP | Direct URL over HTTPS |
|---|---|---|---|
| Dashboard, planning, Astrodex, all tabs | Yes | Yes | Yes |
| Install as an app (PWA, home screen icon) | No | No | Yes |
| Push notifications from MyAstroBoard | No | No | Yes |
| Offline page when the server is unreachable | No | No | Yes |

- **Why not in the panel**: an app can only be installed, and push
  notifications only delivered, for a page the browser opens on its own. The
  panel is a frame inside Home Assistant, and its address changes per install
  and requires a Home Assistant session.
- **Why HTTPS**: browsers only allow installable apps, push notifications and
  offline support on HTTPS addresses (or `localhost`). The plain
  `http://<your-home-assistant>:5000` address is not enough; use a reverse proxy
  with a certificate in front of the direct port.
- **Notifications without a PWA**: enable the MQTT connector (see
  *Home Assistant integration* above) and build a Home Assistant automation on
  the MyAstroBoard entities, for example "notify me when tonight's conditions
  are good". The alerts then arrive through the Home Assistant companion app,
  like your other Home Assistant notifications.
- In the panel, the push notification settings and the install prompt are
  hidden. If you already installed MyAstroBoard as an app from the direct URL,
  it keeps working as before.

### Features that need the direct URL

Some addresses are meant to be opened by other software, not by you in the
panel: the Astrodex stream (Lovelace card, camera entity) and the
MyAstroShine photo return address. Set **Parameters -> Advanced -> External
base URL** to the direct URL (or your reverse proxy URL) so these addresses
point to something reachable. Keep the port enabled in the **Network** section
if you use them.

## Support

Report issues at <https://github.com/myastroboard/myastroboard/issues>.
