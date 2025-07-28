def noteEntity(item) ->dict:
    """
    Note schema for the application.
    """
    return {
        "id": str(item.get("_id")),
        "note": item.get("note"),
        "important": item.get("important", False),
        "created_at": item.get("created_at", "Not specified"),
        "updated_at": item.get("updated_at", "Not specified")
    }

def notesEntity(items) -> list:
    """
    List of notes schema for the application.
    """
    return [noteEntity(item) for item in items]