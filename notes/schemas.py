def one(note) -> dict:
    return {
        "id": str(note["_id"]),
        "createdAt": str(note["createdAt"]),
        "updatedAt": str(note["updatedAt"]),
        "deletedAt": str(note["deletedAt"]),
        "softDeleted": bool(note["softDeleted"]),
        "active": bool(note["active"]),
        "code": str(note["code"]),
        "reference": str(note["reference"]),
        "topic": str(note["topic"]),
        "content": str(note["content"]),
    }


def many(notes) -> list:
    return [one(note) for note in notes]
