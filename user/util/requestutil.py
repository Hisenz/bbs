

def get_session(name, request):
    try:
        return request.session[name]
    except Exception:
        return None