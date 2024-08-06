def one(task) -> dict:
    return {
        "id": str(task["_id"]),
        "createdAt": str(task["createdAt"]),
        "updatedAt": str(task["updatedAt"]),
        "deletedAt": str(task["deletedAt"]),
        "softDeleted": bool(task["softDeleted"]),
        "active": bool(task["active"]),
        "code": str(task["code"]),
        "reference": str(task["reference"]),
        "topic": str(task["topic"]),
        "subject": str(task["subject"]),
        "description": str(task["description"]),
        "deadline": str(task["deadline"]),
        "status": str(task["status"]),
        "owner": str(task["owner"]),
    }


def many(tasks) -> list:
    return [one(task) for task in tasks]
