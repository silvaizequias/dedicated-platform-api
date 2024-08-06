def one(order) -> dict:
    return {
        "id": str(order["_id"]),
        "createdAt": str(order["createdAt"]),
        "updatedAt": str(order["updatedAt"]),
        "deletedAt": str(order["deletedAt"]),
        "softDeleted": bool(order["softDeleted"]),
        "active": bool(order["active"]),
        "code": str(order["code"]),
        "barCode": str(order["barCode"]),
        "serial": str(order["serial"]),
        "control": str(order["control"]),
        "topic": str(order["topic"]),
        "description": str(order["description"]),
        "issuer": str(order["issuer"]),
        "customer": str(order["customer"]),
        "status": str(order["status"]),
    }


def many(orders) -> list:
    return [one(order) for order in orders]
