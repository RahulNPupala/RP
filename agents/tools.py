def get_allowed_channels(record):

    consent = record.get("consent", {})
    channels = []

    if consent.get("email_opt_in", False):
        channels.append("email")

    if consent.get("sms_opt_in", False):
        channels.append("sms")

    if consent.get("voice_opt_in", False):
        channels.append("voice")

    return channels


def get_preferred_channel(record, allowed):

    preferences = record.get("channel_preferences", [])

    for p in preferences:
        if p in allowed:
            return p

    if allowed:
        return allowed[0]

    return None