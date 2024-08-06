def one(evidence) -> dict:
    return {
        "id": str(evidence["_id"]),
        "createdAt": str(evidence["createdAt"]),
        "updatedAt": str(evidence["updatedAt"]),
        "deletedAt": str(evidence["deletedAt"]),
        "softDeleted": bool(evidence["softDeleted"]),
        "active": bool(evidence["active"]),
        "code": str(evidence["code"]),
        "note": str(evidence["note"]),
        "file": str(evidence["file"]),
        "orderId": str(evidence["orderId"])
    }


def many(evidence) -> list:
    return [one(evidence) for evidence in evidence]
