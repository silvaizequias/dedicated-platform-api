def one(account):
    return {
        "id": str(account["_id"]),
        "createdAt": str(account["createdAt"]),
        "updatedAt": str(account["updatedAt"]),
        "deletedAt": str(account["deletedAt"]),
        "softDeleted": bool(account["softDeleted"]),
        "active": bool(account["active"]),
        "lastLogin": str(account["lastLogin"]),
        "role": str(account["role"]),
        "secret": str(account["secret"]),
        "image": str(account["image"]),
        "name": str(account["name"]),
        "email": str(account["email"]),
        "phone": str(account["phone"]),
        "document": str(account["document"]),
        "zipCode": str(account["zipCode"]),
        "street": str(account["street"]),
        "number": str(account["number"]),
        "complement": str(account["complement"]),
        "district": str(account["district"]),
        "city": str(account["city"]),
        "state": str(account["state"]),
        "latitude": float(account["latitude"]),
        "longitude": float(account["longitude"]),
    }


def many(accounts):
    return [one(account) for account in accounts]
