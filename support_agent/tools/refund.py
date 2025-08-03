def refund(context):
    if context.is_premium:
        return f"{context.name}, your refund is being processed."
    return "Refunds are available only for premium users."