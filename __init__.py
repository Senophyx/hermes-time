from datetime import datetime

_WEEKDAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

def current_time():
    import hermes_time
    tz_label = hermes_time._resolve_timezone_name().strip()
    
    if tz_label:
        from zoneinfo import ZoneInfo
        now = datetime.now(ZoneInfo(tz_label))
    else:
        now = datetime.now().astimezone()
        
    weekday = _WEEKDAYS[now.weekday()]
    
    prompt = (
        "<current-time>\n"
        "[Context: This is user's current time. Use this as your time awareness.]\n\n"
        f"{weekday} {now.strftime('%Y-%m-%d')} {now.strftime('%H:%M')} {tz_label}\n"
        "</current-time>"
    )
    
    return prompt


def _pre_llm_call(**kwargs):
    return {"context": current_time()}

def register(ctx):
    ctx.register_hook("pre_llm_call", _pre_llm_call)