def one(subscription):
    return {
        "id": str(subscription["_id"]),
        "createdAt": str(subscription["createdAt"]),
        "updatedAt": str(subscription["updatedAt"]),
        "deletedAt": str(subscription["deletedAt"]),
        "softDeleted": bool(subscription["softDeleted"]),
        "active": bool(subscription["active"]),
        "code": str(subscription["code"]),
        "credit": int(subscription["credit"]),
        "unlimited": bool(subscription["unlimited"]),
        "paymentGateway": str(subscription["paymentGateway"]),
        "customerId": str(subscription["customerId"]),
        "accountId": str(subscription["accountId"]),
    }


def many(subscriptions):
    return [one(subscription) for subscription in subscriptions]
