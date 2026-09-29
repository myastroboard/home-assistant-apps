# MyAstroBoard

Self-hosted astronomy dashboard: observation planning, sky and weather
conditions, SkyTonight recommendations, Astrodex, equipment and sessions.

Full documentation: <https://github.com/myastroboard/myastroboard/tree/main/docs>

## First start

1. Click **Start**, then give it a moment: Home Assistant can take several
   seconds to show the app as started. Don't click **Start** again - that
   restarts it.
2. Click **Open web UI** (port 5000 on your Home Assistant host).
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

The web UI is exposed on your local network and protected by MyAstroBoard's own
sign-in. It is not available through the Home Assistant sidebar (ingress). For
access from outside your network, use a reverse proxy - see the
[reverse proxy guide](https://github.com/myastroboard/myastroboard/blob/main/docs/6.REVERSE_PROXY.md).

## Support

Report issues at <https://github.com/myastroboard/myastroboard/issues>.
